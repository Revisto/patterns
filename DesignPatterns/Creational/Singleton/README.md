# Singleton Pattern 📝

![singleton](https://refactoring.guru/images/patterns/content/singleton/singleton.png)

## Goal 🎯
Ensure a class has only one instance and provide global access to it.

## Real Life Example 🏪
Government of a country:
- Only one president at a time
- Everyone accesses the same government
- Can't create multiple governments

## Examples in Frameworks / Workspaces 💻
```python
from django.conf import settings

# Django's settings is a singleton
print(settings.DEBUG)  # Access same settings object
print(settings.DATABASES)  # Throughout application
```

## Implementation
### Bad Practice ❌
```python
class Database:
    def __init__(self):
        self.connection = "Connected"

# Multiple instances possible
db1 = Database()
db2 = Database()  # Creates second connection
```

### Good Practice ✅
```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected"
        return cls._instance

    def query(self, sql):
        return f"Executing {sql} on {self.connection}"

# Always same instance
db1 = Database()
db2 = Database()
assert db1 is db2  # True
```

## Smell ✨
- Global access point to instance
- Static instance storage
- Configuration objects used application-wide