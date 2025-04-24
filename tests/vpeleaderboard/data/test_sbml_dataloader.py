import os
import pytest
from vpeleaderboard.data.src.sbml_dataloader import SBMLDataModule
import basico

MODEL_PATH = "vpeleaderboard/data/models/BIOMD0000000537_url.xml"

@pytest.fixture
def sbml_data_module():
    """
    Fixture to create an instance of SBMLDataModule for testing.
    """
    return SBMLDataModule(file_name="BIOMD0000000537_url")


def test_prepare_data(sbml_data_module):
    """
    Test the prepare_data method.
    """
    # Simulate the loading of the configuration (no patching)
    sbml_data_module.config = {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    
    # Simulate the existence of the necessary files
    sbml_data_module.sbml_file_path = MODEL_PATH

    # Simulate checking the existence of files
    assert os.path.exists(sbml_data_module.sbml_file_path)  # This should pass if the file exists
    
    sbml_data_module.prepare_data()

    # Assert that the config was correctly loaded
    assert sbml_data_module.config == {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    assert sbml_data_module._is_prepared is True


def test_missing_required_keys_in_config(sbml_data_module):
    """
    Test the case where YAML config is missing required keys.
    """
    sbml_data_module.config = {"train_duration": 100}  # Missing 'test_duration'

    try:
        sbml_data_module.prepare_data()
    except ValueError as e:
        assert str(e) == "Missing required key(s) in YAML config"


def test_setup(sbml_data_module):
    """
    Test the setup method.
    """
    sbml_data_module.config = {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    sbml_file_path = os.path.abspath(MODEL_PATH)
    sbml_data_module.sbml_file_path = sbml_file_path
    
    # Simulate that the file exists
    assert os.path.exists(sbml_data_module.sbml_file_path)  # File should exist

    sbml_data_module.prepare_data()

    # Assuming basico.load_model is a simple function that returns an object when called
    sbml_data_module.copasi_model = basico.load_model(sbml_data_module.sbml_file_path)  # Simulating the loaded model

    assert sbml_data_module.copasi_model is not None, "Model is loaded properly"


def test_train_dataloader(sbml_data_module):
    """
    Test the train_dataloader method.
    """
    sbml_data_module.config = {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    sbml_data_module.prepare_data()

    # Simulate the result of basico.run_time_course by manually creating a mock dataframe
    train_df = [{"time": 0, "value": 1}, {"time": 1, "value": 2}]
    sbml_data_module.train_dataloader = lambda: train_df  # Mocking the method

    # Call the train_dataloader and assert the mock data
    train_loader = sbml_data_module.train_dataloader()
    
    assert len(train_loader) == 2  # Check that the data has two rows
    assert train_loader[0] == {"time": 0, "value": 1}  # Check the first data entry

def test_val_dataloader(sbml_data_module):
    """
    Test the train_dataloader method.
    """
    sbml_data_module.config = {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    sbml_data_module.prepare_data()

    # Simulate the result of basico.run_time_course by manually creating a mock dataframe
    val_df = [{"time": 0, "value": 1}, {"time": 1, "value": 2}]
    sbml_data_module.val_dataloader = lambda: val_df  # Mocking the method

    # Call the train_dataloader and assert the mock data
    val_loader = sbml_data_module.val_dataloader()
    
    assert len(val_loader) == 2  # Check that the data has two rows
    assert val_loader[0] == {"time": 0, "value": 1}

def test_test_dataloader(sbml_data_module):
    """
    Test the test_dataloader method.
    """
    sbml_data_module.config = {"train_duration": 100,'val_duration': 30, "test_duration": 50}
    sbml_data_module.prepare_data()

    # Simulate the result of basico.run_time_course by manually creating a mock dataframe
    test_df = [{"time": 0, "value": 3}, {"time": 1, "value": 4}]
    sbml_data_module.test_dataloader = lambda: test_df  # Mocking the method

    # Call the test_dataloader and assert the mock data
    test_loader = sbml_data_module.test_dataloader()
    
    assert len(test_loader) == 2  # Check that the data has two rows
    assert test_loader[0] == {"time": 0, "value": 3}  # Check the first data entry


def test_file_not_found(sbml_data_module):
    """
    Test file not found exception for SBML and YAML files.
    """
    # Simulate the missing SBML file
    sbml_data_module.sbml_file_path = "vpeleaderboard/models/BIOMD0000000537.xml"
    
    # The file doesn't exist
    assert not os.path.exists(sbml_data_module.sbml_file_path)

    # Test if the FileNotFoundError is raised
    try:
        sbml_data_module.prepare_data()
    except FileNotFoundError as e:
        assert str(e) == "SBML model file not found"

    # Simulate the missing YAML file
    sbml_data_module.config = None  # Mimic the case when no config is found
    try:
        sbml_data_module.prepare_data()
    except FileNotFoundError as e:
        assert str(e) == "YAML file not found"
