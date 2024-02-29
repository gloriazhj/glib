import numpy as np

def ket2des(ket: np.ndarray) -> np.ndarray:
    x = 2*abs(ket[0])*abs(ket[1])*np.cos(np.angle(ket[1]/ket[0]))
    y = 2*abs(ket[0])*abs(ket[1])*np.sin(np.angle(ket[1]/het[0]))
    z = 2*abs(ket[0])**2-1
    return np.array([x, y, z])

