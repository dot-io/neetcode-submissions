class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output
    def decode(self, s: str) -> List[str]:
        i = 0
        state = 0
        num = 0
        tmp = ""
        strings = []
        while i < len(s):
            c = s[i]
            if c == '#':
                state = 1
                num = int(tmp)
                strings.append(s[i+1:i+num+1])
                tmp = ""
                i += num+1
                continue
        
            tmp += c
            i += 1
        return strings

        
