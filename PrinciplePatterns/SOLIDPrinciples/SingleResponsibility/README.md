# Single Responsibility Principle (SRP) 📝

## Goal 🎯
Helps to write decoupled code, where each class has its own job.

## Real Life Example 🏪
A kitchen where:
- Chef only cooks
- Waiter only serves
- Cashier only handles money

## Examples in Frameworks / Workspaces 💻
-

## Implementation
### Bad Practice ❌
```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, message):
        # sending an email to the customer
        pass

    def place_order(self, order):
        # placing an order
        pass

    def generate_invoice(self, invoice):
        # generating an invoice
        pass

    def add_feedback(self, feedback):
        # add feedback
        pass
```

### Good Practice ✅
```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    def send_email(self, customer, message):
        # Sending an email to the customer
        pass

class OrderService:
    def place_order(self, customer, order):
        # Placing an order
        pass

class InvoiceService:
    def generate_invoice(self, customer, invoice):
        # Generating an invoice
        pass

class FeedbackService:
    def add_feedback(self, customer, feedback):
        # add customer feedback
        pass
```

## Smell ✨
- Small and short functions and methods.
