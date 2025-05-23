import os
import json
from datetime import datetime

class Logger:
    LOG_FILE_PATH = "reports/results.log"
    SUMMARY_FILE_PATH = "reports/summary.json"

    @staticmethod
    def log_result(message):
        os.makedirs(os.path.dirname(Logger.LOG_FILE_PATH), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.LOG_FILE_PATH, "a") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")

    @staticmethod
    def log_error(message):
        os.makedirs(os.path.dirname(Logger.LOG_FILE_PATH), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.LOG_FILE_PATH, "a") as log_file:
            log_file.write(f"[{timestamp}] ERROR: {message}\n")

    @staticmethod
    def save_summary(results):
        os.makedirs(os.path.dirname(Logger.SUMMARY_FILE_PATH), exist_ok=True)
        with open(Logger.SUMMARY_FILE_PATH, "w") as summary_file:
            json.dump(results, summary_file, indent=4)

    @staticmethod
    def clear_logs():
        if os.path.exists(Logger.LOG_FILE_PATH):
            open(Logger.LOG_FILE_PATH, "w").close()