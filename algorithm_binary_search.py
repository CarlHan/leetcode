# Uses python3
import sys
import math

def binary_search(a, x, left, right):

    if(left > right):
        return  -1

    mid = (left + math.floor((right-left) / 2))

    if (x == a[mid]):
        return mid
    elif(x < a[mid]):
        return binary_search(a,x,left,mid-1)
    else:
        return binary_search(a,x,mid+1,right)

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        left, right = 0, len(a) - 1
        print(binary_search(a,x,left,right))
