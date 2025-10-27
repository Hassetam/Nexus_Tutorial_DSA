class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        i = 0   
        j = 0
        n = len(s)
        
        while i < n:
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1  
            
            ans.append(s[i])
            i += 1 

        return ''.join(ans)
