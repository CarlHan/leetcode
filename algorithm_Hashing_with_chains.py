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
        self.hashtable = [[]] * bucket_count

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

            self.write_chain(reversed(self.hashtable[query.ind]))
        else:
            if query.type == 'find':
                h_s = self._hash_func(query.s)
                tmp = self.hashtable[h_s]
                was_found = False
                if len(tmp) == 0:
                    was_found = False
                else:
                    for cur in range(len(tmp)):
                        if query.s == tmp[cur]:
                            was_found = True
                #self.write_search_result(was_found)
                if was_found:
                    print('yes')
                else:
                    print('no')

            elif query.type == 'add':
                    h_s = self._hash_func(query.s)
                    tmp = self.hashtable[h_s]
                    ind = False
                    if len(tmp) == 0:
                        (self.hashtable[h_s]).append(query.s)
                    else:
                        for cur in range(len(tmp)):
                            if query.s == tmp[cur]:
                                ind = False
                            else:
                                ind = True
                        if ind:
                            (self.hashtable[h_s]).append(query.s)
            else:
                h_s = self._hash_func(query.s)
                tmp = self.hashtable[h_s]
                if len(tmp) != 0:
                    for cur in tmp:
                        if query.s == cur:
                            self.hashtable[h_s].pop(tmp.index(query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
