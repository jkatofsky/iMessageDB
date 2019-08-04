# iMessageDB

A wrapper for querying local iMessage databases and getting its data in useful DataFrames.

I've written this README under the assumption you're running this on macOS. Obviously, any machine without iMessage will find this module much less useful.

## Installation

First, install this module:

```bash
pip3 install git+git://github.com/jkatofsky/iMessageDB.git
```

Next, use the package

```python
from iMessageDB import iMessageDBWrapper

if __name__ == "__main__":
    wrapper = iMessageDBWrapper()
    #call wrapper's methods
```

Depending on your system's configurations, an error may be thrown when trying to read the database. In this case, you can copy it to your local project directory:

```bash
cp ~/Library/Messages/chat.db .
```

Lastly, if this does not work:

```bash
open ~/Library/Messages/
```

and copy ```chat.db``` to your local project using the Finder.

If you are using a copied database, pass its path when you initialize the wrapper.

```python
wrapper = iMessageDBWrapper("data/chat.db") #example
```
