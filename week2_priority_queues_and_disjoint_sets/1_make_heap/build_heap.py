# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.

    # Naive implementation
    # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps

    if not isinstance(data, list):
        data = data.split(' ')

    swaps = []
    size = len(data)

    for i in range(int(size/2) + 1, 0, -1):

        # Convert 1-based index to 0-based index
        parent = i - 1

        # continue to check its children until they are leaves
        while (parent + 1) * 2 <= size:

            left = (parent + 1) * 2 - 1
            right = left + 1

            # out of range
            # if neither the left nor the right exists
            if left >= size:
                break

            # if the right does not exist
            if right == size:
                if int(data[parent]) > int(data[left]):
                    next_parent = left
                    # swap
                    swaps.append((parent, next_parent))
                    data[parent], data[next_parent] = data[next_parent], data[parent]
                else:
                    break
                break

            # check if the heap condition is already satisfied.
            if int(data[parent]) < int(data[left]) and int(data[parent]) < int(data[right]):
                break
            else:
                # if the left is equal to or smaller than the right
                if int(data[left]) <= int(data[right]):
                    next_parent = left
                # else the right is smaller than the left
                else:
                    next_parent = right
                # swap
                swaps.append((parent, next_parent))
                data[parent], data[next_parent] = data[next_parent], data[parent]

                # assign the next_parent to the parent
                parent = next_parent


    # if len(swaps) == 0:
    #     return 0

    n = len(swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

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
    #             lines = f.readlines()
    #             n = lines[0].strip()
    #             array = lines[1].strip()
    #             f.close()
    #             f = open("./tests/" + filename + '.a', "r")
    #
    #         if f.mode == 'r':
    #             expected_output = f.read().rstrip('\n')
    #             f.close()
    #
    #         output = build_heap(array)
    #
    #         print('Inputs: ')
    #         print('n: ' + str(n))
    #         print('parents: ' + str(array))
    #         print('Expected Output: ' + str(expected_output))
    #         print('Output: ' + str(output))
    #
    #     if str(expected_output) == str(output):
    #         print('Test Passed')
    #     else:
    #         print('Test Failed')
    #         break


if __name__ == "__main__":
    main()
