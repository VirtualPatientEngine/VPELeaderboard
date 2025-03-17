"""
A test class for pytest unit testing.
"""

import os
import unittest.mock
import pytest
import basico
from vpeleaderboard.data.src.basico_model import BasicoModel
from vpeleaderboard.data.src.sys_bio_model import SysBioModel
from tests.vpeleaderboard.data.utils.utils import (
    MockModel,
    model_fixture,
    temp_folder_fixture,
    valid_sbml_folder
)

class TestSysBioModel(SysBioModel):
    """Concrete subclass to test abstract SysBioModel"""
    def get_model_metadata(self):
        """Dummy method implementation for testing"""
        return None

def test_missing_sbml_file_path():
    """
    Test that SysBioModel raises a ValueError when sbml_file_path is not provided.
    """
    with pytest.raises(ValueError, match="sbml_file_path must be provided."):
        TestSysBioModel(name="Test Model")
def test_with_fixtures():
    """Test to ensure all fixtures are accessible and not None."""
    assert model_fixture is not None
    assert temp_folder_fixture is not None
    assert valid_sbml_folder is not None

def test_validate_sbml_file_path_success(tmp_path):
    """
    Test SBML directory validation when XML files exist using a temporary folder.
    """
    sbml_path = tmp_path / "models"
    os.makedirs(sbml_path, exist_ok=True)

    with open(sbml_path / "dummy_model.xml", "w", encoding="utf-8") as f:
        f.write("<sbml></sbml>")

    model = BasicoModel(sbml_file_path=str(sbml_path))
    assert model is not None

def sbml_file_path():
    '''
    Test the check_biomodel_id_or_sbml_file_path method of the BioModel class.
    '''
    with pytest.raises(ValueError):
        SysBioModel(name="Test Model", description="A test model")

def test_validate_sbml_file_path_failure():
    """
    Test SBML directory validation failure
    when no XML files are found using a function-defined path.
    """
    sbml_path = "vpeleaderboard/data/empty_folder"
    os.makedirs(sbml_path, exist_ok=True)
    with pytest.raises(ValueError,
                       match=f"Invalid SBML file format: {sbml_path}. Expected an XML file."):
        BasicoModel(sbml_file_path=sbml_path)

def test_validate_sbml_file_path_failure1(temp_folder):
    """
    Test SBML directory validation failure when no XML files are found.
    """
    os.makedirs(temp_folder, exist_ok=True)

    with unittest.mock.patch("os.listdir", return_value=[]):
        with pytest.raises(
            ValueError,
            match=rf"""Invalid SBML file format: {temp_folder}. Expected an XML file."""):
            BasicoModel(sbml_file_path=str(temp_folder))

def test_non_existent_sbml_directory():
    """
    Test SBML directory validation failure when directory does not exist.
    """
    non_existent_path = "vpeleaderboard/data/non_existent"
    if os.path.exists(non_existent_path):
        os.rmdir(non_existent_path)

    with pytest.raises(ValueError, match=f"SBML file not found: {non_existent_path}"):
        BasicoModel(sbml_file_path=non_existent_path)

def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_file_path="vpeleaderboard/data/models")
    metadata = model.get_model_metadata()
    assert metadata["Model Name"] == 'Teusink2000_Glycolysis'
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] == len(basico.get_parameters())
    assert metadata["Description"] is not None

def test_valid_sbml_directory(valid_sbml_file_path):
    """
    Test case where the SBML directory contains valid XML files.
    """
    model = MockModel(sbml_file_path=str(valid_sbml_file_path), name="ValidModel")
    assert model is not None
