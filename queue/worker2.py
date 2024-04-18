from ListQueue import *
import threading
import time

#2
ShareQueue = ListQueue()

class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.pos = 0
        self.worker = threading.Thread(target = self.run) #Thread 생성

    def get_item(self):
        if self.pos < len(self.items):
            item = self.items[self.pos]
            ShareQueue.enqueue(item)
            self.pos += 1
            return item
        else:
            return None

    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item = self.get_item()
                print("Arrived:", item)
            else:
                break
            
        print("Producer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join() #join()을 불러야 시체가 잘 죽었는지 확인하고 죽음

class Consumer:
    def __init__(self):
        self.__alive = True
        self.worker = threading.Thread(target = self.run) #Thread 생성

    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:    
                boarditem = ShareQueue.dequeue()  
                print("Boaring:", boarditem)
            else:
                break
            
        print("Consumer is dying...")
            
    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

if __name__ == "__main__":
    
    customers = []
    with open("/Users/leeseunghoon/Desktop/Hoon/SSU/4-1/자료구조/자료구조 연습문제/2024_DataStructure/queue/customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names = []
    for c in customers:
        names.append(c[1])

    producer = Producer(names)

    # Priority 
#    producer = Producer(customers)

    consumer = Consumer()    
    producer.start() #Thread 시작
    consumer.start() #Thread 시작
    time.sleep(10)
    producer.finish()
    consumer.finish()
