# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    p = 1000000007
    x = 20
    result = []

    phash = _hash_func(pattern,p,x)
    print(phash)
    H = preHashes(text,len(pattern),p,x)
    print(H)

#    for i in range(len(text) - len(pattern) + 1):
#        thash = _hash_func(text[i:i+len(pattern)],p,x)
#        if phash != thash:
#            continue
#        else:
#            if pattern == text[i:i+len(pattern)]:
#                result.append(i)                   ##这个比较慢，没有理用相近string之间的相似信息。

    for i in range(len(text) - len(pattern)+1):
        if phash != H[i]:
            continue
        else:
            if pattern == text[i:(i+len(pattern))]:
                result.append(i)

    return result


##利用相近的string之间的相似性提前计算所有要求的hash值，提高速度
def preHashes(T,len_P,p,x):
    H = []
    n = len(T) - len_P + 1
    for i in range(n):
        H.append(0)
    s = T[(len(T)-len_P):len(T)]
    H[len(T) - len_P] = _hash_func(s,p,x)

    y = 1

    for i in range(1,len_P+1):
        y = (y * x) % p

    for i in range(len(T) - len_P - 1,-1,-1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len_P])) % p

    return H



def _hash_func(s,p,x):
    ans = 0
    for c in (s):
        ans = ((ans * x + ord(c)) % p + p) % p
    return ans


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
