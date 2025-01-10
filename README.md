# TEXT-SUMMARIZATION-TOOL

**COMPANY**: CODTECHIT SOLUTIONS

**NAME**: SHAIK RIZWANA KHATUN

**INTERN ID**: CT08DHQ

**DOMAIN**: ARTIFICIAL INTELLIGENCE

**BATCH DURATION**: DECEMBER 12TH,2024 TO JANUARY 12TH,2025

**MENTOR NAME**: NEELA SANTHOSH KUMAR

**OVERVIEW**
Certainly! Here's a brief overview of the provided Python script:

### **Overview**:
The Python script uses **Natural Language Processing (NLP)** techniques to summarize lengthy articles into concise summaries. It leverages the `transformers` library from Hugging Face, which provides access to powerful pre-trained models like **BART** or **T5** that are specifically fine-tuned for text summarization tasks.

### **How It Works**:
1. **Model Setup**: 
   The script loads a pre-trained summarization model (`facebook/bart-large-cnn`) using the `pipeline` function from the `transformers` library.

2. **Summarization Process**:
   - The function `summarize_article()` receives a lengthy article as input.
   - It processes the text using the model and generates a concise summary with configurable maximum and minimum length parameters.

3. **Output**: 
   The script prints both the **original article** and the **summary**. The summary is a shorter, more digestible version of the original text that retains the key ideas.

### **Key Features**:
- **Automatic Summarization**: Generates summaries from input articles automatically.
- **Customizable**: You can adjust the length of the summary and swap out models for different summarization approaches.
- **Pre-trained Models**: Uses state-of-the-art transformer models like BART or T5 for high-quality summaries.

In essence, the script is designed to streamline the process of summarizing long text into short, coherent summaries.

#OUTPUT OF THE TASK
![Screenshot (6)](https://github.com/user-attachments/assets/2e57afdc-85c4-4953-9f4c-2061ff0acb74)

