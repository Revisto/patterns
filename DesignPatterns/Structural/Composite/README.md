# Composite Design Pattern 📝

![Composite](https://refactoring.guru/images/patterns/content/composite/composite.png)

## Goal 🎯
Treat individual objects and groups of objects the same way.

## Real Life Example 🏪
File system:
- Files are simple objects
- Folders contain files or other folders
- Both files and folders can be moved, copied, or deleted using the same operations

## Examples in Frameworks / Workspaces 💻

### Django Templates
```python
from django.template import Template, Context

# Both simple tags and nested blocks are treated uniformly
template = Template("""
{% if user.is_authenticated %}
    <h1>Welcome, {{ user.username }}</h1>
    {% include "user_profile.html" %}
{% else %}
    {% include "login_form.html" %}
{% endif %}
""")

context = Context({'user': user})
output = template.render(context)
```

### Flask-WTF Forms
```python
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, FormField

# Simple field (leaf)
class AddressField(FlaskForm):
    street = StringField('Street')
    city = StringField('City')

# Composite form with nested forms
class UserForm(FlaskForm):
    name = StringField('Name')
    # Contains multiple address fields
    addresses = FieldList(FormField(AddressField))
    
# Both simple fields and composite fields have validate() method
form = UserForm()
form.validate()  # Validates all nested fields too
```

## Implementation
### Bad Practice ❌
```python
class File:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"File: {self.name}")

class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []
    
    def add(self, item):
        self.contents.append(item)
    
    def display(self):
        print(f"Folder: {self.name}")
        # Special handling for folders vs files
        for item in self.contents:
            if isinstance(item, File):
                item.display()
            elif isinstance(item, Folder):
                item.display()

# Client needs to know if it's dealing with File or Folder
my_file = File("document.txt")
my_folder = Folder("Documents")
my_folder.add(my_file)
```

### Good Practice ✅
```python
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size
    
    def display(self):
        print(f"File: {self.name}")
    
    def get_size(self):
        return self._size

class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def remove(self, component):
        self.children.remove(component)
    
    def display(self):
        print(f"Folder: {self.name}")
        # Uniform handling of all components
        for child in self.children:
            child.display()
    
    def get_size(self):
        # Size is sum of all children
        return sum(child.get_size() for child in self.children)

# Client works with components uniformly
root = Folder("Root")
docs = Folder("Documents")
file1 = File("resume.pdf", 1000)
file2 = File("photo.jpg", 2000)

root.add(docs)
docs.add(file1)
root.add(file2)

# Same interface for both Files and Folders
root.display()
print(f"Total size: {root.get_size()}")
```

## Smell ✨
- Common interface/abstract class for both individual and container objects
- "Add" and "Remove" operations in container classes
- Recursive operations that work on entire hierarchies