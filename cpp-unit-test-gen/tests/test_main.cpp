import requests
import json

# Load the YAML prompt
with open("prompts/generate_test.yaml", "r") as f:
    prompt = f.read()

# Load the main.cpp code
with open("src/main.cpp", "r") as f:
    cpp_code = f.read()

# Combine both into a message for the LLM
full_prompt = f"""
You are a C++ unit test generator. Follow the strict YAML instructions below.

YAML INSTRUCTIONS:
{prompt}

C++ CODE:
{cpp_code}
"""

# Send request to Ollama local model
response = request
