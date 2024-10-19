
# **Rule Engine with Abstract Syntax Tree (AST)**

This project implements a rule engine using an Abstract Syntax Tree (AST) to dynamically create, combine, and evaluate rules based on conditions such as user attributes (e.g., age, salary, department). The rule engine can be used to assess eligibility or other conditions based on the given data.

## **Features**

- **Rule Creation**: Create rules from string inputs (e.g., `"age > 30 AND department = 'Sales'"`).
- **Rule Combination**: Combine multiple rules into a single expression.
- **Rule Evaluation**: Evaluate rules against data in JSON format to check if conditions are met.
- **AST Representation**: Visual representation of rules using AST structure.
- **Modular Design**: The engine is designed to easily modify or extend rules.

---

## **Project Structure**

```plaintext
RuleEngine/
├── src/
│   ├── __init__.py             # Marks src as a package
│   ├── rule_engine.py          # Logic for rule creation, combination, and evaluation
│   ├── ast.py                  # AST node structure and printing utility
│   └── tests.py                # Unit tests for validating the rule engine
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Ignore unnecessary files (e.g., .pyc, virtual env files)
```

---

## **Installation and Setup**

To set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/RuleEngineWithAST.git
   cd RuleEngineWithAST
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **How to Run**

1. **Create and Combine Rules**:
   You can create rules using the `create_rule` function and combine multiple rules using `combine_rules`. For example:

   ```python
   from rule_engine import create_rule, combine_rules

   rule = create_rule("age > 30 AND department = 'Sales'")
   combined_rule = combine_rules(["age > 30", "salary > 50000"])
   ```

2. **Evaluate Rules**:
   The `evaluate_rule` function evaluates a rule against a data dictionary. Example:

   ```python
   data = {"age": 35, "department": "Sales", "salary": 60000}
   result = evaluate_rule(rule, data)
   print(f"Rule evaluation result: {result}")  # Outputs: True
   ```

3. **Running Tests**:
   Run the test cases to ensure the rule engine works as expected:
   ```bash
   python src/tests.py
   ```

---

## **Dependencies**

The following dependencies are required to run the application:

- **Python 3.x**: Required for running the code.
- **pytest**: For running tests (optional if you want to test).
- **Other Libraries**: Listed in the `requirements.txt` file.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Design Choices**

1. **Abstract Syntax Tree (AST) Design**:
   - The core of the rule engine is built using an **AST** to represent conditions as nodes. This structure allows for flexibility in rule parsing, combination, and evaluation.

2. **Modular Rule Processing**:
   - The design separates rule creation, combination, and evaluation into distinct components to ensure modularity. This way, each piece can be extended or replaced independently.

3. **Testing**:
   - Unit tests have been implemented to ensure the correctness of rule creation, combination, and evaluation. Tests are located in `tests.py` and use `pytest` for validation.

4. **Scalability**:
   - The use of an AST allows for easy scalability. New operators and operands can be added to the rule engine by simply extending the **Node** structure in `ast.py`.

---

## **Testing**

To run all tests, use:

```bash
pytest src/tests.py
```

This ensures that all components of the rule engine function as expected.

---

## **License**

This project is licensed under the MIT License.
