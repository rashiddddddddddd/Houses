class queue:
    def __init__(self,cap):
        self.front = self.size = 0
        self.rear = cap - 1 
        self.capacity = cap
        self.Q = [None]*cap
    
    def isFull(self):
        return self.size == self.cap
    
    def isEmpty(self):
        return self.size == 0
    
    def Enqueue(self,item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.cap)
        self.Q[self.rear] = item
        self.size += 1
        print("% s enqueded to queue" % str(item))

    def Dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        
Queue = queue(10)
Queue.Enqueue