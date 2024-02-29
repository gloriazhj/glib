mu_B = 1.4 # MHz/G

def Lande_gJ(l, s, j):
    try:
        return 1+(j*(j+1)+s*(s+1)-l*(l+1))/(2*j*(j+1))
    except ZeroDivisionError:
        return 0

def Lande_gF(L, S, J, I, F):
    """
    Return Lande g-factor of a hyperfine state ^(2S+1)L_J, I, F
    """
    gJ = Lande_gJ(L, S, J)
    try:
        return gJ*(F*(F+1)-I*(I+1)+J*(J+1))/(2*F*(F+1))
    except ZeroDivisionError:
        return 0
