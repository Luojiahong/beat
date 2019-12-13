"""
Module for customized colormaps.
"""

from matplotlib.colors import LinearSegmentedColormap
from numpy import array

def slip_colormap(nbins=64, return_numpy=False):
    """
    Colormap optimized for distributed Easrthquake-slip models.
    white-blue-green-yellow-orange-red

    Parameters
    ----------
    nbins : int
        Number of bins, smoothness of colormap
        the higher the smoother is the returned colormap

    Returns
    -------
    :class:`matplotlib.colors.LinearSegmentedColormap`
    """

    name = 'slipcolor'
    colors = [
        (1, 1, 1),
        (0.888888888888889, 0.966666666666667, 1),
        (0.777777777777778, 0.933333333333333, 1),
        (0.666666666666667, 0.900000000000000, 1),
        (0.555555555555556, 0.866666666666667, 1),
        (0.444444444444444, 0.833333333333333, 1),
        (0.333333333333334, 0.800000000000000, 1),
        (0.222222222222222, 0.766666666666667, 1),
        (0.111111111111111, 0.733333333333333, 1),
        (0, 0.700000000000000, 1),
        (0, 0.711111111111111, 0.888888888888889),
        (0, 0.722222222222222, 0.777777777777778),
        (0, 0.733333333333333, 0.666666666666667),
        (0, 0.744444444444445, 0.555555555555555),
        (0, 0.755555555555556, 0.444444444444445),
        (0, 0.766666666666667, 0.333333333333334),
        (0, 0.777777777777778, 0.222222222222222),
        (0, 0.788888888888889, 0.111111111111111),
        (0, 0.800000000000000, 0),
        (0.0555555555555556, 0.822222222222222, 0),
        (0.111111111111111, 0.844444444444445, 0),
        (0.166666666666667, 0.866666666666667, 0),
        (0.222222222222222, 0.888888888888889, 0),
        (0.277777777777778, 0.911111111111111, 0),
        (0.333333333333333, 0.933333333333333, 0),
        (0.388888888888889, 0.955555555555556, 0),
        (0.444444444444444, 0.977777777777778, 0),
        (0.500000000000000, 1, 0),
        (0.555555555555555, 1, 0),
        (0.611111111111111, 1, 0),
        (0.666666666666667, 1, 0),
        (0.722222222222222, 1, 0),
        (0.777777777777778, 1, 0),
        (0.833333333333334, 1, 0),
        (0.888888888888889, 1, 0),
        (0.944444444444445, 1, 0),
        (1, 1, 0),
        (1, 0.944444444444445, 0),
        (1, 0.888888888888889, 0),
        (1, 0.833333333333333, 0),
        (1, 0.777777777777778, 0),
        (1, 0.722222222222222, 0),
        (1, 0.666666666666667, 0),
        (1, 0.611111111111111, 0),
        (1, 0.555555555555555, 0),
        (1, 0.500000000000000, 0),
        (1, 0.444444444444445, 0),
        (1, 0.388888888888889, 0),
        (1, 0.333333333333333, 0),
        (1, 0.277777777777778, 0),
        (1, 0.222222222222222, 0),
        (1, 0.166666666666667, 0),
        (1, 0.111111111111111, 0),
        (1, 0.0555555555555554, 0),
        (1, 0, 0),
        (0.944444444444445, 0, 0),
        (0.888888888888889, 0, 0),
        (0.833333333333334, 0, 0),
        (0.777777777777778, 0, 0),
        (0.722222222222222, 0, 0),
        (0.666666666666667, 0, 0),
        (0.611111111111111, 0, 0),
        (0.555555555555555, 0, 0),
        (0.500000000000000, 0, 0)]
    if return_numpy:
        return array(colors)
    else:
        return LinearSegmentedColormap.from_list(name, colors, N=nbins)
