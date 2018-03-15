# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    name = []
    for i in range(10000001):       
        name.append(0)
    ##construct a hash map --- direct address
    
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            index = cur_query.number
            name[index] = cur_query.name

        elif cur_query.type == 'del':
            index = cur_query.number
            name[index] = 0

        else:
            response = 'not found'
            index = cur_query.number
            if name[index] != 0:
                response = name[index]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
