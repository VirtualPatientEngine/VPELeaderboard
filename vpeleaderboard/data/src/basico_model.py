"""
BasicoModel class for loading SBML models
using the basico package.
"""

import os
import logging
from typing import Optional, Dict, Union,Any
import basico
from pydantic import Field
from ..src.sys_bio_model import SysBioModel

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasicoModel(SysBioModel):
    """
    Model that loads SBML models using the basico package.
    Ensures a single instance per component.
    """
    sbml_file_path: str = Field(..., description="Path to an SBML file ")
    simulation_results: Optional[Any] = Field(None, exclude=True)
    name: Optional[str] = ""
    description: Optional[str] = ""
    copasi_model: Optional[object] = Field(None, exclude=True)

    def __init__(self, sbml_file_path: str ,
                 name: Optional[str] = "", description: Optional[str] = ""):
        super().__init__(sbml_file_path=sbml_file_path,
                         name=name, description=description)
        # sbml_file_path = os.path.abspath(sbml_file_path)
        self.sbml_file_path = sbml_file_path
        self.validate_sbml_file_path()

    def validate_sbml_file_path(self):
        """
        Validate that the SBML folder exists and contains XML files.
        """
        if not self.sbml_file_path:
            raise ValueError("SBML file must be provided.")

        if not os.path.exists(self.sbml_file_path):
            raise ValueError(f"SBML file not found: {self.sbml_file_path}")

    def get_model_metadata(self) -> Dict[str, Union[str, int]]:
        """
        Retrieve metadata for a single SBML model.
        """
        # file_path = os.path.join(self.sbml_file_path)
        copasi_model = basico.load_model(self.sbml_file_path)
        model_name = basico.model_info.get_model_name(model=copasi_model)
        species_count = len(basico.model_info.get_species(model=copasi_model))
        parameter_count = len(basico.model_info.get_parameters(model=copasi_model))
        model_description = basico.model_info.get_notes(model=copasi_model)

        return {
            "Model Name": model_name,
            "Number of Species": species_count,
            "Number of Parameters": parameter_count,
            "Description": model_description.strip()

        }
