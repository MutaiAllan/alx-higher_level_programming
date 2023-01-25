#!/usr/bin/python3
"""Defines a node in a singly linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a new node.
        Args:
            data (int): data of the new node.
            next_node (Node): Pointer to the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the value of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes a new singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node.
        Args:
            value (Node): new node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__next_node = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of SInglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
