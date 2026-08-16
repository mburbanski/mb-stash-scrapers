# Language Translation Plugin

This plugin is designed to translate text from one language to another using a large language model (LLM) hosted behind an OpenAI-compatible API. The default target language is English, but it can be adapted for other languages by modifying the configuration.

Any server or service implementing the OpenAI `/v1/chat/completions` API works — this includes local servers (e.g. LM Studio, llama.cpp, vLLM) as well as hosted providers. It supports both an unauthenticated connection (e.g. a local server on your LAN with no key required) and an authenticated connection (e.g. a hosted service over HTTPS with an API key).

## How It Works

1. Configuration: The plugin reads settings from two configuration files:
    - `default_config.py`: Contains default settings that can be overridden.
    - `config.py`: Optional file where you can specify custom settings to override the defaults.
2. Prompt Template: A prompt template is defined in default_config.py and can be customized in config.py. This template guides the LLM on how to translate the text, preserving tone, personality, slang, and other nuances.
3. Translation Function: The translate() function reads input text, constructs a prompt using the specified template, sends it to the LLM via an HTTP POST request to the configured OpenAI-compatible chat completions endpoint (including an API key as a bearer token if one is configured), and returns the translated text.
4. Main Function: The main() function reads JSON data from standard input, translates any provided title and details, and outputs the result in JSON format.

## Customizing Settings

To customize settings:

1. Copy `default_config.py` to `config.py`.
2. Modify `config.py` with your desired settings.
    - `LLM_URL` = the chat completions URL of your OpenAI-compatible service (e.g. `http://localhost:1234/v1/chat/completions` for a local server, or a hosted provider's endpoint).
    - `API_KEY` = the API key for your service, if it requires one. Leave this as an empty string (`""`) for an unauthenticated local/LAN server. If you set a real key, only point `LLM_URL` at an `https://` endpoint — the key is sent as a bearer token and shouldn't be sent over a plain, unencrypted connection.
    - `MODEL` = the model identifier your service expects (check your local server's loaded models, or your hosted provider's model catalog).
    - `TARGET_LANGUAGE` = The name of the target language you want content translated into.
    - `PROMPT_TEMPLATE` = The prompt that will get passed into the LLM that provides directions about what to do with the input text. the string `{target_language}` will be substituted with whatever the value of the `TARGET_LANGUAGE` configuration setting.