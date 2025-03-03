# Facade Design Pattern 📝

## Goal 🎯
Provide a simple interface to a complex system of classes.

## Real Life Example 🏪
Car dashboard:
- Complex systems behind (engine, fuel, electrical)
- Simple interface (speedometer, gas gauge, warning lights)
- Driver doesn't need to understand the complexity underneath

## Examples in Frameworks / Workspaces 💻

### Django's ORM
```python
from django.db import models

# Django ORM is a facade over SQL and database operations
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

# Simple interface that hides complex SQL
users = User.objects.filter(email__endswith="@example.com")

# Behind the scenes:
# SELECT * FROM users WHERE email LIKE '%@example.com';
```

### Requests Library
```python
import requests

# Requests is a facade over complex HTTP operations
response = requests.get('https://api.example.com/data')
data = response.json()

# Behind the scenes:
# - TCP connection
# - HTTP protocol handling
# - Header processing
# - Status code handling
# - Response parsing
```

### Flask Application Context
```python
from flask import Flask, current_app

app = Flask(__name__)

# Flask provides a facade to access application state
with app.app_context():
    # Simple interface to complex context management
    db = current_app.extensions['sqlalchemy'].db
    config = current_app.config['DATABASE_URI']
```

## Implementation
### Bad Practice ❌
```python
# Client code interacting directly with complex subsystems
class Client:
    def run_complex_task(self):
        # Initialize subsystems
        subsystem1 = SubsystemA()
        subsystem2 = SubsystemB()
        database = Database()
        logger = Logger()
        
        # Configuration
        subsystem1.init("config1")
        subsystem2.set_dependency(subsystem1)
        
        # Operation steps
        data = database.fetch_data()
        processed = subsystem1.process(data)
        result = subsystem2.transform(processed)
        logger.log("Operation completed")
        
        return result
```

### Good Practice ✅
```python
class ComplexSystemFacade:
    def __init__(self):
        self.subsystem1 = SubsystemA()
        self.subsystem2 = SubsystemB()
        self.database = Database()
        self.logger = Logger()
        
        # Configure relationships
        self.subsystem1.init("config1")
        self.subsystem2.set_dependency(self.subsystem1)
    
    def run_task(self):
        """Simple interface to complex operations"""
        data = self.database.fetch_data()
        processed = self.subsystem1.process(data)
        result = self.subsystem2.transform(processed)
        self.logger.log("Operation completed")
        return result

# Client code
class Client:
    def perform_task(self):
        facade = ComplexSystemFacade()
        return facade.run_task()
```

## Smell ✨
- Simple methods that orchestrate multiple subsystem operations
- Classes with names ending in "Facade", "Manager", or "Service"
- Few public methods that accomplish complex tasks
- Abstraction of implementation details