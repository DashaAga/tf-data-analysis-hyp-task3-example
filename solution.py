import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha=0.08
    stat, p_val = mannwhitneyu(x, y, alternative='two-sided')

    if p_val < alpha:
        return True
    else:
        return False
