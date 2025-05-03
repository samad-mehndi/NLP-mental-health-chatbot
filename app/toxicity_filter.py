# app/toxicity_filter.py

from detoxify import Detoxify

# Load model once
detox_model = Detoxify('original')

def is_toxic(text: str) -> bool:
    """
    Check if the input text is toxic.
    Returns True if toxicity is high, else False.
    """
    result = detox_model.predict(text)
    return result['toxicity'] > 0.5  # You can adjust threshold
