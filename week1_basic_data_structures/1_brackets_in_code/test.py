
def main():
    # text = input()
    # mismatch = find_mismatch(text)
    # print(mismatch)
    # Printing answer, write your code here
    import os

    filename_list = []

    for root, dirs, files in os.walk("./tests"):

        for filename in files:
            if '.a' not in filename:
                filename_list.append(filename)
                filename_list.sort()

        for filename in filename_list:
            print('........................')
            print('Running Test: ' + filename)
            f = open("./tests/" + filename, "r")

            if f.mode == 'r':
                input = f.read().rstrip('\n')
                f.close()
                f = open("./tests/" + filename + '.a', "r")

            if f.mode == 'r':
                expected_output = f.read().rstrip('\n')
                f.close()

            output = find_mismatch(input)

            print('Input: ' + str(input))
            print('Expected Output: ' + str(expected_output))
            print('Ouput: ' + str(output))

        if str(expected_output) == str(output):
            print('Test Passed')
        else:
            print('Test Failed')
            break


if __name__ == "__main__":
    main()
