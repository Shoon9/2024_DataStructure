class AVLNode:
    def __init__(self, newItem, left, right, h):
        self.item = newItem
        self.left = left
        self.right = right
        self.height = h

class AVLTree:
    def __init__(self):
        self.NIL = AVLNode(None, None, None, 0)
        self.__root = self.NIL
        self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4
        self.NO_NEED = 0
        self.ILLEGAL = -1

    # 검색
    def search(self, x):
        return self.__searchItem(self.__root, x)

    def __searchItem(self, tNode:AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            return self.NIL
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)

    # 삽입
    def insert(self, x):
        self.__root = self.__insertItem(self.__root, x)

    def __insertItem(self, tNode: AVLNode, x) -> AVLNode:
        if tNode == self.NIL:  # insert after a leaf (or into an empty tree)
            tNode = AVLNode(x, self.NIL, self.NIL, 1)
        elif x < tNode.item:  # branch left
            tNode.left = self.__insertItem(tNode.left, x)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
        else:  # branch right
            tNode.right = self.__insertItem(tNode.right, x)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
        return tNode

    # 삭제
    def delete(self, x):
        if x is not None:  # x가 None이 아닌지 확인
            self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode: AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            return self.NIL  # item not found
        else:
            if x == tNode.item:  # item found at tNode
                tNode = self.__deleteNode(tNode)
            elif x < tNode.item:  # search in the left subtree
                tNode.left = self.__deleteItem(tNode.left, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)
                type = self.__needBalance(tNode)
                if type != self.NO_NEED:
                    tNode = self.__balanceAVL(tNode, type)
            else:  # search in the right subtree
                tNode.right = self.__deleteItem(tNode.right, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)
                type = self.__needBalance(tNode)
                if type != self.NO_NEED:
                    tNode = self.__balanceAVL(tNode, type)
            return tNode

    def __deleteNode(self, tNode: AVLNode) -> AVLNode:
        # 3가지 경우
        # 1. tNode가 리프 노드
        # 2. tNode의 자식이 하나만 있음
        # 3. tNode의 자식이 둘 있음
        if tNode.left == self.NIL and tNode.right == self.NIL:  # case 1 (자식이 없음)
            return self.NIL
        elif tNode.left == self.NIL:  # case 2 (오른쪽 자식만)
            return tNode.right
        elif tNode.right == self.NIL:  # case 2 (왼쪽 자식만)
            return tNode.left
        else:  # case 3 (두 자식이 다 있음)
            rtnItem, rtnNode = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
            return tNode

    def __deleteMinItem(self, tNode: AVLNode) -> tuple:
        if tNode.left == self.NIL:
            # found min at tNode
            return (tNode.item, tNode.right)
        else: # keep branching left, then backtrack
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
            return (rtnItem, tNode)
        
    # 균형 잡기
    def __balanceAVL(self, tNode: AVLNode, type: int) -> AVLNode:
        returnNode = self.NIL
        if type == self.LL:
            returnNode = self.__rightRotate(tNode)
        elif type == self.LR:
            tNode.left = self.__leftRotate(tNode.left)
            returnNode = self.__rightRotate(tNode)
        elif type == self.RR:
            returnNode = self.__leftRotate(tNode)
        elif type == self.RL:
            tNode.right = self.__rightRotate(tNode.right)
            returnNode = self.__leftRotate(tNode)
        else:
            print("Impossible type! Should be one of LL, LR, RR, RL")
        return returnNode

    # 좌회전
    def __leftRotate(self, t: AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "'s RChild shouldn't be NIL!")
        RLChild = RChild.left
        RChild.left = t
        t.right = RLChild
        t.height = 1 + max(t.left.height, t.right.height)
        RChild.height = 1 + max(RChild.left.height, RChild.right.height)
        return RChild

    # 우회전
    def __rightRotate(self, t: AVLNode) -> AVLNode:
        LChild = t.left
        if LChild == self.NIL:
            print(t.item, "'s LChild shouldn't be NIL!")
        LRChild = LChild.right
        LChild.right = t
        t.left = LRChild
        t.height = 1 + max(t.left.height, t.right.height)
        LChild.height = 1 + max(LChild.left.height, LChild.right.height)
        return LChild

    def __needBalance(self, t: AVLNode) -> int:
        type = self.ILLEGAL
        if (t.left.height + 2 <= t.right.height):  # R 높음
            if (t.right.left.height) <= t.right.right.height:
                type = self.RR
            else:
                type = self.RL
        elif (t.left.height >= t.right.height + 2):  # L 높음
            if (t.left.left.height) >= t.left.right.height:
                type = self.LL
            else:
                type = self.LR
        else:
            type = self.NO_NEED
        return type

    # 기타
    def isEmpty(self) -> bool:
        return self.__root == self.NIL

    def clear(self):
        self.__root = self.NIL
    
    # 추가 메소드
    def get_root(self):
        return self.__root

    def __iter__(self):
        return self._in_order_traversal(self.__root)

    def _in_order_traversal(self, tNode):
        if tNode != self.NIL:
            yield from self._in_order_traversal(tNode.left)
            yield tNode.item
            yield from self._in_order_traversal(tNode.right)
            
    def find_best_fit(self, size):
        return self.__find_best_fit(self.__root, size, None)

    def __find_best_fit(self, tNode, size, best_fit):
        if tNode == self.NIL:
            return best_fit
        elif tNode.item >= size:
            # 현재 노드가 더 적합하면 best_fit을 업데이트
            if best_fit is None or tNode.item < best_fit.item:
                best_fit = tNode
            # 왼쪽 서브트리에서 더 가까운 매치를 찾기 위해 계속 탐색
            return self.__find_best_fit(tNode.left, size, best_fit)
        else:
            # 오른쪽 서브트리에서 계속 탐색
            return self.__find_best_fit(tNode.right, size, best_fit)