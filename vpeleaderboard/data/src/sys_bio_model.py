# #!/usr/bin/env python3
"""
An abstract base class for Models in the data module.
"""

from typing import Optional
from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field

class SysBioModel(BaseModel, ABC):
    """
    Abstract base class for Models in the data section, allowing
    different mathematical approaches to be implemented in subclasses.

    This class enforces a standard interface for models working
    with SBML (Systems Biology Markup Language) files.
    """
    sbml_file_path: str = Field(..., description="Path to an SBML file")
    name: Optional[str] = Field(..., description="Name of the model")
    description: Optional[str] = Field("", description="Description of the model")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.sbml_file_path:
            raise ValueError("sbml_file_path must be provided.")

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
