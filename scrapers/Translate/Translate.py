import sys
import json
import requests
import os

# Define the path to the config files
CONFIG_FILE = 'config.py'
DEFAULT_CONFIG_FILE = 'default_config.py'

def load_config(file_path):
    global LLM_URL, MODEL, PROMPT_TEMPLATE
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            exec(f.read(), globals())

# Load configurations from default_config.py, then config.py
# This allows local settings to override default settings
load_config(DEFAULT_CONFIG_FILE)
load_config(CONFIG_FILE)

def build_prompt(text):
    return PROMPT_TEMPLATE.format(target_language=TARGET_LANGUAGE, text=text)

def translate(text):
    if not text:
        return text
    prompt = build_prompt(text)
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,    # slightly higher for more natural language
        "top_p": 0.6,          # allows colloquial phrasing without losing accuracy
        "top_k": 20,
    }
    r = requests.post(LLM_URL, json=payload)
    try:
        return r.json().get("response", text).strip()
    except Exception:
        return text

def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print("{}")
        return
    data = json.loads(raw)
    title = data.get("title", "")
    details = data.get("details", "")
    output = {}
    if title:
        output["title"] = translate(title)
    if details:
        output["details"] = translate(details)
    print(json.dumps(output))

if __name__ == "__main__":
    main()