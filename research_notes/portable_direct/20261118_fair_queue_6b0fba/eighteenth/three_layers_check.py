"""Signed AP Cauchy cofactor, primitive Sturm certificates and three-layer dual.
Run with standard Python 3. No source checkout or numerical eigenvalues needed.
"""
from fractions import Fraction as F
from functools import cache
from math import comb, factorial, gcd, lcm, prod
import json


def trim(p):
    while p and p[-1]==0:
        p.pop()
    return p


def primitive(p):
    p=trim(list(p))
    if not p:
        return []
    d=lcm(*(F(x).denominator for x in p))
    a=[int(x*d) for x in p]
    c=gcd(*a)
    return [x//c for x in a]


def determinant(a):
    """Exact, signed Bareiss elimination with positive row-content removal."""
    rows=[]
    multiplier=1
    for row in a:
        den=lcm(*(F(x).denominator for x in row))
        nums=[int(x*den) for x in row]
        common=gcd(*nums) or 1
        rows.append([v//common for v in nums])
        multiplier*=F(common,den)
    previous=1
    n=len(rows)
    for k in range(n-1):
        if not rows[k][k]:
            pivot=next((i for i in range(k+1,n) if rows[i][k]),None)
            if pivot is None:
                return F(0)
            rows[k],rows[pivot]=rows[pivot],rows[k]
            multiplier=-multiplier
        pivot=rows[k][k]
        for i in range(k+1,n):
            left=rows[i][k]
            for j in range(k+1,n):
                value=rows[i][j]*pivot-left*rows[k][j]
                rows[i][j],remainder=divmod(value,previous)
                assert not remainder
        previous=pivot
    return multiplier*rows[-1][-1]


@cache
def unit_layer(m,s):
    n=m-1
    w=[(-1)**i*comb(n,i) for i in range(m)]
    H=[[F(w[i]*w[j],1+i+m*j+s*m*m) for j in range(m)] for i in range(m)]
    A=[[F(0)]*(2*m-1) for _ in range(2*m-1)]
    for i in range(m):
        A[i][i]=sum(H[i])
        for j in range(m-1):
            A[m+j][m+j]+=H[i][j]
            A[i][m+j]=A[m+j][i]=-H[i][j]
    return A


def cofactor(m,coeffs):
    layers=[(F(c),unit_layer(m,s)) for s,c in coeffs if c]
    d=2*m-1
    return determinant([[sum(c*a[i][j] for c,a in layers) for j in range(d)] for i in range(d)])


def weights(m,s,t):
    return [(s+i,(-1)**i*comb(m-1,s+i)*t**i) for i in range(3)]


def interpolate(fn,degree):
    vals=[F(fn(i)) for i in range(degree+1)]
    a=[F(0)]*(degree+1)
    fall=[1]
    for j in range(degree+1):
        c=vals[0]/factorial(j)
        for k,v in enumerate(fall):
            a[k]+=c*v
        vals=[v-u for u,v in zip(vals,vals[1:])]
        fall=[x-y*j for x,y in zip([0]+fall,fall+[0])]
    return trim(a)


def evaluate(p,x):
    y=0
    for v in reversed(p):
        y=y*x+v
    return y


def sturm(p):
    p=primitive(p)
    polys=[p,primitive([i*v for i,v in enumerate(p)][1:])]
    while True:
        a,b=polys[-2:]
        r=a[:]
        while r and len(r)>=len(b):
            lc=r[-1]
            delta=len(r)-len(b)
            sign=(b[-1]>0)-(b[-1]<0)
            r=[abs(b[-1])*v for v in r]
            for j,v in enumerate(b):
                r[j+delta]-=sign*lc*v
            r=primitive(r)
        if not r:
            return polys
        polys.append([-v for v in r])


def variations(seq,x):
    vals=[evaluate(p,x) for p in seq]
    signs=[(v>0)-(v<0) for v in vals if v]
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def roots_on_unit(p):
    seq=sturm(p)
    assert p[0] and evaluate(p,1)
    def intervals(a,b,va,vb):
        if va==vb:
            return []
        if va-vb==1 and b-a<=F(1,1<<15):
            return [[str(a),str(b)]]
        mid=(a+b)/2
        assert evaluate(p,mid)
        vm=variations(seq,mid)
        return intervals(a,mid,va,vm)+intervals(mid,b,vm,vb)
    v0,v1=variations(seq,F(0)),variations(seq,F(1))
    return {'V0':v0,'V1':v1,'count':v0-v1,'globally_squarefree':len(seq[-1])==1,
            'isolating_intervals':intervals(F(0),F(1),v0,v1)}


def triple(m,s):
    n=m-1
    coeff=interpolate(lambda t:cofactor(m,weights(m,s,t)),2*(2*m-1))
    assert coeff[:n]==[0]*n and len(coeff)==3*m
    red=primitive(coeff[n:])
    for t in (F(1,7),F(4,7)):
        assert evaluate(coeff,t)==cofactor(m,weights(m,s,t))
    data=roots_on_unit(red)
    d=len(red)-1
    mobius=[sum(red[i]*comb(d-i,j-i) for i in range(j+1)) for j in range(d+1)]
    assert all(mobius)
    signs=''.join('+' if x>0 else '-' for x in mobius)
    assert sum(a!=b for a,b in zip(signs,signs[1:]))==data['count']
    return {'m':m,'s':s,'degree_after_t_power':d,'primitive_ascending':red,
            'mobius_signs_low_to_high':signs,'sign_at_one':signed(evaluate(red,1)),**data}


def full(m):
    n=m-1
    coeff=interpolate(lambda t:cofactor(m,[(s,(-1)**s*comb(n,s)*t**s) for s in range(m)]),
                      n*(2*m-1))
    assert coeff[:n]==[0]*n
    q=primitive(coeff[n:])
    D=len(q)-1
    beta=[sum(q[i]*comb(D-i,k-i) for i in range(k+1)) for k in range(D+1)]
    assert all(v>0 for v in beta)
    return {'m':m,'mobius_positive_count':len(beta),'degree':D,'positive_at_one':sum(q)>0}


def signed(x):
    return (x>0)-(x<0)


def tail_path(m,t):
    n=m-1
    def term(u):
        return [(s,(-1)**s*comb(n,s)*t**s*(1 if s<3 else u)) for s in range(m)]
    coeff=interpolate(lambda u:cofactor(m,term(u)),2*m-1)
    assert evaluate(coeff,F(1,3))==cofactor(m,term(F(1,3)))
    q=primitive(coeff)
    return {'m':m,'t':str(t),'first_three_sign':signed(q[0]),
            'all_layers_sign':signed(sum(q)),'primitive_ascending':q,**roots_on_unit(q)}


def gram(x,z):
    return [[sum(a*b for a,b in zip(i,j)) for j in zip(*z)] for i in zip(*x)]


def dual_check(m,s,t):
    n=m-1
    b=m*m
    w=[(-1)**i*comb(n,i) for i in range(m)]
    T=[[prod(F(i+b-k,j-k) for k in range(m) if k!=j) for j in range(m)] for i in range(m)]
    X,Z,D=[],[],[]
    for l,c in weights(m,s,t):
        for i in range(m):
            h=[F(w[j],1+i+m*j+b*l) for j in range(m)]
            e=sum(h)
            X.append([int(i==j) for j in range(m)]+[-v/e for v in h[:-1]])
            D.append(c*w[i]*e)
            d=[int(i==j) for j in range(m)]
            col=[row[i] for row in T]
            if l==s: zr=col+[-w[i]]
            elif l==s+1: zr=[-a-bb for a,bb in zip(d,col)]+[w[i]]
            else: zr=d+[0]
            Z.append(zr)
    assert not any(v for row in gram(X,Z) for v in row)
    norm_ratio=determinant(gram(X,X))/determinant(gram(Z,Z))
    assert norm_ratio>0
    Q=gram(Z,[[t*t*v/d for v in row] for row,d in zip(Z,D)])
    dual=norm_ratio*prod(D)*determinant(Q)/t**(2*(m+1))
    primal=cofactor(m,weights(m,s,t))
    assert primal==dual
    return {'m':m,'s':s,'t':str(t),'primal_and_dual_sign':signed(dual)}


def main():
    regimes=[(3,0),(4,0),(4,1),(5,0),(5,1),(5,2),(6,0),(8,0),(10,0)]
    three=[triple(m,s) for m,s in regimes]
    critical=[F(57,100),F(4,7)]
    selected=[signed(cofactor(6,weights(6,0,t))) for t in critical]
    assert selected==[1,-1]
    for t in critical:
        wc=weights(6,0,t)
        assert all(cofactor(6,[wc[i],wc[j]]) for i in range(3) for j in range(i+1,3))
    results={'three_consecutive_windows':three,'full_AP_Bernstein':[full(m) for m in (3,4,5,6)],
             'tail_restoration':[tail_path(5,F(1)),tail_path(6,F(4,7))],
             'm6_certified_bracket':[str(t) for t in critical],'bracket_signs':selected,
             'm6_first_pair_thresholds':['109/185','181/218'],
             'dual_checks':[dual_check(m,s,t) for m,s in [(3,0),(4,1),(5,0),(6,0)]
                            for t in (F(1,3),F(4,7),F(1))]}
    print(json.dumps(results,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
