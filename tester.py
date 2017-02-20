import mltoweb
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


est = RandomForestClassifier()
X = pd.DataFrame(np.random.random((10, 3)), columns=['x', 'y', 'z'])
y = (X < 0.5).astype(int)


mltoweb.make_web(est, X, y, 'web')
