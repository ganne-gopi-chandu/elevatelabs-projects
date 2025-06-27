offensive_words = {"stupid", "kill", "hate", "die", "useless"}

def is_offensive(text):
    return any(word in text.lower() for word in offensive_words)
