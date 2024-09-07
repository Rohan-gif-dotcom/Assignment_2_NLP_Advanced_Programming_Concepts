import spacy


# Load SciSpacy model (for diseases and drugs)
def extract_scispacy_entities(text, chunk_size=1000000):
    nlp = spacy.load("en_ner_bc5cdr_md")

    # Split the text into smaller chunks if it exceeds the max_length
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    scispacy_entities = {"diseases": [], "drugs": []}

    for chunk in chunks:
        doc = nlp(chunk)
        for ent in doc.ents:
            if ent.label_ == "DISEASE":
                scispacy_entities["diseases"].append(ent.text)
            elif ent.label_ == "CHEMICAL":
                scispacy_entities["drugs"].append(ent.text)

    return scispacy_entities


# Example usage
if __name__ == "__main__":
    with open("output/combined_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Extract entities using SciSpacy with chunking
    scispacy_entities = extract_scispacy_entities(text)

    # Output the results
    print(f"Total diseases detected by SciSpacy: {len(scispacy_entities['diseases'])}")
    print(f"Total drugs detected by SciSpacy: {len(scispacy_entities['drugs'])}")
