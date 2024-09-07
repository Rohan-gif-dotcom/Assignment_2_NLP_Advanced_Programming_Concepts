import pandas as pd

# Load CSV files and limit the number of rows to 1000 to
df1 = pd.read_csv('data/CSV1.csv', nrows=1000)
df2 = pd.read_csv('data/CSV2.csv', nrows=1000)
df3 = pd.read_csv('data/CSV3.csv', nrows=1000)
df4 = pd.read_csv('data/CSV4.csv', nrows=1000)

# Extract 'text' column if it exists
def extract_text(df):
    return df['TEXT'].tolist() if 'TEXT' in df.columns else []

# Combine text from all CSVs
text1 = extract_text(df1)
text2 = extract_text(df2)
text3 = extract_text(df3)
text4 = extract_text(df4)

combined_text = text1 + text2 + text3 + text4

# Save the reduced text to a file
with open('output/combined_text.txt', 'w') as f:
    for line in combined_text:
        f.write(f"{line}\n")

print("Reduced combined text saved to 'combined_text.txt'.")
