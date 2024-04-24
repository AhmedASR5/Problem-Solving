class Solution(object):
    def isPalindrome(self, s):

        s =  s.lower()
        list_of_char = []
        

        for char in s:
            if char < 'a' or char > 'z':
                continue
            else:
                list_of_char.append(char)
        
        left ,right =0, len(list_of_char) - 1
        
        while(left <right ):
            if list_of_char[left] == list_of_char[right]:
                left +=1
                right -=1
            else:
                return False
            
        return True    
            