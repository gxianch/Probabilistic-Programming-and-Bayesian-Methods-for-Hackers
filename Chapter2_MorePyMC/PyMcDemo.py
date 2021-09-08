import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df =pd.read_excel('./华南中心数据库信息.xlsx',header=None)
    df.head()
    x=np.array([10, 20, 30, 29, 28, 30, 32, 16, 24, 26, 32, 40, 50, 31, 38, 35, 28])
    from scipy import stats, optimize
    def logprod(mu):
        return np.sum(-1*stats.poisson.logpmf(x,mu)) #-1把求解极大值变为极小值
    result=optimize.minimize_scalar(logprod)
    print(result)  # x=29.3