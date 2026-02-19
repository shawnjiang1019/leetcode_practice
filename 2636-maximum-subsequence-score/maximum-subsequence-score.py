class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sort both arrays by the value of nums1 decreasing 
        tups = [[nums1[i], nums2[i]] for i in range(len(nums1))]
        tups.sort(key=lambda x: -x[1])
        heap = []
        
        max_score = 0
        score = 0
        min_elem = tups[0][1]
        for n1, n2 in tups:
            heapq.heappush(heap, n1)
            score += n1
            if len(heap) > k:
                score -= heapq.heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, score * n2)
        return max_score
            

        
            