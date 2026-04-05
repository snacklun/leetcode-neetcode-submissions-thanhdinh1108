class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return 1
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones) *-1
            stone2 = heapq.heappop(stones) *-1
            different_weight = stone1-stone2
            if (different_weight > 0):
                heapq.heappush(stones, different_weight*-1)
        return stones[0] * -1 if stones else 0
