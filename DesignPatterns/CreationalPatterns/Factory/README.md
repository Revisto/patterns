# Factory Method Pattern 📝

![factory method](https://refactoring.guru/images/patterns/content/factory-method/factory-method-en.png)

## Goal 🎯
Let classes create objects without specifying the exact class to create.

## Real Life Example 🏪
Restaurant franchise:
- All locations follow same menu
- Each location makes dishes their own way
- Orders work the same everywhere

## Examples in Frameworks / Workspaces 💻
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Engine factory creates different database engines
sqlite_engine = create_engine('sqlite:///app.db')
postgres_engine = create_engine('postgresql://localhost/app')

# Session factory creates database sessions
Session = sessionmaker(bind=sqlite_engine)
session = Session()
```

## Implementation
### Bad Practice ❌
```python
class Product:
    def __init__(self, name):
        self.name = name

class ConcreteProductA(Product):
    pass

class ConcreteProductB(Product):
    pass

class Client:
    def create_product(self, product_type):
        if product_type == "A":
            return ConcreteProductA("Product A")
        elif product_type == "B":
            return ConcreteProductB("Product B")
        else:
            return None

# Usage
client = Client()
product_a = client.create_product("A")
product_b = client.create_product("B")
```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class ConcreteProductA(Product):
    def __init__(self, name):
        super().__init__(name)

class ConcreteProductB(Product):
    def __init__(self, name):
        super().__init__(name)

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        return self.factory_method()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA("Product A")

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB("Product B")

# Usage
creator_a = ConcreteCreatorA()
product_a = creator_a.create_product()

creator_b = ConcreteCreatorB()
product_b = creator_b.create_product()
```

## Smell ✨
- Configuration or dependency injection frequently selecting between factories
- Presence of abstract factory classes or methods