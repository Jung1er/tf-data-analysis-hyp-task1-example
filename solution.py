import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest


chat_id = 392609262 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    a = 0.08
    z_st, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], value=0, alternative='smaller')
    z_cr = np.abs(norm.ppf(a))
    if z_st < -z_cr:
        return True
    else:
        return False
