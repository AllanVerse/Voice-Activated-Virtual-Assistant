# Install required libraries
!pip install gTTS spacy
!python -m spacy download en_core_web_sm

from gtts import gTTS
from IPython.display import Audio
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Read input from a text file
file_path = "input.txt"  # Make sure this file exists in your working directory

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# NLP processing
doc = nlp(text)

# Clean and format text
sentences = [sent.text.strip().capitalize() for sent in doc.sents]
processed_text = " ".join(sentences)

# Optional: Show named entities
print("Named Entities found:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")

# Convert processed text to speech
tts = gTTS(processed_text, lang='en')
tts.save("output.mp3")

# Play the audio
Audio("output.mp3")
