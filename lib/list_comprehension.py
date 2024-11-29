#!/usr/bin/env python3

def return_evens(num):
    return [n for n in num if n % 2 == 0]
    # make_list = [ n for n in n range(1,11)]
num_list = range(1,10,2)

print(return_evens(num_list))

def make_exclamation(sentence_list):

    return [n + "!" for n in sentence_list]



print (make_exclamation("I like computers"))