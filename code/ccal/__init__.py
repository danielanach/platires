"""
Computational Cancer Analysis Library

Authors:
    Huwate (Kwat) Yeerna (Medetgul-Ernar)
        kwat.medetgul.ernar@gmail.com
        Computational Cancer Analysis Laboratory, UCSD Cancer Center

    Pablo Tamayo
        ptamayo@ucsd.edu
        Computational Cancer Analysis Laboratory, UCSD Cancer Center
"""

RANDOM_SEED = 20121020

import sys

sys.setrecursionlimit(10000)

from .support.system import install_libraries

install_libraries([
    'rpy2',
    'plotly',
])

from .computational_cancer_biology import association, oncogps, mutual_vulnerability, gsea, inference
from .support.plot import plot_points, plot_distribution, plot_violin_box_or_bar, plot_heatmap, plot_clustermap, \
    plot_nmf
from .support.file import read_gct, write_gct, read_gmt, read_gmts, write_rnk, load_data_table, write_data_table
from .support.simple_funcs import extract_top_bottom_features
