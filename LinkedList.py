# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/16/23
# Description: This code implements a LinkedList class with recursive methods for adding, removing, checking, inserting,
# reversing, and converting a linked list to a plain Python list. The class uses recursion to perform these operations.
# The Node class represents individual nodes in the linked list, storing data and a reference to the next node.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self._head = None

    def get_head(self):
        """Returns the first Node object in the linked list."""
        return self._head

    def _rec_add(self, node, data):
        """Recursive method to add a new node at the end of the linked list."""
        if node.next is None:
            node.next = Node(data)
        else:
            self._rec_add(node.next, data)

    def add(self, data):
        """Adds a new node with the given data at the end of the linked list."""
        if self._head is None:
            self._head = Node(data)
        else:
            self._rec_add(self._head, data)

    def _rec_remove(self, prev_node, curr_node, data):
        """Recursive method to remove the first occurrence of a node with the given data."""
        if curr_node is None:
            return
        if curr_node.data == data:
            if prev_node is None:
                self._head = curr_node.next
            else:
                prev_node.next = curr_node.next
        else:
            self._rec_remove(curr_node, curr_node.next, data)

    def remove(self, data):
        """Removes the first occurrence of a node with the given data from the linked list."""
        self._rec_remove(None, self._head, data)

    def _rec_contains(self, node, data):
        """Recursive method to check if a node with the given data exists in the linked list."""
        if node is None:
            return False
        if node.data == data:
            return True
        return self._rec_contains(node.next, data)

    def contains(self, data):
        """Checks if a node with the given data exists in the linked list."""
        return self._rec_contains(self._head, data)

    def _rec_insert(self, prev_node, curr_node, data, index):
        """Recursive method to insert a new node with the given data at the specified index."""
        if index == 0:
            if prev_node is None:
                self._head = Node(data, curr_node)
            else:
                prev_node.next = Node(data, curr_node)
        else:
            if curr_node is None:
                return
            self._rec_insert(curr_node, curr_node.next, data, index - 1)

    def insert(self, data, index):
        """Inserts a new node with the given data at the specified index in the linked list."""
        if index < 0:
            raise ValueError("Index must be a non-negative integer.")
        self._rec_insert(None, self._head, data, index)

    def _rec_reverse(self, prev_node, curr_node):
        """Recursive method to reverse the order of the nodes in the linked list."""
        if curr_node is None:
            self._head = prev_node
            return
        next_node = curr_node.next
        curr_node.next = prev_node
        self._rec_reverse(curr_node, next_node)

    def reverse(self):
        """Reverses the order of the nodes in the linked list."""
        self._rec_reverse(None, self._head)

    def _rec_to_plain_list(self, node, plain_list):
        """Recursive method to convert the linked list to a plain Python list."""
        if node is None:
            return plain_list
        plain_list.append(node.data)
        return self._rec_to_plain
