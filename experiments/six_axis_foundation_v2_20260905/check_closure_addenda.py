from fractions import Fraction
from itertools import product
from six_axis import ChartSignConnection, quadratic_extension
from closure_addenda import (
    triangle_products, is_fcc_orientation_connection, gauge_to_all_negative,
    quadratic_components, quadratic_spectral_extension, metric_eigenvalues,
)


def main():
    good=[]
    for signs in product((-1,1), repeat=6):
        c=ChartSignConnection(signs)
        if is_fcc_orientation_connection(c):
            good.append(signs)
            assert triangle_products(c)==(-1,-1,-1,-1)
            eps=gauge_to_all_negative(c)
            assert c.gauge(eps).signs==(-1,)*6
    assert len(good)==8
    assert [x for x in good if len(set(x))==1]==[(-1,)*6]

    samples=((0,0,0,0,0,0),(1,2,3,4,5,6),(10,0,7,2,9,3))
    for n in samples:
        plus,minus=quadratic_components(n)
        assert all(plus[i]+minus[i]==n[i] for i in range(6))
        for c in (Fraction(-3,4),Fraction(0),Fraction(2,5),Fraction(9,10)):
            assert quadratic_extension(n,c)==quadratic_spectral_extension(n,c)
            assert metric_eigenvalues(c)==((1+c,3),(1-c,3))
    print('PASS closure addenda: 64 sign connections exhausted; metric spectral identity exact')

if __name__=='__main__':
    main()
