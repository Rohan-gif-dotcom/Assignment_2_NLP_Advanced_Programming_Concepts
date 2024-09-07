import spacy
import pandas as pd

# Load the SpaCy models
nlp_sci = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

# Function to extract entities from text in chunks
def extract_entities_in_chunks(nlp, text, entity_labels, chunk_size=100000):
    entities = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        doc = nlp(chunk)
        entities.extend([(ent.text, ent.label_) for ent in doc.ents if ent.label_ in entity_labels])
    return entities

# Open and read the combined text file
with open('output/combined_text.txt', 'r') as file:
    text = file.read()

# Define the labels you're interested in (diseases, drugs, etc.)
disease_drug_labels = ['DISEASE', 'CHEMICAL']

# Extract entities in chunks
sci_entities = extract_entities_in_chunks(nlp_sci, text, disease_drug_labels)
bc5cdr_entities = extract_entities_in_chunks(nlp_bc5cdr, text, disease_drug_labels)

# Save the extracted entities to CSV files for comparison
df_sci = pd.DataFrame(sci_entities, columns=['Entity', 'Label'])
df_bc5cdr = pd.DataFrame(bc5cdr_entities, columns=['Entity', 'Label'])

df_sci.to_csv('sci_entities.csv', index=False)
df_bc5cdr.to_csv('bc5cdr_entities.csv', index=False)

print(f"SpaCy SciSpaCy Model detected {len(sci_entities)} disease/drug entities.")
print(f"SpaCy BC5CDR Model detected {len(bc5cdr_entities)} disease/drug entities.")