# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:06:45 2024

@author: Abk
"""
# ran in eclipse not in spyder bcoz of module problem.
#import PyPDF2
import os
from PyPDF2 import PdfWriter
src = "C:\\Users\\lab\\HundredDaysOfCode\\PDfs"

file1 = os.path.join(src, "Image1.pdf");
file2 = os.path.join(src, "Image3.pdf");
file3 = os.path.join(src, "Image6.pdf");
file4 = os.path.join(src, "Image26.pdf");
merger = PdfWriter()

for pdf in [file1, file2, file3, file4]:
    merger.append(pdf)

merger.write("merged-pdf-eclipse.pdf")
merger.close()
print("done!")
