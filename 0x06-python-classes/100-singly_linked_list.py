#!/usr/bin/python3
"""Create Singly linked list data structure."""


class Node:
    """Singly linked list node.

    Attributes:
        data (int): Integer to be stored in the node
        next_node (Node): Next node object

    """

    @property
    def data(self):
        """Get `Data` to be stored in the `Node`."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next `Node` object."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """Instatiate a Node object.

        Args:
            data (int): Integer to be stored in the node
            next_node (Node): Next node object
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Define Singly Linked List.

    Attributes:
        head: Head Node

    """

    def __init__(self):
        """Instantiate a Singly Linked List object."""
        self.__head = None

    def __str__(self):
        """Return string of the entire list,
        each `Node data` on a separate line.
        """
        string = ""
        node = self.__head
        while node:
            string += str(node.data) + "\n"
            node = node.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Insert a new `Node` into the correct sorted position in the list.

        Args:
            value (int): Data to be stored in the new `Node`
        """
        if not self.__head:
            self.__head = Node(value, None)
            return
        if value < self.__head.data:
            node = Node(value, self.__head)
            self.__head = node
            return
        prev_node = self.__head
        next_node = self.__head.next_node
        while next_node:
            if value < next_node.data:
                prev_node.next_node = Node(value, next_node)
                return
            prev_node = next_node
            next_node = next_node.next_node
        prev_node.next_node = Node(value, None)
