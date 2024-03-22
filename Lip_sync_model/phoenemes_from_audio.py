import pyttsx3
import pronouncing

def text_to_wav(text, audio_file_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Save the speech to a WAV audio file
    engine.save_to_file(text, audio_file_path)

    # Wait for the speech to be generated
    engine.runAndWait()

    # Extract phonemes from the generated audio
    phonemes = extract_phonemes_from_audio(audio_file_path)
    print("Phonetic representations:", phonemes)

def extract_phonemes_from_audio(audio_file):
    # Perform phoneme extraction (you can use your own method here)
    # For simplicity, let's just split the text into words and use the pronouncing library
    text = " ".join(audio_file.split("_"))  # Convert file name back to text
    words = text.split()
    phonemes = []
    for word in words:
        word_phonemes = pronouncing.phones_for_word(word)
        if word_phonemes:
            phonemes.append(word_phonemes[0])
    return phonemes

# Example usage:
text_message = "Hello, how are you?"
audio_file_path = "output_audio.wav"

# Convert text message to WAV audio file and extract phonemes
text_to_wav(text_message, audio_file_path)
