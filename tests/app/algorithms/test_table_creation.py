#!/usr/bin/env python3
'''
This script demonstrates test of creating tables in Markdown.
'''

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd 
from app.algorithms.table import main  # Ensure correct import

class TestMarkdownScript(unittest.TestCase):
    """
    Test class for the Markdown script.
    """

    @patch("app.algorithms.table.pd.read_csv")
    @patch("app.algorithms.table.create_markdown")
    @patch("app.algorithms.table.save_markdown")
    @patch("app.algorithms.table.hydra.initialize")
    @patch("app.algorithms.table.hydra.compose")
    def test_main(self, *mocks):
        """
        Tests the main function of the markdown table creation script.
        It mocks dependencies, ensuring proper function calls and flow.
        """
        mock_objects = {
            "mock_compose": mocks[0],
            "mock_initialize": mocks[1],
            "mock_save_markdown": mocks[2],
            "mock_create_markdown": mocks[3],
            "mock_read_csv": mocks[4],
        }

        # Mock Hydra config
        mock_cfg = MagicMock()
        mock_cfg.algorithms.paths.input_file = "test.csv"
        mock_cfg.algorithms.paths.template_dir = "templates"
        mock_cfg.algorithms.paths.template_file = "template.md"
        mock_cfg.algorithms.paths.output_file = "output.md"
        mock_objects["mock_compose"].return_value = mock_cfg

        # Mock Pandas DataFrame
        mock_df = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6]})
        mock_objects["mock_read_csv"].return_value = mock_df

        # Mock create_markdown function
        mock_objects["mock_create_markdown"].return_value = "# Sample Markdown"

        # Execute main function
        main()

        # Assertions
        mock_objects["mock_initialize"].assert_called_once()
        mock_objects["mock_compose"].assert_called_once_with(config_name="config",
                                                             overrides=["algorithms=default"])
        mock_objects["mock_read_csv"].assert_called_once_with("test.csv")
        mock_objects["mock_create_markdown"].assert_called_once_with(mock_df,
                                                                     "templates", "template.md")
        mock_objects["mock_save_markdown"].assert_called_once_with("# Sample Markdown", "output.md")

if __name__ == "__main__":
    unittest.main()
