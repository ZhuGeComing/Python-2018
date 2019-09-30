import os
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline

os.chdir(r'C:\Users\Conan\Documents\Python\2018-08')
churn = pd.read_csv('telecom_churn.csv', skipinitialspace=True)
churn.plot(x = 'duration', y = 'churn', kind = 'scatter')


