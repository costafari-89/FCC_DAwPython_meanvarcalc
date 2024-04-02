import numpy as np

def calculate(list):
    input_array = np.array(list)

    try:
        input_3x3 = input_array.reshape(3,3)
    
    except ValueError:
        print("List must contain nine numbers.")

    else:
        calculations = {
            'mean': [axis1, axis2, flattened],
            'variance': [axis1, axis2, flattened],
            'standard deviation': [axis1, axis2, flattened],
            'max': [axis1, axis2, flattened],
            'min': [axis1, axis2, flattened],
            'sum': [axis1, axis2, flattened]
            }





    return calculations
