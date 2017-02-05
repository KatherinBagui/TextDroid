# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 20:18:44 2016

@author: Usuario
"""

from pdfminer.pdfparser import PDFParser

from pdfminer.pdfdocument import PDFDocument

from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from pdfminer.converter import TextConverter

from pdfminer.layout import LAParams

from pdfminer.pdfpage import PDFPage






def convertir(archivo, paginas=None):
    if not paginas:
        pagenums = set()
    else:
        pagenums = set(paginas)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = file("Licenciatura19.pdf", 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    texto = output.getvalue()
    output.close
    return texto

if __name__ == "__main__":


 print convertir("Licenciatura19.pdf")
 

