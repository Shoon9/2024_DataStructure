from listNode import *
from circularLinkedList import *
        
class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache = CircularLinkedList()
        self.cache_hit = 0
        self.tot_cnt = 0

    def do_sim(self, page):
        if page in self.cache:
            # Cache hit 발생
            self.cache_hit += 1
            self.cache.remove(page)
            self.cache.append(page)
        else:
            # Cache miss 발생
            if self.cache.size() == self.cache_slots:
                self.cache.pop(0)
            self.cache.append(page)

        self.tot_cnt += 1
    
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)

if __name__ == "__main__":

    data_file = open("/Users/leeseunghoon/Desktop/Hoon/SSU/4-1/자료구조/자료구조 연습문제/2024_DataStructure/LRU/linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()