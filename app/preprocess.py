# app/preprocess.py

import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    """
    Lowercase, remove URLs, punctuation, and extra spaces.
    """
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-z\s]", "", text)  # Remove non-alphabetic characters
    text = re.sub(r"\s+", " ", text)      # Remove extra spaces
    return text.strip()

def extract_entities(text: str):
    """
    Extract named entities from text using spaCy.
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]