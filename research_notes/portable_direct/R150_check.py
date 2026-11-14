#!/usr/bin/env python3
"""R150 exact lag-difference/inversion checks: only integer arithmetic/Fraction."""
from fractions import Fraction as Q
from math import gcd, lcm
from random import Random
from json import dump

def units(n):
    return [s for s in range(n) if gcd(s,n)==1] if n>1 else [0]

def gamma(n,s,u,m,t,v):
    g=gcd(n,m)
    A=[2*((s*j+u)%g)-(g-1) for j in range(g)]
    B=[2*((t*j+v)%g)-(g-1) for j in range(g)]
    return [Q(sum(A[j]*B[(j+h)%g] for j in range(g)),4*g*n*m) for h in range(g)]

def check(n,s,u,m,t,v,independent_full_period=False):
    g=gcd(n,m)
    assert gcd(s,n)==1 and gcd(t,m)==1
    F=gamma(n,s,u,m,t,v)
    ell=pow(s,-1,g) if g>1 else 0
    jstar=(-u*ell)%g if g>1 else 0
    q=Q(g-1,2)
    jumps=[F[(h+ell)%g]-F[h] for h in range(g)]
    B=[((t*(jstar+h)+v)%g)-q for h in range(g)]
    assert all(jumps[h]==B[h]/(n*m) for h in range(g))
    assert sorted(n*m*d for d in jumps)==[Q(j)-q for j in range(g)]
    assert sum(d*d for d in jumps)==Q(g*(g*g-1),12*n*n*m*m)
    assert sum(F)==0
    p=Q(0)
    cumul=[]
    locations=[]
    for i in range(g):
        h=(i*ell)%g if g>1 else 0
        locations.append(h)
        cumul.append(p)
        p += B[h]/(n*m)
    assert p==0
    baseline=sum(cumul)/g
    assert all(F[locations[i]]==cumul[i]-baseline for i in range(g))
    if g>1:
        recovered=[n*m*(F[(h+ell)%g]-F[h])+q for h in range(g)]
        assert all(int(x)==x and 0<=x<g for x in recovered)
        vrec=int(recovered[(-jstar)%g])
        trec=(int(recovered[(1-jstar)%g])-vrec)%g
        assert vrec==v%g and trec==t%g
    if independent_full_period:
        P=lcm(n,m)
        ar=[Q((s*k+u)%n,n) for k in range(P)]
        br=[Q((t*k+v)%m,m) for k in range(P)]
        meanA=Q(n-1,2*n); meanB=Q(m-1,2*m)
        for h in range(g):
            actual=sum((ar[k]-meanA)*(br[(k+h)%P]-meanB) for k in range(P))/P
            assert actual==F[h]
    return F

def main():
    tested=0; independent=0; example={}
    for g in range(1,13):
        for s in units(g):
            for t in units(g):
                for u in range(g):
                    for v in range(g):
                        check(g,s,u,g,t,v)
                        tested+=1
    rng=Random(150)
    for _ in range(1200):
        n=rng.randint(1,24);m=rng.randint(1,24)
        s=rng.choice(units(n));t=rng.choice(units(m))
        u=rng.randint(-200,200);v=rng.randint(-200,200)
        check(n,s,u,m,t,v,independent_full_period=True)
        independent+=1
    for name,params in [('w_r2_00100100',(4,1,-2,8,-3,0)),('w_r4_00001000010000',(6,1,-2,14,-3,0)),('zero_lag_example',(5,1,0,5,1,1))]:
        n,s,u,m,t,v=params
        F=check(n,s,u,m,t,v,True)
        ell=pow(s,-1,gcd(n,m))
        example[name]={'g':gcd(n,m),'ell':ell,'lag_covariance':[str(x) for x in F], 'lag_derivatives':[str(F[(i+ell)%len(F)]-F[i]) for i in range(len(F))]}
    out={'marker':'R150_EXACT_LAG_DERIVATIVE_INVERSE_PASS','exhaustive_g_range':'1..12','exhaustive_cases':tested,'independent_full_period_cases':independent,'total_cases':tested+independent+len(example),'arithmetic':'Python integers and fractions, exact; no floats','examples':example}
    with open('R150_verification.json','w',encoding='utf-8') as f:dump(out,f,indent=2,ensure_ascii=False)
    print(out)

if __name__=='__main__': main()
