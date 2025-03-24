class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        no_deleted_list = 0
        # sort the intervals 
        intervals.sort(key=lambda x:x[1])

        # end needs to be the last non overlapping end 

        # [[1,2],[1,3],[2,3],[3,4]]
        #[[1, 11], [2, 12], [11, 22], [1, 100]]
        end = intervals[0][1]
        for i in range(1, len(intervals)): 
            if intervals[i][0] < end:
                no_deleted_list += 1
            else:
                end = intervals[i][1]
               

        return no_deleted_list