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
3. Cloudflare free account[results.log](tests%2Freports%2Fresults.log)
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
1. Initialize the Framework:
Import and set up the framework.

2. Test Data file:
tests/test_data.js
3. You can change the prompt and expected results in the test_data.json file.
4. You can adjust the validation accuracy in the validators.py file.
5. Run Automated Tests:
Execute load_test_data as python program, not as a test.

6. Reports:
Generated output will be stored in tests/reports folder
