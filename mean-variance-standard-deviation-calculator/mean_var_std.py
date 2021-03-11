import numpy as np

functions = {
    'mean': 'mean',
    'variance': 'var',
    'standard deviation': 'std',
    'max': 'max',
    'min': 'min',
    'sum': 'sum'
}

result = {}

def calculate(digits):
    if len(digits) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(digits).reshape(3, 3)
    
    for key in functions.keys():
        func = getattr(np, functions[key])
        result[key] = [x.tolist() for x in [func(matrix, axis=0), func(matrix, axis=1), func(matrix)]]

    return result
