import re
import string

STOPWORDS = set("""
a about above after again against all am an and any are as at be because been
before being below between both but by can cannot could did do does doing
down during each few for from further had has have having he her here hers
herself him himself his how i if in into is it its itself let me more most
my myself no nor not of off on once only or other our ours ourselves out
over own same she should so some such than that the their theirs them
themselves then there these they this those through to too under until up
very was we were what when where which while who whom why will with you
your yours yourself yourselves
""".split())

UNICODE_PUNCT = "\u2019\u2018\u201c\u201d\u2014\u2013\u2026"
ALL_PUNCT = string.punctuation + UNICODE_PUNCT


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = text.translate(str.maketrans("", "", ALL_PUNCT))
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = [w for w in text.split() if w not in STOPWORDS and len(w) > 1]
    return " ".join(tokens)
