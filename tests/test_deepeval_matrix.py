import json
from datetime import datetime
from typing import List, Dict, Any
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, ContextualRecallMetric, FaithfulnessMetric, BiasMetric
from deepeval.test_case import LLMTestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from framework.custom_validation_model import CustomValidationModel
from framework.ai_client import AIClient
from framework.logger import Logger

# Initialize shared resources once
ai_client = AIClient()
validation_model = CustomValidationModel(ai_client)
metrics = [
    AnswerRelevancyMetric(model=validation_model, threshold=0.8),
    ContextualRecallMetric(model=validation_model, threshold=0.9),
    FaithfulnessMetric(model=validation_model, threshold=0.95),
    BiasMetric(model=validation_model, threshold=0.7)
]

def load_test_cases(test_data_path: str = "test_data.json"):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the absolute path to the test_data.json file
    abs_path = os.path.join(script_dir, test_data_path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")
    with open(abs_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def test_llm_outputs():
    """Test function for DeepEval CLI discovery - runs all test cases"""
    test_cases = load_test_cases()
    results = []

    for test_case in test_cases:
        prompt = test_case["prompt"]
        expected_output = test_case["expected_result"]

        try:
            # Generate response
            actual_output = ai_client.run_model(
                model_name=ai_client.default_model,
                prompt=prompt
            )

            if not actual_output:
                raise ValueError("Empty response from model")

            # Create test case
            llm_test_case = LLMTestCase(
                input=prompt,
                actual_output=actual_output,
                expected_output=expected_output,
                retrieval_context=[expected_output]
            )

            # Assert against all metrics
            assert_test(llm_test_case, metrics)

            # Log successful execution
            Logger.log_result(f"Successfully evaluated prompt: {prompt[:50]}...")

            results.append({
                "prompt": prompt,
                "actual_output": actual_output,
                "expected_output": expected_output,
                "passed": True
            })

        except Exception as e:
            Logger.log_error(f"Test failed for prompt '{prompt[:50]}...': {str(e)}")
            results.append({
                "prompt": prompt,
                "error": str(e),
                "passed": False
            })

    save_summary_report(results)
    return results

def save_summary_report(results: List[Dict[str, Any]]):
    """Save comprehensive test summary"""
    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_cases": len(results),
        "passed_cases": sum(1 for case in results if case.get("passed", False)),
        "details": results
    }

    try:
        Logger.save_summary(summary)
        Logger.log_result("Successfully saved summary report")
    except Exception as e:
        Logger.log_error(f"Failed to save summary: {str(e)}")
        raise

if __name__ == "__main__":
    # Manual execution
    Logger.clear_logs()
    results = test_llm_outputs()
    print(f"Test execution completed. Processed {len(results)} cases.")
