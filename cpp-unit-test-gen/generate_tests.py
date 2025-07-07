import requests

# Load the YAML prompt
with open("prompts/generate_test.yaml", "r") as f:
    yaml_prompt = f.read()

# Load the C++ code
with open("src/main.cpp", "r") as f:
    cpp_code = f.read()

# Final prompt to send to the LLM
prompt = f"""
You are a professional C++ developer.
Follow the instructions given in YAML below to generate Google Test unit tests.

YAML INSTRUCTIONS:
{yaml_prompt}

C++ CODE:
{cpp_code}
"""

# Send to Ollama LLM
response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3",
    "prompt": prompt,
    "stream": False
})

# Print the result to be redirected to a file
print(response.json()["response"])
