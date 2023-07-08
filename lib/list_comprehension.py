#!/usr/bin/env python3

def return_evens(num_list):
    evens_comprehension = [n for n in num_list if n % 2 == 0]
    if len(evens_comprehension) == 0:
        return []
    else:
        return evens_comprehension
    

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    else:
        exclamations = [(string + "!") for string in sentence_list]
        return exclamations