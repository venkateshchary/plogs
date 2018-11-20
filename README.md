# plogs — Pretty Logs 

### Description
Pretty Logs is multipurpose logging tool designed to make debugging easier and colorful. 

### Importing
Importing and 
```python3
from plogs import PLogger

logging = PLogger()
```

### Print Colored Logs
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


### Install
```
pip3 install plogs
```
