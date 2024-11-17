import requests
import json
from pathlib import Path


class AIClient:
    CONFIG_PATH = Path("../config/settings.json")

    def __init__(self):
        self._load_config()

    def _load_config(self):
        """Load configuration from JSON file."""
        with self.CONFIG_PATH.open("r") as file:
            config = json.load(file)
            self.api_base_url = config["api_base_url"]
            self.api_token = config["api_token"]
            self.default_model = config["default_model"]

    def run_model(self, model_name, inputs):
        """Send a request to the AI model."""
        headers = {"Authorization": f"Bearer {self.api_token}"}
        payload = {"messages": inputs}
        response = requests.post(f"{self.api_base_url}{model_name}", headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API Error {response.status_code}: {response.text}")
