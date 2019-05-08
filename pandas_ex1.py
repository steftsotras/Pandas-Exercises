#Step 1

import numpy as np
import pandas as pd

#Step 2
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
#Step 3
chipo = pd.read_csv(url, sep = '\t')

#Step 4
print(chipo.head(10))

#Step 5

