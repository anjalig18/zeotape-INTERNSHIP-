# rule_engine.py

import re
from ast import Node, print_ast

def create_rule(rule_string):
    """
    Parses a rule string into an AST.
    :param rule_string: String representing a rule, e.g., "age > 30 AND department = 'Sales'"
    :return: The root node of the corresponding AST.
    """

    
    def parse_condition(condition):
        # First, check for numeric comparison (e.g., age > 30)
        match = re.match(r'(\w+)\s*(>=|<=|=|>|<)\s*(\d+)', condition)
        if match:
           field, operator, value = match.groups()
           return Node('operand', value=(field, operator, int(value)))
  
         # Check for string comparison (e.g., department = 'Sales')
        match = re.match(r"(\w+)\s*=\s*'(.+)'", condition)
        if match:
           field, value = match.groups()
           return Node('operand', value=(field, '=', value))

        # Raise an error if the condition can't be parsed
        raise ValueError(f"Invalid condition: {condition}")


    def parse_rule(rule):
        # Parse AND/OR logic and build the AST
        tokens = re.split(r'\s+(AND|OR)\s+', rule)
        stack = []
        for token in tokens:
            if token in ('AND', 'OR'):
                node = Node('operator', value=token)
                node.left = stack.pop()
                stack.append(node)
            else:
                stack.append(parse_condition(token))
        while len(stack) > 1:
            right = stack.pop()
            operator = stack.pop()
            operator.right = right
            stack.append(operator)
        return stack[0]

    return parse_rule(rule_string)

def combine_rules(rules):
    """
    Combines multiple rules into one AST.
    :param rules: A list of rule strings.
    :return: Root node of the combined AST.
    """
    root = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if root is None:
            root = rule_ast
        else:
            combined_node = Node('operator', left=root, right=rule_ast, value='AND')
            root = combined_node
    return root

def evaluate_rule(node, data):
    """
    Evaluates the rule against a data dictionary.
    :param node: Root node of the AST.
    :param data: Dictionary with attribute values (e.g., {"age": 35, "department": "Sales"}).
    :return: True if the data matches the rule, False otherwise.
    """
    if node is None:
        return False

    if node.type == 'operand':
        field, operator, value = node.value
        if operator == '>':
            return data.get(field, 0) > value
        elif operator == '<':
            return data.get(field, 0) < value
        elif operator == '=':
            return data.get(field) == value
    elif node.type == 'operator':
        left_result = evaluate_rule(node.left, data) if node.left else False
        right_result = evaluate_rule(node.right, data) if node.right else False
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result
    return False
  