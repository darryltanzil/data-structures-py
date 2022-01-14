#/usr/bin/python3

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

tests = []

test = {
    'input': {
        'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 7
    },
    'output': 3
}

tests.append(test)

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# assume the problem will return -1 in case cards does not return query

def locate_card(self, cards: List[int], query: int) -> int:
    pass

result = locate_card(**test['input'], test['output']) 


