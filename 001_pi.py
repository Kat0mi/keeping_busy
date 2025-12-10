# -- Task --

# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Limit
# how far the program will go. 

# -- [10/12/25] --

import numpy as np

def round_pi(value):
    print(round(np.pi, len(str(value)) - 1))

round_pi(357364)