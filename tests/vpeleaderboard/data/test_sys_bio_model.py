"""
A test class for pytest unit testing.
"""

import os
import basico
from vpeleaderboard.data.src.basico_model import BasicoModel
from vpeleaderboard.data.src.sys_bio_model import SysBioModel
from ...utils.utils import (
    MockModel,
    temp_folder_fixture,
    valid_sbml_folder
)

class TestSysBioModel(SysBioModel):
    """Concrete subclass to test abstract SysBioModel"""
    def get_model_metadata(self):
        """Dummy method implementation for testing"""
        return None

def test_with_fixtures():
    """Test to ensure all fixtures are accessible and not None."""
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

def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_file_path="vpeleaderboard/data/models/BIOMD0000000064_url.xml")
    metadata = model.get_model_metadata()
    assert metadata["Model Name"] == 'Dwivedi2014 - Crohns IL6 Disease model - Anti-IL6R Antibody'
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] == len(basico.get_parameters())
    assert metadata["Description"] is not None

def test_valid_sbml_directory(valid_sbml_file_path):
    """
    Test case where the SBML directory contains valid XML files.
    """
    model = MockModel(sbml_file_path=str(valid_sbml_file_path), name="ValidModel")
    assert model is not None
