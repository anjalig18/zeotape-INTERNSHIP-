# ast.py

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        """
        Node for Abstract Syntax Tree (AST)
        :param type: 'operator' or 'operand'
        :param left: Left child node (for operators)
        :param right: Right child node (for operators)
        :param value: Value for operand nodes (e.g., condition or comparison value)
        """
        self.type = type  # 'operator' or 'operand'
        self.left = left
        self.right = right
        self.value = value

def print_ast(node, depth=0):
    """
    Utility function to print the AST for debugging purposes.
    :param node: The root node of the AST.
    :param depth: Used for indentation in print (for visualizing depth in the tree).
    """
    if node is None:
        return
    print(f"{'  ' * depth}Node(type={node.type}, value={node.value})")
    print_ast(node.left, depth + 1)
    print_ast(node.right, depth + 1)
