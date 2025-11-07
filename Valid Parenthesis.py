class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for x in s:
            if x in pairs:     
                stack.append(x)
            else:                     
                if not stack:         
                    return False
                if pairs[stack.pop()] != x: 
                    return False

  
        return not stack
