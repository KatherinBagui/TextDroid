# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:31:01 2016

@author: Usuario
"""

import json 
import nltk
import re, string 


with open('/Users/Usuario/archi/TEXTD.json') as file:
     data=json.load(file)
def tokenize(data):
    data = re.sub("[^a-zA-Z]"," ",data)
    data = re.sub(r'\b\w{1,2}\b',' ',data)
    data = re.sub(r'http[\bs]*',' ',data)
    data = re.sub(r'telefonos','telefono',data)
    data=  re.sub('[^\w]' % re.escape(string.punctuation),' ',data)
    tokens = nltk.word_tokenize(data)
    return tokens
print (data)