"""Environment-based application configuration. No credentials are stored here."""
import os


def get_app_config():
    return {
        "base_url": os.getenv("BASE_URL", "https://www.saucedemo.com").rstrip("/"),
    }
