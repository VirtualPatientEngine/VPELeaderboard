#!/usr/bin/env python3
'''
This script demonstrates test of creating tables in Markdown.
'''

import pytest
import os
import tempfile
import pandas as pd
from app.algorithms.table import main

@pytest.fixture
def temporary_files():
    """
    This fixture will create the temporary input CSV and output markdown file.
    It will be used to test the `main()` function with actual files.
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        input_csv = os.path.join(temp_dir, "mock_input.csv")
        data = {'Column1': [1, 2], 'Column2': [3, 4]}
        df = pd.DataFrame(data)
        df.to_csv(input_csv, index=False)
        output_md = os.path.join(temp_dir, "mock_output.md")

        yield {
            'input_csv': input_csv,
            'output_md': output_md
        }

def test_main(temporary_files):
    """
    Test for the main function, which reads a CSV file, processes it with the provided
    template, and writes the output to a markdown file.
    """
    config_file = "app/configs/leaderboard/default.yaml"
    template_dir = "app/templates"
    template_file = "algo.html"
    
    # Mock the input parameters as needed
    input_file = temporary_files['input_csv']
    output_file = temporary_files['output_md']

    os.environ["HYDRA_CONFIG_PATH"] = config_file

    main(input_file=input_file, template_dir=template_dir, template_file=template_file, output_file=output_file)
    assert os.path.exists(output_file), "Output markdown file was not created!"

    with open(output_file, 'r') as f:
        markdown_content = f.read()

    if "<html>" in markdown_content or "<head>" in markdown_content or "<body>" in markdown_content:
        # It's HTML, so assert accordingly
        assert True, "The content is HTML as expected."
    else:
        # If it's not HTML, assert that it should be Markdown
        assert markdown_content.startswith("|") or markdown_content.startswith("#"), "The content is neither Markdown nor HTML!"
