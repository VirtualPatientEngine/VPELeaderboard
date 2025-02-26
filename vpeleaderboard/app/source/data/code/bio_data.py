# import logging
# import os
# from typing import Optional, Dict, Union, List
# import pandas as pd
# import basico
# from abc import ABC, abstractmethod
# from pydantic import BaseModel, Field, model_validator
# from jinja2 import Environment, FileSystemLoader
# from source.data.utils.markdown import create_markdown, save_markdown

# # Initialize logger
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class SysBioModel(ABC, BaseModel):
#     """
#     Abstract base class for BioModels in the BioModels repository.
#     """
#     sbml_file_path: Optional[str] = Field(None, description="Path to an SBML file")

#     @model_validator(mode="after")
#     def validate_sbml_file_path(cls, values):
#         """
#         Ensure the SBML directory contains valid XML files.
#         """
#         xml_dir = "docs/app/code/data/xml_files"
#         if not os.path.exists(xml_dir) or not os.listdir(xml_dir):
#             raise ValueError("No SBML files found in the directory docs/app/code/data/xml_files.")
#         return values

#     @abstractmethod
#     def get_model_metadata(self) -> pd.DataFrame:
#         """
#         Abstract method to retrieve metadata of the model.
#         """

# class ModelData(SysBioModel):
#     """
#     Model that loads and simulates SBML models using the basico package.
#     """
#     copasi_model: Optional[object] = None  # Holds the loaded Copasi model

#     def get_model_metadata(self) -> pd.DataFrame:
#         """
#         Retrieve metadata for all SBML models in the directory.
#         """
#         xml_dir = "docs/app/code/data/xml_files"
#         xml_files = [f for f in os.listdir(xml_dir) if f.endswith(".xml")]
        
#         if not xml_files:
#             raise ValueError("No SBML files found in the directory docs/app/code/data/xml_files.")
        
#         metadata_list = []
#         for xml_file in xml_files:
#             file_path = os.path.join(xml_dir, xml_file)
#             copasi_model = basico.load_model(file_path)
#             model_name = basico.model_info.get_model_name(model=copasi_model)
#             species_count = len(basico.model_info.get_species(model=copasi_model))
#             parameter_count = len(basico.model_info.get_parameters(model=copasi_model))
#             model_description = basico.model_info.get_notes(model=copasi_model)
            
#             metadata_list.append({
#                 "Model Name": model_name,
#                 "Number of Species": species_count,
#                 "Number of Parameters": parameter_count,
#                 "Description": model_description.strip()  # Kept for abstract toggle
#             })
        
#         return pd.DataFrame(metadata_list)

# # Example usage
# if __name__ == "__main__":
#     biomodel = ModelData()
#     metadata_df = biomodel.get_model_metadata()
#     metadata_list = metadata_df.to_dict(orient='records')
    
#     markdown_content = biomodel.markdown.create_markdown(metadata_list, "docs/templates", "topic.txt")
#     biomodel.save_markdown(markdown_content, "docs/reports/biomodel_report.md")
#     print(metadata_df)
import os
import sys
import logging
import pandas as pd
import basico
from pydantic import Field, model_validator
from typing import Optional, Dict, Union
from vpeleaderboard.app.source.data.code.sys_model import SysModel
from vpeleaderboard.app.source.data.utils.markdown import create_markdown, save_markdown

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelData(SysModel):
    """
    Model that loads and simulates SBML models using the basico package.
    """
    sbml_folder_path: Optional[str] = Field(None, description="Path to an SBML files folder")
    simulation_results: Optional[pd.DataFrame] = None
    name: Optional[str] = Field("", description="Name of the model")
    description: Optional[str] = Field("", description="Description of the model")

    copasi_model: Optional[object] = None
    model_config = {"arbitrary_types_allowed": True}

    @model_validator(mode="after")
    def validate_sbml_folder_path(self):
        """
        Validate that the SBML folder exists and contains XML files.
        """
        if not self.sbml_folder_path:
            logger.error("SBML folder path must be provided.")
            raise ValueError("SBML folder path must be provided.")

        if not os.path.exists(self.sbml_folder_path):
            logger.error(f"SBML folder not found: {self.sbml_folder_path}")
            raise ValueError(f"SBML folder not found: {self.sbml_folder_path}")

        xml_files = [f for f in os.listdir(self.sbml_folder_path) if f.endswith(".xml")]
        if not xml_files:
            logger.error(f"No SBML files found in {self.sbml_folder_path}.")
            raise ValueError(f"No SBML files found in {self.sbml_folder_path}.")
        
        return self  # Ensure the validator returns the object itself
    def get_model_metadata(self, sbml_file: str) -> Dict[str, Union[str, int]]:
            """
            Retrieve metadata for a single SBML model.
            
            Returns:
                Dictionary with model metadata.
            """
            file_path = os.path.join(self.sbml_folder_path, sbml_file)
            copasi_model = basico.load_model(file_path)

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

        # xml_dir = "docs/app/code/data/xml_files"
        # xml_files = [f for f in os.listdir(xml_dir) if f.endswith(".xml")]
        
        # if not xml_files:
        #     raise ValueError("No SBML files found in the directory docs/app/code/data/xml_files.")
        
        # metadata_list = []
        # for xml_file in xml_files:
        #     file_path = os.path.join(xml_dir, xml_file)
        #     copasi_model = basico.load_model(file_path)
        #     model_name = basico.model_info.get_model_name(model=copasi_model)
        #     species_count = len(basico.model_info.get_species(model=copasi_model))
        #     parameter_count = len(basico.model_info.get_parameters(model=copasi_model))
        #     model_description = basico.model_info.get_notes(model=copasi_model)
            
        #     metadata_list.append({
        #         "Model Name": model_name,
        #         "Number of Species": species_count,
        #         "Number of Parameters": parameter_count,
        #         "Description": model_description.strip()
        #     })
        
        # return pd.DataFrame(metadata_list)
    def generate_markdown_report(self, output_path: str = "docs/reports/biomodel_report.md"):
        """
        Generate and save a markdown report of the models' metadata.
        """
        metadata_list = [self.get_model_metadata(file) for file in os.listdir(self.sbml_folder_path) if file.endswith(".xml")]
        metadata_df = pd.DataFrame(metadata_list)  # Convert list to DataFrame
        
        metadata_records = metadata_df.to_dict(orient='records')  # Convert DataFrame to list of dicts
        markdown_content = create_markdown(metadata_records, "vpeleaderboard/templates", "topic.txt")

        output_file = "docs/reports/biomodel_report.md"  # ✅ Ensure correct path
        save_markdown(markdown_content, output_file)

        logger.info(f"Markdown report saved at: {output_file}")


# Example usage
# if __name__ == "__main__":
    # biomodel = ModelData()
    # metadata_df = biomodel.get_model_metadata()
    # metadata_list = metadata_df.to_dict(orient='records')
    
    # markdown_content = create_markdown(metadata_list, "vpeleaderboard/templates", "topic.txt")
    # save_markdown(markdown_content, "vpeleaderboards/reports/biomodel_report.md")
    # print(metadata_df)
if __name__ == "__main__":
    logger.info("Running bio_data.py as main script")

    folder_path = "vpeleaderboard/app/source/data/models"  # Folder containing multiple SBML files
    biomodel = ModelData(sbml_folder_path=folder_path)

    # Get all XML files in the folder
    xml_files = [f for f in os.listdir(folder_path) if f.endswith(".xml")]

    metadata_records = []  # List to store metadata dictionaries

    # Loop through each file and collect metadata
    for xml_file in xml_files:
        metadata = biomodel.get_model_metadata(xml_file)
        metadata_records.append(metadata)

    # Convert to DataFrame
    metadata_df = pd.DataFrame(metadata_records)

    # Print metadata
    print("Model Metadata for all files:")
    print(metadata_df)

    # Generate markdown report
    biomodel.generate_markdown_report()

