import spacy

# Load the English model for spaCy
nlp = spacy.load('en_core_web_lg')

# Function to perform named entity recognition (NER)
def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to extract noun phrases
def extract_noun_phrases(text):
    doc = nlp(text)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

# Main program
text = "Apple Inc. was founded in 1976 by Steve Jobs and, Steve Wozniak, and Ronald Wayne. It is headquartered in Cupertino, California."

# Perform named entity recognition
entities = perform_ner(text)
print("Named Entities:")
for entity in entities:
    print(entity)

print()

# Extract noun phrases
noun_phrases = extract_noun_phrases(text)
print("Noun Phrases:")
for phrase in noun_phrases:
    print(phrase)
