# iMessageDB

A python package for querying local iMessage databases and getting its data in useful DataFrames.

## Support

While it is possible to copy the iMessage database file to any system, this module has been tested on macOS only.

## Installation

```bash
pip3 install git+git://github.com/jkatofsky/iMessageDB.git
```

## Usage

To automatically read from your active iMessage database:

```python
from iMessageDB.iMessageDBWrapper import iMessageDBWrapper

if __name__ == "__main__":
    wrapper = iMessageDBWrapper()
    #call wrapper's methods
```

Or, if you wish to copy the database to your project's directory:

```bash
cd data #example
cp ~/Library/Messages/chat.db .
```

Then, pass the wrapper the new path:

```python
wrapper = iMessageDBWrapper("data/chat.db") #example
```

## Troubleshooting

Depending on your system's configurations, an error may be thrown when trying to read the database. In this case, go to ```System Preferences > Security and Privacy > Privacy > Full Disk Access``` and check the box beside the editor or terminal from which you are running your code.
