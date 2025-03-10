class Solution:
    def merge(self,intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []

        intervals.sort(key = lambda x: x[0])

        merged = [[intervals[0]]]

        #merged = [[1,3]]
        #start,end = 2,6

        for start, end in intervals [1:]:
            last_end = merged[-1][1]

            if start > last_end:
                merged.append([start, end])
            else:
                merged[-1][1] = max(last_end,end)    