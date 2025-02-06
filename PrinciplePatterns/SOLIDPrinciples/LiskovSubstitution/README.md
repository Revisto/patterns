# Liskov Substitution Principle (LSP) 📝

## Goal 🎯
A child class should be able to do everything its parent class can do. If you have a function that works with the parent class, it should work just as well with the child class.

## Real Life Example 🏪
Think of a TV remote control:
- Any remote control (universal or original) should be able to turn the TV on/off
- Any remote should be able to change channels and volume
- A smart remote can add new features but shouldn't break basic functionality

Electric cars vs Gas cars:
- Both can drive, brake, and park
- Both fulfill the basic "car" functions
- Switching from gas to electric shouldn't break driving experience

## Examples in Frameworks / Workspaces 💻
- SQLAlchemy's Engine types: PostgreSQL/MySQL/SQLite engines all work the same way
- Flask's views: MethodView subclasses maintain HTTP method handling
```python
# Works with any engine
from sqlalchemy import create_engine

# PostgreSQL engine
engine = create_engine('postgresql://user:pass@localhost/db')
# SQLite engine - can replace PostgreSQL without changes
engine = create_engine('sqlite:///db.sqlite')
```


## Implementation
### Bad Practice ❌
```python
from abc import ABC, abstractmethod

class TransporationDevice(ABC):
        @abstractmethod
        def start_engine(self):
            pass

class Car(TransporationDevice):
        def start_engine(self):
           print("Starting Engine...")

class Bike(TransporationDevice):
        def start_engine(self):
           print("Starting Engine...")

class Cycle(TransporationDevice):
        def start_engine(self):
          # Bicyles don't have engines
          raise NotImplementedError()
```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class TransporationDevice(ABC):
    @abstractmethod
    def start(self):
        """Steps to start the vehicle"""

class TransporationDeviceWithoutEngine(ABC):
    pass

class TransporationDeviceWithEngine(ABC):        
    @abstractmethod
    def start_engine(self):
        """Process to start the engine"""

class Car(TransporationDeviceWithEngine):

        def start(self):
            # First start engine
            self.start_engine()
            # Do other steps here

        def start_engine(self):
           print("Starting Engine...")

class Bike(TransporationDeviceWithEngine):
        def start(self):
            # First start the engine
            self.start_engine()
            # Do other steps here

        def start_engine(self):
           print("Starting Engine...")


class Cycle(TransporationDeviceWithoutEngine):
        def start(self):
            print("Hit pedals....")
```

## Smell ✨
- Abstract Base Classes with clear contracts
- Consistent method signatures across inheritance chain