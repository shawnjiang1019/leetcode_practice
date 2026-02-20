class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the start time
        intervals.sort(key=lambda x: (x[0], x[1]))

        result = 0
        prev_end = intervals[0][0] - 1
        for start, end in intervals:
            if start < prev_end:
                result += 1
                prev_end = min(prev_end, end)
                continue
            prev_end = end
        return result

