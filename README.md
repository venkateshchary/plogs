# plogs — Pretty Logs

### Description
Pretty Logs is multipurpose logging tool designed to make debugging colorful and easier.


### Install
```
pip3 install plogs
```

### Importing
```python3
from plogs import Logger

logging = Logger()
```

### Log With Colors
```python3
# prints gray
logging.info('hello world')

# prints green
logging.success('tests passed')

# prints orange
logging.warning('something needs tweaking')

# prints red
logging.critical('reponse: 404')

# prints bold
logging.status('Running Tests:')
```

### Log Table
```python3
from plogs import Logger
logging = Logger()

class Example:

    def __init__(self, a, b):
        self.a = a
        self.b = b


ex1 = Example(1, 2)
ex2 = Example('a', 'b')

logging.table(ex1, ex2)
```
```
+ --------------- +
|     |  a  |  b  |
+ --------------- +
| ex1 |  1  |  2  |
| ex2 | 'a' | 'b' |
+ --------------- +
```
