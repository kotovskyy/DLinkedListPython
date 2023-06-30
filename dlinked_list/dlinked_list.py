from dlinked_list_node import Node

class DLinkedList():
    def __init__(self) -> None:
        self.__head = Node()
        self.__tail = Node()
        self.__head.setNext(self.__tail)
        self.__tail.setPrev(self.__head)
        
    def __str__(self) -> str:
        result = "[" + str(self.__head.getNext().getValue())
        current = self.__head.getNext().getNext()
        while (current != self.__tail):
            result += ", " + str(current.getValue())
            current = current.getNext()
        result += "]"
        return result
            
    def isEmpty(self) -> bool:
        return self.__head.getNext() == self.__tail
    
    def addFront(self, value, *args) -> None:
        self._add(self.__head, value)
        for arg in args:
            self._add(self.__head, arg)
    
    def addBack(self, value, *args) -> None:
        self._add(self.__tail.getPrev(), value)
        for arg in args:
            self._add(self.__tail.getPrev(), arg)
        
    def removeFront(self) -> None:
        self._remove(self.__head.getNext())
    
    def removeBack(self) -> None:
        self._remove(self.__tail.getPrev())
        
    def find(self, key) -> Node:
        current = self.__head.getNext()
        while (current != self.__tail):
            if (current.getValue() == key):
                return current
            current = current.getNext()
        return None
    
    # protected methods
    def _add(self, node: Node, value) -> None:
        new_node = Node()
        new_node.setValue(value)
        new_node.setPrev(node)
        new_node.setNext(node.getNext())
        node.getNext().setPrev(new_node)
        node.setNext(new_node)
        
    def _remove(self, node : Node):
        node.getPrev().setNext(node.getNext())
        node.getNext().setPrev(node.getPrev())
        

def main():
    dlist = DLinkedList()
    dlist.addFront(5, 3, 2, 8, 12, 1, 16)
    print(dlist)
    dlist.addBack(28, 123, 14, 57)
    print(dlist)
    dlist.removeBack()
    print(dlist)
    dlist.removeFront()
    print(dlist)
    print(dlist.find(123))
    print(dlist.find(1))
    

if __name__ == '__main__':
    main()