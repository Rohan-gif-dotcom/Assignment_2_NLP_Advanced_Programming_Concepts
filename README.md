# Assignment 2: Natural Language Processing and Programming Challenges

**This repository contains solutions to Assignment 2, focusing on NLP tasks, image processing, string manipulation, and code decryption.** It leverages Python libraries such as SpaCy, SciSpacy, BioBERT, and PIL to solve these tasks.

---

## 🛠 Installation Instructions

To install and set up the environment for this assignment, use the provided `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate assignment2_env
```

---

## 💻 Models and Libraries Used

| Library        | Description                               | Install URL |
|----------------|-------------------------------------------|-------------|
| spaCy          | General NLP library                       | [SpaCy](https://spacy.io/) |
| scispaCy       | Biomedical text processing                | [scispaCy](https://allenai.github.io/scispacy/) |
| BioBERT        | Transformer-based model for biomedical NLP | [BioBERT](https://github.com/dmis-lab/biobert) |
| PIL            | Image processing in Python                | [Pillow](https://pypi.org/project/Pillow/) |

---

## 📂 File Structure

The repository is organized as follows:

```
Assignment2/
├── Question1/
│   ├── data/                       # Input CSV files
│   ├── output/                     # Generated outputs (CSV, text files)
│   ├── task1_text_extraction.py    # Code for text extraction
│   ├── task2_library_installation.md  # Installation instructions for NLP libraries
│   ├── task3_common_words.py       # Common word extraction
│   ├── task3_tokenizer.py          # Tokenization using BioBERT
│   ├── task4_ner.py                # Named Entity Recognition (NER) using SciSpacy
│   ├── task4_comparison.py         # NER model comparison
├── Question2/
│   ├── images/                     # Image files
│   ├── output/                     # Processed images and result files
│   ├── chapter1_image_processing.py  # Image pixel modification task
│   ├── chapter2_string_manipulation.py  # String manipulation task
│   ├── chapter3_caesar_cipher_decryption.py  # Caesar cipher decryption task
├── Question3/
│   ├── decrypted_code.py           # Decrypt and correct an encrypted Python code
├── environment.yml                 # Conda environment setup file
└── README.md                       # Project overview
```

---

## 📝 Task Descriptions

### **Question 1: NLP Tasks with CSV Data**

#### Task 1: Text Extraction (`task1_text_extraction.py`)
- **Objective**: Extract the text from multiple CSV files and combine it into a single `.txt` file.
- **Output**: `combined_text.txt` (saved in the `output` directory).

#### Task 2: Library Installation (`task2_library_installation.md`)
- **Objective**: Install necessary NLP libraries like SpaCy, SciSpacy, and BioBERT using Conda.

#### Task 3.1: Common Words Count (`task3_common_words.py`)
- **Objective**: Count the top 30 most common words in the combined text file.
- **Output**: CSV file containing top 30 words (`top_30_words.csv`).

#### Task 3.2: Tokenization (`task3_tokenizer.py`)
- **Objective**: Tokenize the text using BioBERT's Auto Tokenizer and count the top 30 tokens.
- **Output**: CSV file containing top 30 tokens (`top_30_tokens.csv`).

#### Task 4: Named Entity Recognition and Comparison (`task4_ner.py`, `task4_comparison.py`)
- **Objective**: Perform Named Entity Recognition (NER) using SciSpacy and BioBERT models, and compare the results.
- **Output**: Entity recognition results in `sci_entities.csv` and `bc5cdr_entities.csv`.

---

### **Question 2: Image and String Manipulation Tasks**

#### Chapter 1: Image Processing (`chapter1_image_processing.py`)
- **Objective**: Modify pixel values in an image and sum the red pixel values.
- **Output**: Modified image saved as `chapter1out.png`.

#### Chapter 2: String Manipulation (`chapter2_string_manipulation.py`)
- **Objective**: Process a string by separating numbers and letters, then convert even numbers and uppercase letters to ASCII values.
- **Output**: The resulting ASCII values are printed.

#### Chapter 3: Caesar Cipher Decryption (`chapter3_caesar_cipher_decryption.py`)
- **Objective**: Decrypt a Caesar cipher using either a known shift value or brute-force all possible shifts.
- **Output**: Decrypted text is printed.

---

### **Question 3: Code Decryption and Error Fixing**

#### Decrypted Code (`decrypted_code.py`)
- **Objective**: Decrypt and correct a Python script encrypted with a Caesar cipher. Add comments explaining the corrections.
- **Output**: Corrected code with comments is printed.

---

## ▶️ Running the Code

Ensure that your environment is activated:
```bash
conda activate assignment2_env
```

Then, run the scripts by calling Python commands. For example:
```bash
# Run the text extraction task in Question 1
python Question1/task1_text_extraction.py
```

Follow the task-specific instructions for further details on the outputs.

