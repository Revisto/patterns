# Pattern Name 📝

## Goal 🎯
Don't force classes to implement methods they don't use. Split big interfaces into smaller ones.


## Real Life Example 🏪
### Django REST Framework
```python
from rest_framework import mixins, viewsets

# Instead of using full ModelViewSet, split into focused views
class ListCreateBookAPI(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateDeleteBookAPI(mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin, 
                         viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## Examples in Frameworks / Workspaces 💻
Restaurant Staff Roles:
- Waiter: takes orders, serves food
- Chef: cooks food
- Cleaner: cleans tables
Instead of one "RestaurantEmployee" doing everything, each role has specific duties.


## Implementation
### Bad Practice ❌
```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

## Smell ✨
- Multiple small interfaces instead of one large interface
- Classes implementing only methods they need