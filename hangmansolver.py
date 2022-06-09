import re
import itertools
import time
from itertools import permutations, combinations, product
import string
import numpy
import enchant
from english_words import english_words_set
from qualifier import make_table

def hangman(word):
	d = enchant.Dict("en_US")
	word = re.sub("-", ".", word) + "$"
	possibilities = [x for x in english_words_set if re.match(word, x)]
	resultList = []
	count=0
	if possibilities:
		for x in possibilities:
			count+=1
			resultList.append([count, x])
		return make_table(resultList, ["No.", "Word"], centered=True)
	else:
		print("No matches lmao, ur hangman game is trippin")

wordd = input("input a word mf\n")
print(hangman(wordd))