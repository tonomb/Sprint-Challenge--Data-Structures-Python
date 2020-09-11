class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.counter = 0

    def append(self, item):
        # check if buffer is full
        if len(self.storage) == self.capacity:
            #if full override value at counter, 
            self.storage[self.counter] = item
            # change counter
            self.counter = (self.counter + 1 ) % self.capacity
        #otherwise append value to list
        else:
            self.storage.append(item)
            #change counter
            self.counter = (self.counter + 1 ) % self.capacity

    def get(self):
        return self.storage


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']