import pronouncing

def text_to_phonemes(text):
    words = text.split()
    phonemes = [pronouncing.phones_for_word(word)[0] for word in words if pronouncing.phones_for_word(word)]
    return phonemes

# Example usage:
text_response = "What a basketball looks like?"

phonemes = text_to_phonemes(text_response)
print("Phonetic representations:", phonemes)
