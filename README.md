ML to Web
=========

Make a quick demo website for your sklearn models

Installation
------------

```bash
pip install git+https://github.com/theSage21/mltoweb
```


Usage
-----

```python
import mltoweb
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


est = RandomForestClassifier()
X = pd.DataFrame(np.random.random((10, 3)), columns=['x', 'y', 'z'])
y = (X < 0.5).astype(int)


mltoweb.make_web(est, X, y, 'web')
```


This creates 2 files in a directory called `web`, namely:

- `estimator.pickle`: This is the pickle of the estimator used to create predictions
- `website.py`: A bottle app which  provides a form to start getting predictions from your data
