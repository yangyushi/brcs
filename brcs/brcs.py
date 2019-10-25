#!/usr/bin/env python3
import numpy as np

def get(number, bias=(1.0, 0.7, 0.8), lightness=(0.25, 1.0)):
    if number > 1:
        rgbs = np.random.uniform(lightness[0], lightness[1], (number, 3))
    else:
        rgbs = np.random.uniform(lightness[0], lightness[1], 3)
    colors = rgbs * np.array(bias)
    return colors
