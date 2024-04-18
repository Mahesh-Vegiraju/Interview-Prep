class Solution:
    def reverseVowels(self, s: str) -> str:
        # use two pointers, one going forward and the other going backward
        # when one pointer finds a vowel, stop and wait for the other pointer to find a vowel
        # when both pointers have a vowel, replace them
        # keep going until the left pointer > right pointer or right pointer < left pointer
        # return the string
        p1, p2 = 0, len(s) - 1
        v1, v2 = None, None
        s = list(s)
        while p1 <= p2:
            if v1 is None and s[p1] in 'aeiouAEIOU':
                v1 = p1
                p1 += 1
            
            if v2 is None and s[p2] in 'aeiouAEIOU':
                v2 = p2
                p2 -= 1
            
            if v1 is None:
                p1 += 1
            
            if v2 is None:
                p2 -= 1

            if v1 is not None and v2 is not None:
                s[v1], s[v2] = s[v2], s[v1]
                v1 = None
                v2 = None
        
        return "".join(s)