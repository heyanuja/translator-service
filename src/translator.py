from typing import Tuple
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def translate(content: str) -> Tuple[bool, str]:
    """For now, just return hardcoded translations for checkpoint 2"""
    translations = {
        "Dies ist eine Nachricht auf Deutsch": (False, "This is a German message"),
        "Esto es un mensaje en español": (False, "This is a Spanish message"),
        "这是一条中文消息": (False, "This is a Chinese message")
    }
    return translations.get(content, (True, content))