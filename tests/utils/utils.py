"""
A test markdown class for pytest unit testing.
"""

import os
import pytest
import pandas as pd
from vpeleaderboard.data.src.basico_model import BasicoModel
from vpeleaderboard.data.src.sys_bio_model import SysBioModel

@pytest.fixture(name="temp_folder")
def temp_folder_fixture():
    """Checks for an empty temporary directory."""
    return "vpeleaderboard/data/models"

@pytest.fixture(name="valid_sbml_file_path")
def valid_sbml_folder(tmp_path):
    """Creates a temporary directory with a dummy XML file."""
    folder = tmp_path / "models"
    os.makedirs(folder, exist_ok=True)
    with open(folder / "dummy_model.xml", "w", encoding="utf-8") as f:
        f.write("<sbml></sbml>")
    return folder

class MockModel(SysBioModel):
    """Mock implementation of SysBioModel for testing."""
    def get_model_metadata(self) -> pd.DataFrame:
        return pd.DataFrame()
