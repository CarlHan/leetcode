# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    p = 5000003
    x = 58
    result = []

    phash = _hash_func(pattern,p,x)
    #H = preHashes(text,len(pattern),p,x)
    #print(H)

    for i in range(len(text) - len(pattern) + 1):
        thash = _hash_func(text[i:i+len(pattern)],p,x)
        if phash != thash:
            continue
        else:
            if pattern == text[i:i+len(pattern)]:
                result.append(i)

#    for i in range(len(text) - len(pattern)):
#        if phash != H[i]:
#            continue
#        else:
#            if pattern == text[i:(i+len(pattern))]:
#                result.append(i)

    return result

##可以提前快速计算text的所有hash
def preHashes(T,len_P,p,x):
    H = []
    n = len(T) - len_P + 1
    for i in range(n):
        H.append(0)
    s = T[(len(T)-len_P):len(T)]
    H[-1] = _hash_func(s,p,x)

    y = 1

    for i in range(1,len_P):
        y = (y * x) % p

    for i in range(len(T) - len_P - 1,-1,-1):
        H[i] = (x * H[i+1] + ord(T[i]) - y * ord(T[i + len_P])) % p

    return H



def _hash_func(s,p,x):
    ans = 0
    for c in (s):
        ans = (ans * x  + ord(c)) % p
    return ans


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
