# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code her
            if len(opening_brackets_stack) == 0:
                return i + 1

            top = opening_brackets_stack[-1]

            if are_matching(top[0], next):
                opening_brackets_stack.pop(-1)
            else:
                return i + 1

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[-1][1] + 1
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # # Printing answer, write your code here
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
    #             input = f.read().rstrip('\n')
    #             f.close()
    #             f = open("./tests/" + filename + '.a', "r")
    #
    #         if f.mode == 'r':
    #             expected_output = f.read().rstrip('\n')
    #             f.close()
    #
    #         output = find_mismatch(input)
    #
    #         print('Input: ' + str(input))
    #         print('Expected Output: ' + str(expected_output))
    #         print('Ouput: ' + str(output))
    #
    #     if str(expected_output) == str(output):
    #         print('Test Passed')
    #     else:
    #         print('Test Failed')
    #         break


if __name__ == "__main__":
    main()
