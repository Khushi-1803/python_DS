"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order."""
s1 = "geeks"
s2 = "kseeg"

if len(s1) != len(s2):
    print("Not anagrams")
elif sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")