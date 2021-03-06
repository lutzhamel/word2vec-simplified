#!/usr/bin/env python
"""
#####################################################################
word2vec.py

An example program that uses our simplified word2vec model.

written by Lutz Hamel, (c) 2018 - The University of Rhode Island
#####################################################################
"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = 'word2vec.pkl'

#####################################################################
# execute only if run as a script
if __name__ == "__main__":

    # load our word2vec model into memory
    word2vec = pd.read_pickle(MODEL_NAME)

    # let's peek at some of the words in the model
    words = list(word2vec.index)
    print("Some example words in the model: {}"\
              .format(words[30:35]))
    
    # pull out some words and look at their semantic similarity
    tree_vec = word2vec.loc['tree']
    branch_vec = word2vec.loc['branch']
    triangle_vec = word2vec.loc['triangle']

    # cosine_similarity is an easy metric in order to compare
    # the similarity between two vectors.
    result = cosine_similarity([tree_vec],
                               [branch_vec,triangle_vec])

    tree_branch_sim = result[0,0]
    tree_triangle_sim = result[0,1]

    if tree_branch_sim > tree_triangle_sim:
        print("branch is more related to tree than triangle")
    else:
        print("triangle is more related to tree than branch")

    # let's try the classic example: king-man+woman = queen
    king_vec = word2vec.loc['king']
    man_vec = word2vec.loc['man']
    woman_vec = word2vec.loc['woman']
    queen_vec = word2vec.loc['queen']

    female_king_vec = king_vec - man_vec + woman_vec

    result = cosine_similarity([female_king_vec,king_vec],
                               [queen_vec])

    female_king_queen_sim = result[0,0]
    king_queen_sim = result[1,0]

    if female_king_queen_sim > king_queen_sim:
        print("female king is more similar to queen than king")
    else:
        print("king is more similar to queen than female king")


