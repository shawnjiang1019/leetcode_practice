class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append([startTime, endTime])
            return True
        # do a binary search to find any overlap

        left, right = 0, len(self.bookings)

        while left < right:
            mid = left + (right - left) // 2
            mid_start, mid_end = self.bookings[mid]
            if mid_start < endTime:
                left = mid + 1
            else:
                right = mid

        if left > 0 and self.bookings[left - 1][1] > startTime:
            return False
        if right < len(self.bookings) and self.bookings[left][1] < endTime:
            return False
        
        self.bookings.insert(left, [startTime, endTime])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)