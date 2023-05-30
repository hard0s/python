class Singleton(object): # Class Singleton нужен для того, тобы при многократном вызове handler окна, все окна являлись одном Instance
    def __new__(cls, *args, ** kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it
    
    def init(self, *args, **kwds):
        pass