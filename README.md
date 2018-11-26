# plogs — Pretty Logs

### Project Goals
In the beginning, the goal of Pretty Logs was to create a colorful logging system designed for scalable projects. Later,
my vision for Pretty Logs widened in scope to also include useful debugging tools that are found in JavaScript and
aren't that readily available in Python.

In the future, we anticipate better control to configure logging settings and a debugging log level where debug tools
can only print to.


### Installation
The easiest way to install Pretty Logs is to install via pip.

```
pip3 install -U plogs
```

Is also possible to download and import Pretty Logs directly into your project. If you are you looking to do so, I
recommend cloning the GitHub repository to ensure the plogs module hierarchy is kept the same.

```
$ git clone https://github.com/11/plogs.git
```

### Setup

Importing Pretty Logs into your project is quite simple. All that's required is to <b>import plogs</b> and instantiate an instance of <b>Logger</b>.

```python3
from plogs import Logger
logging = Logger()
```

It's recommend to do the following steps inside a `__init__.py` file at the root level of your project so Pretty Logs can referenced throughout the entire application.

### Log With Colors

Pretty Logs' main feature is color coding different logging levels and statues. The default logging levels are set mapped to:

| Log Level         | Color |
| ---               | --- |
| logging.info	    | gray |
| logging.status	| bold |
| logging.success	| green |
| logging.warning	| orange |
| logging.critical	| red |


### Log Tables
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
