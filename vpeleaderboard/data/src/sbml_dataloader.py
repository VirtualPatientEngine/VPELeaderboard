#!/usr/bin/env python3
"""
This module handles loading and simulating SBML models using PyTorch Lightning.
"""

import os
from typing import Optional, Any
import yaml
import hydra
import basico
import torch
from pytorch_lightning import LightningDataModule
from torch.utils.data import IterableDataset, DataLoader

class SBMLDataModule(LightningDataModule):
    """
    A LightningDataModule for simulating and loading SBML-based time course data.
    """

    class SBMLTimeCourseDataset(IterableDataset):
        """
        Dataset class for iterating over SBML simulation results.
        """

        def __init__(self, data: Any):
            """
            Args:
                data (Any): Data to be used in the dataset (e.g., pandas DataFrame).
            """
            self.data = data

        def __iter__(self):
            """
            Iterator method for the dataset.

            Yields:
                torch.Tensor: Each row in the dataset as a tensor.
            """
            for _, row in self.data.iterrows():
                yield torch.tensor(row.values, dtype=torch.float)

        def __getitem__(self, index: int):
            raise NotImplementedError("Indexing is not supported for this IterableDataset.")

    def __init__(self, file_name: str):
        """
        Initializes the SBMLDataModule with the given SBML model file name.

        Args:
            file_name (str): The name of the SBML model to load.
        """
        super().__init__()
        self.fine_name = file_name

        self.config = None
        self.sbml_file_path = None
        self.copasi_model: Optional[Any] = None

        self._is_prepared = False
        self._is_setup = False

    def prepare_data(self) -> None:
        """
        Loads YAML config and locates the SBML file.

        This method will locate and load the YAML configuration file, validate its contents,
        and check for the necessary SBML model file.

        Raises:
            FileNotFoundError: If the SBML model or YAML config file is not found.
            ValueError: If the YAML config file is empty or missing required keys.
        """
        script_dir = os.path.dirname(__file__)
        script_dir = "\\".join(script_dir.split("\\")[:-1])
        script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        with hydra.initialize(version_base=None,
                              config_path="../../configs"):
            cfg = hydra.compose(config_name="config")

        model_directory = os.path.join(script_dir, cfg.model_directory)
        model_directory = os.path.abspath(model_directory)

        sbml_path = os.path.join(model_directory, f"{self.fine_name}.xml")
        if not os.path.exists(sbml_path):
            raise FileNotFoundError(
                f"SBML model file not found for model '{self.fine_name}'. "
                f"Expected at: {sbml_path}"
            )
        self.sbml_file_path = sbml_path
        yaml_file = os.path.join(script_dir, "../configs/data", f"{self.fine_name}.yaml")
        if not os.path.exists(yaml_file):
            raise FileNotFoundError(f"YAML file not found: {yaml_file}")

        with open(yaml_file, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)

        if not self.config:
            raise ValueError(f"YAML config {yaml_file} is empty or malformed.")

        required_keys = ['train_duration', 'test_duration', 'val_duration']
        missing_keys = [key for key in required_keys
                        if key not in self.config or self.config[key] is None]
        if missing_keys:
            raise ValueError(
                f"Missing required key(s) in YAML config {yaml_file}: {', '.join(missing_keys)}"
            )

        self._is_prepared = True

    def setup(self, stage: Optional[str] = None) -> None:
        """
        Loads the SBML model only after prepare_data has been called.

        Args:
            stage (Optional[str]): The stage of setup, typically used in multi-stage setups.

        Raises:
            RuntimeError: If `prepare_data()` has not been called before `setup()`.
            FileNotFoundError: If the SBML file is not found.
        """
        if not self._is_prepared:
            raise RuntimeError("You must call `prepare_data()` before `setup()`.")

        if not os.path.exists(self.sbml_file_path):
            raise FileNotFoundError(f"SBML model file not found: {self.sbml_file_path}")

        self.copasi_model = basico.load_model(self.sbml_file_path)

    def train_dataloader(self) -> DataLoader:
        """
        Creates the DataLoader for the training dataset based on the SBML simulation results.

        Returns:
            DataLoader: The DataLoader for the training dataset.
        """
        train_df = basico.run_time_course(
            duration=self.config['train_duration'],
            use_initial_values=False
        )
        dataset = self.SBMLTimeCourseDataset(train_df)
        return DataLoader(dataset)
    def val_dataloader(self) -> DataLoader:
        """
        Creates the DataLoader for the validating dataset based on the SBML simulation results.

        Returns:
            DataLoader: The DataLoader for the validating dataset.
        """
        val_df = basico.run_time_course(
            duration=self.config['val_duration'],
            use_initial_values=False
        )
        dataset = self.SBMLTimeCourseDataset(val_df)
        return DataLoader(dataset)

    def test_dataloader(self) -> DataLoader:
        """
        Creates the DataLoader for the test dataset based on the SBML simulation results.

        Returns:
            DataLoader: The DataLoader for the test dataset.
        """
        test_df = basico.run_time_course(
            duration=self.config['test_duration'],
            automatic=False,
            use_initial_values=False,
            update_model=False
        )
        dataset = self.SBMLTimeCourseDataset(test_df)
        return DataLoader(dataset)
