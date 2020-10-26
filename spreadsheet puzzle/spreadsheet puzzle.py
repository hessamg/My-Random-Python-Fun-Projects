import csv
import PyPDF2
import re

# Grab all the lines of data.
data = open('Exercise_Files/find_the_link.csv', encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str += data[row_num]

f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)

pattern = r'\d{3}.\d{3}.\d{4}' 
all_text = ''

for n in range(pdf.numPages):
    
    page  = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern,page_text)
    
    if match:
        print(match.group())