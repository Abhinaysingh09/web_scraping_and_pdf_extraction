import re
import json

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\W', ' ', text)   # Remove special characters
    return text.lower()

def preprocess_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    cleaned_data = {key: clean_text(value) for key, value in data.items()}
    return cleaned_data

webpage_cleaned_data = preprocess_data("webpage_data.json")
pdf_cleaned_data = preprocess_data("pdf_data.json")

with open("cleaned_data.json", 'w') as f:
    json.dump({**webpage_cleaned_data, **pdf_cleaned_data}, f)
