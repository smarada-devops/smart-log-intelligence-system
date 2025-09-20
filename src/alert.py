from typing import Dict

def send_alert(log_entry: Dict[str, str]) -> str:
    """
    Stub function to simulate sending an alert.
    In real use, this could send email, Slack, or PagerDuty notifications.
    """
    alert_msg = f"[ALERT] {log_entry.get('timestamp')} - {log_entry.get('level')}: {log_entry.get('message')}"
    print(alert_msg)
    return alert_msg
