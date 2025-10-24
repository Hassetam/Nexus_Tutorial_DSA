class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j = 0, len(skill)-1
       
        ans = [(skill[i] * skill[j])]
        while i < j-1:
            if skill[i] + skill[j] == skill[i+1] + skill[j-1]:
                ans.append((skill[i+1] * skill[j-1]))
            else:
                return -1
            i +=1
            j -=1
        answer= sum(ans)
        return answer
