# plogs — Pretty Logs


### Install
You can install Pretty Logs [via pip](https://pypi.org/project/plogs/).

```
$ pip install plogs
```

### Features
- Offers a ready to use logger -- no boilerplate config needed
- Log out to files, stdout, or any file-descriptor you like
- Pretty Logs is thread-safe and multiprocess-safe
- Format your logs with Python3.6's modern string formatting
- Customizable log levels
- Stylized Debug tools
- Get insights into errors with color-coded stack traces


### Setup

Importing Pretty Logs into your project is quite simple. All that's required is to <b>import plogs</b> and instantiate an instance of <b>Logger</b>.

```python3
from plogs import get_logger
logging = get_logger()
```

It's recommend to do the following steps inside a `__init__.py` file at the root level of your project so Pretty Logs can be referenced throughout the entire application.


### Log with Colors

Pretty Logs' main feature is color coding different logging levels and statuses. The default logging levels are set mapped to:

| Log Level | Color |
| --- | --- |
| logging.info| gray |
| logging.status | bold |
| logging.success | green |
| logging.warning | orange |
| logging.error | red |
| logging.critical | red highlights |


### Log to a File
Pretty Logs can write colored logs to files. This is done through Pretty Logs' <b>config</b> function.

```python3
from plogs import get_logger

logging = get_logger()
logging.config(to_file=True)

logging.info('this is will be written to a file')
```

By default, files are written to `/var/log/plogs/plog_01.log`. `/var/log/` is chosen as the default directory because it is commonly used on unix based machines and in
docker images services.

If you are looking to use another filename and location, it can simply be edited like such:

```python3
logging.config(to_file=True, file_location='your/filepath/here/', filename='new_file.log')
```

<b>Note</b>: It's recommended to view colored logs with the `less` terminal command - if `less` doesn't work be default, `less -r` is worth trying. Also, Pretty Logs
was not designed to show colored files in Vim, Atom, Sublime, and other popular text editors.



### Formating Logs

Pretty Logs allows for a lot of customization. Customizing logs is done by editing the logging <b>config</b> and supplying Pretty Logs with a formatted string.

The following are all the configurable variables:


| Variable | Type | Format Keyword | Description |
| --- | --- | --- | --- |
| `pretty` | `bool` | `N/A` | Setting to `True` will add color to logs, `False` will un-color logs |
| `show_levels` | `bool` | `{level}` | Setting to `True` will show logging level in formatted log, `False` show no logging level |
| `show_time` | `bool` | `{time}` | Setting to `True` will show time in formatted log, `False` doesn't show time |
| `to_file` | `bool` | `N/A` | Setting to `True` writes logs to `file_location`, `False` writes to `standard output` |
| `file_location` | `str`  | `{file_location}` | Default `file_location` is `/var/log/plogs/`, otherwise a file location of your choice |
| `filename` | `str`  | `{filename}` | Default log file is `plog_01.log`, otherwise a filename of your choice |
| `N\A` | `N/A` | `{msg}` | Shows the log message in formatted log |


An example of a formatted logs would be like such:

```python3
from plogs import get_logger

logging = get_logger()

# configure plogs to allow logging level and date/time
logging.config(show_levels=True, show_time=True)

# config logs with the `{level}` keyword to show the logging level,
# `{time}` to show the date & time of when the log was written
# and `{msg} to show the logging message
logging.format('[{level}] - {time} - {msg}')

# finally write logs
logging.status('Show me the logs')
logging.info('We got some info')

# Output:
# [STATUS] - 2018-12-11 11:56:05 - Show me the logs
# [INFO] - 2018-12-11 11:56:09 - We got some info
```

<b>NOTE</b>: In order to format Pretty Logs you must put the variable you want written inside `{}` - ie like so: `{filename}`, `{file_location}`, `{levels}`, etc.
These values will be substituted for the variable they represent

### How can I Contribute?
If you are looking to contribute, you can check out you the [how to contribute doc](https://github.com/11/plogs/blob/master/docs/contribute.md)
