# Feature Lists


### Working Features:
- [x] Colored logs
- [x] Log formatting
- [x] Writing to file
- [x] Date


### Future Features:
- [ ] Special debug log level
- [ ] Add a table that allows user to debug with
- [ ] Allow users to add their own log levels
- [ ] Allow users to add map their own colors to log


Logging tables feature example
### Log Tables
```python3
from plogs import get_logger
logging = get_logger()

class Example:

    def __init__(self, a, b):
        self.a = a
        self.b = b


ex1 = Example(1, 2)
ex2 = Example('a', 'b')

logging.table(ex1, ex2)
```
The output would be like
```
+ --------------- +
|     |  a  |  b  |
+ --- | --- | --- +
| ex1 |  1  |  2  |
+ --- | --- | --- |
| ex2 | 'a' | 'b' |
+ --------------- +
```
