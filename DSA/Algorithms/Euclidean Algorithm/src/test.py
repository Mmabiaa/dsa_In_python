

import main


def test():
    x, y = 252, 356
    obj = main.euclidean_algorithm(252, 356)
    gcd = obj.GCD()
    print('GCD = ', gcd)

test()
