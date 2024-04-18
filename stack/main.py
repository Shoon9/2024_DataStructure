from linkedStack import *

#1
st1 = ListStack()
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty', st1.isEmpty())

#2
def checkString(string):
    stack= ListStack()
    i = 0
    for i in range(len(string)):
        if (string[i] == '$'): break
        stack.push(string[i])
    
    for j in range(i+1, len(string)):
        if (stack.isEmpty()): return False
        if (stack.pop() != string[j]): return False
        
    if (stack.isEmpty()): return True
    else: return False
    
st1 = checkString("abc$cba")
st2 = checkString("abc$abc")
st3 = checkString("abc$abcd")
print(st1)
print(st2)
print(st3)

#3
