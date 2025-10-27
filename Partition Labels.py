class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        output = []
        i = 0

        while i < len(s):
            end = last[s[i]]
            j = i

            while j < end:
                end = max(end, last[s[j]])
                j += 1
            output.append(j - i + 1)
            i = j + 1
        
        return output
        
