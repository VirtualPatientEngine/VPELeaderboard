#!/usr/bin/env python3

"""
BasicoModel class for loading SBML models
using the basico package.
"""

import os
import logging
from typing import Optional, Dict, Union
import pandas as pd
import basico
from pydantic import Field, model_validator
from vpeleaderboard.data.src.sys_bio_model import SysBioModel

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasicoModel(SysBioModel):
    """
    Model that loads SBML models using the basico package.
    """
    sbml_folder_path: Optional[str] = Field(None, description="Path to an SBML files folder")
    simulation_results: Optional[pd.DataFrame] = None
    name: Optional[str] = Field("", description="Name of the model")
    description: Optional[str] = Field("", description="Description of the model")

    copasi_model: Optional[object] = None
    model_config = {"arbitrary_types_allowed": True}

    @model_validator(mode="after")
    def validate_sbml_folder_path(self):
        """
        Validate that the SBML folder exists and contains XML files.

        Args:
            sbml_folder_path (str): The path to the SBML folder.

        Returns:
            ModelData: The validated instance of the class.

        Raises:
            ValueError: If the folder path is missing or does not contain XML files.
        """
        if not self.sbml_folder_path:
            raise ValueError("SBML folder path must be provided.")

        if not os.path.exists(self.sbml_folder_path):
            raise ValueError(f"SBML folder not found: {self.sbml_folder_path}")

        xml_files = [f for f in os.listdir(self.sbml_folder_path) if f.endswith(".xml")]
        if not xml_files:
            raise ValueError(f"No SBML files found in {self.sbml_folder_path}.")
        return self

    def get_model_metadata(self, sbml_file: str) -> Dict[str, Union[str, int]]:
        """
        Retrieve metadata for a single SBML model.

        Args:
            sbml_file (str): The name of the SBML file in the folder.

        Returns:
            Dict[str, Union[str, int]]: A dictionary containing metadata of the SBML model.
        """
        file_path = os.path.join(self.sbml_folder_path, sbml_file)
        copasi_model = basico.load_model(file_path)

        model_name = basico.model_info.get_model_name(model=copasi_model)
        species_count = len(basico.model_info.get_species(model=copasi_model))
        parameter_count = len(basico.model_info.get_parameters(model=copasi_model))
        model_description = basico.model_info.get_notes(model=copasi_model)

        return {
            "Model Name": model_name,
            "Number of Species": species_count,
            "Number of Parameters": parameter_count,
            "Description": model_description.strip()
        }
