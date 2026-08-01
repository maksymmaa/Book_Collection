A modular, clean command-line application designed to catalogue books, evaluate library scopes and seamlessly sort or compare distinct literary works.

## Features
* **Advanced Operator Overloading (Dunder Methods):** Leverages Python's native magic methods within the core data structure:
  * `__lt__` (Less Than): Automatically enables native Python engines like `max()` and `sorted()` to rank book instances by their total physical page length.
  * `__eq__` (Equality): Evaluates whether two separate book records are identical based strictly on their Title and Author.
  * `__len__`: Overloaded to dynamically map the object's length to its page count.
  * `__contains__`: Simplifies substring lookups directly within book title fields.
* **Smart Data Sorting & Extraction:** Features automatic workflows to compute and point out the longest book inside the collection or order the catalog instantly.
* **Robust Input Validation:** Wraps user configuration loops with safe try/except guards preventing application crashes on invalid integer fields (e.g., Year or Page fields).
* **Decoupled Data Pipeline:** Serializes custom object states directly into standard JSON formats for stable data survival between runs.

## Project Structure
The repository is separated into structured logic components according to scalable python layout practices:

```text
Book Collection/
├── book_collection/
│   ├── json_files/
│   │   └── books.json          # Persistent local storage (git-ignored)
│   ├── models/
│   │   ├── __init__.py          # Package initializer
│   │   └── book.py             # Data entity with overloaded operators & mappings
│   ├── services/
│   │   ├── __init__.py          # Package initializer
│   │   └── book_service.py     # IO abstraction, search algorithms, and sorting adapters
│   ├── config.py                # Global configurations and resource routes
│   └── main.py                  # Primary runtime system menu loops
├── .gitignore                   # Workspace configuration exclusions
├── LICENSE                      # Open-source operational terms
└── README.md                    # Project documentation
```

## Prerequisites
Python 3.10 or higher is required due to the structural implementation of match/case statement menus.

## How to Run
Clone this directory onto your computer, navigate to the source root containing main.py and launch it via terminal:

```Bash
python main.py
