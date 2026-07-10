class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        s = ''
        for i in strs:
            s += (i + 'é')
        return s

    def decode(self, s: str) -> List[str]:
        print(len(s))
        left = 0
        res = []

        for i in range(len(s)):
            if s[i] == 'é':
                res.append(s[left:i])
                left = i + 1
            
        # res.append(s[left:len(s)])

        return res