import datetime
class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.insert(0,x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.queue:
            return self.queue.pop()
        return False

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        return False
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        return False
        
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        day = datetime.date(year,month,day)
        return weekdays[day.weekday()]

print(Solution().dayOfTheWeek(day = 31, month = 8, year = 2019))
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()