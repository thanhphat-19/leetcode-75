class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isVowels(c):
            return ( c =='u' or c == 'U' or c =='e' or c == 'E' 
                    or c == 'o' or c== 'O' or c == 'a'or c == 'A'
                    or c == 'i' or c == 'I')

        list_s = list(s)
        start = 0 
        end = len(list_s) - 1
        while start < end:
            if not isVowels(list_s[start]):
                start += 1
                continue
            if not isVowels(list_s[end]):
                end -= 1
                continue

            # Swap the vowels found at the start and end positions.
            list_s[start], list_s[end] =list_s[end], list_s[start]
            
            # Move the pointers towards each other for the next iteration.
            start += 1
            end -= 1    
        return "".join(list_s)
