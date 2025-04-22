# ai_client.py
import json
import os
from pathlib import Path

import requests

from framework.logger import Logger


class AIClient:
    def __init__(self):
        self._load_config()

    def _load_config(self):
        """Load configuration from JSON file with robust path resolution"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(script_dir, '..', 'config', 'settings.json')
            config_path = os.path.normpath(os.path.abspath(config_path))
            self.CONFIG_PATH = Path(config_path)
            if not self.CONFIG_PATH.exists():
                raise FileNotFoundError(f"Settings file not found at {config_path}")
            with self.CONFIG_PATH.open("r") as file:
                config = json.load(file)
                self.api_base_url = config["api_base_url"].rstrip("/")
                self.api_token = config["api_token"]
                self.default_model = config["generation_model"]
                self.validation_model = config["validation_model"]
        except Exception as e:
            Logger.log_error(f"Config loading failed: {str(e)}")
            raise

    def run_model(self, model_name: str, prompt: str, max_tokens: int = 256) -> str:
        """Execute model request"""
        endpoint = f"{self.api_base_url}/{model_name}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json().get("result", {}).get("response", "")
        except requests.RequestException as e:
            Logger.log_error(f"API request failed: {str(e)}")
            raise RuntimeError(f"Model request failed: {str(e)}") from e

    def run_validation_model(self, prompt: str) -> str:
        """Execute validation model request"""
        return self.run_model(self.validation_model, prompt)
