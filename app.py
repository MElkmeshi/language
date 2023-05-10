import time
import pyautogui
import pyperclip

english_to_arabic = {
    "q": "ض",
    "w": "ص",
    "e": "ث",
    "r": "ق",
    "t": "ف",
    "y": "غ",
    "u": "ع",
    "i": "ه",
    "o": "خ",
    "p": "ح",
    "[": "ج",
    "]": "د",
    "a": "ش",
    "s": "س",
    "d": "ي",
    "f": "ب",
    "g": "ل",
    "h": "ا",
    "j": "ت",
    "k": "ن",
    "l": "م",
    ";": "ك",
    "'": "ط",
    "z": "ئ",
    "x": "ء",
    "c": "ؤ",
    "v": "ر",
    "b": "لا",
    "n": "ى",
    "m": "ة",
    ",": "و",
    ".": "ز",
    "/": "ظ",
    "`": "ذ",
    " ": " ",
}
arabic_to_english = {v: k for k, v in english_to_arabic.items()}


def arabic_to_english_text(arabic_text):
    english_text = ''.join([arabic_to_english.get(char, char)
                           for char in arabic_text])
    return english_text


time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')
time.sleep(0.1)

clipboard_text = pyperclip.paste()

# TO DO: detech language
converted_text = arabic_to_english_text(clipboard_text)

pyperclip.copy(converted_text)

pyautogui.hotkey('ctrl', 'v')
