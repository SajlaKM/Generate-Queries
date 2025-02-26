import pymupdf  
from transformers import pipeline

# Load Pre-trained Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)  # Open PDF
    pages_text = []
    
    for i in range(len(doc)):  # Iterate through pages
        text = doc[i].get_text("text")
        if text.strip():  # Ignore empty pages
            pages_text.append(text)

    return pages_text

# Function to Split Long Text into Chunks
def split_text(text, max_words=400):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

# Function to Summarize Each Page 
def summarize_pdf(pdf_path, start_page=2):  # Skip cover & contents (Page 0 & 1)
    pages_text = extract_text_from_pdf(pdf_path)
    summaries = {}

    for i in range(start_page, len(pages_text)):  # Start from actual content
        page_text = pages_text[i]

        if len(page_text.split()) > 50:  # Avoid summarizing very short pages
            text_chunks = split_text(page_text, max_words=400)  # Break large text
            summary_chunks = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in text_chunks]
            summary = " ".join(summary_chunks)  # Combine summaries
            summaries[f"Page {i+1}"] = summary  # Store summary

    return summaries

# Run the summarization on your PDF
pdf_path = "/content/Artificial Intelligence.pdf"  # Replace with your file path
page_wise_summaries = summarize_pdf(pdf_path, start_page=2)

# Print Summaries
for page, summary in page_wise_summaries.items():
    print(f"\n# {page} Summary:\n{summary}")
