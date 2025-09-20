from typing import Dict

def detect_anomaly(log_entry: Dict[str, str]) -> bool:
    """
    Very basic anomaly detection.
    Flags ERROR and CRITICAL log levels as anomalies.
    """
    level = log_entry.get("level", "")
    return level in {"ERROR", "CRITICAL"}
