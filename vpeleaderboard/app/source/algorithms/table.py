#!/usr/bin/env python3
'''
This script demonstrates draft of creating tables in Markdown.
'''
import os
import pandas as pd
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
        headers=["Abstract"] + df.columns.tolist()
        # headers=df.columns.tolist()
    )
    return markdown_content

def save_markdown(markdown_content, output_path):
    """Saves the generated markdown content to a file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def main():
    input_file = "docs/app/code/algorithms/mock_data/query.csv"
    template_dir = "docs/templates"
    template_file = "topic.txt"
    output_file = "docs/output1.md"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Read the data
    df = read_tsv(input_file)
    print("DEBUG: Extracted Data ->", df)
    # Generate Markdown content
    markdown_content = create_markdown(df, template_dir, template_file)
    print("DEBUG: Rendered HTML ->", markdown_content)
    
    # Save the Markdown file
    save_markdown(markdown_content, output_file)
    print(f"Markdown file saved to {output_file}")

if __name__ == "__main__":
    main()


