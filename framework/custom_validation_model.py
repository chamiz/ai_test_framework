from deepeval.models.base_model import DeepEvalBaseLLM
from framework.logger import Logger

class CustomValidationModel(DeepEvalBaseLLM):
    def __init__(self, ai_client):
        self.ai_client = ai_client

    def load_model(self):
        return self

    def generate(self, prompt: str) -> str:
        """Generate validation response using validation model"""
        try:
            return self.ai_client.run_validation_model(prompt)
        except Exception as e:
            Logger.log_error(f"Validation generation failed: {str(e)}")
            return ""

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return "CustomValidationModel"