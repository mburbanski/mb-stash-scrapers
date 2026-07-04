# Where is your Ollama installation running?
LLM_URL = "http://localhost:11434/api/generate"


# Which translation model to use?
# How beefy is your hardware?
MODEL   = "translategemma:4b"
# MODEL   = "translategemma:12b"
# MODEL   = "translategemma:27b"


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