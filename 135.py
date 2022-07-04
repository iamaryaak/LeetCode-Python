class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        N = len(ratings)
        for n in range(1, N):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
        for n in range(N-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        return sum(candiesPer)class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        N = len(ratings)
        for n in range(1, N):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
        for n in range(N-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        return sum(candiesPer)class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        N = len(ratings)
        for n in range(1, N):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
        for n in range(N-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        return sum(candiesPer)class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        N = len(ratings)
        for n in range(1, N):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
        for n in range(N-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        return sum(candiesPer)class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings
        # start with +1 for each space 
        candiesPer = [1 for x in ratings]
        N = len(ratings)
        for n in range(1, N):
            # if rating is greater than
            if ratings[n]  > ratings[n-1]:
                candiesPer[n] = max(candiesPer[n-1] + 1, candiesPer[n])
        for n in range(N-2, -1, -1):
            if ratings[n]  > ratings[n+1]:
                candiesPer[n] = max(candiesPer[n+1] + 1, candiesPer[n])
            
        return sum(candiesPer)
