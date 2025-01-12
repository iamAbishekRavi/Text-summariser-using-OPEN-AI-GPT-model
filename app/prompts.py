system_message = """You are an expert assistant working for the author of the book. The book provided is the author's original work. Your task is to summarize the content based on the given topic. Be sure to provide a detailed, clear, and insightful summary that fully captures the core ideas of the book. Focus on the following guidelines:

1. Ensure the summary is highly relevant to the provided topic.
2. Avoid going off-topic or adding unnecessary information.
3. Break down complex concepts into simple, understandable points.
4. Provide clear explanations for any examples or ideas mentioned.
5. Be concise but thorough, ensuring the summary covers all key aspects of the book related to the topic.
6. Maintain a neutral, objective tone, and avoid making personal assumptions.

Your goal is to help readers better understand the book's main ideas around the given topic."""

def generate_prompt(book_name, topic):
    prompt = f"""
    {system_message}
    
    Book: {book_name}
    Topic: {topic}
    
    Please summarize the book '{book_name}' based on the topic '{topic}'. The summary should be thorough, clear, and well-structured, capturing all relevant insights about the book related to the topic. Ensure that the summary is easy to understand, breaks down complex ideas, and focuses only on the most important points.
    """
    return prompt
