class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0:
                # Check if current plot and neighbors are all empty
                if sum(flowerbed[i-1:i+2]) == 0:
                    # Plant a flower and update count
                    flowerbed[i] = 1
                    count += 1
        return count >= n
        


        