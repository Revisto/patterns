# Pattern Name 📝

## Goal 🎯
High-level modules shouldn't depend on low-level modules. Both should depend on abstractions.


## Real Life Example 🏪
TV and Remote Control:
- TV doesn't depend on specific remote brand
- Any remote following the standard protocol works
- Both TV and remote depend on the protocol (abstraction)

## Examples in Frameworks / Workspaces 💻
```python
# Dependencies through abstract settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or sqlite3, mysql
        'NAME': 'mydb',
    }
}
```

## Implementation
### Bad Practice ❌
```python
class Logger:
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:

    def __init__(self):
        self.logger = Logger()

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result
```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result
```

## Smell ✨
- Factory methods creating dependencies
- Configuration-based dependency selection