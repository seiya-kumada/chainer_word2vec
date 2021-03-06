# Word Embedding

This is an example of word embedding.
We implemented Mikolov's Skip-gram model and Continuous-BoW model with Hierarchical softmax and Negative sampling.

Run `train_word2vec.py` to train and get `word2vec.model` which includes embedding data.
You can find top-5 nearest embedding vectors using `search.py`.

This example is based on the following word embedding implementation in C++.
https://code.google.com/p/word2vec/

# Procedures

## generate word2index and index2word

Use `load_data.py` through `run_load_data`.

## reduce words

We have to make the number of words be less than 661000 to avoid the cuda memory error.
To do this, use `reduce_words.py` throught `run_reduce_words`.

## select words which are used for DeViSE

There are many categories each of which has some images(<=1000).
Names of categories which are used for the project, DeViSE, must be included in vocabularies for word2vec.
Using `find_words.py` through `run_find_word`, categories which meet the condition are decided. 

## check out categories for CNN to assure that they are included in the vocabularies for word2vec 
use `run_check_words`.

## copy selected directories

Directories with those names which are decided in above procedure are copied.
Use `copy_selected_image_directory.py` through `run_copy_selected_image_directory`.

## make index file 

All words appeared in Wiki corpus are converted to indices by means of word2index.
Use `index_sequence_maker.py` through `run_index_sequence_maker`.

## training 

Use `train_word2vec.py` through `run_train`.

## prediction

Observe the accuracy of a language model by using labels which are trained by CNN.
Use `run_predict_similarities`.`
