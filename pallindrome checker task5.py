def pallindrome_checker(pallindrome):
    str=pallindrome[::-1]
    if str==pallindrome:
        print("it is a pallindrome")
    else:
        print("it is not a pallindrome")
    return str
pallindrome=input("enter the string")
checker=pallindrome_checker(pallindrome)

