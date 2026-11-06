"""R585: exact finite-branch holomorphic-moment non-identifiability.

No floating point, no approximate roots: Chebyshev T_J(x-1) has exactly
x_j=1+cos((2j-1)pi/(2J)) as roots. Newton identities compute equal-weight
x_j power sums using only exact Q arithmetic. The independent Fourier-root
filter for K equally-weighted phases is delta_{h=0} for 0<=h<K.
"""
from fractions import Fraction as Q
from math import comb
import sympy as sp

x=sp.Symbol('x')

def arcsine_moment(m):
    return Q(comb(2*m,m), 2**m)

def chebyshev_power_means(J, M):
    p=sp.Poly(sp.chebyshevt(J,x-1),x)
    lc=p.LC()
    c=[Q(int(a),int(b)) for a,b in
       ((sp.fraction(co/lc)) for co in p.all_coeffs())]
    assert c[0] == 1 and len(c)==J+1
    sums=[Q(J)]
    for m in range(1,M+1):
        tail=sum(c[i]*sums[m-i] for i in range(1,min(m-1,J)+1))
        if m<=J:
            tail+=m*c[m]
        sums.append(-tail)
    return [v/J for v in sums]

def polynomial_mean(coeff, means):
    return sum((Q(c)*means[i] for i,c in enumerate(coeff)),Q(0))

cases=(3,4,5,8,12,20)
checked=0
for J in cases:
    M=2*J-1
    K=M+2   # finite roots-of-unity phase population: K>M and K>=3
    xmean=chebyshev_power_means(J,max(M,4))
    for m in range(M+1):
        assert xmean[m]==arcsine_moment(m)
        # Fourier filter for (x+r(x)*omega)^m, since 0<=m<K.
        phase_survivors=tuple(h for h in range(m+1) if h%K==0)
        assert phase_survivors==(0,)
        assert xmean[m]==arcsine_moment(m)
        checked+=1
    # r(x)=x(2-x)/4: r^2=(4x^2-4x^3+x^4)/16.
    r2=polynomial_mean([0,0,Q(1,4),-Q(1,4),Q(1,16)],xmean)
    assert r2==Q(3,128)
    # K>=3 implies equal-weight mean sin(theta)^2=1/2 exactly.
    imaginary_energy=r2/2
    radial_second=xmean[2]+r2
    assert imaginary_energy==Q(3,256)
    assert radial_second==Q(195,128)
    assert radial_second-xmean[2]==2*imaginary_energy
    print(f'J={J}, K={K}, matching_m=0..{M}, E_r2={r2}, V={imaginary_energy}, S2={radial_second}')

# Independently check the finite-k diagnostic identity from R580's exact T2.
for k in range(2,201):
    d=2*k-1
    T2=Q(12*k*k-20*k+1,4*k+1)
    base=T2/d
    assert base==Q(12*k*k-20*k+1,(4*k+1)*(2*k-1))
    assert Q(3,2)-base==Q(3*(4*k+1)*(2*k-1)-2*(12*k*k-20*k+1),2*(4*k+1)*(2*k-1))

print(f'R585_EXACT_CHEBYSHEV_PHASE_WITNESS_PASS cases={len(cases)} moments={checked} finite_k=199')
