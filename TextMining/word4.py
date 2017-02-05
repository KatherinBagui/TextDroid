# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:00:07 2016

@author: Usuario
"""
  

import docx2txt
my_text = docx2txt.process("creaciondeunaguarderia.docx")
my_text.close()


