#python 3.7.1
class Node:
    """
    Represents a node in a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None  # Initially points to None

class LinkedList:
    """
    Implements a singly linked list data structure.
    """

    def __init__(self):
        self.head = None  # Head node initially points to None

    def is_empty(self):
        """
        Checks if the linked list is empty.

        Returns:
            True if the list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Prepends a new node with the given data to the beginning of the linked list.

        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """
        Inserts a new node with the given data after the specified node.

        Args:
            prev_node: The node before which the new node should be inserted.
            data: The data to store in the new node.

        Raises:
            ValueError: If the provided prev_node is not found in the linked list.
        """
        if not prev_node:
            raise ValueError("Previous node cannot be None")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        """
        Deletes the first node containing the given data from the linked list.

        Args:
            data: The data to search for and delete.

        Returns:
            True if the node was deleted, False otherwise.
        """
        if self.is_empty():
            return False

        prev_node = None
        current = self.head
        while current:
            if current.data == data:
                if not prev_node:
                    self.head = current.next
                else:
                    prev_node.next = current.next
                return True
            prev_node = current
            current = current.next
        return False

    def print_list(self):
        """
        Prints the contents of the linked list in a human-readable format.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.insert_after(linked_list.head.next, 15)  # Insert after the first node

print("Linked list contents:")
linked_list.print_list()

linked_list.delete_node(15)

print("\nAfter deletion:")
linked_list.print_list()