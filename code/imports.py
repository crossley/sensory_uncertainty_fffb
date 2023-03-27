import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from scipy.optimize import differential_evolution, LinearConstraint
import pingouin as pg
import statsmodels.formula.api as smf
from patsy.contrasts import Diff
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
plt.rcParams['text.usetex'] = False
