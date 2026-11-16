"""Exact rational certificate for injectivity of three derivatives of the balanced center."""
from fractions import Fraction as F
from math import comb
import json
import ray_certificate as rc

# All operations through order three use exact rational arithmetic.
def center_jet(s,t):
    rc.N=4
    a=rc.block_s((1,2),(s,2),5)
    b=rc.block_s((s,2),(t,2),3)
    W=rc.div_s(rc.rising_s(t,4,3),840)
    def col(j):
        p=rc.div_s(1,rc.add_s(1,rc.mult_s(j,W)))
        return rc.div_s(rc.add_s(1, rc.mult_s(b,p)),
                        rc.add_s(rc.add_s(1,a),rc.mult_s(b,p)))
    return rc.div_s(col(F(1,2)),col(5))


def solve(M,Y):
    rows=[list(map(F,x))+[F(y)] for x,y in zip(M,Y)]
    n=len(rows)
    for i in range(n):
        pivot=next(j for j in range(i,n) if rows[j][i])
        rows[i],rows[pivot]=rows[pivot],rows[i]
        rows[i]=[x/rows[i][i] for x in rows[i]]
        for j in range(n):
            if j!=i:
                k=rows[j][i]
                rows[j]=[x-k*y for x,y in zip(rows[j],rows[i])]
    return [row[-1] for row in rows]


def certificate():
    indices=[(i,k-i) for k in range(4) for i in range(k+1)]
    M=[[s**i*t**j for i,j in indices] for s,t in indices]
    Y=[center_jet(s,t) for s,t in indices]
    coeffs=[dict(zip(indices,solve(M,[p[d] for p in Y]))) for d in range(4)]
    assert all(not c or i+j<=d for d,poly in enumerate(coeffs) for (i,j),c in poly.items())
    A,B=(coeffs[1][q] for q in ((1,0),(0,1)))
    assert A < 0 and B < 0
    def on_line(d,L):
        # Return s-polynomial of jet coefficient with t=(L-A*s)/B.
        S=[F(0)]*(d+1)
        for (i,j),g in coeffs[d].items():
            if not g:continue
            for k in range(j+1):
                S[i+k]+=g*comb(j,k)*L**(j-k)*(-A)**k/B**j
        return S
    def data(L):
        t0,t1,t2=on_line(2,L)
        p0,p1,p2,p3=on_line(3,L)
        assert t2 and p3
        K=-t1/t2
        P=K*K+(p2*K+p1)/p3
        return K,K*K-4*P
    k0,d0=data(F(0))
    k1,d1=data(F(1))
    km,dm=data(F(-1))
    ks=k1-k0
    assert -ks==km-k0
    da,db=(d1+dm)/2-d0,(d1-dm)/2
    threshold=(2-k0)/ks
    dd=da*threshold**2+db*threshold+d0
    assert ks<0 and threshold<0 and da>0 and dd<0 and d0<0
    assert data(threshold)[1]==dd
    # Coarse, strictly rational, human-readable certificates.
    assert F(999,1000)<k0<1 and -2249<ks<-2246
    assert 13_649_000<da<13_651_000 and 2895<db<2896 and -8<d0<-7
    assert F(-5,10000)<threshold<F(-4,10000) and -7<dd<-5
    return dict(jet_order=3,anchor=[2,2,2],line_A=str(A),line_B=str(B),
                K_intercept=str(k0),K_slope=str(ks),
                discriminant_coefficients=[str(da),str(db),str(d0)],
                endpoint_L=str(threshold),discriminant_at_endpoint=str(dd),
                rational_center_degrees_per_ray=42,comparison_degree_bound=84)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
