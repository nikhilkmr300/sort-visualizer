import numpy as np
import sys

def random(low, high, size, seed=None):
    """
    Returns array of random integers.

    Parameters:
    low (int): Lower bound (inclusive) of values in array.
    high (int): Upper bound (non-inclusive) of values in array.
    size (int): Number of values in array.
    seed (int): Seed to PRNG.

    Returns:
    NumPy ndarray
    """

    if(high <= low):
        print('initializer.random: high must be greater than low')
        sys.exit()

    np.random.seed(seed)

    return np.random.randint(low, high, size=size)

def reverse(high, low, size=None):
    """
    Returns reverse-sorted array (values sorted in descending order).

    Parameters:
    low, high and size same as for random.

    Returns:
    NumPy ndarray
    """

    if(high <= low):
        print('initializer.reverse: high must be greater than low')
        sys.exit()

    if(size is not None):
        return np.flip(np.linspace(low, high, num=size))
    else:
        return np.arange(high, low, step=-1)

def many_same(choice_elements, size, seed=None):
    """
    Returns array with many repeated elements.

    Parameters:
    size and seed same as for random.
    choice_elements (arraylike): Collection of unique values in array.

    Returns:
    NumPy ndarray
    """
    np.random.seed(seed)

    return np.random.choice(choice_elements, size=size)

def error(anchor, size, error=0.1, seed=None):
    """
    Returns array with values in the range [anchor - error * anchor,
    array + error * anchor].

    Parameters:
    size and seed same as for random.
    anchor (int): Number around which numbers in the array are centred.
    error (int): Allowed percentage of anchor around which array elements may
        take values.

    Returns:
    NumPy ndarray
    """
    
    np.random.seed(seed)
    anchor_array = np.ones(size) * anchor
    max_error = error * anchor
    error_array = np.random.random(size) * max_error * np.random.choice([-1, 1], size=size)

    return anchor_array + error_array
