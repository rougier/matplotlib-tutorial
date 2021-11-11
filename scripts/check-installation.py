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

# Check for basemap or cartopy
try:
    import mpl_toolkits.basemap as basemap
    check_for_cartopy = False
except:
    check_for_cartopy = True
else:
    print("Check for basemap: ", end="")
    if LooseVersion(basemap.__version__) < LooseVersion("1.0"):
        print("basemap is too old (< 1.0) \n")
        sys.exit()
    else:
        print("ok")

if check_for_cartopy:
    try:
        import cartopy
    except:
        print("This tutorial requires either basemap or cartopy\n")
        sys.exit()

    print("Check for cartopy: ", end="")
    if LooseVersion(cartopy.__version__) < LooseVersion("0.15"):
        print("cartopy is too old (< 0.15) \n")
        sys.exit()
    else:
        print("ok")
