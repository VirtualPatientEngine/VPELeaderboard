"""
A test markdown class for pytest unit testing.
"""

import os
import pytest
from vpeleaderboard.data.src.basico_model import BasicoModel
from app.data.markdown_report import generate_markdown_report

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
    assert os.path.exists(empty_folder)
    assert len(os.listdir(empty_folder)) == 0
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

def test_generate_markdown_report():
    """
    Test the generate_markdown_report function.
    """
    folder_path = "vpeleaderboard/data/models"
    output_path = "tests/test_index.md"
    assert os.path.exists(folder_path)
    generate_markdown_report(folder_path, output_path)
    assert os.path.exists(output_path)
    os.remove(output_path)
