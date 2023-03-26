import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("sample.pdf")

single_line_text = text.replace("\n", "")

print(single_line_text)

# pattern = re.compile(r"")
# matches = pattern.findAll(text)
# names = [n[:-2] for n in matches]
# print(names)
