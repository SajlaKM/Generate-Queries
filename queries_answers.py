from transformers import pipeline

# Load the question-generation model
question_generator = pipeline("text2text-generation", model="t5-small")

def generate_questions(sentences):
    """Generate questions from important sentences"""
    questions = []
    for sentence in sentences:
        q = question_generator(f"generate question: {sentence}", max_length=50)
        questions.append(q[0]['generated_text'])
    return questions

# Generate questions
generated_questions = generate_questions(key_sentences)

# Display results
for i, (q, a) in enumerate(zip(generated_questions, key_sentences)):
    print(f"Q{i+1}: {q}")
    print(f"A{i+1}: {a}\n")
