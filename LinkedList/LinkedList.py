class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def insertFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertBack(self, data):
        new_node = Node(data)

        current = self.head
        while current is not None:
            if current.next is None:
                current.next = new_node
                break
            current = current.next

    def insert(self, node, data):
        new_node = Node(data)

        new_node.next = node.next
        node.next = new_node

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                break
            current = current.next

        return current

    def traversal(self):
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next

    def reverse(self):
        parent = self.head
        me = parent.next
        child = me.next

        parent.next = None
        while child is not None:
            me.next = parent
            parent = me
            me = child
            child = child.next
        me.next = parent
        self.head = me

        return self.head

def main():
    root = LinkedList()
    for i in range(1, 5):
        root.insertFront(i * 10)
    print('----- size -----', root.size())

    number = 30
    node = root.search(number)

    print('----- insert ----')
    root.insert(node, 150)
    root.insertBack(65)

    print('----- traversal -----')
    print(root.traversal())

    root.reverse()
    print('----- reverse -----')
    print(root.traversal())
    print('----- size -----', root.size())

if __name__ == '__main__':
    main()