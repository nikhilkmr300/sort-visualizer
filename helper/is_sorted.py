import numpy as np

def is_sorted(array, desc=False):
    if(desc == False):
        return (np.diff(array) >= 0).all()
    elif(desc == True):
        return (np.diff(array) <= 0).all()

if(__name__ == '__main__'):
    arr1 = np.array([1, 2, 3, 4, 4, 5, 6, 6])
    arr2 = np.array([6, 6, 5, 4, 3, 3, 2, 1, 1])
    arr3 = np.array([1, 5, 9, 4, 6, 7, 7, 8])
    print(is_sorted(arr1))
    print(is_sorted(arr1, desc=True))
    print(is_sorted(arr2, ))
    print(is_sorted(arr2, desc=True))
    print(is_sorted(arr3))
    print(is_sorted(arr3, desc=True))
