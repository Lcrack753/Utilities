from collections import Counter
import math
import re
import unicodedata
from typing import Iterable, Tuple, Mapping

def normalize_text(text: str) -> str:
    text = re.sub(r'[^\w\s]', ' ', text)
    text = text.upper()
    text = re.sub(r'\s+', ' ', text.strip())
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text

def to_vector(txt: str, wordbook: set) -> list:
    txt = normalize_text(txt).split()
    return [txt.count(word) for word in wordbook]

def get_wordbook(txt1: str, txt2: str) -> set:
    txt1 = normalize_text(txt1).split()
    txt2 = normalize_text(txt2).split()
    return set(txt1).union(set(txt2))

def cosine_similarity(v1: list, v2: list) -> float:
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_v1 = math.sqrt(sum(a * a for a in v1))
    norm_v2 = math.sqrt(sum(b * b for b in v2))
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return dot_product / (norm_v1 * norm_v2)

def best_match_score(txt1: str, txt2: str) -> float:
    wordbook = get_wordbook(txt1, txt2)
    v1 = to_vector(txt1, wordbook)
    v2 = to_vector(txt2, wordbook)
    return cosine_similarity(v1, v2)

class BestMatch:
    def __init__(self, text: str = '') -> None:
        self.text = text

    @property
    def norm_text(self):
        return normalize_text(self.text)

    def find_in_texts(self, txts: Iterable[str]) -> list:
        txts = list(enumerate(txts))
        scores = [(i, best_match_score(self.text, txt)) for i, txt in txts]
        max_score = max(score for _, score in scores)
        return [txts[i] for i, score in scores if score == max_score]

    def find_in_maps(self, iter: Iterable[Mapping], col: str) -> list:
        txts = [i.get(col, '') for i in iter]
        finded = self.find_in_texts(txts)
        return [iter[i[0]] for i in finded]

    def find_in_list(self, iter: Iterable[Iterable], col: int = None) -> list:
        if col is None:
            for idx, value in enumerate(iter[0]):
                if isinstance(value, str):
                    col = idx
                    break
        assert col is not None and col < len(iter[0]), 'Column number out of index'
        txts = [i[col] for i in iter]
        finded = self.find_in_texts(txts)
        return [iter[i[0]] for i in finded]

