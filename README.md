# **AI Test Framework**

AI Test Framework is a flexible tool designed to automated testing AI generated content of LLMA models. It provides tools and methods for validating AI-generated content, ensuring accuracy.

This document is a sample code of. Please refer that page for more information

Full article 
https://medium.com/@ambahera/can-we-automate-the-testing-of-ai-generated-content-practical-example-d124e99df52d

**📋 Features**

Handles scenarios where AI models produce varying results for the same input.

**AI models/Tools used**
llma
Spacy

**🚀 Getting Started**

Follow these steps to set up and start using AI Test Framework:

## **Prerequisites**

1. Python 3.8 or higher
2. Pip (Python package installer)
3. Cloudflare free account 
   Follow this guide to setup Cloudflare account and get API token to execute this project.
   https://developers.cloudflare.com/workers-ai/get-started/rest-api/
4. A supported AI/ML model (LLMA)
5. Follow this guide to install Spacy package.
   https://spacy.io/usage/models#quickstart


## **Installation**

Clone the repository:

git clone https://github.com/yourusername/ai_test_framework.git  
cd ai_test_framework  

**Install the required dependencies:**

pip install -r requirements.txt  
Set up environment variables (optional):

Add your model's API keys or file paths to a config/settings.json file in the project directory.

## 🛠 Usage
Initialize the Framework:
Import and set up the framework.

Config files
In settings.json set api_base_url , api_token as instructed in https://developers.cloudflare.com/workers-ai/get-started/rest-api/
In you can adjust the validation accuracy in the validators.py file.

Test Data file:
tests/test_data.js

You can change the prompt and expected results in the test_data.json file.
Run Automated Tests:
Execute test_similarity_check_runner.py as python program, not as a test.

Reports:
Generated output will be stored in tests/reports folder

## Version 2.0

# AI Test Framework with DeepEval Integration

A robust, extensible framework for automated testing and validation of AI-generated content, featuring seamless integration with [DeepEval](https://deepeval.com) and support for custom LLMs.

---

## Features

- **DeepEval Integration**: Evaluate outputs using advanced metrics such as Answer Relevancy, Contextual Recall, Faithfulness, and Bias Detection.
- **Custom LLM Support**: Use your own language model backend—no OpenAI API key required.
- **Configurable**: Prompts, expected results, and thresholds are defined in JSON files.
- **Comprehensive Reporting**: Detailed logs and summary reports for every test run.
- **Extensible**: Easily add new metrics, validators, or model adapters.

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/chamiz/ai_test_framework.git
    cd ai_test_framework
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    pip install -U deepeval
    ```

---

## Configuration

- **Model Settings:**  
  Configure your custom LLM in `config/settings.json`:
    ```
    {
      "validation_model": "your-custom-model-name-or-path"
    }
    ```

- **Test Cases:**  
  Add prompts and expected results in `tests/test_data.json`:
    ```
    [
      {
        "prompt": "Explain why the sky is blue.",
        "expected_result": "The sky appears blue because molecules in the atmosphere scatter blue light from the sun more than they scatter red light, a phenomenon known as Rayleigh scattering."
      }
    ]
    ```

---

## How to Run DeepEval Tests

1. **(Optional) Clear previous logs:**
    ```
    python -c "from framework.logger import Logger; Logger.clear_logs()"
    ```

   2. **Run the DeepVal test:**
       ```
       deepeval login
       deepeval test run test_deepeval_matrix.py
       ```

      - This will:
         - Use your custom LLM for generating and validating responses.
         - Evaluate each response using DeepEval metrics.
         - Log individual results to `reports/results.log`.
         - Save a summary in `reports/summary.json`.
         - Results will be uploaded to DeepVal Dashboard

---

## Advanced Usage

- **Integrate additional models** by creating a new class that inherits from `DeepEvalBaseLLM` and implements the required interface.
- **Parallel execution and CI/CD integration** are supported—add your test script to your pipeline as needed.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.

---

## License

MIT License

---

## References

- [DeepEval Documentation](https://www.deepeval.com/docs/getting-started)
- [AI Test Framework Article Series](https://medium.com/@ambahera)

---

*This project is maintained by Chamila Ambahera.*

