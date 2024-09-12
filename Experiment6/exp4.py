def CheckPalindrome(String):
    return String == String[::-1]

def main():
    String = str(input("input a string: "))

    Check = CheckPalindrome(String)

    if Check:
        print(String, "is a palindrome.")
    else:
        print(String, "is not a palindrome.")


if __name__=='__main__':
    main()