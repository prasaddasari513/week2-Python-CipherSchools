def palindrome(n):
    if n==n[::-1]:
        return True
    return False
n = input()
print(palindrome(n))
def is_palindrome(word):
    return word == word[::-1]
word = input()
print(is_palindrome(word))