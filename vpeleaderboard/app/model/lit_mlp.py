#!/usr/bin/env python3

'''
This module contains the MLP class, which is a subclass of torch.nn.Module.
It is a simple Multi-Layer Perceptron model that consists of three linear layers.
The first layer takes the node features as input and outputs 64 features.
The second layer takes these 64 features as input and outputs 32 features.
The final layer takes these 32 features as input and outputs the final output (7).
'''

from typing import Any, Dict, Tuple
import torch
from torch import nn
from lightning import LightningModule
from torchmetrics import MeanMetric

class MLP(LightningModule):
    """Example of a `LightningModule` for MLP

    A `LightningModule` implements 8 key methods:

    ```python
    def __init__(self):
    # Define initialization code here.

    def setup(self, stage):
    # Things to setup before each stage, 'fit', 'validate', 'test', 'predict'.
    # This hook is called on every process when using DDP.

    def training_step(self, batch, batch_idx):
    # The complete training step.

    def validation_step(self, batch, batch_idx):
    # The complete validation step.

    def test_step(self, batch, batch_idx):
    # The complete test step.

    def predict_step(self, batch, batch_idx):
    # The complete predict step.

    def configure_optimizers(self):
    # Define and configure optimizers and LR schedulers.
    ```

    Docs:
        https://lightning.ai/docs/pytorch/latest/common/lightning_module.html
    """

    def __init__(
        self,
        optimizer: torch.optim.Optimizer,
        scheduler: torch.optim.lr_scheduler._LRScheduler,
    ) -> None:
        """
        Initialize an 'MLP' model.

        Args:
            optimizer: The optimizer to use for training.
            scheduler: The learning rate scheduler to use for training.

        Returns:
            None
        """
        super().__init__()

        # this line allows to access init params with 'self.hparams' attribute
        # also ensures init params will be stored in ckpt
        self.save_hyperparameters(logger=False)

        self.layers = nn.Sequential(
                    nn.Linear(1433, 64),
                    nn.ReLU(),
                    nn.Linear(64, 32),
                    nn.ReLU(),
                    nn.Linear(32, 7)
                    )

        # loss function
        self.criterion = torch.nn.CrossEntropyLoss()

        # for tracking training loss
        self.train_loss = MeanMetric()

        # for tracking validation loss
        self.val_loss = MeanMetric()

        # for tracking test loss
        self.test_loss = MeanMetric()

    def forward(self, batch) -> torch.Tensor:
        """
        Perform a forward pass through the model `self.layers`.

        Args:
            batch: A batch of data.
        
        Returns:
            torch.Tensor: The model output.
        """
        x, _ = batch.x, batch.edge_index
        return self.layers(x)

    def on_train_start(self) -> None:
        """
        Lightning hook that is called when training begins.

        Args:
            None

        Returns:
            None
        """
        # by default lightning executes validation step sanity checks before training starts,
        # so it's worth to make sure validation metrics don't store results from these checks
        self.val_loss.reset()

    def model_step(self,
                   batch: Tuple[torch.Tensor, torch.Tensor],
                    mode: str
                   ) -> torch.Tensor:
        """
        Perform a single model step on a batch of data.

        Args:
            batch: A batch of data (a tuple) containing the input 
                    tensor of images and target labels.
            mode: The mode of the model step.

        Returns:
            torch.Tensor: The model loss.
        """
        if mode == 'train':
            mask = batch.train_mask
        elif mode == 'val':
            mask = batch.val_mask
        elif mode == 'test':
            mask = batch.test_mask
        else:
            raise ValueError('mode should be either train, val or test')
        output = self.forward(batch)
        loss = self.criterion(output[mask], batch.y[mask])
        return loss

    def training_step(self,
                      batch: Tuple[torch.Tensor, torch.Tensor],
                      batch_idx: int) -> torch.Tensor:
        """
        Perform a single training step on a batch of data from the training set.

        Args:
            batch: A batch of data (a tuple) containing the input tensor of images and target
                labels.
            batch_idx: The index of the current batch.
        
        Returns:
            torch.Tensor: A tensor of losses between model predictions and targets.
        """
        loss = self.model_step(batch, mode = 'train')
        # update and log metrics
        self.train_loss.update(loss)
        # return loss or backpropagation will fail
        return loss

    def on_train_epoch_end(self) -> None:
        """
        Lightning hook that is called when a training epoch ends.

        Args:
            None

        Returns:
            None
        """
        self.log('train_loss', self.train_loss.compute())

    def validation_step(self,
                        batch: Tuple[torch.Tensor,
                        torch.Tensor],
                        batch_idx: int) -> None:
        """
        Perform a single validation step on a batch of data from the validation set.

        Args:
            batch: A batch of data (a tuple) containing the input tensor of images and target
                labels.
            batch_idx: The index of the current batch.

        Returns:
            None
        """
        loss = self.model_step(batch, mode = 'val')
        # update and log metrics
        self.val_loss.update(loss)
        return loss

    def on_validation_epoch_end(self) -> None:
        """
        Lightning hook that is called when a validation epoch ends.

        Args:
            None

        Returns:
            None
        """
        self.log('val_loss', self.val_loss.compute())

    def test_step(self,
                  batch: Tuple[torch.Tensor, torch.Tensor],
                  batch_idx: int) -> None:
        """
        Perform a single test step on a batch of data from the test set.

        Args:
            batch: A batch of data (a tuple) containing the input tensor of images and target
                labels.
            batch_idx: The index of the current batch.

        Returns:
            None
        """
        loss = self.model_step(batch, mode = 'test')
        # update and log metrics
        self.test_loss.update(loss)

    def on_test_epoch_end(self) -> None:
        """
        Lightning hook that is called when a test epoch ends.

        Args:
            None

        Returns:
            None
        """
        self.log('test_loss', self.test_loss.compute())
        return self.test_loss.compute()

    def setup(self, stage: str) -> None:
        """
        Lightning hook that is called at the beginning of fit (train + validate), validate,
        test, or predict.

        This is a good hook when you need to build models dynamically or adjust something about
        them. This hook is called on every process when using DDP.

        Args:
            stage: Either `"fit"`, `"validate"`, `"test"`, or `"predict"`.

        Returns:
            None
        """
        # for example, dynamically adjust the network structure
        # uncomment to see the effect
        # if self.hparams.compile and stage == "fit":
        #     self.net = torch.compile(self.net)

    def configure_optimizers(self) -> Dict[str, Any]:
        """
        Choose what optimizers and learning-rate schedulers to use in your optimization.
        Normally you'd need one. But in the case of GANs or similar you might have multiple.

        Examples:
            https://lightning.ai/docs/pytorch/latest/common/lightning_module.html#configure-optimizers
        
        Args:
            None

        Returns:
            Dict[str, Any]: A dict containing the configured optimizers and 
                learning-rate schedulers to be used for training.
        """
        optimizer = self.hparams.optimizer(params=self.trainer.model.parameters())
        return {"optimizer": optimizer}
