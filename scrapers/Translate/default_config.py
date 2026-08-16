# Where is your OpenAI-compatible LLM server running?
# This works with any service that implements the OpenAI /v1/chat/completions
# API — e.g. a local server (LM Studio, llama.cpp, vLLM, etc.) or a hosted
# provider reachable over HTTPS.
LLM_URL = "http://localhost:1234/v1/chat/completions"


# API key for the above service, if one is required.
# - Local/LAN servers with no auth: leave this as an empty string.
# - Hosted/authenticated services: set this to your API key. Since it will
#   be sent as a bearer token over the connection to LLM_URL, only use a key
#   with a service reachable over HTTPS so it isn't sent in the clear.
API_KEY = ""


# Which translation model to use?
# This must match the model identifier the service expects
# (for a local server, check its running/loaded models list;
# for a hosted provider, check their model catalog).
MODEL   = "translategemma-4b"
# MODEL   = "translategemma-12b"
# MODEL   = "translategemma-27b"


# What language do you want to translate into?
TARGET_LANGUAGE = "English"


# What prompt do you want to send to the LLM?
PROMPT_TEMPLATE = """
You are a professional multilingual translator.
Your job is to:
1. Identify the source language automatically.
2. If the text is already {target_language}, return no text whatsoever (STRICT).
3. Otherwise translate it into natural, fluent {target_language}.
4. Preserve tone, personality, slang, colloquial phrasing, and NSFW terminology.
5. Produce ONLY the {target_language} translation with no explanations, notes, or commentary.
Translate the following text:
{text}
"""