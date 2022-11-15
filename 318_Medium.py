class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0

        n = len(words)    
        ch = [set(words[i]) for i in range(n)] # precompute hashset for each word  

        for i in range(n):
            for j in range(i+1,n):
                if not (ch[i] & ch[j]): # if nothing common
                    res = max(res, len(words[i]) * len(words[j]))

        return res
        
        
                                                      