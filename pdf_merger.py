from PyPDF2 import PdfMerger
import sys

pdfs = sys.argv[1:]
if len(pdfs) < 2:
    print("Pass at least to files")
    exit

result_file_name = pdfs[0][:-4] + '_merged.pdf'
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(result_file_name)
merger.close()