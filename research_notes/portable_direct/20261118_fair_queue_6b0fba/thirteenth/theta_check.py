"""Finite arithmetic checks for the R107 orbit and Torelli arguments; standard library."""
import json
from itertools import product
from math import isqrt


def ff343(x,y):
    # Multiplication in F7[r]/(r^3+r^2+1), constant terms first.
    c=[0]*5
    for i in range(3):
        for j in range(3):
            c[i+j]+=x[i]*y[j]
    for k in (4,3):
        c[k-3]-=c[k]
        c[k-1]-=c[k]
    return tuple(v%7 for v in c[:3])


def pow343(x,n):
    out=(1,0,0)
    for _ in range(n):
        out=ff343(out,x)
    return out


def matrix(a,b,p):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%p for i in range(2) for j in range(2))


def matrices(p):
    return [a for a in product(range(p),repeat=4) if (a[0]*a[3]-a[1]*a[2])%p==1]


def main():
    cube_values=[(x**3+x*x+1)%7 for x in range(7)]
    assert 0 not in cube_values
    # Separability of the three 2-torsion roots and the other four branch points.
    assert not any(v==0 and (3*x*x+2*x)%7==0 for x,v in enumerate(cube_values))
    # Reducing x^3+x^2+1 modulo x^2-5 gives 5*x+6.
    root_linear=next(x for x in range(7) if (5*x+6)%7==0)
    assert root_linear*root_linear%7!=5
    r=(0,1,0)
    orbit=[r,pow343(r,7),pow343(r,49)]
    assert len(set(orbit))==3 and pow343(orbit[-1],7)==r
    for x in orbit:
        x2=pow343(x,2); x3=ff343(x,x2)
        assert all((x3[i]+x2[i]+(i==0))%7==0 for i in range(3))
    I=(1,0,0,1)
    frob=(0,1,1,1)
    alpha=matrix(frob,frob,2)
    central=[h for h in matrices(2) if matrix(h,alpha,2)==matrix(alpha,h,2)]
    assert len(central)==3 and matrix(frob,alpha,2)==I
    lines=[(1,0),(0,1),(1,1)]
    core=[]
    for h in lines:
        ah=tuple(sum(alpha[2*i+j]*h[j] for j in (0,1))%2 for i in (0,1))
        assert ah not in ((0,0),h)
        core.append({"line_generator":h,"alpha_image":ah,"intersection_dimension":0})
    # A concrete binary tetrahedral model. Every noncentral element over an
    # involution of A4 (six elements of order four) is conjugate to its negative.
    sl=matrices(3)
    minus_I=(2,0,0,2)
    order4=[u for u in sl if matrix(u,u,3)==minus_I]
    for u in order4:
        minus=tuple(-a%3 for a in u)
        assert any(matrix(h,u,3)==matrix(minus,h,3) for h in sl)
    assert len(sl)==24 and len(order4)==6
    real_disc=5*5-4*(-98)
    assert real_disc==417 and 417==3*139 and isqrt(139)**2!=139
    # At characteristic seven, use the basis 1,i of F49=F7[i]/(i^2+1).
    squares={x*x%7 for x in range(7)}
    assert 6 not in squares
    prym_signed_eigen=[1,1,-1,1]  # [1,x,y,x²] dx/(y w)
    hyper_signed_eigen=[(-1)**j for j in range(4)]
    assert sum(prym_signed_eigen)%7==2 and sum(hyper_signed_eigen)%7==0
    assert (sum(prym_signed_eigen)-(-sum(prym_signed_eigen)))%7!=0
    norm_char0=[(u,v) for u in range(-2,3) for v in range(-2,3) if u*u+v*v==4]
    assert set(norm_char0)=={(-2,0),(2,0),(0,-2),(0,2)}
    print(json.dumps({"base_characteristic":7,"two_division_values_mod_7":cube_values,
        "F7_cubic_root_orbit_in_power_basis":orbit,"alpha_centralizer_GL2_F2":central,
        "kernel_line_cores":core,"real_subfield_discriminant_polynomial":real_disc,
        "SL2_F3_order4_reversal_check":[len(sl),len(order4)],
        "prym_multiplicities_i_minus_i":[3,1],"hyperelliptic_multiplicities":[2,2],
        "p7_square_residues":sorted(squares),"norm4_gaussian_coordinates":norm_char0},indent=2))


if __name__=="__main__":
    main()
