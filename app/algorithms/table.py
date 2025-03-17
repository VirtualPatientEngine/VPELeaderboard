#!/usr/bin/env python3
'''
This script demonstrates draft of creating tables in Markdown.
'''

import pandas as pd
import hydra
from app.utils.markdown_save import save_markdown, create_markdown

def main():
    """Main function using Hydra for configuration management."""
    # Load hydra configuration
    with hydra.initialize(version_base=None, config_path="../configs"):
        cfg = hydra.compose(config_name="config",
                            overrides=["algorithms=default"])
    cfg = cfg.algorithms

    input_file = cfg.paths.input_file
    template_dir = cfg.paths.template_dir
    template_file = cfg.paths.template_file
    output_file = cfg.paths.output_file
    df = pd.read_csv(input_file)
    markdown_content = create_markdown(df, template_dir, template_file)
    save_markdown(markdown_content, output_file)

if __name__ == "__main__":
    main()
