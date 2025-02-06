# Builder Pattern 📝

![builder](https://refactoring.guru/images/patterns/content/builder/builder-en.png)


## Goal 🎯
Build complex objects step by step.

## Real Life Example 🏪
Making a sandwich at a factory:
- Same steps: bread, meat, veggies, sauce
- Different ingredients at each step
- End result: many possible sandwich combinations

## Examples in Frameworks / Workspaces 💻
```python
from django.db.models import Q

# QuerySet builds complex queries step by step
User.objects.filter(
    is_active=True
).exclude(
    last_login=None
).order_by(
    '-date_joined'
).select_related(
    'profile'
)
```

## Implementation
### Bad Practice ❌
```python
class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, sauce):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.sauce = sauce

# Many parameters, hard to remember order
pizza = Pizza("large", True, False, True, "regular")
```

### Good Practice ✅
```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.sauce = None

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def build(self):
        return self.pizza

# Clear, step by step construction
pizza = (PizzaBuilder()
         .size("large")
         .add_cheese()
         .add_mushrooms()
         .add_sauce("regular")
         .build())
```

## Smell ✨
- Method chaining with builder.method().method()
- Step-by-step object construction