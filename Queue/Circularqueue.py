class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = 0
        self.count = 0


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        
        return True
        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1 ) % self.size
        self.count -= 1

        return True


        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.rear-1) % self.size]





    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()