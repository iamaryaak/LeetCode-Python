# Space = O(n)
# Time = O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        
        # for increasing slope
        for n in range(1, len(ratings)):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
                
        # for decreasing slope
        for n in range(len(ratings)-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        # return the sum since candiesPer tracks candies per person
        return sum(candiesPer)
