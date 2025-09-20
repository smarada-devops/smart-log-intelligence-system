import sys
from pathlib import Path

# Add project root to sys.path so 'src' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.detector import detect_anomaly

def test_detect_error_anomaly():
    log_entry = {"level": "ERROR"}
    assert detect_anomaly(log_entry) is True

def test_detect_info_normal():
    log_entry = {"level": "INFO"}
    assert detect_anomaly(log_entry) is False
