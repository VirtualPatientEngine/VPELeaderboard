#!/usr/bin/env python3
'''
This script demonstrates draft of creating tables in Markdown.
'''

import os
import pandas as pd
import hydra
from jinja2 import Environment, FileSystemLoader

def read_tsv(file_path):
    """Reads a TSV file and returns a Pandas DataFrame."""
    return pd.read_csv(file_path)

def create_markdown(df, template_dir, template_file):
    """Generates a markdown file from a Jinja2 template and a DataFrame."""
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)
    markdown_content = template.render(
        current_time=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        table=df.to_dict(orient='records'),
        headers=df.columns.tolist()
    )
    return markdown_content

def save_markdown(markdown_content, output_path):
    """Saves the generated markdown content to a file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def main():
    """Main function using Hydra for configuration management."""
    # Load hydra configuration
    with hydra.initialize(version_base=None, config_path="../config/leaderboard"):
        cfg = hydra.compose(config_name='default')
    
    input_file = cfg.paths.input_file
    template_dir = cfg.paths.template_dir
    template_file = cfg.paths.template_file
    output_file = cfg.paths.output_file
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = read_tsv(input_file)
    markdown_content = create_markdown(df, template_dir, template_file)
    save_markdown(markdown_content, output_file)

if __name__ == "__main__":
    main()
