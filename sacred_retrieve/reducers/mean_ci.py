from .reducer import Reducer

class MeanCI(Reducer):
    def __init__(self, args):
        Reducer.__init__(self, args)
        self.info = "Compute the mean with the confidence intervals"
        self.name = "Mean CI"

        self.confidence = args.mean_ci
    
    def add_args(parser):
        parser.add_argument('--mean-ci',
                    type=float,
                    help='Confidence intervals for the mean (default 0.95)',
                    default=0.95
                    )
        

    def __call__(self, *data):
        import numpy as np
        import scipy.stats
        arr = 1.0 * np.array(*data)
        n = len(arr)
        m, se = np.mean(arr), scipy.stats.sem(arr)
        h = se * scipy.stats.t.ppf((1 + self.confidence) / 2., n-1)
        return ("%2f +/- %2f") % (m, h)