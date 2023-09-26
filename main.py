
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_self(self):
        print(self.value)
        if self.next is None:
            return
        self.next.print_self()


class LinkedList:
    
    def __init__(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three
        self.root = one

        #self.root = None

   
    def print(self):
        # Non Recursive Version
        # pointer = self.root
        # while pointer is not None:
        #     print(pointer.value)
        #     pointer = pointer.next

        # Recursive Version
        pointer = self.root
        if pointer is None:
            return
        pointer.print_self()

LinkedList().print()
