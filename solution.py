import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha=0.08
    t_stat, p_value = ttest_ind(x, y, equal_var=False)
    return p_value/2 < alpha # двухсторонний тест, делаем односторонним
