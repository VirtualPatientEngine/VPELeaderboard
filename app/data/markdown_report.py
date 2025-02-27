# """
# Markdown report generator for SBML model metadata.

# This script loads SBML models from a specified folder,
# extracts metadata, and generates a markdown report.
# """

# import os
# import logging
# import pandas as pd
# from vpeleaderboard.data.src.basico_model import ModelData
# from vpeleaderboard.data.utils.markdown import create_markdown, save_markdown

# # Initialize logger
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def generate_markdown_report(folder_path: str, output_path: str = "docs/data/index.md"):
#     """
#     Generate and save a markdown report of the models' metadata.

#     Args:
#         input_folder_path (str): Path to the folder containing SBML XML files.
#         output_path (str, optional): Path where the markdown report will be saved.
#                                      Defaults to "docs/data/index.md".

#     Returns:
#         None
#     """
#     # print("📌 SBML folder path being passed to ModelData: %s", input_folder_path)
#     biomodel = ModelData(sbml_folder_path=folder_path)
#     # Get metadata for all XML files
#     metadata_list = [
#         biomodel.get_model_metadata(file)
#         for file in os.listdir(folder_path)
#         if file.endswith(".xml")
#         ]
#     metadata_df = pd.DataFrame(metadata_list)
#     # Convert DataFrame to list of dicts
#     metadata_records = metadata_df.to_dict(orient='records')
#     markdown_content = create_markdown(metadata_records, "app/templates", "data.txt")
#     print("DEBUG: Rendered HTML ->", markdown_content)
#     # Save the markdown report
#     save_markdown(markdown_content, output_path)
#     logger.info("Markdown report saved at: %s", output_path)

# if __name__ == "__main__":
#     logger.info("Generating markdown report")
#     FOLDER_PATH = "vpeleaderboard/data/models"  # Folder containing SBML files
#     # print(f"Using SBML folder path: {folder_path}")
#     # print(f"Absolute path: {os.path.abspath(folder_path)}")
#     # print(f"Directory exists: {os.path.exists(folder_path)}")
#     # print(f"Files in directory: {os.listdir(folder_path)
#     # if os.path.exists(folder_path) else 'Directory not found'}")
#     generate_markdown_report(FOLDER_PATH)
"""
Markdown report generator for SBML model metadata.

This script loads SBML models from a specified folder,
extracts metadata, and generates a markdown report.
"""

import os
import logging
import pandas as pd
from vpeleaderboard.data.src.basico_model import ModelData
from vpeleaderboard.data.utils.markdown import create_markdown, save_markdown

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_markdown_report(folder_path: str, output_path: str = "docs/data/index.md"):
    """
    Generate and save a markdown report of the models' metadata.

    Args:
        input_folder_path (str): Path to the folder containing SBML XML files.
        output_path (str, optional): Path where the markdown report will be saved.
                                     Defaults to "docs/data/index.md".

    Returns:
        None
    """
    # print("📌 SBML folder path being passed to ModelData: %s", input_folder_path)
    biomodel = ModelData(sbml_folder_path=folder_path)
    # Get metadata for all XML files
    metadata_list = [
        biomodel.get_model_metadata(file)
        for file in os.listdir(folder_path)
        if file.endswith(".xml")
        ]
    metadata_df = pd.DataFrame(metadata_list)
    # Convert DataFrame to list of dicts
    metadata_records = metadata_df.to_dict(orient='records')
    markdown_content = create_markdown(metadata_records, "app/templates", "data.txt")
    print("DEBUG: Rendered HTML ->", markdown_content)
    # Save the markdown report
    save_markdown(markdown_content, output_path)
    logger.info("Markdown report saved at: %s", output_path)

if __name__ == "__main__":
    logger.info("Generating markdown report")
    FOLDER_PATH = "vpeleaderboard/data/models"  # Folder containing SBML files
    # print(f"Using SBML folder path: {folder_path}")
    # print(f"Absolute path: {os.path.abspath(folder_path)}")
    # print(f"Directory exists: {os.path.exists(folder_path)}")
    # print(f"Files in directory: {os.listdir(folder_path)
    # if os.path.exists(folder_path) else 'Directory not found'}")
    generate_markdown_report(FOLDER_PATH)
