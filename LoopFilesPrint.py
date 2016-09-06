__author__ = 'jymutua'
__email__ = "jyumbya@yahoo.com"

import os
rootdir = 'Z:/CIAT GIS DATASETS/Country Level/Tanzania'
extensions = ('.tif', '.shp')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            print (os.path.join(subdir, file))
