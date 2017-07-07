#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# import time
import gzip


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


def load_name_documents():
    filename = "f:/data/004_modernbusinessbsolutions/name_grams.txt"
    file = open(filename, 'rU')
    # fout = gzip.open('f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz', 'wb')    
    counter = 0
    for line in file:
        counter += 1
        if counter % 250000 == 0:
            print counter
        if counter > 1000000:
            return
        line = line.strip()
        print line


def main():
    load_name_documents()


if __name__ == '__main__':
    main()
