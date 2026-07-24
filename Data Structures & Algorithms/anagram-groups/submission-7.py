import numpy as np

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_hash = {}
        for string in strs:
            hash_val = [0] * 26
            for c in string:
                hash_val[ord(c)-ord('a')] += 1
                print(hash_val)
            key = "".join([chr(e) for e in hash_val])
            print(key)
            if not key in letter_hash.keys():
                letter_hash[key] = []
            letter_hash[key].append(string)
        return list(letter_hash.values())


        