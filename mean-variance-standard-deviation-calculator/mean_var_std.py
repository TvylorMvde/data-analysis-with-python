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
    
    matrix = np.asarray(digits).reshape(3, 3)
    
    for key in ["mean", "variance", "standard deviation", "max", "min", "sum"]:
        func = getattr(np, functions[key])
        result[key] = [x.tolist() for x in [func(matrix, axis=0), func(matrix, axis=1), func(matrix)]]

    return result
