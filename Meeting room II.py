"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop, heapify
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        st = []
        et =[]
        for item in intervals:
            st.append(item.start)
            et.append(item.end)
        
        st.sort()
        et.sort()
        i, j = 1, 0
        rooms = 1
        maxx = rooms
        while i < len(st) and j < len(et):
            if st[i] <= et[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            maxx = max(maxx, rooms)
            

        return maxx


        return 0
