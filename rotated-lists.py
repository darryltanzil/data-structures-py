num = [5, 6, 9, 0, 2, 3, 4]
result1 = 3

test1 = [1,2,3,4,5,6]
result1 = 0

test2 = [5,1,1,1,2,3,4]
result2 = 1

test3 = [2,3,4,5,1]
result3 = 4


tests = [test1, test2, test3]
results = [result1, result2, result3]

# given original list, determine amount of rotations before reaching new list
# rotation is defined as taking last index of list and putting it before the 1st

# find the lowest number in the list, if is the lowest, then check for its index

def findLowest(l:list) -> int:
    low = 0
    high = len(l)
    mid = 0
    i = 0

    while low <= high:
        mid = (low + high) // 2
        i += 1
        if l[mid-1] > l[mid]:
            return i 
        elif  l[mid-1] < mid: # if the lowest is greater then mid, ignore lower half, otherwise, ignore higher half
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

for count, values in enumerate(tests):
    print(f"Test Output: {findLowest(values)} --> Expected output: {results[count]}")




