#Retirado de https://www.programiz.com/dsa/circular-queue

# Circular Queue implementation in Python
class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
        self.size = 0

    # Insert an element into the circular queue
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            self.size += 1
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            self.size += 1

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            self.size -= 1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            self.size -= 1
            return temp

    def mudarLugar(self):
        self.enqueue(self.dequeue())

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


