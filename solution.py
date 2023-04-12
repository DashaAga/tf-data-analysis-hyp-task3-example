import pandas as pd
import numpy as np

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
     n_permutations=10000
     alpha=0.08
     observed_difference = np.mean(y) - np.mean(x)

     combined = np.concatenate([x, y])

     differences = np.zeros(n_permutations)

     for i in range(n_permutations):
         permuted = np.random.permutation(combined)
         x_permuted = permuted[:len(x)]
         y_permuted = permuted[len(x):]

     differences[i] = np.mean(y_permuted) - np.mean(x_permuted)

     p_value = (differences >= observed_difference).sum() / n_permutations

     return p_value < alpha
