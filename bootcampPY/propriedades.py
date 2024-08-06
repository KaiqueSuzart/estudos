class foo:
    def __init__(self, x=None):
        self._x = x 
    
    def x(self):
        return self._x or 0
    
    