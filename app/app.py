import os
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load the environment variables from .env file
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client with your API key
client = OpenAI(
    api_key=os.environ.get('OPEN_AI_API_KEY'),
)

# Constants for the OpenAI model and summary configuration
model = "gpt-3.5-turbo"  # You can switch to "gpt-4" if you have access
temperature = 0.3
max_tokens = 500
topic = "money"  # Topic for the summary (can be any topic)

# Read the PDF file
file_path =   "Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf"# Update with your PDF path

book_text = ""

with pdfplumber.open(file_path) as pdf:
    # Extract text from a specific range of pages
    start_page = 23
    end_page = len(pdf.pages) - 30  # Adjust based on your PDF structure
    for page_num in range(start_page, end_page):
        page = pdf.pages[page_num]
        book_text += page.extract_text()

# Check if the text extraction worked
print(f"Extracted text: {book_text[:500]}")  # Preview first 500 characters of the extracted text

# Create a prompt based on the extracted text and the desired topic
def generate_prompt(book, topic):
    return f"""
    You are a helpful assistant. You have the following book text:
    {book}

    Please provide a summary of the key points related to the topic "{topic}".
    """

# Prepare the system message and user input for the OpenAI model
system_message = "You are a helpful assistant that summarizes books based on a given topic."
prompt = generate_prompt(book_text, topic)

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompt},
]

# Function to get the summary from OpenAI API
def get_summary():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return completion.choices[0].message.content

# Print the summary
print(get_summary())
