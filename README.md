# README.md

## Arabic-English Keyboard Mapper

This script is a simple tool to convert Arabic text typed using an English keyboard to the correct Arabic characters. It uses the Python libraries `time`, `pyautogui`, and `pyperclip`.

### How it works

The script contains two dictionaries, `english_to_arabic` and `arabic_to_english`, that store the mappings between English and Arabic characters. The script then defines a function `arabic_to_english_text` that converts Arabic text into English text based on the `arabic_to_english` dictionary.

### Usage

1. Install the required Python libraries:

   ```
   pip install pyautogui
   pip install pyperclip
   ```

2. Run the script:

   ```
   python app.py
   ```

3. Type or paste the Arabic text you want to convert into any text input field (e.g., a text editor or web form).

4. Select the text you want to convert and wait for 2 seconds.

5. The script will automatically select all the text (`Ctrl + A`), cut it (`Ctrl + X`), convert it, and paste the converted text back (`Ctrl + V`).

**Note:** The script currently only supports converting Arabic text typed using an English keyboard to Arabic characters. It does not support converting English text typed using an Arabic keyboard to English characters.

this text was made by Chat-GPT
