class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        temp_list = []
        i = 0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                temp_list.append(word1[i])
            if i<len(word2):
                temp_list.append(word2[i])
            i = i+1
        return ''.join(temp_list)

        
        