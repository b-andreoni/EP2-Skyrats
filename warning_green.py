from Funcao1 import *
import numpy as np


def warning_green(mask):
    found_green = np.argwhere(mask).size
    if found_green > 0:
        return True
    return False

if __name__ == '__main__':
    print(warning_green(mascara))