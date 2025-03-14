import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
from app.utils.markdown_save import save_markdown, create_markdown
import hydra
from app.leaderboard.table import main  # Assuming the script is saved as table.py

class TestMarkdownScript(unittest.TestCase):
    @patch("app.leaderboard.table.pd.read_csv")
    @patch("app.leaderboard.table.create_markdown")
    @patch("app.leaderboard.table.save_markdown")
    @patch("app.leaderboard.table.hydra.initialize")
    @patch("app.leaderboard.table.hydra.compose")
    @patch("app.leaderboard.table.os.makedirs")  # ✅ Mock os.makedirs to prevent real folder creation
    def test_main(self, mock_makedirs, mock_compose, mock_initialize, mock_save_markdown, mock_create_markdown, mock_read_csv):
        # Mock Hydra config
        mock_cfg = MagicMock()
        mock_cfg.leaderboard.paths.input_file = "test.csv"
        mock_cfg.leaderboard.paths.template_dir = "templates"
        mock_cfg.leaderboard.paths.template_file = "template.md"
        mock_cfg.leaderboard.paths.output_file = "output/output.md"  # ✅ Ensure it has a directory
        mock_compose.return_value = mock_cfg

        # Mock Pandas DataFrame
        mock_df = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6]})
        mock_read_csv.return_value = mock_df

        # Mock create_markdown function
        mock_create_markdown.return_value = "# Sample Markdown"

        # Execute main function
        main()

        # Assertions
        mock_initialize.assert_called_once()
        mock_compose.assert_called_once_with(config_name="config", overrides=["leaderboard=default"])
        mock_read_csv.assert_called_once_with("test.csv")
        mock_create_markdown.assert_called_once_with(mock_df, "templates", "template.md")
        mock_save_markdown.assert_called_once_with("# Sample Markdown", "output/output.md")

        # ✅ Ensure os.makedirs is called with the correct directory
        mock_makedirs.assert_called_once_with("output", exist_ok=True)

if __name__ == "__main__":
    unittest.main()
