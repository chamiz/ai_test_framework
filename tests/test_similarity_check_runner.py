from framework.ai_client import AIClient
from framework.logger import Logger
import json
import en_core_web_sm


def load_test_data(file_path):
    """Load test cases from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def run_tests():
    """Run all test cases."""
    ai_client = AIClient()  # Initialize the AI client
    test_data = load_test_data("test_data.json")
    results = {"passed": 0, "failed": 0, "details": []}

    for test_case in test_data:
        prompt = test_case["prompt"]
        expected_output = test_case["expected_output"]

        # Prepare input for the AI model
        inputs = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        try:
            # Get AI response
            response = ai_client.run_model(ai_client.default_model, inputs)
            actual_output = response.get('result', {}).get('response', "")

            # Validate the response
            is_valid, validation_message = validate_output(actual_output, expected_output)
            if is_valid:
                results["passed"] += 1
                results["details"].append({"prompt": prompt, "status": "passed", "message": validation_message,
                                           "actual_output": actual_output})
                Logger.log_result(f"Test Passed - Prompt: {prompt} | Message: {validation_message}")
            else:
                results["failed"] += 1
                results["details"].append({"prompt": prompt, "status": "failed", "message": validation_message,
                                           "actual_output": actual_output})
                Logger.log_result(f"Test Failed - Prompt: {prompt} | {validation_message}")

        except Exception as e:
            results["failed"] += 1
            results["details"].append({"prompt": prompt, "status": "error", "error": str(e)})
            Logger.log_result(f"Test Error - Prompt: {prompt} | Error: {e}")

    # Save summary
    Logger.save_summary(results)


def validate_output(actual_output, expected_output):
    nlp = en_core_web_sm.load()
    doc1 = nlp(actual_output)
    doc2 = nlp(expected_output)
    similarity = doc1.similarity(doc2)

    # Define the similarity threshold
    threshold = 0.8  # 0.8 is 80% similarity threshold

    if similarity >= threshold:
        return True, f"Output matches expected result. Similarity: {similarity:.2f}"
    else:
        return False, f"Output mismatch. Similarity: {similarity:.2f}"


if __name__ == "__main__":
    run_tests()
