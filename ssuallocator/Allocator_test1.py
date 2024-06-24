from circularDoublyLinkedList import *
from bidirectNode import *
from AVLTree import *

class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 4 KB
        self.allocated_space = CircularDoublyLinkedList()
        self.free_space = AVLTree()
        self.total_memory = 0  # 전체 메모리 크기
        self.used_memory = 0  # 사용 중인 메모리 크기

    def print_stats(self):
        print("Arena:", self.total_memory / 1024, "MB")
        print("In-use:", self.used_memory / 1024, "MB")
        util = (self.used_memory / self.total_memory * 100) if self.total_memory else 0
        print("Utilization:", f"{util:.2f}%")

    def malloc(self, id, size):
        # 메모리 요청이 전체 사용 가능 메모리를 초과할 경우 추가 메모리 할당
        while size > (self.total_memory - self.used_memory):
            self.total_memory += self.chunk_size
            self.free_space.insert(self.chunk_size)

        node = self.free_space.search(size)  # 적절한 블록 찾기
        if node is self.free_space.NIL:  # 적절한 블록이 없는 경우
            print("No suitable block found")
            return

        # 적합한 블록 찾아서 할당
        self.free_space.delete(node.item)
        if node.item > size:  # 남은 메모리를 free space에 다시 추가
            self.free_space.insert(node.item - size)
        self.allocated_space.append((id, size))
        self.used_memory += size

    def free(self, id):
        # Allocated space에서 블록 찾아 삭제
        curr_node = self.allocated_space._findNode(id)
        if curr_node is not None:
            self.allocated_space.remove(curr_node.item)
            self.free_space.insert(curr_node.item[1])  # 메모리 블록 사이즈를 free space에 추가
            self.used_memory -= curr_node.item[1]
        else:
            print("Block not found with ID:", id)


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
