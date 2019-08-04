# iMessageDB

A wrapper for querying local iMessage databases and getting its data in useful DataFrames.

## Getting Started

I've written this README under the assumption you're running this on macOS. Obviously, any machine without iMessage will find this module much less useful.

## Installation

First, install this module:

```bash
pip3 install git+git://github.com/jkatofsky/iMessageDB.git
```

Then, copy your local iMessage databse to a desired location in your project directory:

```bash
cd /your/project/directory
cp ~/Library/Messages/chat.db .
```

Then, use the package

```python
from iMessageDB import iMessageDBWrapper

if __name__ == "__main__":
    wrapper = iMessageDBWrapper("path/to/chat.db")
    #call wrapper's methods
```
