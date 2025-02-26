"""
An abstract base class for Models in the Models.
"""

import os
from typing import Optional
from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field, model_validator

class SysModel(ABC, BaseModel):
    """
    Abstract base class for Models in the data section allowing
    different mathematical approaches to be implemented in subclasses.
    """
    sbml_file_path: Optional[str] = Field(None, description="Path to an SBML file")
    name: Optional[str] = Field(..., description="Name of the model")
    description: Optional[str] = Field("", description="Description of the model")

    @model_validator(mode="after")
    def validate_sbml_file_path(self):
        """
        Ensure the SBML directory contains valid XML files.
        """
        xml_dir = "vpeleaderboard/app/source/data/models"
        if not os.path.exists(xml_dir) or not os.listdir(xml_dir):
            raise ValueError(
                "No SBML files found in the directory "
                "vpeleaderboard/app/source/data/models."
            )
        return self

    @abstractmethod
    def get_model_metadata(self) -> pd.DataFrame:
        """
        Abstract method to retrieve metadata of the model.
        """
