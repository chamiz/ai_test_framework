# **AI Test Framework**

A robust framework for automated testing of AI-generated content, featuring seamless integration with [DeepEval](https://deepeval.com) and support for custom Language Models (LLMs).

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Features

- **DeepEval Integration**: 
  - Answer Relevancy Metrics (threshold: 0.8)
  - Contextual Recall Metrics (threshold: 0.9)
  - Faithfulness Metrics (threshold: 0.95)
  - Bias Detection (threshold: 0.7)
- **Custom LLM Support**: Bring your own language model
- **Configurable Testing**: JSON-based test case management
- **Comprehensive Reporting**: 
  - Detailed logs in `reports/results.log`
  - Summary reports in `reports/summary.json`
  - Integration with DeepEval Dashboard

## Prerequisites

1. Python 3.8 or higher
2. Git
3. DeepEval account (Sign up at [deepeval.com](https://deepeval.com))
4. One of the following LLMs:
   - Cloudflare Workers AI (Follow setup at [Cloudflare Workers AI Guide](https://developers.cloudflare.com/workers-ai/get-started/rest-api/))
   - Custom LLM implementation

## Installation

1. **Clone the repository:**
    ```powershell
    git clone https://github.com/chamiz/ai_test_framework.git
    cd ai_test_framework
    ```

2. **Set up virtual environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3. **Install dependencies:**
    ```powershell
    pip install -r requirements.txt
    pip install -U deepeval
    ```

4. **Login to DeepEval:**
    ```powershell
    deepeval login
    ```

## Configuration

### Model Settings (config/settings.json)
```json
{
  "api_base_url": "your-api-base-url",
  "api_token": "your-api-token",
  "validation_model": "your-model-name"
}
```

### Test Cases (tests/test_data.json)
```json
[
  {
    "prompt": "Your test prompt",
    "expected_result": "Expected response"
  }
]
```

### Metric Thresholds
Adjust metric thresholds in `tests/test_deepeval_matrix.py`:
```python
metrics = {
    "Answer Relevancy": AnswerRelevancyMetric(model=validation_model, threshold=0.8),
    "Contextual Recall": ContextualRecallMetric(model=validation_model, threshold=0.9),
    "Faithfulness": FaithfulnessMetric(model=validation_model, threshold=0.95),
    "Bias": BiasMetric(model=validation_model, threshold=0.7)
}
```

## Usage

1. **Clear previous logs (optional):**
    ```powershell
    python -c "from framework.logger import Logger; Logger.clear_logs()"
    ```

2. **Run tests:**
    ```powershell
    deepeval test run tests/test_deepeval_matrix.py
    ```

3. **View results:**
   - Check `reports/results.log` for detailed logs
   - View `reports/summary.json` for test summary
   - Access DeepEval Dashboard for comprehensive analysis

## Metrics

### Answer Relevancy (threshold: 0.8)
Measures how well the response answers the given prompt.

### Contextual Recall (threshold: 0.9)
Evaluates if the response includes all necessary context from the prompt.

### Faithfulness (threshold: 0.95)
Checks if the response remains true to the given context without hallucination.

### Bias Detection (threshold: 0.7)
Identifies potential biases in the generated responses.

## Troubleshooting

### Common Issues

1. **"NoneType object is not callable" Error**
   - Ensure your validation model is properly initialized
   - Check if all required dependencies are installed

2. **Invalid JSON Output**
   - Verify the LLM output format
   - Check the prompt formatting

3. **Metric Evaluation Failures**
   - Review metric thresholds
   - Validate expected results format

### Debug Mode
Enable detailed logging by setting verbose mode in your test configuration.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See LICENSE file for details.

## References

- [DeepEval Documentation](https://www.deepeval.com/docs/getting-started)
- [AI Test Framework Article Series](https://medium.com/@ambahera)
- [Project GitHub Repository](https://github.com/chamiz/ai_test_framework)

---

*Maintained by Chamila Ambahera*
Last updated: May 2025

