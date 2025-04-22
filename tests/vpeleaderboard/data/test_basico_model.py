"""
A test BasicoModel class for pytest unit testing.
"""

import os
from vpeleaderboard.data.src.basico_model import BasicoModel

MODEL_PATH = "vpeleaderboard/data/models/BIOMD0000000064_url.xml"

def test_validate_sbml_folder_path_success():
    """
    Test SBML directory validation when XML files exist.
    """
    assert os.path.exists("vpeleaderboard/data/models")
    assert len([f for f in os.listdir("vpeleaderboard/data/models") if f.endswith(".xml")]) > 0
    model = BasicoModel(MODEL_PATH)
    assert model is not None

def test_get_model_metadata():
    """
    Test the get_model_metadata method of the BasicoModel class.
    """
    model = BasicoModel(sbml_file_path=MODEL_PATH)
    metadata = model.get_model_metadata()
    assert metadata["Model Name"] is not None
    assert metadata["Number of Species"] >= 0
    assert metadata["Number of Parameters"] >= 0
    assert metadata["Description"] is not None
