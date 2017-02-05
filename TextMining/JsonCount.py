# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:53:57 2016

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:01:33 2016

@author: usuario
"""
import ijson
from string import punctuation
from operator import itemgetter

N = 200
words = {}


words_gen = (word.strip(punctuation).lower() for line in open("TEXTDROID-SERVICE-JSONDocuments.json")
                                             for word in line.split())
                                          
for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]

for word, frequency in top_words:
    print "%s: %d" % (word, frequency)