class Node():
    # Double linked list node 
    def __init__(self) -> None:
        self.__value = None
        self.__next = None
        self.__prev = None

    def __str__(self) -> str:
        return f"{self.getPrev().getValue()}->{self.getValue()}->{self.getNext().getValue()}"
        
    def setValue(self, value) -> None:
        self.__value = value
    
    def setNext(self, next) -> None:
        self.__next = next
    
    def setPrev(self, prev) -> None:
        self.__prev = prev
        
    def getValue(self) -> None:
        return self.__value
    
    def getNext(self) -> None:
        return self.__next

    def getPrev(self) -> None:
        return self.__prev
    