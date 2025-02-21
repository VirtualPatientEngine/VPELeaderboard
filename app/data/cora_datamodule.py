#!/usr/bin/env python3

'''
This module contains the CORADataModule class,
which is a subclass of LightningDataModule.
It is a simple DataModule for the CORA dataset.
'''

from typing import Any, Dict, Optional
import torch_geometric.data as geom_data
from lightning import LightningDataModule
from torch.utils.data import DataLoader
from torch_geometric.datasets import Planetoid

class CORADataModule(LightningDataModule):
    """`LightningDataModule` for the CORA dataset.

    The CORA dataset is a widely used benchmark dataset in the field of machine learning, 
    particularly in the area of document classification and information retrieval. 
    It is commonly used for tasks such as text classification, citation matching, and 
    document clustering.
    
    The CORA dataset consists of academic research papers from a variety of different 
    research areas, including computer science, physics, and biology. 
    Each document in the dataset is represented by a bag-of-words feature vector, 
    where each feature corresponds to a word in the vocabulary and the value represents 
    the frequency of that word in the document. Additionally, the dataset contains 
    citation links between the documents, allowing researchers to explore relationships 
    between different papers and perform tasks such as citation matching and link prediction.

    One of the key characteristics of the CORA dataset is its labeled nature. 
    Each document is associated with one or more predefined class labels, 
    indicating the research area or topic of the paper. These labels are typically used 
    for supervised learning tasks, such as text classification, where the goal is to 
    predict the class labels of unseen documents based on their content.

    A `LightningDataModule` implements 7 key methods:

    ```python
        def prepare_data(self):
        # Things to do on 1 GPU/TPU (not on every GPU/TPU in DDP).
        # Download data, pre-process, split, save to disk, etc...

        def setup(self, stage):
        # Things to do on every process in DDP.
        # Load data, set variables, etc...

        def train_dataloader(self):
        # return train dataloader

        def val_dataloader(self):
        # return validation dataloader

        def test_dataloader(self):
        # return test dataloader

        def predict_dataloader(self):
        # return predict dataloader

        def teardown(self, stage):
        # Called on every process in DDP.
        # Clean up after fit or test.
    ```

    This allows you to share a full dataset without explaining how to download,
    split, transform and process the data.

    Read the docs:
        https://lightning.ai/docs/pytorch/latest/data/datamodule.html
    """

    def __init__(
        self,
        data_dir: str = "/tmp/cora", # where do you want to download and save the data
        batch_size: int = 64,
        num_workers: int = 0,
        pin_memory: bool = False,
    ) -> None:
        """Initialize a `CORADataModule`.

        Args:
            data_dir: The data directory. Defaults to `"data/"`.
            train_val_test_split: The train, validation and test split.
                                Defaults to `(55_000, 5_000, 10_000)`.
            batch_size: The batch size. Defaults to `64`.
            num_workers: The number of workers. Defaults to `0`.
            pin_memory: Whether to pin memory. Defaults to `False`.
        """
        super().__init__()

        # this line allows to access init params with 'self.hparams' attribute
        # also ensures init params will be stored in ckpt
        self.save_hyperparameters(logger=False)

        # you can set up the data processing pipeline here
        # for example, you can define transforms here
        # uncomment the following lines to define transforms
        # don't forget to import the necessary modules
        # self.transforms = transforms.Compose(
        #     [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        # )

        self.data = None
        self.batch_size_per_device = batch_size

    @property
    def num_classes(self) -> int:
        """
        Get the number of classes.

        Args:
            None

        Returns:
            int: The number of classes in the dataset.
        """
        return 7

    def prepare_data(self) -> None:
        """
        Download data if needed. Lightning ensures that `self.prepare_data()` is 
        called only within a single process on CPU, so you can safely add your 
        downloading logic within. In case of multi-node training, the execution of 
        this hook depends upon `self.prepare_data_per_node()`.

        Do not use it to assign state (self.x = y).

        Args:
            None

        Returns:
            None
        """
        dataset = Planetoid(root='/tmp/Cora', name='Cora')
        self.data = dataset

    def setup(self, stage: Optional[str] = None) -> None:
        """
        Load data. Set variables: `self.data_train`, `self.data_val`, `self.data_test`.

        Called at the beginning of fit (train + validate), validate, test, or predict. 
        This is a good hook when you need to build models dynamically or adjust 
        something about them. This hook is called on every process when using DDP.

        Args:
            stage: The stage to setup. Either `"fit"`, `"validate"`, `"test"`, or `"predict"`.

        Returns:
            None
        """

    def train_dataloader(self) -> DataLoader[Any]:
        """
        Create and return the train dataloader.

        Args:
            None

        Returns:
            DataLoader: The train dataloader.
        """
        return geom_data.DataLoader(dataset=self.data,
                                    batch_size=1,
                                    num_workers=self.hparams.num_workers,
                                    shuffle=True)

    def val_dataloader(self) -> DataLoader[Any]:
        """
        Create and return the validation dataloader.

        Args:
            None

        Returns:
            DataLoader: The validation dataloader.
        """
        return geom_data.DataLoader(self.data,
                                    batch_size=1,
                                    num_workers=self.hparams.num_workers,
                                    shuffle=False)

    def test_dataloader(self) -> DataLoader[Any]:
        """
        Create and return the test dataloader.

        Args:
            None

        Returns:
            DataLoader
        """
        return geom_data.DataLoader(self.data,
                                    batch_size=1,
                                    num_workers=self.hparams.num_workers,
                                    shuffle=False)

    def teardown(self, stage: Optional[str] = None) -> None:
        """
        Lightning hook for cleaning up after `trainer.fit()`, `trainer.validate()`,
        `trainer.test()`, and `trainer.predict()`.

        Args:
            stage: The stage being torn down. 
                    Either `"fit"`, `"validate"`, `"test"`, or `"predict"`.
                    Defaults to ``None``.

        Returns:
            None
        """
        # pass

    def state_dict(self) -> Dict[Any, Any]:
        """
        Called when saving a checkpoint.
        Implement to generate and save the datamodule state.

        Args:
            None

        Returns:
            Dict: A dictionary containing the datamodule state that you want to save.
        """
        return {}

    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """
        Called when loading a checkpoint. Implement to reload datamodule state 
        given datamodule
        `state_dict()`.

        Args:
            state_dict: The datamodule state returned by `self.state_dict()`.

        Returns:
            None
        """
        # pass
