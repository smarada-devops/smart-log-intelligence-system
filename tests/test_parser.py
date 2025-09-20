import sys
from pathlib import Path

# Add project root to sys.path so 'src' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.parser import parse_log_line

def test_parse_valid_log():
    line = "2025-09-20 12:34:56 ERROR Something went wrong"
    parsed = parse_log_line(line)
    assert parsed["level"] == "ERROR"
    assert "Something went wrong" in parsed["message"]

def test_parse_invalid_log():
    line = "INVALID LOG LINE"
    parsed = parse_log_line(line)
    assert "raw" in parsed
