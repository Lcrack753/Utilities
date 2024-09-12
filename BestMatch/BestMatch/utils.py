import re
import unicodedata

def normalize_text(text: str) -> str:
    text = re.sub(r'[^\w\s]', ' ', text)
    text = text.upper()
    # Eliminar espacios al principio y al final, y reducir múltiples espacios internos a uno solo
    text = re.sub(r'\s+', ' ', text.strip())
    # Normalizar para eliminar acentos y tildes
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    
    return text


if __name__ == '__main__':
    txt = normalize_text("Hola    qué t'al como and,an")
    print(txt)