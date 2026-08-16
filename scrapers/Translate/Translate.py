import sys
import json
import requests
import os

# Define the path to the config files
CONFIG_FILE = 'config.py'
DEFAULT_CONFIG_FILE = 'default_config.py'

def load_config(file_path):
    global LLM_URL, MODEL, PROMPT_TEMPLATE, API_KEY, TARGET_LANGUAGE
    global TOP_K, REPETITION_PENALTY, MAX_TOKENS
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            exec(f.read(), globals())

# Sensible fallbacks in case an older config.py predates these settings
API_KEY = ""
TOP_K = 20
REPETITION_PENALTY = 1.05
MAX_TOKENS = 4096

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
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "temperature": 0.7,               # slightly higher for more natural language
        "top_p": 0.6,                     # allows colloquial phrasing without losing accuracy
        "top_k": TOP_K,
        "repetition_penalty": REPETITION_PENALTY,
        "max_tokens": MAX_TOKENS,
    }
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    # Plain chat-completions with string content. Deliberately avoids
    # hardcoding any model-specific turn markers here -- each model's own
    # chat template (loaded by the server) handles formatting. This works
    # as-is for standard templates (e.g. Hunyuan-MT), and for TranslateGemma
    # via its patched template's plain-string fallback (see
    # translategemma_prompt_template.jinja), which auto-detects the source
    # language and translates to English. If you need a non-English target
    # with TranslateGemma specifically, its patched template also supports
    # a richer structured message schema -- ask if you want that wired up.
    r = requests.post(LLM_URL, json=payload, headers=headers)
    try:
        return r.json()["choices"][0]["message"]["content"].strip()
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