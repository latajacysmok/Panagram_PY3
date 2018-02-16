# copression.py the program checks if the given string is a panagram

import string
def pangram(s):
    check = string.ascii_lowercase
    answer = [letter for letter in s.lower() if letter in check]
    print(len(set(answer)) == len(check))

pangram("The quick brown fox jumps over the lazy dog.")
#"False, I see false, this exam I may pass"