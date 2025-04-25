"""
Markdown report generator for SBML model metadata.

This script loads SBML models from a specified folder,
extracts metadata, and generates a markdown report.
"""

import sys
import os
import logging
import pandas as pd
import hydra
from vpeleaderboard.data.src.basico_model import BasicoModel
from ..utils import create_markdown, save_markdown

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def generate_markdown_report(input_folder: str,
                             template_dir: str,
                             template_file: str,
                             output_file: str):
    """
    Generate and save a markdown report of the models' metadata.

    Args:
        input_folder (str): Path to the folder containing SBML XML files.
        template_dir (str): Path to the template directory.
        template_file (str): Template file name.
        output_file (str): Path where the markdown report will be saved.
    """
    metadata_list = []
    for file in os.listdir(input_folder):
        if file.endswith(".xml"):
            file = os.path.abspath(os.path.join(input_folder, file))
            biomodel = BasicoModel(sbml_file_path=file)
            metadata_list.append(biomodel.get_model_metadata())
    metadata_df = pd.DataFrame(metadata_list)
    metadata_records = metadata_df.to_dict(orient='records')

    markdown_content = create_markdown(metadata_records, template_dir, template_file)
    save_markdown(markdown_content, output_file)
    logger.info("Markdown report saved at: %s", output_file)

if __name__ == "__main__":
    with hydra.initialize(version_base=None, config_path="../configs"):
        cfg = hydra.compose(config_name="config",
                            overrides=["data=default"])
    cfg = cfg.data
    logger.info("Generating markdown report")
    generate_markdown_report(
        input_folder=cfg.paths.input_folder,
        template_dir=cfg.paths.template_dir,
        template_file=cfg.paths.template_file,
        output_file=cfg.paths.output_file
    )
