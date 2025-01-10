# Import necessary libraries
from transformers import pipeline

# Create a summarizer pipeline using a pretrained BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(article_text: str, max_length: int = 150, min_length: int = 50):
    """
    Summarizes a lengthy article using a pre-trained BART model.
    
    Parameters:
        article_text (str): The article content to summarize.
        max_length (int): The maximum length of the summary in tokens.
        min_length (int): The minimum length of the summary in tokens.

    Returns:
        str: A concise summary of the article.
    """
    
    # Generate the summary
    summary = summarizer(article_text, max_length=max_length, min_length=min_length, do_sample=False)
    
    return summary[0]['summary_text']

# Example Input: A lengthy article (can be replaced with any text)
article_text = """
In the ever-evolving field of technology, artificial intelligence (AI) stands as one of the most groundbreaking
advancements of the 21st century. AI has permeated various sectors including healthcare, finance, transportation,
and entertainment, transforming the way industries operate and improving efficiencies. The concept of AI revolves
around machines or systems being able to perform tasks that would typically require human intelligence. This includes
tasks such as problem-solving, learning, pattern recognition, and even understanding and generating human language.
Despite the vast potential of AI, there are concerns regarding its ethical implications, privacy issues, and the
impact on employment. As AI continues to develop, society must carefully navigate these challenges while harnessing
its potential to improve quality of life and increase productivity.
"""

# Summarize the article
summary = summarize_article(article_text)
print("Original Article:\n", article_text)
print("\nConcise Summary:\n", summary)