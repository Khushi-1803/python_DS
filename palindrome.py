"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards."""

str = "madam"
rev = str[::-1]
if(str == rev):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")