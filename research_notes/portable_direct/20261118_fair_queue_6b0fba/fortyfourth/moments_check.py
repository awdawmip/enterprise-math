"""Independent positive Beta integrals and exact rational Sturm checks; no input from trace programs."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import cache
from itertools import product
from math import comb, factorial, prod
import json


@cache
def beta(a, b):
    """B(a,b) for rational a>0 and integral b>=1."""
    assert a>0 and b>=1
    return Q(factorial(b-1),1)/prod(a+j for j in range(b))


def moment_positive(m,r,j):
    # Coefficients of (1+t+...+t^(m-1))^j.
    c=[1]
    for _ in range(j):
        out=[0]*(len(c)+m-1)
        for i,v in enumerate(c):
            for k in range(m):
                out[i+k]+=v
        c=out
    return sum(v*beta(m*r+1+i,m+j) for i,v in enumerate(c))


def moment_difference(m,r,j):
    return sum((-1)**k*comb(j,k)*beta(m*(r+k)+1,m) for k in range(j+1))


def determinant(a):
    a=[row[:] for row in a]
    det=Q(1)
    for i in range(len(a)):
        j=next((j for j in range(i,len(a)) if a[j][i]),None)
        if j is None:
            return Q(0)
        if i!=j:
            a[i],a[j]=a[j],a[i]
            det=-det
        pivot=a[i][i]; det*=pivot
        for j in range(i+1,len(a)):
            ratio=a[j][i]/pivot
            for k in range(i+1,len(a)):
                a[j][k]-=ratio*a[i][k]
    return det


def ordered_positive(m,r,n,s):
    """Independent direct ordered n-fold integral. Accumulate Bernstein monomials by exponent tuple."""
    zero=(0,)*n
    poly={zero:1}; degrees=[0]*n; powers=[(i+1)*m*r+i for i in range(n)]
    def times_complement(i,j,d):
        # 1-(z_i ... z_j)^d in a multi-degree (d,...,d) nonnegative basis.
        terms=[]
        for exp in product(range(d+1),repeat=j-i+1):
            if all(e==d for e in exp):
                continue
            full=(0,)*i+exp+(0,)*(n-j-1)
            terms.append((full,prod(comb(d,e) for e in exp)))
        out=defaultdict(int)
        for a,v in poly.items():
            for b,c in terms:
                out[tuple(x+y for x,y in zip(a,b))]+=v*c
        for k in range(i,j+1):
            degrees[k]+=d
        return out
    for i in range(n):
        for _ in range(m-1):
            poly=times_complement(i,n-1,1)
        for _ in range(s):
            poly=times_complement(i,n-1,m)
        for j in range(i+1,n):
            # (t_j^m-t_i^m)^2 = t_j^(2m) (1-(z_i...z_{j-1})^m)^2
            for h in range(j,n):
                powers[h]+=2*m
            for _ in range(2):
                poly=times_complement(i,j-1,m)
    value=sum(v*prod(beta(a+p+1,d-a+1) for a,p,d in zip(exp,powers,degrees))
              for exp,v in poly.items())
    return value, len(poly)


def poly_trim(p):
    while p and p[-1]==0:p.pop()
    return p


def sturm(poly):
    seq=[poly,[k*v for k,v in enumerate(poly)][1:]]
    while len(seq[-1])>1:
        rem=seq[-2][:]
        divisor=seq[-1]
        while len(rem)>=len(divisor):
            d=len(rem)-len(divisor)
            c=rem[-1]/divisor[-1]
            for k,v in enumerate(divisor):
                rem[d+k]-=c*v
            poly_trim(rem)
        assert rem
        seq.append([-v for v in rem])
    return seq


def values(seq,x):
    signs=[]
    for p in seq:
        y=0
        for a in reversed(p):y=y*x+a
        if y:signs.append(1 if y>0 else -1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def roots(poly,upper):
    seq=sturm(poly); bottom=values(seq,0)
    assert bottom-values(seq,upper)==len(poly)-1
    out=[]
    for rank in range(1,len(poly)):
        lo=Q(0);hi=Q(upper)
        for _ in range(72):
            mid=(lo+hi)/2
            if bottom-values(seq,mid)>=rank:hi=mid
            else:lo=mid
        out.append((lo+hi)/2)
    return out


def orthogonal(mu,n):
    H=[mu[i:i+n] for i in range(n)]
    den=determinant(H)
    coeff=[]
    for j in range(n):
        mat=[row[:] for row in H]
        for i in range(n):mat[i][j]=-mu[n+i]
        coeff.append(determinant(mat)/den)
    return coeff+[Q(1)]


def spectral(m,s,n):
    lam=m+s
    L=orthogonal([Q(factorial(lam+j-1)) for j in range(2*n)],n)
    ref=roots(L,4*n+2*lam+4)
    rows=[]
    for r in (128,512,2048):
        mu=[r**j*moment_positive(m,Q(r),s+j) for j in range(2*n)]
        scaled=roots(orthogonal(mu,n),r)
        first=[-v*(v+2*n+s+Q(1,m))/2 for v in ref]
        residual=[r*r*(x-y-c/r) for x,y,c in zip(scaled,ref,first)]
        # Bounds are Jacobi nodes on [0,1], rescaled by r.
        b=Q(r)+Q(1,m); d=Q((m-1)**2,2*m)
        def jacobi(rate):
            # B(lam+j,rate)=B(rate,lam+j).
            return roots(orthogonal([r**j*beta(rate,lam+j) for j in range(2*n)],n),r)
        lower=jacobi(b); upper=jacobi(b-d)
        assert all(a<=x<=z for a,x,z in zip(lower,scaled,upper))
        rows.append({'r':r,'scaled_nodes':[round(float(x),9) for x in scaled],
                     'scaled_second_order_residuals':[round(float(v),7) for v in residual],
                     'jacobi_upper_gaps_times_r2':[round(float(r*r*(z-x)),7) for x,z in zip(scaled,upper)]})
    gap_scale=Q((m-1)*(m*m-1),24*m*m)
    gap_limit=[gap_scale*v*(v+2*n+lam) for v in ref]
    return {'jacobi_upper_gap_limit':[round(float(v),7) for v in gap_limit],
            'm':m,'s':s,'n':n,'laguerre_nodes':[round(float(v),9) for v in ref],'runs':rows}


def jacobi_det(a,b,n):
    # Gamma factors combined into B(b+j,a+j) divided by (a+b+2j)_(n-1-j)
    return prod(Q(factorial(j))*beta(b+j,a+j)/prod(a+b+2*j+k for k in range(n-j-1))
                for j in range(n))


def test():
    checks=0
    for m in (1,2,3,7):
        for r in (Q(-1,2*m),Q(0),Q(1,3),Q(13),Q(301)):
            for j in range(10):
                assert moment_positive(m,r,j)==moment_difference(m,r,j)
                checks+=1
    positives=[]
    cases=[(1,Q(-1,2),4,1),(2,Q(1,3),3,1),(3,Q(-1,7),3,0),(7,Q(2,3),2,1)]
    for m,r,n,s in cases:
        h=determinant([[moment_difference(m,r,s+i+j) for j in range(n)] for i in range(n)])
        pos,terms=ordered_positive(m,r,n,s)
        bounds=jacobi_det(s+m,r+Q(1,m),n)
        assert h==pos and Q(1,m**(m*n))*bounds<=h<=Q(1,m**n)*bounds
        positives.append({'m':m,'r':str(r),'s':s,'n':n,'positive_terms':terms,'det':str(h)})
    jacobi=0
    for r in (Q(-1,3),Q(0),Q(11,5),Q(40)):
        for s in range(3):
            for n in range(1,6):
                ans=determinant([[moment_difference(1,r,s+i+j) for j in range(n)] for i in range(n)])
                assert ans==jacobi_det(1+s,1+r,n)
                jacobi+=1
    det_asym=[]
    for m,s,n in ((1,0,3),(3,2,3),(7,1,3)):
        lam=m+s; N=n*(n+lam-1)
        c=Q(prod(factorial(k)*factorial(lam+k-1) for k in range(n)),m**(m*n))
        b=-N*(2*n+s-1+Q(1,m))/2
        row=[]
        for r in (128,512,2048,8192):
            h=determinant([[moment_positive(m,Q(r),s+i+j) for j in range(n)] for i in range(n)])
            row.append([r,round(float(r*(h*r**N/c-1)),9)])
        det_asym.append({'m':m,'s':s,'n':n,'predicted_first_correction':str(b),'measured':row})
    return {'positive_vs_difference_moments':checks,'full_positive_determinant_examples':positives,
            'm1_exact_Selberg_tests':jacobi,'determinant_asymptotics':det_asym,
            'pencil_spectra':[spectral(1,0,3),spectral(3,2,3),spectral(7,1,3)]}


if __name__=='__main__':
    print(json.dumps(test(),sort_keys=True,indent=2))
