# Language Translation Plugin

This plugin is designed to translate text from one language to another using a large language model (LLM) hosted on an Ollama server. The default target language is English, but it can be adapted for other languages by modifying the configuration.

## How It Works

1. Configuration: The plugin reads settings from two configuration files:
    - `default_config.py`: Contains default settings that can be overridden.
    - `config.py`: Optional file where you can specify custom settings to override the defaults.
2. Prompt Template: A prompt template is defined in default_config.py and can be customized in config.py. This template guides the LLM on how to translate the text, preserving tone, personality, slang, and other nuances.
3. Translation Function: The translate() function reads input text, constructs a prompt using the specified template, sends it to the LLM via an HTTP POST request, and returns the translated text.
4. Main Function: The main() function reads JSON data from standard input, translates any provided title and details, and outputs the result in JSON format.

## Customizing Settings

To customize settings:

1. Copy `default_config.py` to `config.py`.
2. Modify `config.py` with your desired settings.
    - `LLM_URL` = the URL of the Ollama server
    - `MODEL` = the name of the model you want to use (must be available on your ollama installation)
    - `TARGET_LANGUAGE` = The name of the target language you want content translated into.
    - `PROMPT_TEMPLATE` = The prompt that will get passed into the LLM that provides directions about what to do with the input text. the string `{target_language}` will be substituted with whatever the value of the `TARGET_LANGUAGE` configuration setting.