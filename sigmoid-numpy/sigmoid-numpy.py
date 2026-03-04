import numpy as np

def sigmoid_for_val(val):
    return 1/(1 + np.exp(-val))
def sigmoid(x):
    x = np.array(x)
    # res = []
    # for val in x:
    #     res.append(sigmoid_for_val(val))

    # return res

    return 1 / (1 + np.exp(-x))