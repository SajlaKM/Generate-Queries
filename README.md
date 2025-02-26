# Generate-Queries
# **📘 AI PDF Summarizer & Q&A Generator**  
🔹 **Extract Extractive & Abstractive Summaries** from research papers  
🔹 **Generate Key Queries & Answers** using NLP & Transformers  
🔹 **Process PDFs Automatically & Save Results as JSON**  

---

## **📌 Features**  
✔ **Download PDFs** from URLs  
✔ **Extract Text** from PDFs  
✔ **Generate Extractive Summaries** (TextRank)  
✔ **Generate Abstractive Summaries** (BART/T5)  
✔ **Generate Important Q&A** (TF-IDF + T5)  
✔ **Save Q&A in JSON Format**  

---

## **📥 Installation**  

Clone this repository:  
```bash
git clone https://github.com/your-username/AI-PDF-Summarizer.git
cd AI-PDF-Summarizer
```

### **🔹 Install Dependencies**  
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## **🚀 Usage**  

### **1️⃣ Download PDF from URL**  
```python
python download_pdf.py --url "https://example.com/sample.pdf" --output "document.pdf"
```

### **2️⃣ Extract Text from PDF**  
```python
python extract_text.py --pdf "document.pdf"
```

### **3️⃣ Generate Extractive Summary**  
```python
python extractive_summary.py --pdf "document.pdf" --sentences 10
```

### **4️⃣ Generate Abstractive Summary**  
```python
python abstractive_summary.py --pdf "document.pdf" --max_length 200
```

### **5️⃣ Generate Q&A from Text**  
```python
python generate_qna.py --pdf "document.pdf" --top_n 10
```

### **6️⃣ Save Results as JSON**  
Q&A results are saved automatically in `qa_pairs.json`.  

---

## **📝 Example Output**  
```json
{
  "question": "What are the ethical concerns of AI?",
  "answer": "Ethical concerns about AI development continue to grow due to its unpredictable risks and biases."
}
```

---

## **📌 File Structure**
```
📂 AI-PDF-Summarizer
├── 📜 README.md
├── 📜 requirements.txt
├── 📄 download_pdf.py
├── 📄 extract_text.py
├── 📄 extractive_summary.py
├── 📄 abstractive_summary.py
├── 📄 generate_qna.py
├── 📂 data
│   ├── 📄 document.pdf
│   ├── 📜 extracted_text.txt
│   ├── 📜 qa_pairs.json
```

---

## **🤝 Contributing**
1. **Fork** the repository  
2. **Clone** your fork  
   ```bash
   git clone https://github.com/your-username/AI-PDF-Summarizer.git
   ```
3. **Create a new branch**  
   ```bash
   git checkout -b feature-branch
   ```
4. **Make changes & commit**  
   ```bash
   git commit -m "Added new feature"
   ```
5. **Push to GitHub**  
   ```bash
   git push origin feature-branch
   ```
6. **Create a Pull Request (PR)**  

---

## **📜 License**
This project is licensed under the **MIT License**.  

---

## **📧 Contact**  
For issues & improvements, open a GitHub **issue** or reach out at:  
📩 **sajiss5751@gmail.com**  

---

