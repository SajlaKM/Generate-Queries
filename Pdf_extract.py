import pymupdf
import re
import nltk
from nltk.tokenize import sent_tokenize

import spacy
nlp = spacy.load("en_core_web_sm")

# Function to Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text("text") + "\n"

    return text

# Load PDF file to be summarized 
pdf_text = extract_text_from_pdf("Artificial Intelligence.pdf")
print(pdf_text[:1000]) 

# Preprocess Text
pdf_text = re.sub(r'\s+', ' ', pdf_text).strip()  # Remove extra spaces

doc = nlp(pdf_text)
sentences = [sent.text for sent in doc.sents]

print(f"\nExtracted {len(sentences)} sentences from the PDF!")
