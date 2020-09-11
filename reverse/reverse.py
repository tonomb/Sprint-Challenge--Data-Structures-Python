class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return
        else:
            if node.next_node is not None:
                self.head = node.next_node
                node.next_node = prev
                # print(node.value)
                self.reverse_list(self.head, node)
            else:
                node.next_node = prev

    def print_order(self,node):
        if node.next_node is not None:
            print(node.value)
            self.print_order(node.next_node)
        else:
            print(node.value)

# list = LinkedList()

# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# # print(list.head.value) # 5
# # print('reverse')
# list.reverse_list(list.head, None)
# print(list.head.value)
# list.print_order(list.head)


# # print(list.head.value) # 1
