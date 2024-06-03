class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        def largest(arr):
            max = arr[0]
            for i in range(len(arr)):
                if arr [i] > max:
                    max = arr[i]
            return max
        max_candies = largest(candies)
        res = []
        for i in range(len(candies)):
            if extraCandies + candies[i] < max_candies:
                res.append(False)
            else:
                res.append(True)
        return res

    
        