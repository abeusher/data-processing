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
    #simple_quadgrams = zip(*[name_phrase[i:] for i in range(4)])
    #word_quadgrams = simple2word(simple_quadgrams)
    all_words = []
    all_words.extend(word_trigrams)
    #all_words.extend(word_quadgrams)
    all_words.sort()
    return all_words


def parse_modern_business_solutions():
    filename = "f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz"
    file = gzip.open(filename, 'rU')
    # fout = gzip.open('f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz', 'wb')
    fout = open(
            'f:/data/004_modernbusinessbsolutions/name_grams.txt', 'w')
    counter = 0
    for line in file:
        counter += 1
        if counter % 250000 == 0:
            print counter
        if counter > 1000000:
            return
        line = line.strip()
        parts = line.split('\t')
        if len(parts) < 11:
            continue
        if len(parts) == 11:
            parts.extend(['', '', ])
        if len(parts) == 12:
            parts.extend(['', ])
        if len(parts) > 13:
            parts = parts[0:13]
        first_name, last_name, gender, address1, city, state, zipcode, email, job, ipv4_address, inAccountName, createdAt, updatedAt = parts
        name_phrase = first_name + last_name
        name_grams = name2grams(name_phrase)
        text = " ".join(name_grams)
        fout.write(text + '\n')
    print counter
    print "All done."
    fout.close()


def main():
    parse_modern_business_solutions()


if __name__ == '__main__':
    main()
