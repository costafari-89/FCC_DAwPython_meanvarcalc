import numpy as np

def calculate(list):
    input_array = np.array(list)

    try:
        input_3x3 = input_array.reshape(3,3)
    
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    else:
        calculations = {
            'mean': [input_3x3.mean(axis=0).tolist(), input_3x3.mean(axis=1).tolist(), input_3x3.mean()],
            'variance': [input_3x3.var(axis=0).tolist(), input_3x3.var(axis=1).tolist(), input_3x3.var()],
            'standard deviation': [input_3x3.std(axis=0).tolist(), input_3x3.std(axis=1).tolist(), input_3x3.std()],
            'max': [input_3x3.max(axis=0).tolist(), input_3x3.max(axis=1).tolist(), input_3x3.max()],
            'min': [input_3x3.min(axis=0).tolist(), input_3x3.min(axis=1).tolist(), input_3x3.min()],
            'sum': [input_3x3.sum(axis=0).tolist(), input_3x3.sum(axis=1).tolist(), input_3x3.sum()]
            }

    return calculations
