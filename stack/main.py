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
st2 = ListStack()
print(st2.check_reverse("abc$cba"))  # True 반환
print(st2.check_reverse("abc$abc"))  # False 반환

#3