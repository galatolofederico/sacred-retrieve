from .reducer import Reducer

class List(Reducer):
    def __init__(self, args):
        Reducer.__init__(self, args)
        self.info = "Output the list of values"
        self.name = "List"

        self.delimiter = args.delimiter
    
    def add_args(parser):
        parser.add_argument('--delimiter',
                    type=str,
                    help='Delimiter character for the list reducer',
                    default=";"
                    )
        

    def __call__(self, data):
        return self.delimiter.join([str(elem) for elem in data])