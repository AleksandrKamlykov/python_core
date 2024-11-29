def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def is_palindrome(s):
    return s == s[::-1]

def unique_elements(lst):
    return list(set(lst))

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage of find_min
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_min(numbers))  # Output: 1

# Example usage of is_palindrome
s = "racecar"
print(is_palindrome(s))  # Output: True

s = "hello"
print(is_palindrome(s))  # Output: False

# Example usage of unique_elements
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(lst))  # Output: [1, 2, 3, 4, 5]

# Example usage of are_anagrams
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # Output: True

s1 = "hello"
s2 = "world"
print(are_anagrams(s1, s2))  # Output: False