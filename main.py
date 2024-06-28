def main():

    result = []

    while True:
        start = input('Enter a letter: ')
        end = input('Enter another letter: ')
        if (start.isalpha() and end.isalpha()) and (start < end) and (len(start) == 1 or len(end) == 1):
            break
        else:
            print('try again')

    for x in range (ord(start), ord(end) + 1):
        result.append(chr(x))
    print(*result)


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
