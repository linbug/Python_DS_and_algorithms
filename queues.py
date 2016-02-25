import random

class Node(object):

def __init__(self, other = None):
self.other = other
self.next = None
self.previous = None

def __str__(self):
return str(self.other)

class List(object):
def __init__(self):
self.head = None
self.tail = None

def append(self, value):

newNode = Node(value)
if self.head == None:
self.head = newNode
self.tail = newNode

else:
self.tail.next = newNode
newNode.previous = self.tail
self.tail = newNode

def __str__(self):
someString = “”
current = self.head
while current != None:
someString = someString + current.other
current = current.next
return someString

class Queue(List):
def enqueue(self, value):
self.append(value)

def dequeue(self):
self.temp = self.head
self.head = self.head.next
return self.temp
class Stack(List):
def push(self, value):
self.append(value)

def pop(self):
self.temp = self.tail
self.tail = self.tail.previous
return self.temp
def main():
list1 = List()
for i in xrange(0, 100):
list1.append(str(random.randrange(0,100)))
print list1
queue = Queue()
for i in xrange(0,100):
queue.enqueue(str(random.randrange(0,100)))
for i in xrange(0,100):
print queue.dequeue()
for i in range(0, 10):
print “——————————————-”
stack = Stack()
for i in xrange(0,100):
stack.push(str(random.randrange(0,100)))
for i in xrange(0,100):
print stack.pop()

if __name__ == ‘__main__’:
main()

