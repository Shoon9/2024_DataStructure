from listNode import ListNode
from linkedListBasic import LinkedListBasic
from circularLinkedList import CircularLinkedList

if __name__ == "__main__":
    
    names = ["Amy", "Kevin", "Mary", "David"]
    
    #name_list = LinkedListBasic()
    name_list = CircularLinkedList()
    
    for name in names:
        name_list.append(name)
    
    for name in name_list:
        print(name)
        
    name_list.pop(name_list.size() -1)
    name_list.insert(0, "Rose")
    name_list.sort()
    name_list.printList()
    