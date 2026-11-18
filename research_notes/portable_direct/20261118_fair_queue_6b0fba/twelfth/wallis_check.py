"""Independent exact regressions for the T5 dyadic filters, moment brackets and RG jets."""
import json
from fractions import Fraction as F
from math import comb, factorial, prod
from wallis_t5 import (dyadic_annihilation_weights, high_order_spectral_certificate,
                       phase_moment_fractions, phase_moments)


def coeff_product(a,b,n=None):
    m=len(a)+len(b)-1 if n is None else n+1
    return [sum((a[i]*b[j-i] for i in range(max(0,j-len(b)+1),min(j,len(a)-1)+1)),F(0))
            for j in range(m)]


def eval_poly(p,x):
    return sum((c*x**i for i,c in enumerate(p)),F(0))


def filters():
    out=[]
    for order in range(17):
        w=dyadic_annihilation_weights(order)
        assert sum(w)==1 and sum(map(abs,w))==prod(F(4**r+1,4**r-1) for r in range(1,order+1))<2
        for k in range(1,order+4):
            response=sum(c*F(1,4**(j*k)) for j,c in enumerate(w))
            target=prod(((4**r)*F(1,4**k)-1)/(4**r-1) for r in range(1,order+1))
            assert response==target
            assert (response==0)==(k<=order)
        if order in (0,1,2,4,8,16):
            out.append([order,str(sum(map(abs,w)))])
    return out


def quadratures():
    out=[]
    for n in range(1,11):
        m=phase_moments(2*n+1)
        for k in range(2*n+1):
            c=F(2,(k+1)**2*comb(2*k+2,k+1))
            assert m[k]==4**k*c
        (a,b),(c,d)=phase_moment_fractions(n)
        lhs=coeff_product(b,c,2*n)
        rhs=coeff_product(a,d,2*n)
        difference=[v-w for v,w in zip(lhs,rhs)]
        assert difference[:-1]==[0]*(2*n) and difference[-1]>0
        # Independently expand integrals of the squared cardinal polynomials.
        p=list(reversed(b))
        sstar=[d[0]]
        for v in d[1:-1]:
            sstar.append(sstar[-1]+v)
        s=list(reversed(sstar))
        sq=coeff_product(s,s)
        residue_poly=[F(0)]+sq+[F(0)]
        for i,v in enumerate(sq):
            residue_poly[i+2]-=v
        kappa=sum(m[i]*(v+w) for i,(v,w) in enumerate(zip(coeff_product(p,p),residue_poly)))
        assert kappa==difference[-1] and kappa>0
        # Both resolvents agree with all 2n given moments.
        for num,den in ((a,b),(c,d)):
            series=[]
            for k in range(2*n):
                val=(num[k] if k<len(num) else 0)-sum(den[i]*series[k-i] for i in range(1,min(k,len(den)-1)+1))
                series.append(val)
            assert series==m[:2*n]
        z=F(1,2)
        lo,hi=eval_poly(a,z)/eval_poly(b,z),eval_poly(c,z)/eval_poly(d,z)
        assert hi-lo==kappa*z**(2*n)/(eval_poly(b,z)*eval_poly(d,z))
        if n in (1,2,3,5):
            out.append({"n":n,"K":str(kappa),"tau_squared_q2_exact":[str(8*lo),str(8*hi)]})
    return out


def rg_coefficients():
    tested=0
    for j in range(27):
        elementary=[F(1)]
        for k in range(1,j+1):
            elementary=coeff_product(elementary,[1,k*k])
        for ell in range(j+1):
            k=j+1-ell
            c=[F(2,(h+1)**2*comb(2*h+2,h+1)) for h in range(ell+1)]
            power=[F(1)]
            for _ in range(k):
                power=coeff_product(power,c,ell)
            phase=(j+1)*2*F((-1)**(k-1),factorial(2*k))*power[ell]
            central=F((-1)**(j+ell),factorial(2*j+1))*elementary[ell]
            assert central==phase
            tested+=1
    return tested


def certificates():
    out=[]
    for q in (2,4,16,64):
        previous=None
        for n in (1,2,3,4,5,8):
            c=high_order_spectral_certificate(q,n,bits=168)
            lo,hi=c.interval
            assert 0<lo<hi and c.moment_count==2*n
            if previous is not None:
                assert previous[0]<=lo and hi<=previous[1]
            previous=c.interval
            if n in (2,4,8):
                width=hi-lo
                bits=(width.denominator//width.numerator).bit_length()-1
                out.append([q,n,bits])
        for n in range(5):
            r=high_order_spectral_certificate(q,n,method="richardson",bits=168)
            assert max(r.interval[0],previous[0])<=min(r.interval[1],previous[1])
    return out


if __name__=="__main__":
    print(json.dumps({"filter_order_max":16,"filter_l1_samples":filters(),
                      "quadrature_order_max":10,"quadrature_samples":quadratures(),
                      "rg_independent_coefficient_count":rg_coefficients(),
                      "q_n_certified_absolute_bits":certificates(),
                      "frozen_tool_revision":"9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c",
                      "tool_family":"T5_PRECISION_REFINEMENT",
                      "subtool":"precision.spectral_decimation_completion"},indent=2))
