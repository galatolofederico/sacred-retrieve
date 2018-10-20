from .reducer import Reducer

class Min(Reducer):
    def __init__(self, args):
        Reducer.__init__(self, args)
        self.info = "Compute the minimum value"
        self.name = "Min"
        
    def __call__(self, *data):
        return str(min(*data))