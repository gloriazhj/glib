from sympy.physics.wigner import wigner_3j, wigner_6j, clebsch_gordan

def cg(j1, m1, j2, m2, J, M):
    """
    Inputs: j1, m1, j2, m2, J, M

    Returns <j1m1j2m2|JM>
    """
    return float(clebsch_gordan(j1, j2, J, m1, m2, M))

def w3j(j1, j2, j3, m1, m2, m3):
    return float(wigner_3j(j1, j2, j3, m1, m2, m3))

def w6j(j1, j2, j3, j4, j5, j6):
    return float(wigner_6j(j1, j2, j3, j4, j5, j6))
