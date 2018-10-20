from .reducer import Reducer

class Count(Reducer):
    def __init__(self, args):
        Reducer.__init__(self, args)
        self.info = "Compute the number of samples"
        self.name = "# Samples"
        
    def __call__(self, *data):
        return str(len(*data))