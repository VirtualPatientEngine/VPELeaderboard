#!/usr/bin/env python3
"""
An abstract base class for Models in the Models.
"""

import os
from typing import Optional
from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field, model_validator

class SysBioModel(ABC, BaseModel):
    """
    Abstract base class for Models in the data section, allowing
    different mathematical approaches to be implemented in subclasses.

    This class enforces a standard interface for models working
    with SBML (Systems Biology Markup Language) files.
    """
    sbml_file_path: Optional[str] = Field(None, description="Path to an SBML file")
    name: Optional[str] = Field(..., description="Name of the model")
    description: Optional[str] = Field("", description="Description of the model")

    @model_validator(mode="after")
    def validate_sbml_file_path(self):
        """
        Ensure the SBML directory contains valid XML files.

        Args:
            sbml_folder_path (str): The path to the SBML folder.

        Raises:
            ValueError: If the SBML directory does not exist or contains no XML files
        """
        xml_dir = "vpeleaderboard/src/data/models"
        if not os.path.exists(xml_dir) or not os.listdir(xml_dir):
            raise ValueError(
                "No SBML files found in the directory "
                "vpeleaderboard/src/data/models"
            )
        return self

    @abstractmethod
    def get_model_metadata(self) -> pd.DataFrame:
        """
        Abstract method to retrieve metadata of the SBML model.

        This method must be implemented in subclasses to extract and return
        relevant details about the SBML model, such as its structure, components,
        and parameters.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the metadata of the model.
        """
