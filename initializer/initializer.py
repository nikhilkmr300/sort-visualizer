import numpy as np
import sys

def random(low, high, size, seed=None):
    if(high <= low):
        print('initializer.random: high must be greater than low')
        sys.exit()

    np.random.seed(seed)

    return np.random.randint(low, high, size=size)

def reverse(high, low, size=None):
    if(high <= low):
        print('initializer.reverse: high must be greater than low')
        sys.exit()

    if(size is not None):
        return np.flip(np.linspace(low, high, num=size))
    else:
        return np.arange(high, low, step=-1)

def many_same(choice_elements, size, seed=None):
    np.random.seed(seed)

    return np.random.choice(choice_elements, size=size)

def error(anchor, size, error=0.1, seed=None):
    np.random.seed(seed)
    anchor_array = np.ones(size) * anchor
    max_error = error * anchor
    error_array = np.random.random(size) * max_error * np.random.choice([-1, 1], size=size)
    
    return anchor_array + error_array
