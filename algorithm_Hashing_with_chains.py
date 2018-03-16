# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.hashtable = []
        
        ##建表，表长为bucket_count，每个位置处是一个chain结构
        for i in range(self.bucket_count):
            self.hashtable.append([])
        ##这个位置建表的时候可千万别用 self.hashtable = [[]] * self.bucket_count, 这样出现的问题是：
        ##python此时并没有一个含有bucket_count数目的独立的[]，而只是在内存中指向同一个[]，所以导致的结果就是
        ##如果想对其中一个比如hashtable[3].append(3)时，此时打印整个table会发现table中所有元素[]都append进去了一个3，因为它们
        ##指向的都是同一个内存位置。所以需要用上面那个操作来保持各个元素[]之间的内存独立性！！！千万不要有所指……………………

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    #def write_search_result(self, was_found):
    #    print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            #if self.hashtable[query.ind] == None:
            #    self.write_chain([])
            h_s = query.ind
            chain = (self.hashtable[h_s])
            print(' '.join(reversed(chain)))
        else:
            if query.type == "find":
                h_s = self._hash_func(query.s)
                tmp = self.hashtable[h_s]
                i = 0
                if len(tmp) == 0:
                    print('no')
                else:
                    for cur in range(len(tmp)):
                        if query.s == tmp[cur]:
                            i = 1
                    if i == 0:
                        print('no')
                    else:
                        print('yes')
                #self.write_search_result(was_found)

            elif query.type == "add":
                    h_s = self._hash_func(query.s)
                    i = 1
                    if len(self.hashtable[h_s]) == 0:
                        (self.hashtable[h_s]).append(query.s)
                    else:
                        for cur in range(len(self.hashtable[h_s])):
                            if query.s == self.hashtable[h_s][cur]:
                                i = 0
                        if i == 1:
                            (self.hashtable[h_s]).append(query.s)
            else:
                h_s = self._hash_func(query.s)
                if len(self.hashtable[h_s]) != 0:
                    for cur in self.hashtable[h_s]:
                        if query.s == cur:
                            self.hashtable[h_s].pop(self.hashtable[h_s].index(query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

