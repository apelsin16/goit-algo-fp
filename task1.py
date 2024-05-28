class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    ll.head = prev

def sorted_insert(sorted_head, new_node):
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

def insertion_sort(ll):
    sorted_head = None
    current = ll.head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    ll.head = sorted_head


def merge_sorted_lists(ll1, ll2):
    dummy = Node()
    tail = dummy
    a = ll1.head
    b = ll2.head

    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a:
        tail.next = a
    if b:
        tail.next = b

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Створюємо та виводимо список
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(2)
ll.append(4)

print("Оригінальний список:")
ll.print_list()

# Реверсування списку
reverse_list(ll)
print("Реверсований список:")
ll.print_list()

# Сортування списку
insertion_sort(ll)
print("Відсортований список:")
ll.print_list()

# Злиття двох відсортованих списків
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("Перший відсортований список:")
ll1.print_list()
print("Другий відсортований список:")
ll2.print_list()

merged_list = merge_sorted_lists(ll1, ll2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
