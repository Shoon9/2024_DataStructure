class Allocator:
    def __init__(self):
        self.chunk_size = 4096
        
    def print_stats(self): # 현재 메모리 할당자의 상태를 출력하는 메소드 : 메모리 풀의 총 크기, 사용 중인 메모리의 양, 공간 활용률을 계산해 출력
        
        
        
        print("Arena: XX MB")
        print("In-use: XX MB")
        print("Utilization: 0.XX")


    def malloc(self, id, size): # 메모리 할당 요청 메소드 : id와 size 매개변수를 받아, 해당 id로 size 만큼의 메모리를 할당
        
        
        
        pass
    
    def free(self, id): # 메모리 해제 요청을 처리하는 메소드 : 할당된 메모리 블록의 id를 매개변수로 받아 해당 메모리를 해제
        
        
        
        pass


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