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
        self.elems = {}

    def _hash_func(self, s):
        """ hash function """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        """ print 'yes' if true, 'no' otherwise """
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        """ print list elements in a line """
        print(' '.join(chain))

    def read_query(self):
        """ read and return a Query object """
        return Query(input().split())

    def process_query(self, query):
        """ process a query depending on 'self.type' """
        if query.type == "check":
            # check if the chain exists
            if query.ind in self.elems:
                chain_elems = self.elems.get(query.ind)
                self.write_chain(elem for elem in chain_elems)
            # print a empty line if the chain does not exist
            else:
                print(' ')

        elif query.type == 'find':
            # see which chain might contain the given string
            chain = self._hash_func(query.s)
            if chain in self.elems:
                chain_elems = self.elems.get(chain)
                if query.s in chain_elems:
                    print("yes")
                else:
                    print("no")
            else:
                print("no")

        else:
            if query.type == 'add':
                chain = self._hash_func(query.s)
                # see if the chain exists
                if chain in self.elems:
                    # ignore the query if the string already exists in the chain
                    chain_elems = self.elems[chain]
                    if query.s not in chain_elems:
                        self.elems[chain].insert(0, query.s)

                # create a new list if the chain does not exist
                else:
                    self.elems[chain] = [query.s]

            elif query.type == 'del':
                chain = self._hash_func(query.s)
                # see if the chain exists and ignore the query otherwise
                if chain in self.elems:
                    chain_elems = self.elems[chain]
                    if query.s in chain_elems:
                        self.elems[chain].remove(query.s)

            else:
                print("invalid type")

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

    # import os
    #
    # filename_list = []
    #
    # for root, dirs, files in os.walk("./tests"):
    #
    #     for filename in files:
    #         if '.a' not in filename:
    #             filename_list.append(filename)
    #             filename_list.sort()
    #
    #     for filename in filename_list:
    #         print('........................')
    #         print('Running Test: ' + filename)
    #         f = open("./tests/" + filename, "r")
    #
    #         if f.mode == 'r':
    #             f.close()
    #             f = open("./tests/" + filename + '.a', "r")
    #
    #         if f.mode == 'r':
    #             expected_output = f.read().rstrip('\n')
    #             f.close()
    #
    #         bucket_count = int(input())
    #         proc = QueryProcessor(bucket_count)
    #         proc.process_queries()
    #
    #         print('Inputs: ')
    #         print('n: ' + str(n))
    #         print('parents: ' + str(parents))
    #         print('Expected Output: ' + str(expected_output))
    #         print('Ouput: ' + str(output))
    #
    #     if str(expected_output) == str(output):
    #         print('Test Passed')
    #     else:
    #         print('Test Failed')
    #         break
