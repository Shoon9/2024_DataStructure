from listNode import *
from linkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__stack = LinkedListBasic()
    
    def push(self, x):
        self.__stack.insert(0,x)
        
    def pop(self):
        return self.__stack.pop(0)
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack.get(0)
        
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()
        
    def printStack(self):
        print("Stack from bottom:", end = ' ')
        for i in range(self.__stack.size()-1, -1, -1):
            print(self.__stack.get(i), end = ' ')
        print()
        
    def reverse(str):
        st = LinkedStack()
        for i in range(len(str)):
            st.push(str[i])
        out = ""
        while not st.isEmpty():
            out += st.pop()
        return out   
    
    def copy(self):
        b = LinkedStack()
        for i in range(self.__stack.size()-1, -1, -1):
            tmp = self.__stack.get(i)
            b.push(tmp)
        return b
    
        
