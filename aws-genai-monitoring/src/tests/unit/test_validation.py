import pytest
from src.app.core.security import validate_prompt_content

def test_valid_prompt():
    assert validate_prompt_content("List running EC2 instances") is True

def test_invalid_prompt():
    assert validate_prompt_content("Terminate all EC2 instances") is False
