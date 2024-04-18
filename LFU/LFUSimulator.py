from minHeap import *

class CacheNode:
    def __init__(self, lpn, frequency):
        self.lpn = lpn
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0
    cache = {}
    frequency_dict = {} 
    heap = MinHeap()    
  
    data_file = open("/Users/leeseunghoon/Desktop/Hoon/SSU/4-1/자료구조/자료구조 연습문제/2024_DataStructure/LFU/linkbench.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt += 1

        if lpn in frequency_dict:
            frequency_dict[lpn] += 1
        else:
            frequency_dict[lpn] = 1
            
        if lpn in cache:
            cache_hit += 1
        else:
            if len(cache) >= cache_slots:
                removed = heap.deleteMin()
                del cache[removed.lpn]
            entry = CacheNode(lpn, frequency_dict[lpn])
            cache[lpn] = entry
            heap.insert(entry)

    data_file.close()
    hit_ratio = cache_hit / tot_cnt
    return cache_hit, tot_cnt, hit_ratio    


if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        cache_hit, tot_cnt, hit_ratio = lfu_sim(cache_slots)  # Unpack the returned values
        print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", hit_ratio)
      

