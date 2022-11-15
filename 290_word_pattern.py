class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        pattern_list = [x for x in pattern]
        
        if len(s_list) != len(pattern_list):
            return False

        d1 = {}
        d2 = {}
       
        for i in range(len(pattern)):
            
            p = pattern_list[i]
            q = s_list[i]

            if p in d1:
                
                if d1[p] != q:
                    
                    return False
                
            if q in d2:

                if d2[q] != p:
                    
                    return False
            
            d1[p] = q
            d2[q] = p


        return True
            


        
        return True





