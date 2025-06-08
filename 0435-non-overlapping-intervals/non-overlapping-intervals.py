class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        start = 0 
        min_removes = 0 
        intervals.sort(key = lambda x:x[1])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[start][1]:
                min_removes += 1
            else:
                start = i  
        return min_removes 
