#!/usr/bin/env python3

"""Test the models"""

import sys
import hydra
import pytest
import torch
sys.path.append('..')

def inputs_cfg(model_name: str):
    '''Return the configuration object for the model_name model'''
    with hydra.initialize(version_base=None, config_path="../configs"):
        cfg = hydra.compose(config_name='config', overrides=[f'model={model_name}'])
        cfg.logger.experiment_name = "test"
        cfg.logger.run_name = f"{model_name}_test"
    cfg.trainer.max_epochs = 1
    return cfg

@pytest.fixture(name="inputs_mlp")
def inputs_mlp_fixture():
    '''Return the configuration object for the mlp model, 
    the model object and the cora dataset object'''
    cfg = inputs_cfg("mlp")
    model_obj = hydra.utils.instantiate(cfg.model)
    cora_dataset = hydra.utils.instantiate(cfg.data)
    return cfg, model_obj, cora_dataset

@pytest.fixture(name="inputs_gcn")
def inputs_gcn_fixture():
    '''Return the configuration object for the gcn model, 
    the model object and the cora dataset object'''
    cfg = inputs_cfg("gcn")
    model_obj = hydra.utils.instantiate(cfg.model)
    cora_dataset = hydra.utils.instantiate(cfg.data)
    return cfg, model_obj, cora_dataset

def test_trainer_mlp(inputs_mlp) -> None:
    '''Test the trainer for the mlp model'''
    cfg, model_obj, cora_dataset = inputs_mlp
    trainer = hydra.utils.instantiate(cfg.trainer, logger=cfg.logger)
    trainer.fit(model=model_obj, datamodule=cora_dataset)
    test_metrics = trainer.test(model=model_obj, datamodule=cora_dataset)
    assert test_metrics[0]['test_loss'] < 2.0

def test_trainer_gcn(inputs_gcn) -> None:
    '''Test the trainer for the gcn model'''
    cfg, model_obj, cora_dataset = inputs_gcn
    trainer = hydra.utils.instantiate(cfg.trainer, logger=cfg.logger)
    trainer.fit(model=model_obj, datamodule=cora_dataset)
    test_metrics = trainer.test(model=model_obj, datamodule=cora_dataset)
    assert test_metrics[0]['test_loss'] < 2.0

def test_cora_dataset(inputs_mlp) -> None:
    '''Test the cora dataset object'''
    _, _, cora_dataset = inputs_mlp
    assert cora_dataset.num_classes == 7
    assert cora_dataset.state_dict() == {}

def test_models(inputs_mlp, inputs_gcn) -> None:
    '''Test the models'''
    _, model_mlp, _ = inputs_mlp
    _, model_gcn, _ = inputs_gcn
    for model in [model_mlp, model_gcn]:
        # assert that model_obj.model_step raise a ValueError
        with pytest.raises(ValueError):
            model.model_step((torch.tensor([1, 2, 3]), torch.tensor([1, 2, 3])), mode='xyz')
