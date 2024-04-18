from ListQueue import *

#test
q1 = ListQueue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue("aaa")
q1.printQueue()

#1
def checkString(string):
    queue = ListQueue()
    i = 0
    for i in range(len(string)):
        if (string[i] == '$'): break
        queue.enqueue(string[i])
    
    for j in range(i+1, len(string)):
        if (queue.isEmpty()): return False
        if (queue.dequeue() != string[j]): return False
        
    if (queue.isEmpty()): return True
    else: return False
    
st1 = checkString("abc$abc")
st2 = checkString("abc$cba")
st3 = checkString("abc$abcd")
print(st1)
print(st2)
print(st3)

#2
class TwoQueueStack:
    def __init__(self):
        self.queue1 = ListQueue()
        self.queue2 = ListQueue()
    


#3
