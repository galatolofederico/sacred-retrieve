class Reducer:
    def add_args(parser):
        # static method that is called with the argparse object before the parsing
        # in order to let the Reducer add CLI arguments
        pass

    def __init__(self, args):
        self.info = "Description of the reducer"
        self.name = "Column name"
        # the constructor is called with the parsed args as arguments
        # in order to let the Reducer get its arguments

    def __call__(self, *args):
        raise NotImplementedError("A Reducer must implement the __call__ function")