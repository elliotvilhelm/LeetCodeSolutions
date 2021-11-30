class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        new_intervals = []
        
        for interval in intervals:
            if len(new_intervals) == 0:
                new_intervals.append(interval)
            else:
                latest_interval = new_intervals[-1]
                if interval[0] <= latest_interval[1]:
                    # join and replace
                    new_intervals[-1] = [new_intervals[-1][0], max(interval[1], new_intervals[-1][1])]
                else:
                    new_intervals.append(interval)
        return new_intervals