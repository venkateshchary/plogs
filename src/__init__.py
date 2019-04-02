name = 'plogs'
__all__ = ['plogutils.py', 'logutils.py', 'tableutils.py', 'errorutils']


from .plogutils import _get_logger

def get_logger():
    return _get_logger()
