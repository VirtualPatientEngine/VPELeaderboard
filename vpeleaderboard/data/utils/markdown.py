'''
file with functions to generate markdown.
'''

import os
from typing import List, Dict, Union
import pandas as pd
from jinja2 import Environment, FileSystemLoader


def create_markdown(data: List[Dict[str, Union[str, int]]],
                    template_dir: str, template_file: str) -> str:
    """
    Generates a Markdown file using Jinja2 templating.

    Args:
        data (List[Dict[str, Union[str, int]]]): The data to be rendered in the template.
        template_dir (str): The directory containing the Jinja2 template file.
        template_file (str): The name of the Jinja2 template file.

    Returns:
        str: The generated Markdown content.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    markdown_content = template.render(
        current_time=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        table=data,
        headers=["Model Name", "Number of Species", "Number of Parameters"]
    )
    return markdown_content


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
    print(f"Markdown file saved to {output_path}")
