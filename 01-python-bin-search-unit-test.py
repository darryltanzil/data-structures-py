import unittest

#/usr/bin/env python3

# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down
# in a sequence on a table. She challenges Bob to pick out the card 
# containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# 1 State problem clearly.
# 2 Write signature.
# 3 Check-expects
# 4 Come up with correct solution.

# 1 Write a program to find position of a given number in a list of numbers arranged in
# decreasing order.

# Test cases

# The number query occurs somewhere in the middle of the list cards.
# query is the first element in cards.
# query is the last element in cards.
# The list cards contains just one element, which is query.
# The list cards does not contain number query.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number query occurs at more than one position in cards.
# (can you think of any more variations?)

# assume the problem will return -1 in case cards does not return query
# function returns the first occurence of query

# state the brute force solution

def locate_card(cards, query) -> int:
    pass
    
assert locate_card([13, 11, 10, 7, 4, 3, 1, 0], 7), 3




    


