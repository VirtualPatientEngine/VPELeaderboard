"""
A test markdown class for pytest unit testing.
"""

import os
import pytest
from vpeleaderboard.data.src.basico_model import BasicoModel
from app.data.markdown_report import generate_markdown_report

def test_validate_sbml_folder_path_success():
    """
    Test SBML directory validation when XML files exist.
    """
    assert os.path.exists("vpeleaderboard/data/models")
    assert len([f for f in os.listdir("vpeleaderboard/data/models") if f.endswith(".xml")]) > 0
    model = BasicoModel(sbml_file_path="vpeleaderboard/data/models")
    assert model is not None

def test_sbml_folder_not_found():
    """
    Test that a ValueError is raised when the sbml_folder_path does not exist.
    """
    non_existent_folder = "vpeleaderboard/data/non_existent_models"
    # Ensure the folder does not exist
    assert not os.path.exists(non_existent_folder), \
        f"Test setup issue: {non_existent_folder} should not exist."

    # Expect ValueError due to missing folder
    with pytest.raises(ValueError, match=f"SBML file not found: {non_existent_folder}"):
        BasicoModel(sbml_file_path=non_existent_folder)

def test_validate_sbml_folder_path_failure():
    """
    Test SBML directory validation failure when no XML files are found.
    """
    empty_folder = "vpeleaderboard/data/empty_folder"
    os.makedirs(empty_folder, exist_ok=True)
    assert os.path.exists(empty_folder)
    assert len(os.listdir(empty_folder)) == 0
    with pytest.raises(ValueError,
                       match=f"Invalid SBML file format: {empty_folder}. Expected an XML file."):
        BasicoModel(sbml_file_path=empty_folder)

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

def test_generate_markdown_report():
    """
    Test the generate_markdown_report function.
    """
    folder_path = "vpeleaderboard/data/models"
    output_path = "tests/test_index.md"
    template_dir = "app/templates"
    template_file = "data.html"
    assert os.path.exists(folder_path)
    generate_markdown_report(folder_path, template_dir, template_file, output_path)
    assert os.path.exists(output_path)
    os.remove(output_path)
