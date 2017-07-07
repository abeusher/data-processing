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
    simple_quadgrams = zip(*[name_phrase[i:] for i in range(4)])
    word_quadgrams = simple2word(simple_quadgrams)
    all_words = []
    all_words.extend(word_trigrams)
    all_words.extend(word_quadgrams)
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


def load_name_documents():
    filename = "f:/data/004_modernbusinessbsolutions/name_grams.txt"
    file = open(filename, 'rU')
    # fout = gzip.open('f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz', 'wb')
    #texts = [[word for word in line.split()] for line in file]
    texts = []
    for line in file:
        try:
            line.encode('ascii')
        except Exception, e:
          continue
        words = line.split()
        texts.append(words)
        #for text in texts:
        #  print text
        """
        #https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/Corpora_and_Vector_Spaces.ipynb
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1
        texts = [[token for token in text if frequency[token] > 1] for text in texts]
        for text in text:
          print text
        """
    print 'Making dictionary'
    dictionary = corpora.Dictionary(texts)            
    print 'Filtering extremes'
    dictionary.filter_extremes(no_below=10, no_above=0.7)
    print 'Removing 15 most common'
    dictionary.filter_n_most_frequent(15)
    print 'Compacting dictionary'
    dictionary.compactify()
    print "Saving dictionary"
    dictionary.save('c:/temp/gensim/c/name_grams.dict')
    dictionary.save_as_text('c:/temp/gensim/c/name_grams_text.txt', sort_by_word=False)
    print 'Dictionary size', len(dictionary)# 163908 unique name fragments
    print 'creating corpus of dictionary and texts'
    corpus = [dictionary.doc2bow(text) for text in texts]
    print 'Saving corpus'
    corpora.MmCorpus.serialize('c:/temp/gensim/c/name_grams.mm', corpus)


def load_dictionary():
    dictionary = get_dictionary()    
    corpus = corpora.MmCorpus('c:/temp/gensim/c/name_grams.mm')
    print 'make an LDA model'
    # lda = models.LdaModel(corpus, id2word=dictionary, num_topics=10)
    # https://rare-technologies.com/multicore-lda-in-python-from-over-night-to-over-lunch/
    lda = models.LdaMulticore(corpus, id2word=dictionary, num_topics=10, workers=3)
    lda.save('c:/temp/gensim/c/model.lda') # same for tfidf, lda, ...


def main():
    # load_name_documents()
    load_dictionary()


if __name__ == '__main__':
    main()
