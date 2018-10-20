from .reducer import Reducer

class Max(Reducer):
    def __init__(self, args):
        Reducer.__init__(self, args)
        self.info = "Compute the maximum value"
        self.name = "Max"
        
    def __call__(self, *data):
        return str(max(*data))