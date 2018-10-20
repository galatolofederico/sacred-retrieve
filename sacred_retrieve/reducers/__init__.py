from .mean_ci import MeanCI
from .min import Min
from .max import Max
from .count import Count

reducers=dict(
    mean=MeanCI,
    min=Min,
    max=Max,
    count=Count
)