import os
from parser import parse_log_line
from detector import detect_anomaly
from alert import send_alert

LOG_FILE = os.path.join("sample_logs", "app.log")

def main():
    if not os.path.exists(LOG_FILE):
        print(f"No log file found at {LOG_FILE}")
        return

    with open(LOG_FILE, "r") as f:
        for line in f:
            log_entry = parse_log_line(line.strip())
            if detect_anomaly(log_entry):
                send_alert(log_entry)

if __name__ == "__main__":
    main()
