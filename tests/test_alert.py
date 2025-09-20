import sys
from pathlib import Path

# Add project root to sys.path so 'src' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.alert import send_alert

def test_send_alert(capsys):
    log_entry = {"timestamp": "2025-09-20 12:34:56", "level": "ERROR", "message": "Disk full"}
    msg = send_alert(log_entry)
    captured = capsys.readouterr()
    assert "[ALERT]" in msg
    assert "Disk full" in captured.out
