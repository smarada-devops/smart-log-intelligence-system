import re
from typing import Dict

LOG_PATTERN = re.compile(r"(?P<timestamp>\S+ \S+) (?P<level>\w+) (?P<message>.+)")

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parse a single log line into structured format.
    Example log:
    2025-09-20 12:34:56 ERROR Something went wrong
    """
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return {"raw": line}
