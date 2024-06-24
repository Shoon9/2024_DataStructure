class HashNode:
    def __init__(self, key, value):
        self.key = key  # 노드가 저장할 키
        self.value = value  # 노드가 저장할 값
        self.next = None  # 연결 리스트에서 다음 노드를 가리키는 포인터

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity  # 해시 테이블의 크기
        self.size = 0  # 현재 해시 테이블에 저장된 요소의 수
        self.buckets = [None] * self.capacity  # 해시 버킷 배열

    def _hash(self, key):
        # 키를 해시하여 해당 버킷의 인덱스를 계산
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)  # 키에 대한 인덱스 계산
        node = self.buckets[index]  # 해당 인덱스의 버킷을 가져옴
        last_node = None  # 이전 노드를 추적하기 위한 변수
        while node is not None:
            if node.key == key:
                node.value = value  # 이미 존재하는 키라면 값을 업데이트
                return
            last_node = node
            node = node.next
        if last_node is None:
            self.buckets[index] = HashNode(key, value)  # 새 노드를 버킷의 첫 번째 노드로 설정
        else:
            last_node.next = HashNode(key, value)  # 새 노드를 마지막 노드의 다음 노드로 연결
        self.size += 1  # 테이블 크기 증가

    def get(self, key):
        index = self._hash(key)  # 키에 대한 인덱스 계산
        node = self.buckets[index]  # 해당 인덱스의 버킷을 가져옴
        while node is not None:
            if node.key == key:
                return node.value  # 키가 일치하는 노드의 값을 반환
            node = node.next
        return None  # 키를 찾지 못하면 None 반환

    def delete(self, key):
        index = self._hash(key)  # 키에 대한 인덱스 계산
        node = self.buckets[index]  # 해당 인덱스의 버킷을 가져옴
        prev_node = None  # 삭제할 노드의 이전 노드를 추적하기 위한 변수
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.buckets[index] = node.next  # 첫 번째 노드를 삭제하는 경우
                else:
                    prev_node.next = node.next  # 중간 노드를 삭제하는 경우
                self.size -= 1  # 테이블 크기 감소
                return True  # 삭제 성공
            prev_node = node
            node = node.next
        return False  # 삭제할 키를 찾지 못한 경우


