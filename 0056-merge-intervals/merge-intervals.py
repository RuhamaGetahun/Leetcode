class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []
        intervals.sort(key = lambda x:x[0])
        new_intervals.append(intervals[0])

        for start, end in intervals[1:]:
            last = new_intervals[-1][1]
            if start <= last : 
                new_intervals[-1][1] = max(end, last)
            else:
                new_intervals.append([start, end])
        return new_intervals 


    

        