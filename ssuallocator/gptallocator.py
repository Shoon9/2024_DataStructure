class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 기본 청크 크기를 4KB로 설정
        self.total_memory = 0  # 할당된 전체 메모리 크기
        self.used_memory = 0  # 사용 중인 메모리 크기
        self.free_blocks = {}  # 해제된 메모리 블록 관리 (id: size)
        self.allocated_blocks = {}  # 할당된 메모리 블록 관리 (id: size)
        
    def print_stats(self):
        # 메모리 풀의 총 크기와 사용 중인 메모리의 양, 공간 활용률을 계산해 출력
        if self.total_memory == 0:
            utilization = 0
        else:
            utilization = (self.used_memory / self.total_memory) * 100
        print(f"Arena: {self.total_memory / 1024} KB")
        print(f"In-use: {self.used_memory / 1024} KB")
        print(f"Utilization: {utilization:.2f}%")

    def malloc(self, id, size):
        # 필요한 경우 메모리 청크를 추가로 할당
        while self.total_memory < self.used_memory + size:
            self.total_memory += self.chunk_size
        
        # 메모리 할당 처리
        self.allocated_blocks[id] = size
        self.used_memory += size
        if id in self.free_blocks:
            del self.free_blocks[id]  # 혹시나 free dictionary에 남아있는 블록 정보 삭제

    def free(self, id):
        # 메모리 해제 요청을 처리
        if id in self.allocated_blocks:
            size = self.allocated_blocks.pop(id)
            self.used_memory -= size
            self.free_blocks[id] = size  # 해제된 메모리 블록 정보 저장

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