# First install the 'pdf2docx'
pip install pdf2docx

# Now import 'Converter' from 'pdf2docx' to convert pdf file docx file 
from pdf2docx import Converter

# Assign a PDF document that must be converted to Docx. 
pdf_file = 'Project proposal.pdf'

# Replace "sample" with the desired file name you want for the docx file.
docx_file = 'sample.docx'

# initialize converter
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()