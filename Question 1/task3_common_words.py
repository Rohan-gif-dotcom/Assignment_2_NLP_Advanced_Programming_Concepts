import re
from collections import Counter
import pandas as pd

# Step 1 - Open and read the combined text file
with open('output/combined_text.txt', 'r') as file:
    text = file.read()

# Step 2 - Split the text into words using regular expressions
words = re.findall(r'\w+', text.lower())

# Step 3 - Count word occurrences
word_counts = Counter(words)

# Step 4 - Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Step 5 - Save to CSV
df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df.to_csv('top_30_words.csv', index=False)

print("Top 30 most common words saved to 'top_30_words.csv'.")
