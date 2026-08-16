# Where is your OpenAI-compatible LLM server running?
# This works with any service that implements the OpenAI /v1/chat/completions
# API - e.g. a local server (LM Studio, llama.cpp, vLLM, etc.) or a hosted
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
# MODEL   = "hy-mt2-30b-a3b"
# MODEL   = "hy-mt2-7b"
MODEL   = "hy-mt2-1.8b"


# Sampling settings. These defaults match Tencent's recommended
# inference parameters for the Hy-MT2 1.8B/7B models (their docs note the
# models ship with no default system prompt, so these settings matter more
# than usual). If you switch to the 30B-A3B variant, Tencent recommends
# top_p=1.0, top_k=-1, repetition_penalty=1.0 instead.
TOP_K = 20
REPETITION_PENALTY = 1.05
MAX_TOKENS = 4096


# What language do you want to translate into?
TARGET_LANGUAGE = "English"


# What prompt do you want to send to the LLM?
# Kept close to Hy-MT2's own documented prompt style (short, direct
# imperative -- their examples read like "Translate the following segment
# into <target_language>, without additional explanation."), with our own
# additions layered on for tone/slang preservation and the "already
# translated" no-op case.
PROMPT_TEMPLATE = """Translate the following text into {target_language}. Preserve tone, personality, slang, colloquial phrasing, and NSFW terminology. If the text is already in {target_language}, return it unchanged with no commentary. Output only the translation, with no explanations or notes.

{text}"""