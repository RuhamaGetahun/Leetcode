class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

       output = []
       # add the newInterval to the Intervals
       intervals.append(newInterval)


       # sort them out based on the the Interval start
       intervals.sort(key = lambda x:x[0])
       #[[1,3],[4,7],[6,9]]
       output.append(intervals[0])
      
       for start, end in intervals[1:]:
           last = output[-1][1]
           if last >= start:
               output[-1][1] =  max(last, end)
           else:
               output.append([start,end])


       return output




     


        