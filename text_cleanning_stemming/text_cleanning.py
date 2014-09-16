# ################################################################## #
# File name: mr_per_term_idf.py                                      #
# Author: Yixin Chen, Shareaholic, Inc.                              #
# Created: 07/24/2014                                                #
# Last modified: 07/24/2014                                          #
# Python Version: 2.7                                                #
# Dependencies: argsparse, NLTK                                      #
# Note: this text-cleaning script removes all the images, html       #
#       tags and stoplist, as well as stemming the text.             #
# cmd: python text_cleanning.py --input file.txt                     #
# ################################################################## #

import argparse
from nltk.corpus import stopwords
from nltk.stem.porter import *
import re

if (__name__ == "__main__"):

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', action='store', dest='input', help='text cleanning & stemming.')
    args = parser.parse_args()
    input_file_ori = args.input
    input_file = input_file_ori.replace('.txt','').replace('.nlp','')

    stemmer = PorterStemmer()
    f_o = open('{0}_after_cleanning_stemming.txt'.format(input_file), 'w')
    f_i = open(input_file_ori)
    for line in f_i:
        new_line = ''
        # remove all the html tags
        line = re.sub(r'</?\w+((\s+\w+(\s*=\s*(?:".*?"|\'.*?\'|[^\'">\s]+))?)+\s*|\s*)/?>', ' ', line)
        # remove all the punctuations
        line = re.sub(r'[^\w]', ' ', line)

        word_set = line.split(' ')
        for w in word_set:
            # remove all the stop words
            if w not in stopwords.words('english'):
                # stemming
                new_line = new_line + stemmer.stem(w) + ' '
        f_o.write(new_line+'\n')
        
    f_i.close()
    f_o.close()
    print('process finish.')
 