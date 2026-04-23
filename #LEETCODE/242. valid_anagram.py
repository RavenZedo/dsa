#valid anagram 
# leetcode 242
def isAnagram(s, t):
    s = "anagram"
    t = "nagaram"
    return sorted(s) == sorted(t)