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
$ pip3 install -U plogs
```

Is also possible to download and import Pretty Logs directly into your project. If you are you looking to do so, I
recommend cloning the GitHub repository to ensure the plogs module hierarchy is kept the same.

```
$ git clone https://github.com/11/plogs.git
```

### Setup

Importing Pretty Logs into your project is quite simple. All that's required is to <b>import plogs</b> and instantiate an instance of <b>Logger</b>.

```python3
from plogs import get_logger
logging = get_logger()
```

It's recommend to do the following steps inside a `__init__.py` file at the root level of your project so Pretty Logs can be referenced throughout the entire application.

### Log With Colors

Pretty Logs' main feature is color coding different logging levels and statuses. The default logging levels are set mapped to:

| Log Level         | Color |
| ---               | --- |
| logging.info	    | gray |
| logging.status	| bold |
| logging.success	| green |
| logging.warning	| orange |
| logging.error     | red |
| logging.critical	| red highlight |


### Format Your Logs

Pretty Logs allows for custom logs by adding your own formatting. This can be done by editing the logging <b>config</b> and giving `plogs` a formatted string.

The following are the configurable variables:


| Variable      | Type   | Description |
| ---           | ---    | ---         |
| pretty        | `bool` | `True` colors logs, `False` uncolors logs|
| show_levels   | `bool` | `True` shows logging level in formatted log, `False` show no logging level |
| show_time     | `bool` | `True` shows time in formatted log, `False` doesn't show time |
| to_file       | `bool` | `True` writes to `file_location`, `False` writes to `std.out` |
| file_location | `str`  | Default is `/var/log/plogs`, otherwise a file location of your choice |
| filename      | `str`  | Default is `plog_01.log`, otherwise a filename of your choice |


An example of a formatted log would be like so:

```python3
from plogs import get_logger

logging = get_logger()

# configure plogs to allow `levels` and `datetime` in log
logging.config(show_levels=True, show_time=True)

# can now format logs with `{level}` to show the logging level, and `{time}` to show the datetime the log was written
logging.format('[{level}] - {time} - {msg}')

# finally write log
logging.status('Show me the logs')

# Output:
# [STATUS] - 2018-12-11 11:56:05 - Show me the logs
```


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
