from transformers import pipeline

# Load Pre-trained Summarization Pipeline
summarizer = pipeline("summarization", model="t5-small")

# Function for Abstractive Summarization
def summarize_text_abstractive(text, max_length=150, min_length=50):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Generate Abstractive Summary
abstractive_summary = summarize_text_abstractive(pdf_text, max_length=150, min_length=50)

print("Abstractive Summary:\n", abstractive_summary)
