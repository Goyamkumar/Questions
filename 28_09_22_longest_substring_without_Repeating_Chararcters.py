class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        new_list =set()
        x=0
        new=0
        for i in range(n):
            while s[i] in new_list: 
                new_list.remove(s[x])
                x+=1
            new_list.add(s[i])
            new = max(new,i-x+1)
        
        print(new_list)
        return new