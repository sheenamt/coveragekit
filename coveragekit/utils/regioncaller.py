
from coveragekit.version import __version__

class RegionCaller(dict):
    """Event subscription-like dict. Got this from http://stackoverflow.com/questions/1092531/event-system-in-python

    A list of callable objects. Calling an instance of this will cause a
    call to each item in the list in ascending order by index.

    Example Usage:
    >>> def f(x):
    ...     print 'f(%s)' % x
    >>> def g(x):
    ...     print 'g(%s)' % x
    >>> e = Event()
    >>> e()
    >>> e.append(f)
    >>> e(123)
    f(123)
    >>> e.remove(f)
    >>> e()
    >>> e += (f, g)
    >>> e(10)
    f(10)
    g(10)
    >>> del e[0]
    >>> e(2)
    g(2)

    """
    def __call__(self, *args, **kwargs):
        for key,f in self.items():
            f(*args, **kwargs)

    def __repr__(self):
        return "Event(%s)" % dict.__repr__(self)