import json
from datetime import datetime

from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, ContextualRecallMetric, FaithfulnessMetric, BiasMetric
from deepeval.test_case import LLMTestCase

from framework.ai_client import AIClient
from framework.logger import Logger


# Load test data from JSON file
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Generate AI response
def generate_response(prompt):
    ai_client = AIClient()  # Initialize the AI client

    # Prepare input for the AI model
    inputs = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = ai_client.run_model(ai_client.default_model, inputs)
    actual_output = response.get('result', {}).get('response', "")
    return actual_output

# Validate test cases using DeepEval
def validate_with_deepeval(test_cases):
    results = []

    for case in test_cases:
        prompt = case["prompt"]
        expected_result = case["expected_result"]
        actual_output = generate_response(prompt)

        test_case = LLMTestCase(
            input=prompt,
            actual_output=actual_output,
            retrieval_context=[expected_result]
        )

        metrics = [
            AnswerRelevancyMetric(threshold=0.8),
            ContextualRecallMetric(threshold=0.9),
            FaithfulnessMetric(threshold=0.95),
            BiasMetric(threshold=0.7)
        ]

        case_results = {}
        for metric in metrics:
            result = assert_test(test_case, [metric])
            metric_name = metric.__class__.__name__
            case_results[metric_name] = {
                "passed": result.passed,
                "score": result.score
            }

            # Log individual result using your existing Logger
            Logger.log_result(
                f"Prompt: {prompt[:50]}... | "
                f"Metric: {metric_name} | "
                f"Passed: {result.passed} | "
                f"Score: {result.score}"
            )

        results.append({"prompt": prompt, "results": case_results})

    return results

if __name__ == "__main__":
    # Clear previous logs before starting new test run
    Logger.clear_logs()

    # Load test cases
    test_cases = load_test_data("test_data.json")

    # Run validation
    results = validate_with_deepeval(test_cases)

    # Save summary report
    Logger.save_summary({
        "timestamp": datetime.now().isoformat(),
        "total_cases": len(results),
        "passed_cases": sum(1 for case in results if all(m["passed"] for m in case["results"].values())),
        "details": results
    })

    print("Test execution completed. Results logged and summary saved.")