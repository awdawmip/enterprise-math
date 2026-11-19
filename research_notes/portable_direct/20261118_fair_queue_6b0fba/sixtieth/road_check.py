"""Exact arithmetic and outward rational intervals; Python standard library."""
import json
from fractions import Fraction as F
from math import prod

S = 10**10


def factors(n):
    return [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1))]


def divisors(m):
    return [d for d in range(1,m+1) if m%d==0]


def mu(m):
    ps=factors(m)
    return (-1)**len(ps) if prod(ps)==m else 0


def weights(m):
    return [(d,d*mu(m//d)) for d in divisors(m)]


def table(m):
    w=weights(m)
    return [sum(c*(n//d) for d,c in w) for n in range(m)]


def rank(rows):
    mat=[list(map(F,row)) for row in rows]
    k=0
    for j in range(len(rows[0])):
        idx=next((i for i in range(k,len(mat)) if mat[i][j]),None)
        if idx is None: continue
        mat[idx],mat[k]=mat[k],mat[idx]
        a=mat[k][j]
        for i in range(k+1,len(mat)):
            c=mat[i][j]/a
            if c: mat[i]=[u-c*v for u,v in zip(mat[i],mat[k])]
        k+=1
        if k==len(mat):break
    return k


def rounded(a,b):
    return a*S//b,-((-a*S)//b)


def big_m_gap(m,p,q,H):
    # sqrt(pq)*(continuous minus discrete). Integral cell products are constant.
    a=table(m);ap=table(m*p);aq=table(m*q);bound=max(map(abs,a))**2
    lower=upper=0
    for n in range(1,H+1):
        u,v=a[n//p%m],a[n//q%m]
        x,y=ap[n%(m*p)],aq[n%(m*q)]
        assert x==p*u-a[n%m] and y==q*v-a[n%m]
        lo,hi=rounded(p*q*u*v*n-x*y*(n+1),n*n*(n+1))
        lower+=lo; upper+=hi
    error=bound*(F(p*q,2*H*H)+F(p+q+1,H))
    lo,hi=F(lower,S)-error,F(upper,S)+error
    assert -8*bound<lo<=hi<8*bound
    return [str(lo),str(hi)]


def base_gap(p,q,H,sub=16):
    # Monotone integrand in each unit cell: composite left/right rules.
    lo=hi=S
    for n in range(p,H+1):
        a,b=n%p,n%q
        for j in range(sub+1):
            v=(sub*a+j)*(sub*b+j)*n*n-a*b*(sub*n+j)**2
            L,U=rounded(v,sub*(sub*n+j)**2*n*n)
            if j<sub:lo+=L
            if j:hi+=U
    return [str(F(lo,S)),str(F(hi,S)+F(p+q,2*H))]


def B2(x):
    u=x%1
    return u*u-u+F(1,6)


def primitive(m,x):
    return -sum(F(d*d*mu(m//d),2)*B2(x/d) for d in divisors(m))


def B_integer_over_zeta(m,k):
    # Only used when the periodic coefficients depend on gcd(n,m).
    def weight(n):
        c=sum(v for d,v in weights(m) if n%d==0)
        return -c*primitive(m,F(k*n))
    w={d:sum(mu(d//e)*weight(e) for e in divisors(d)) for d in divisors(m)}
    for n in range(1,2*m+1):
        assert weight(n)==sum(v for d,v in w.items() if n%d==0)
    return sum(w[d]/(d*d) for d in w)


def main():
    ps=[11,17,23,31,43]
    total=0;rank_samples={}
    for m in [1,2,3,6,10]:
        tabs=[table(m*p) for p in ps]
        rows=[[t[n%len(t)] for t in tabs] for n in range(1,46)]
        for H in range(1,46):
            observed=rank(rows[:H])
            assert observed==min(len(ps),1+sum(p<=H for p in ps))
            total+=1
        rank_samples[str(m)]=[rank(rows[:H]) for H in (1,11,17,23,31)]
    filter_values=0
    for m in (2,3,6,10,15,30):
        a=table(m)
        for j in range(440):
            x=F(j,7)
            assert -sum(v*((x/d)%1) for d,v in weights(m))==a[int(x)%m]
            filter_values+=1
    far={str(k):str(B_integer_over_zeta(6,k)) for k in (0,3)}
    assert far=={"0":"2/3","3":"-4/3"}
    gaps={str((m,p,q)):big_m_gap(m,p,q,8000) for m in (2,3,6) for p,q in [(11,17),(11,101)]}
    base={str((p,q)):base_gap(p,q,10000) for p,q in [(11,11),(11,101),(11,1009)]}
    # dyadic Zak proof: broad rational estimates (1/sqrt(2)<71/100<3/4).
    assert 71**2>5000 and F(1,1+F(71,100))-F(1,16)>F(1,2)
    delta=F(1,2**16)
    assert delta/(8*(1+delta)**2)>F(1,2**20)
    print(json.dumps(dict(finite_prefix_rank_cases=total,rank_at_bounds_1_11_17_23_31=rank_samples,
          exact_fractional_part_filter_evaluations=filter_values,
          scaled_gap_sqrt_pq_continuous_minus_discrete=gaps,base_gap_intervals=base,
          base_gap_tail="(p+q)/(2H), H=10000, 16 monotone subcells",
          far_periodic_coefficient_m6_divided_by_zeta2=far,dyadic_continuous_lower_bound=">2^-20"),
          ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
