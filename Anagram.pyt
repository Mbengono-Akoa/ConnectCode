# mot1 = Car || mot2 = rac
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def Anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS, CountT = {}, {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        
        for c in CountS:
            if CountS[c] != CountT[c]:
                return False
            
        return True

s = "anagram"
t = "nagarama"
print(f"{Solution.Anagram(s,t)}")