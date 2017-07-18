# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key = lambda i: i.start): # lambda!
            if res and res[-1].end >= i.start: # last index!
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += i,  # need comma here!
        return res


    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        return self.merge(intervals + [newInterval])
        

s = Solution()
print s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 4))
