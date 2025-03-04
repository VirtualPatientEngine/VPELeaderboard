"""
A test BasicoModel class for pytest unit testing.
"""

import os
import pytest
from vpeleaderboard.data.src.basico_model import BasicoModel

@pytest.fixture(name="model")
def model_fixture():
    """
    A fixture for the BasicoModel class.
    """
    return BasicoModel(sbml_folder_path="vpeleaderboard/data/models")

def test_validate_sbml_folder_path_success():
    """
    Test SBML directory validation when XML files exist.
    """
    assert os.path.exists("vpeleaderboard/data/models")
    assert len([f for f in os.listdir("vpeleaderboard/data/models") if f.endswith(".xml")]) > 0
    model = BasicoModel(sbml_folder_path="vpeleaderboard/data/models")
    assert model is not None

def test_validate_sbml_folder_path_failure():
    """
    Test SBML directory validation failure when no XML files are found.
    """
    empty_folder = "vpeleaderboard/data/empty_folder"
    os.makedirs(empty_folder, exist_ok=True)

    with pytest.raises(ValueError, match="No SBML files found in vpeleaderboard/data/empty_folder"):
        BasicoModel(sbml_folder_path=empty_folder)

def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_folder_path="vpeleaderboard/data/models")
    metadata = model.get_model_metadata("BIOMD0000000064_url.xml")
    assert metadata["Model Name"] is not None
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] >= 0
    assert metadata["Description"] is not None

def test_sbml_folder_path_not_provided():
    """
    Test that a ValueError is raised when sbml_folder_path is not provided.
    """
    with pytest.raises(ValueError, match="SBML folder path must be provided."):
        BasicoModel(sbml_folder_path=None)

def test_sbml_folder_not_found():
    """
    Test that a ValueError is raised when the sbml_folder_path does not exist.
    """
    non_existent_folder = "vpeleaderboard/data/non_existent_models"
    assert not os.path.exists(non_existent_folder), f"""
    No SBML files found in the directory {non_existent_folder}
    """
    with pytest.raises(ValueError, match=f"SBML folder not found: {non_existent_folder}"):
        BasicoModel(sbml_folder_path=non_existent_folder)
