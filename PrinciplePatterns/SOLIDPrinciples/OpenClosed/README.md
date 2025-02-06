# Open-Closed Principle (OCP) 📝

## Goal 🎯
Software entities should be open for extension, but closed for modification.

## Real Life Example 🏪
A car is a closed entity, but you can add new features like a GPS, a new stereo, or a new paint job.


## Examples in Frameworks / Workspaces 💻
```markdown


## Smell ✨

### Signature & Recognition
- **Conditional Complexity:** Multiple if/else or switch statements to select behavior for new requirements.
- **Tight Coupling:** Modifications in core classes are needed each time a new feature is added.
- **Rigid Architecture:** Implementations aren't easily extendable via inheritance or composition.
- **Lack of Abstraction:** Absence of interfaces or abstract classes forcing code changes instead of extensions.

### Examples in Python Workspaces
#### Flask Example
Flask supports extensions via blueprints and plugins, keeping the core app closed for modification.
```python
from flask import Flask, Blueprint

app = Flask(__name__)

# Define blueprint to extend Flask functionality
custom_bp = Blueprint('custom_bp', __name__)

@custom_bp.route("/extended")
def extended_route():
    return "This is an extended route!"

# Register blueprint without modifying the core app logic
app.register_blueprint(custom_bp)
```


## Implementation
### Bad Practice ❌
```python
def calculate(income, deduction, country):
    # tax_amount variable is defined
    # in each calculation
    tax_amount = int()
    taxable_income = income - deduction
    if country == "India":
        # calculation here
        pass
    elif country == "US":
        # calculation here
        pass
    elif country == "UK":
        # calculation here
        pass
    return tax_amount
```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class CountryTaxCalculator(ABC):
    @abstractmethod
    def calculate_tax_amount(self):
        pass

class TaxCalculatorForUS(CountryTaxCalculator):
    def __init__(self, total_income, total_deduction):
        self.total_income = total_income
        self.total_deduction = total_deduction

    def calculate_tax_amount(self):
        taxable_income = self.total_income - self.total_deduction
        # calculation here 
        return taxable_income 


class TaxCalculatorForUK(CountryTaxCalculator):
    def __init__(self, total_income, total_deduction):
        self.total_income = total_income
        self.total_deduction = total_deduction

    def calculate_tax_amount(self):
        taxable_income = self.total_income - self.total_deduction
        # calculation here 
        return taxable_income
```

## Smell ✨
- Abstract base classes with concrete implementations
- Plugin architectures