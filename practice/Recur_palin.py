def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

test_string = "radar"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
