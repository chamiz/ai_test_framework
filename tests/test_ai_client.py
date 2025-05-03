import pytest
from framework.ai_client import AIClient

@pytest.fixture
def ai_client():
    return AIClient()

def test_load_config(ai_client):
    assert ai_client.api_base_url is not None
    assert ai_client.api_token is not None

def test_run_model(ai_client):
    response = ai_client.run_model("test-model", "Hello, world!")
    assert isinstance(response, str)