"""
Word to Bitstring to Boolean List

Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

Locate the position of the letter in the English alphabet (from 1 to 26).
Odd positions will be represented as 1 and 0 otherwise.
Convert the represented positions to boolean values, 1 for True and 0 for False.
Store the conversions into an array.
Examples
to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0

to_boolean_list("loves") ➞ [False, True, False, True, True]

to_boolean_list("tesh") ➞ [False, True, True, False]

Notes
The letter A is at position 1 and Z at 26.
All input strings are in lowercase letters of the English alphabet.
"""




################################################################
"""
Solution 1
"""


def to_boolean_list(word):
	return [ord(ch)%2 for ch in word]




################################################################
"""
Solution 2
"""


def to_boolean_list(word):
	return [bool(" abcdefghijklmnopqrstuvwxyz".index(i)%2) for i in word]





################################################################
"""
Solution 3
"""


def to_boolean_list(word):
	A=[]
	for x in word:
		if (ord(x)-ord('a')+1)%2:
			A.append(True)
		else:
			A.append(False)
	return A




################################################################
"""
Solution 4
"""


def to_boolean_list(word):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	ans = []
	for i in list(word):
		if i in alphabet:
			if alphabet.index(i) % 2 == 0:
				ans.append(True)
			else:
				ans.append(False)
	return ans



