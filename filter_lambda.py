import string

# Functions utilizing the filter & lambda functions

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    return set(s) == alphabet

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def sum_evens_from_num_list(num_list):
    evens = filter(is_even, num_list)
    return sum(evens)

def filter_strings_by_length(string_list, target_length):
    return list(filter(lambda s: len(s) == target_length, string_list))

def filter_palindromes_from_string_list(string_list):
    return list(filter(lambda s: s == s[::-1], string_list))

def filter_by_substring(string_list, target_substring):
    return list(filter(lambda s:  target_substring in s.lower(), string_list))


print(is_pangram("The quick brown fox jumps over the lazy dog"))
# True

print(is_pangram("The quick brown fox jumps over the lazy do"))
# False

print(sum_evens_from_num_list([1,2,3,4,5,6]))
# 12

print(filter_strings_by_length(["hello", "eggs", "horse"], 5))
# ['hello', 'horse']

print(filter_palindromes_from_string_list(["hello", "racecar", "step on no pets", "eggplant"]))
# ['racecar', 'step on no pets']

print(filter_by_substring(["apple", "apps", "house", "Appalachia"], "app"))
# ['apple', 'apps', 'Appalachia']