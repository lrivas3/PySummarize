# NOT READY YET, MIGHT CHANGE SEVERAL THINGS! :exclamation:

# PDF Summarization using Python and AI

This project is designed to assist students in summarizing their class material. The project uses Python and AI to analyze PDF documents and generate summaries of the text. The summaries can be used by students to study and review the material covered in class.

## Requirements

To run this project, you will need:

- Python 3.x
- pdfminer.six module
- NLTK module

## Installation

1. Clone the repository to your local machine
2. Navigate to the project directory in your terminal
3. Create a new virtual environment:

```python3
python3 -m venv env
```

4. Activate the virtual environment:

```
# POSIX 

# bash
source env/bin/activate

# Windows 

# CMD
<venv>\Scripts\activate.bat
# Powershell 
<venv>\Scripts\activate.bat
```

5. Install the required packages:

```python3
pip install pdfminer.six nltk
```


## Usage

To use this project, follow the steps below:

1. Place the PDF file you want to summarize in the `input` folder
2. Navigate to the project directory in your terminal
3. Activate the virtual environment:

```bash
source env/bin/activate
```

4. Run the following command to generate the summary:

```
python summarize.py --input_file <file_name>.pdf --num_sentences <number_of_sentences>
```

Replace `<file_name>` with the name of your PDF file, and `<number_of_sentences>` with the number of sentences you want in your summary.

For example:

```
python summarize.py --input_file sample.pdf --num_sentences 3
```

This command will generate a summary of the `sample.pdf` file with three sentences.

## How it works

The project uses the pdfminer.six module to read the PDF document and extract the text. The text is then preprocessed using the NLTK module, which includes tasks such as tokenization, stopword removal, and stemming. The preprocessed text is then passed to an AI model, which uses natural language processing (NLP) techniques to generate a summary of the text.

## Conclusion

This project provides an easy and efficient way for students to generate summaries of their class material. The use of Python and AI simplifies the process of summarization and provides accurate results.

