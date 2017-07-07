#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# import time
# from collections import defaultdict
import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
from gensim import corpora, models, similarities

MAX_LINES_TO_PROCESS = 1000000


def simple2word(simple_trigrams):
    words = []
    for trigram in simple_trigrams:
        word = ''.join(trigram)
        words.append(word)
    return words


def name2grams(name_phrase):
    # http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    simple_trigrams = zip(*[name_phrase[i:] for i in range(3)])
    word_trigrams = simple2word(simple_trigrams)
    #simple_quadgrams = zip(*[name_phrase[i:] for i in range(4)])
    #word_quadgrams = simple2word(simple_quadgrams)
    all_words = []
    all_words.extend(word_trigrams)
    #all_words.extend(word_quadgrams)
    all_words.sort()
    return all_words

def get_dictionary():
    print 'Loading dictionary'
    filename = "f:/data/004_modernbusinessbsolutions/name_grams.txt"
    file = open(filename, 'rU')   
    texts = []
    for line in file:
        try:
            line.encode('ascii')
        except Exception, e:
          continue
        words = line.split()
        texts.append(words)
    dictionary = corpora.Dictionary(texts)
    print 'Filtering extremes'
    dictionary.filter_extremes(no_below=10, no_above=0.7)
    print 'Removing 15 most common'
    dictionary.filter_n_most_frequent(15)
    print 'Compacting dictionary'
    dictionary.compactify() 
    return dictionary

def test_lda():
    dictionary = get_dictionary()
    lda = models.LdaModel.load('c:/temp/gensim/c/model.lda')
    print lda
    #lda.print_topics(10)
    doc = "Daniel Usher".upper()
    vec_bow = dictionary.doc2bow(doc.split())
    vec_lsa = lda[vec_bow]
    print vec_lsa


def main():
    # load_name_documents()
    test_lda()

if __name__ == '__main__':
    main()
