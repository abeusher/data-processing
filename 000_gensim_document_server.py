#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import utils
from simserver import SessionServer
service = SessionServer('c:/temp/gensim')  # or wherever


def index_input_texts():
    texts = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
    corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
              for num, text in enumerate(texts)]
    # service.index(corpus)
    service.train(corpus, method='lsi')
    service.index(corpus)  # index the same documents that we trained on...

def query_the_index(input):
    doc = {'tokens': utils.simple_preprocess(input)}
    results = service.find_similar(doc, min_score=0.4, max_results=5)
    for result in results:
        document_id, score_number, junk_variable = result
        print "document_id:%s\t score:%.2f" % (document_id, score_number)


def main():
    input_to_query = "Human machine interface of random binary unordered trees"
    query_the_index(input_to_query)


if __name__ == '__main__':
    main()
