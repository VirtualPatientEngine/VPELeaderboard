"""
A test markdown class for pytest unit testing.
"""

import os
import unittest.mock
import pytest
import basico
import pandas as pd
from vpeleaderboard.data.src.basico_model import BasicoModel
from vpeleaderboard.data.src.sys_bio_model import SysBioModel

@pytest.fixture(name="model_instance")
def model_fixture():
    """
    Fixture for the BasicoModel class.
    """
    return BasicoModel(sbml_folder_path="vpeleaderboard/data/models")

@pytest.fixture(name="temp_folder")
def temp_folder_fixture():
    """Checks for an empty temporary directory."""
    return "vpeleaderboard/data/models"

@pytest.fixture(name="dynamic_model_creator")
def dynamic_model_factory():
    """
    A fixture to create a BasicoModel instance
    with a function-defined SBML path.
    Each test can pass its own path as an argument.
    """
    def _create_model(sbml_path):
        return BasicoModel(sbml_folder_path=sbml_path)

    return _create_model

# ✅ SUCCESSFUL SBML DIRECTORY VALIDATION (CUSTOM PATH)
def test_validate_sbml_file_path_success(tmp_path):
    """
    Test SBML directory validation when XML files exist using a temporary folder.
    """
    sbml_path = tmp_path / "models"
    os.makedirs(sbml_path, exist_ok=True)

    with open(sbml_path / "dummy_model.xml", "w", encoding="utf-8") as f:
        f.write("<sbml></sbml>")

    model = BasicoModel(sbml_folder_path=str(sbml_path))
    assert model is not None

# ✅ FAILURE WHEN SBML DIRECTORY IS EMPTY (CUSTOM PATH)
def test_validate_sbml_file_path_failure(dynamic_model_creator):
    """
    Test SBML directory validation failure
    when no XML files are found using a function-defined path.
    """
    sbml_path = "vpeleaderboard/data/empty_folder"
    os.makedirs(sbml_path, exist_ok=True)
    with pytest.raises(ValueError,
                       match=rf"No SBML files found in {str(sbml_path).replace('\\', '/')}"):
        dynamic_model_creator(str(sbml_path))

def test_validate_sbml_file_path_failure1(temp_folder):
    """
    Test SBML directory validation failure when no XML files are found.
    """
    os.makedirs(temp_folder, exist_ok=True)

    with unittest.mock.patch("os.listdir", return_value=[]):
        with pytest.raises(ValueError,
                           match=rf"No SBML files found in {str(temp_folder).replace('\\', '/')}"):
            BasicoModel(sbml_folder_path=str(temp_folder))

# ✅ TEST FAILURE WHEN SBML DIRECTORY DOES NOT EXIST
def test_non_existent_sbml_directory():
    """
    Test SBML directory validation failure when directory does not exist.
    """
    non_existent_path = "vpeleaderboard/data/non_existent"
    if os.path.exists(non_existent_path):
        os.rmdir(non_existent_path)

    with pytest.raises(ValueError, match=f"SBML folder not found: {non_existent_path}"):
        BasicoModel(sbml_folder_path=non_existent_path)

# ✅ TEST METADATA EXTRACTION
def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_folder_path="vpeleaderboard/data/models")
    metadata = model.get_model_metadata("BIOMD0000000064_url.xml")
    assert metadata["Model Name"] == 'Teusink2000_Glycolysis'
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] == len(basico.get_parameters())
    assert metadata["Description"] is not None

# ✅ MOCK TEST CLASS FOR ABSTRACT `SysBioModel`
class MockModel(SysBioModel):
    """
    Mock implementation of SysBioModel for testing.
    """
    def get_model_metadata(self) -> pd.DataFrame:
        """Mock implementation returning empty DataFrame"""
        return pd.DataFrame()

# ✅ TEST VALID SBML DIRECTORY
@pytest.fixture(name="valid_sbml_folder_path")
def valid_sbml_folder(tmp_path):
    """Creates a temporary directory with a dummy XML file."""
    folder = tmp_path / "models"
    os.makedirs(folder, exist_ok=True)
    with open(folder / "dummy_model.xml", "w", encoding="utf-8") as f:
        f.write("<sbml></sbml>")
    return folder

def test_valid_sbml_directory(valid_sbml_folder_path):
    """
    Test case where the SBML directory contains valid XML files.
    """
    model = MockModel(sbml_file_path=str(valid_sbml_folder_path), name="ValidModel")
    assert model is not None
