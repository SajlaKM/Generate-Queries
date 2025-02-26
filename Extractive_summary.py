import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function for Extractive Summarization using spaCy
def summarize_text_spacy(text, num_sentences=5):
    # Tokenize sentences using spaCy
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    # Extract the first few sentences 
    summary = " ".join(sentences[:num_sentences])
    
    return summary

# Generate Extractive Summary
extractive_summary = summarize_text_spacy(pdf_text, num_sentences=10)

print(" Extractive Summary:\n", extractive_summary)
