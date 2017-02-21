#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle
import argparse
import util
import load_data


if __name__ == "__main__":
    try:
        # set command-line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--histogram_path", help="input: set a path a histogram(.pkl)")
        parser.add_argument("--min_count", help="input: ignore a word whose frequency is less than it")
        parser.add_argument("--word2index_path", help="output: set a path a word2index file(.pkl)")
        parser.add_argument("--index2word_path", help="output: set a path an index2word file(.pkl)")

        # parse arguments
        args = parser.parse_args()
        histogram_path = args.histogram_path
        min_count = int(args.min_count)
        word2index_path = args.word2index_path
        index2word_path = args.index2word_path

        # check paths
        util.check_input_path(histogram_path)
        util.check_output_path(word2index_path)
        util.check_output_path(index2word_path)

        histogram = cPickle.load(open(histogram_path))
        print(len(histogram))
        load_data.reduce_words(histogram, min_count=min_count)
        print(len(histogram))
    except IOError, e:
        print(e)
