import numpy as np

def getMagnitude(a):
    return np.sqrt(np.dot(a, a))
    
def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    if(np.dot(a, b) == 0):
        return 0
    # Write code here
    return np.dot(a, b)/(getMagnitude(a) * getMagnitude(b))
    