"""
A test markdown class for pytest unit testing.
"""
import pandas as pd
import pytest
from app.utils import create_markdown, save_markdown

# Sample data for testing
SAMPLE_DATA = [
    {"Model Name": "Model A", "Number of Species": 5, "Number of Parameters": 10},
    {"Model Name": "Model B", "Number of Species": 8, "Number of Parameters": 15},
]

# Sample Jinja2 template
SAMPLE_TEMPLATE = """
# Model Report

Generated on: {{ current_time }}

| Model Name | Number of Species | Number of Parameters |
|------------|------------------|----------------------|
{% for row in table %}
| {{ row['Model Name'] }} | {{ row['Number of Species'] }} | {{ row['Number of Parameters'] }} |
{% endfor %}
"""

@pytest.fixture(name= "temp_template")
def temp_template_file(tmp_path):
    """Create a temporary Jinja2 template file."""
    template_file = tmp_path / "template.md"
    template_file.write_text(SAMPLE_TEMPLATE)
    return str(tmp_path), "template.md"

def test_save_markdown(tmp_path):
    """Test if markdown content is saved correctly."""
    output_file = tmp_path / "output.md"
    markdown_content = "# Sample Markdown\n\nThis is a test."
    save_markdown(markdown_content, str(output_file))
    # Check if file was created
    assert output_file.exists()
    # Check file content
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Sample Markdown" in content
    assert "This is a test." in content

def test_create_markdown_with_dataframe(temp_template):
    """Test create_markdown with a Pandas DataFrame input."""
    template_dir, template_file = temp_template

    # Create DataFrame
    df_data = pd.DataFrame([
        {"Model Name": "Model X", "Number of Species": 10, "Number of Parameters": 20},
        {"Model Name": "Model Y", "Number of Species": 15, "Number of Parameters": 25},
    ])

    markdown_content = create_markdown(df_data, template_dir, template_file)

    assert "Model Report" in markdown_content
    assert "Model X" in markdown_content
    assert "10" in markdown_content
    assert "Number of Parameters" in markdown_content
    assert "| Model Name | Number of Species | Number of Parameters |" in markdown_content


def test_create_markdown_with_list_of_dicts(temp_template):
    """Test create_markdown with a list of dictionaries input."""
    template_dir, template_file = temp_template

    # Create List of Dictionaries
    list_data = [
        {"Model Name": "Model A", "Number of Species": 5, "Number of Parameters": 10},
        {"Model Name": "Model B", "Number of Species": 8, "Number of Parameters": 15},
    ]

    markdown_content = create_markdown(list_data, template_dir, template_file)

    assert "Model Report" in markdown_content
    assert "Model A" in markdown_content
    assert "5" in markdown_content
    assert "Number of Parameters" in markdown_content
    assert "| Model Name | Number of Species | Number of Parameters |" in markdown_content


def test_create_markdown_with_empty_list(temp_template):
    """Test create_markdown with an empty list to ensure it handles no data correctly."""
    template_dir, template_file = temp_template

    markdown_content = create_markdown([], template_dir, template_file)

    assert "Model Report" in markdown_content
    assert "| Model Name | Number of Species | Number of Parameters |" in markdown_content
    assert "Generated on" in markdown_content
