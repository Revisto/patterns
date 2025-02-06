# Memento Design Pattern 📝

![memento](https://refactoring.guru/images/patterns/content/memento/memento-en.png)

## Goal 🎯
Save and restore an object's previous state without revealing its details.

## Real Life Example 🏪
Text editor's undo feature:
- Save state before changes
- Restore previous state when undo
- Multiple undo levels available

## Examples in Frameworks / Workspaces 💻

### Git Version Control
```bash
# Save current state (create memento)
git commit -m "Save current state"

# Restore previous state
git checkout HEAD~1

# View saved states
git log

# Restore specific state
git checkout <commit-hash>
```

```python
from sqlalchemy.orm import Session

# Session tracks object states
session = Session()
user = User(name="John")
session.add(user)

# Rollback to previous state
session.rollback()
```

## Implementation
### Bad Practice ❌
```python
class Editor:
    def __init__(self):
        self.content = ""
        self.previous_content = ""
    
    def write(self, text):
        self.previous_content = self.content  # Mixed responsibility
        self.content = text
    
    def undo(self):
        self.content = self.previous_content  # Only one undo level
```

### Good Practice ✅
```python
class EditorState:
    def __init__(self, content):
        self.content = content

class Editor:
    def __init__(self):
        self.content = ""
        self.states = []
    
    def write(self, text):
        self.states.append(EditorState(self.content))
        self.content = text
    
    def undo(self):
        if self.states:
            state = self.states.pop()
            self.content = state.content

# Usage
editor = Editor()
editor.write("Hello")
editor.write("Hello World")
editor.undo()  # Returns to "Hello"
```

## Smell ✨
- Undo/Redo functionality
- Objects that maintain state history
- Rollback capabilities