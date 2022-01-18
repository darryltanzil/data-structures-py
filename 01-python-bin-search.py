from typing import List

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

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# brute force algorithm
def locate_card(cards, query) -> int:
	res = -1
	for count, value in enumerate(cards):
		if value == query:
			res = count
	return res 
	
# assume the problem will return -1 in case cards does not return query
# function returns the first occurence of query

# binary search
def locate_card(cards, query, start, end) -> int:
if start > end:
	return -1
mid = (start + end) // 2
if query == cards[mid]
	return mid
elif query > cards[mid]
	return locate_card(cards, query, mid+1, end)
else:
	return locate_card(cards, query, start, mid-1)

# iterative solution 
​​class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
	
        def bin_search(nums, target, start, end):
            if start > end:
                return -1
            
            mid = (start + end) // 2

            if target == nums[mid]
			
		elif target > nums[mid]:
			return bin_search(nums, target, mid+1, end)
		else:
			return bin_search(nums, target, start, mid-1)

for i in tests:
    result = locate_card(i.get('input', {}).get('cards'), i.get('input', {}).get('query'), 0, len(i.get('input', {}).get('cards')))
    print("input: " + str(i) + "output: " + str(result))
    print('Test has passed! \n' if result == i.get('output') else "Test has not passed. \n")



    


