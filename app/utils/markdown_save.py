#!/usr/bin/env python3
'''
This script demonstrates creating tables in Markdown using data from a TSV file.
'''

import os
import logging
from typing import List, Dict, Union
import pandas as pd
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_markdown(markdown_content: str, output_path: str):
    """
    Saves the generated Markdown content to a file, creating the directory if necessary.
    
    Args:
        markdown_content (str): The markdown content to save.
        output_path (str): The file path where markdown should be saved.
    """
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    logger.info("Markdown report saved at: %s", output_path)

def create_markdown(data: Union[List[Dict[str, Union[str, int]]], pd.DataFrame],
                    template_dir: str, template_file: str) -> str:
    """
    Generates a Markdown file using Jinja2 templating.

    Args:
        data (Union[List[Dict[str, Union[str, int]]], pd.DataFrame]):
        The data to be rendered in the template.
        template_dir (str): The directory containing the Jinja2 template file.
        template_file (str): The name of the Jinja2 template file.

    Returns:
        str: The generated Markdown content.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    # Convert DataFrame to list of dictionaries if necessary
    if isinstance(data, pd.DataFrame):
        df_dict = data.to_dict(orient='records')
        headers = data.columns.tolist()
    else:
        df_dict = data
        headers = data[0].keys() if data else []
    markdown_content = template.render(
        current_time=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        table=df_dict,
        headers=headers
    )
    return markdown_content
