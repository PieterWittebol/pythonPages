import os
from os.path import join as pjoin, expanduser
from PyPDF2 import PdfFileReader

totalPages = 0
totalFiles = 0
directory = expanduser("/mnt/z")
for name in os.listdir(directory):
    if name[-4:] == ".pdf":
        totalFiles += 1
        p=pjoin(directory, name)
        reader = PdfFileReader(open(p, mode="rb"),strict=False)
        pages = reader.getNumPages()
        totalPages += pages
print("Total PDF files:",totalFiles)
print("Total pages in PDF files:",totalPages)
