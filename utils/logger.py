from datetime import datetime


def log(message: str):
    """Print a message with the computer's local date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
