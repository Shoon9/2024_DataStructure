import time
from AVLTree import *
from HashTable import *

class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 청크 크기는 4KB
        self.total_memory = 0   # 전체 메모리 크기
        self.used_memory = 0    # 사용중인 메모리 크기
        self.free_space = AVLTree()  # 자유 공간을 관리하는 AVL 트리
        self.allocated_space = HashTable(277)  # 할당된 공간을 관리하는 해시 테이블
        self.start_time = time.time()  # 프로그램 시작 시간

    def print_stats(self):
        # 메모리 풀의 총 크기, 사용 중인 메모리의 양, 공간 활용률을 계산해 출력
        print(f"Arena: {self.total_memory / 1024} KB")
        print(f"In-use: {self.used_memory / 1024} KB")
        utilization = (self.used_memory / self.total_memory) * 100 if self.total_memory > 0 else 0
        print(f"Utilization: {utilization:.2f}%")
        
        end_time = time.time()  # 프로그램 종료 시간
        execution_time = end_time - self.start_time  # 실행 시간 계산
        print(f"Execution Time: {execution_time:.2f} seconds")

    def malloc(self, id, size):
        # 메모리 할당 요청 처리
        node = self.free_space.search(size)
        if node is not self.free_space.NIL:
            # 적절한 노드가 있다면 할당 후 남은 부분을 업데이트
            remaining_size = node.item - size
            if remaining_size > 0:
                self.free_space.insert(remaining_size)
            self.free_space.delete(node.item)
        else:
            # 적합한 블록이 없다면 새로운 청크 할당
            self.total_memory += self.chunk_size
            remaining_size = self.chunk_size - size
            if remaining_size > 0:
                self.free_space.insert(remaining_size)
        self.allocated_space.insert(id, size)
        self.used_memory += size

    def free(self, id):
        # 메모리 해제 요청을 처리
        size = self.allocated_space.get(id)
        if size:
            self.allocated_space.delete(id)
            self.free_space.insert(size)
            self.used_memory -= size

if __name__ == "__main__":
    allocator = Allocator()
    
    with open ("/Users/leeseunghoon/Desktop/Hoon/SSU/4-1/자료구조/과제/input.txt", "r") as file:
        n=0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                allocator.free(int(req[1]))

            # if n%100 == 0:
            #     print(n, "...")
            
            n+=1
    
    allocator.print_stats()