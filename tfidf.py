# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:50:34 2018

@author: Veronica Schmidt
"""
import math

def wordCount(word, word_list):
    return word_list.count(word)

def tf(word, word_list):
    return word_list.count(word)/len(word_list)

def n_containing(word, list_of_word_lists):
    return sum(1 for w in list_of_word_lists if word in w)

def idf(word, list_of_word_list):
    return math.log(len(list_of_word_list) / (1 + n_containing(word, list_of_word_list)))

def tfidf(word, word_list, list_of_word_lists):
    return tf(word, word_list) * idf(word, list_of_word_lists)

def getTopWords(list_of_word_lists, num):
    topWords =[]
    for i, word_list in enumerate(list_of_word_lists):
        scores = {word: tfidf(word, word_list, words) for word in word_list}
        sorted_words = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:num])
        topWords.append(sorted_words)      
    return topWords