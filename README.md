# plogs — Pretty Logs

### Description
Pretty Logs is multipurpose logging tool designed to make debugging colorful and easier.


### Install
```
pip3 install plogs
```

### Importing
```python3
from plogs import PrettyLogger

plog = PrettyLogger()
```

### Log With Colors
```python3
# prints gray
plog.info('hello world')

# prints green
plog.success('tests passed')

# prints orange
plog.warning('something needs tweaking')

# prints red
plog.critical('reponse: 404')

# prints bold
plog.status('Running Tests:')
```

### Log Table
```python3
class Example:

    def __init__(self, a, b):
        self.a = a
        self.b = b


ex1 = Example(1, 2)
ex2 = Example('a', 'b')

plog.table(ex1, ex2)
```
```
+ --------------- +
|     |  a  |  b  |
+ --------------- +
| ex1 |  1  |  2  |
| ex2 | 'a' | 'b' |
+ --------------- +
```
