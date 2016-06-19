# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
from distutils.version import LooseVersion

# Check for python
import sys
if sys.version_info <= (3,0):
    print("This tutorial requires Python 3\n")
    sys.exit()

# Check for numpy
try:
    import numpy as np
except:
    print("This tutorial requires numpy\n")
    sys.exit()
print("Check for numpy: ", end="")
if LooseVersion(np.__version__) < LooseVersion("1.0"):
    print("numpy too old (< 1.0)\n")
    sys.exit()
else:
    print("ok")
    

# Check for matplotlib
try:
    import matplotlib as mpl 
except:
    print("This tutorial requires matplotib\n")
    sys.exit()
print("Check for matplotlib: ", end="")
if LooseVersion(mpl.__version__) < LooseVersion("1.5"):
    print("matplotlib too old (< 1.5)\n")
    sys.exit()
else:
    print("ok")

# Check for basemap
try:
    import mpl_toolkits.basemap as basemap 
except:
    print("This tutorial requires basemap\n")
    sys.exit()
print("Check for basemap: ", end="")
if LooseVersion(basemap.__version__) < LooseVersion("1.0"):
    print("basemape is too old (< 1.0) \n")
    sys.exit()
else:
    print("ok")
        
# Check for urllib
try:
    import urllib
except:
    print("This tutorial requires urllib")
else:
    print("Check for urllib: ok")
