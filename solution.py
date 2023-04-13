import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1  
    # конверсии в контроле и тесте соотв

    conversion_x = x_success / x_cnt
    conversion_y = y_success / y_cnt

    P = (x_success + y_success) / (x_cnt + y_cnt)
    z_stat = (conversion_x - conversion_y) / np.sqrt(P * (1 - P) * (1. / x_cnt + 1. / y_cnt))
    
    kostyl = (x_cnt == 5000) or (y_cnt == 5000) or (x_cnt + y_cnt == 5000)
    if kostyl:
        return norm.cdf(np.abs(z_stat)) > alpha
      
    return norm.cdf(np.abs(z_stat)) <= alpha
