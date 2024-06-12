import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)


def reverse_in_order_traversal(root, result):
    if root:
        reverse_in_order_traversal(root.right, result)
        result.append(root.value)
        reverse_in_order_traversal(root.left, result)


def sort_up(values, i=None):
    root = None
    for value in values:
        root = insert(root, value)
    result = []
    in_order_traversal(root, result)
    return result


def sort_down(values, i=None):
    root = None
    for value in values:
        root = insert(root, value)
    result = []
    reverse_in_order_traversal(root, result)
    return result
