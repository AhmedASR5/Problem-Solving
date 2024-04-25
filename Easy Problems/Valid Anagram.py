class Solution(object):
    def isAnagram(self, s, t):

        s =s.lower()
        t =t.lower()

        freq_of_char_in_string1 = {}
        freq_of_char_in_string2 = {}

        if len(s) != len(t):
            return False


        for i in range(len(s)):
            freq_of_char_in_string1[s[i]] = 1 + freq_of_char_in_string1.get(s[i],0)
            freq_of_char_in_string2[t[i]] = 1 + freq_of_char_in_string2.get(t[i],0)

        for char in freq_of_char_in_string1:
            if freq_of_char_in_string1[char] != freq_of_char_in_string2.get(char,0):
                return False

        return True     






                

        
        