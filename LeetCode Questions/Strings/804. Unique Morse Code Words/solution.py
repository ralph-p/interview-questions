class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes = [[] for i in range(len(words))]
        for i,word in enumerate(words):
            for l in word:
                codes[i].append(morseCode[ord(l.lower())-97])
            codes[i] = ''.join(codes[i])
        return(len(set(codes)))

Solution().uniqueMorseRepresentations(['aaa','aaa'])