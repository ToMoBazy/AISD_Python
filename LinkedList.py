from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any=None):
         self.value = value
         self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        node = Node(value) #tworzenie wezla i przypisanie do niego wartosci value
        node.next = self.head  # glowa calej listy
        self.head = node
        if node.next is None:
              self.tail = node


    def __str__(self):
        self.lst = []
        n = self.head
        while n:
            print(n.value)
            self.lst.append(str(n.value))
            n = n.next
        return ' -> '.join(self.lst)

    def append(self, value: Any) -> None:
          node = Node(value) #tworzenie wezla i przypisanie do niego wartosci value
          if self.head is None:
              self.head = node
          else:
              n = self.head
              while n.next is not None:
                  n = n.next
              n.next = node
          if node.next is None:
              self.tail = node

    def __len__(self):
        return len(self.lst)

    def node(self, at: int) -> Node:
        self.at = at
        n = self.head
        counter: int = 0
        while n:

            if (counter == at):
                return n
            n = n.next
            counter = counter + 1

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        temp = self.head
        while (temp):
            if temp.next == after:
                temp = temp.next

















list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
print(list_)
print(len(list_))
x = list_.node(3)
print(x)


middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
# assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
# print(list_)

