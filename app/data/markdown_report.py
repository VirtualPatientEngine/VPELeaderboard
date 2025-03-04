"""
Markdown report generator for SBML model metadata.

This script loads SBML models from a specified folder,
extracts metadata, and generates a markdown report.
"""

import os
import logging
import pandas as pd
import hydra
from vpeleaderboard.data.src.basico_model import BasicoModel
from app.data.utils.markdown import create_markdown, save_markdown

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_markdown_report(folder_path: str,
                             template_dir: str,
                             template_file: str,
                             output_path: str):
    """
    Generate and save a markdown report of the models' metadata.

    Args:
        folder_path (str): Path to the folder containing SBML XML files.
        template_dir (str): Path to the template directory.
        template_file (str): Template file name.
        output_path (str): Path where the markdown report will be saved.
    """
    biomodel = BasicoModel(sbml_folder_path=folder_path)
    metadata_list = [
        biomodel.get_model_metadata(file)
        for file in os.listdir(folder_path)
        if file.endswith(".xml")
    ]
    metadata_df = pd.DataFrame(metadata_list)
    metadata_records = metadata_df.to_dict(orient='records')
    markdown_content = create_markdown(metadata_records, template_dir, template_file)
    save_markdown(markdown_content, output_path)
    logger.info("Markdown report saved at: %s", output_path)

if __name__ == "__main__":
    with hydra.initialize(version_base=None, config_path="config"):
        cfg = hydra.compose(config_name="config")

    logger.info("Generating markdown report")
    generate_markdown_report(
        folder_path=cfg.paths.folder_path,
        template_dir=cfg.paths.template_dir,
        template_file=cfg.paths.template_file,
        output_path=cfg.paths.output_path
    )
