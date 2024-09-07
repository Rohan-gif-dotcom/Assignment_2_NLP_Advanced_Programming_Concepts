from transformers import AutoTokenizer
from collections import Counter
import pandas as pd

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Function to process text in chunks
def tokenize_in_chunks(text, chunk_size=10000):
    tokens = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        tokens.extend(tokenizer.tokenize(chunk))
    return tokens

# Open and read the combined text file in chunks
with open('output/combined_text.txt', 'r') as file:
    text = file.read()

# Tokenize the text in chunks to reduce memory usage
tokens = tokenize_in_chunks(text)

# Count token occurrences
token_counts = Counter(tokens)

# Get the top 30 most common tokens
top_30_tokens = token_counts.most_common(30)

# Save to CSV
df_tokens = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])
df_tokens.to_csv('top_30_tokens.csv', index=False)

print("Top 30 most common tokens saved to 'top_30_tokens.csv'.")