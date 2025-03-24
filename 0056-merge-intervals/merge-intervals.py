class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # create a new list to add on the non-overlapping intervals 
        output = []

        # sort the array 
        intervals.sort(key = lambda x:x[0])
        # hold on to an end 
        output.append(intervals[0])
        # compare by going from 1 and above 
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output 

        