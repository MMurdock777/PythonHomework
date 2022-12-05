def check_palindrome(line: str):
    not_palindrome = 1
    for i in range(0, len(line) // 2 + 1):
        if line[i] == line[len(line)-1-i]:
            continue
        else:
            not_palindrome = 0
            break

    return bool(not_palindrome)


print(check_palindrome("civic"))
