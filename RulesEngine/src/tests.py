import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rule_engine import create_rule, combine_rules, evaluate_rule
from ast import print_ast

def test_create_rule():
    # Test the creation of an individual rule
    rule = create_rule("age > 30 AND department = 'Sales'")
    print_ast(rule)

def test_combine_rules():
    # Test the combination of two rules
    rules = [
        "age > 30 AND department = 'Sales'",
        "salary > 50000"
    ]
    combined_rule = combine_rules(rules)
    print_ast(combined_rule)

def test_evaluate_rule():
    # Test evaluating a rule against data
    rule = create_rule("age > 30 AND department = 'Sales'")
    data = {"age": 35, "department": "Sales", "salary": 60000}
    result = evaluate_rule(rule, data)
    print(f"Rule evaluation result: {result}")  # Should print True

if __name__ == "__main__":
    print("Test: Create Rule")
    test_create_rule()
    
    print("\nTest: Combine Rules")
    test_combine_rules()
    
    print("\nTest: Evaluate Rule")
    test_evaluate_rule()
