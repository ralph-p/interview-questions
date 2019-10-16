class Solution(object):
    def commonChars(self, A):
        hash_map = [0 for i in range(256)]
        for c in A[0]:
            key = (ord(c)%256)
            hash_map[key] += 1
        for a in A[1:]:
            char_map = [0 for i in range(256)]
            for c in a:
                key = (ord(c)%256)
                char_map[key] += 1
            
            hash_map = self.clean_letters(hash_map,char_map)
        return self.print_map(hash_map)
    
    def clean_letters(self,hm1,hm2):
        new_map = [0 for i in range(len(hm1))]
        for i in range(len(hm1)-1):
            if hm1[i] and hm2[i]:
                new_map[i] = min(hm1[i],hm2[i])
        
        return new_map
    
    def print_map(self,hm):
        chars = []
        for i in range(len(hm)-1):
            if hm[i]:
                for x in range(hm[i]):
                    chars.append(chr(i))
                # print(chr(i),hm[i])
        return chars


        
    


print(Solution().commonChars(["bella","label","roller"]))