# pytest tests for mini_internet.py (safe, non-executing)
# This test does NOT import mini_internet.py because the script runs interactive code at import-time.
# Instead it reads the file contents and asserts the presence of key strings (imports and prompts).

from pathlib import Path

REPO_ROOT = Path(__file__).parent
SCRIPT_PATH = REPO_ROOT / "mini_internet.py"

def test_file_exists():
    assert SCRIPT_PATH.exists(), "mini_internet.py should exist in the repository root"

def test_contains_webbrowser_import():
    text = SCRIPT_PATH.read_text(encoding="utf-8")
    assert "import webbrowser as wb" in text, "Expected 'import webbrowser as wb' in mini_internet.py"

def test_contains_user_prompts():
    text = SCRIPT_PATH.read_text(encoding="utf-8")
    # check for the choice prompt and at least one of the search prompts
    assert "Enter the choice" in text or "Enter the choice (1 or 2)" in text, "Expected choice prompt in script"
    assert "Enter your query on Google" in text or "Enter your query on YouTube" in text, "Expected query prompts in script"