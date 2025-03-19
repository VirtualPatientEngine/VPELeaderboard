"""
A test BasicoModel class for pytest unit testing.
"""

import os
import pytest
from vpeleaderboard.data.src.basico_model import BasicoModel

def test_validate_sbml_folder_path_success():
    """
    Test SBML directory validation when XML files exist.
    """
    assert os.path.exists("vpeleaderboard/data/models")
    assert len([f for f in os.listdir("vpeleaderboard/data/models") if f.endswith(".xml")]) > 0
    model = BasicoModel("vpeleaderboard/data/models/BIOMD0000000064_url 1.xml")
    assert model is not None

def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_file_path="vpeleaderboard/data/models/BIOMD0000000064_url 1.xml")
    metadata = model.get_model_metadata()
    assert metadata["Model Name"] is not None
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] >= 0
    assert metadata["Description"] is not None

# def test_sbml_file_path_not_provided():
#     """
#     Test that a ValueError is raised when sbml_folder_path is not provided.
#     """
#     # with pytest.raises(ValueError,
#     #                    match="sbml_file_path must be provided."):
#     #     BasicoModel(sbml_file_path=None)
#     model = BasicoModel()
#     print("_____________________________________________________")
#     print(model)
#     assert model == "SBML file must be provided."

# def test_sbml_file_not_found():
#     """
#     Test that a ValueError is raised when the sbml_folder_path does not exist.
#     """
#     non_existent_folder = "vpeleaderboard/data/non_existent_models"
#     assert not os.path.exists(non_existent_folder), f"""
#     No SBML files found in the directory {non_existent_folder}
#     """
#     # with pytest.raises(ValueError, match=f"SBML file not found: {non_existent_folder}"):
#     #     BasicoModel(sbml_file_path=non_existent_folder)
