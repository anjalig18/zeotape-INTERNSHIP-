# Rule Engine with Abstract Syntax Tree (AST)

This project implements a rule engine using an Abstract Syntax Tree (AST) to dynamically create, combine, and evaluate rules based on conditions such as user attributes (e.g., age, salary, department). The rule engine can be used to assess eligibility based on data input.

## Features

- **Rule Creation**: Create rules from string inputs (e.g., `"age > 30 AND department = 'Sales'"`).
- **Rule Combination**: Combine multiple rules into a single expression.
- **Rule Evaluation**: Evaluate rules against data in JSON format to check if conditions are met.
- **AST Representation**: Visual representation of rules using AST structure.
- **Modular Design**: The engine is designed to easily modify or extend rules.

## Project Structure

```bash
RuleEngine/
│
├── src/
│   ├── __init__.py
│   ├── rule_engine.py         # Logic for rule creation, combination, and evaluation
│   ├── ast.py                 # AST node structure and printing utility
│   └── tests.py               # Unit tests for validating the rule engine
│
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignore unnecessary files (e.g., .pyc, virtual env files)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/RuleEngineWithAST.git
cd RuleEngineWithAST
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Creating and Combining Rules
You can create rules using the create_rule function and combine multiple rules using combine_rules. For example:

python
Copy code
from rule_engine import create_rule, combine_rules

rule = create_rule("age > 30 AND department = 'Sales'")
combined_rule = combine_rules(["age > 30", "salary > 50000"])
Evaluating Rules
The evaluate_rule function evaluates a rule against a data dictionary. Example:

python
Copy code
data = {"age": 35, "department": "Sales", "salary": 60000}
result = evaluate_rule(rule, data)
print(f"Rule evaluation result: {result}")  # Outputs: True
Running Tests
Run the test cases to ensure the rule engine works as expected:

bash
Copy code
python src/tests.py
Testing
To run all tests, use:

bash
Copy code
pytest src/tests.py
