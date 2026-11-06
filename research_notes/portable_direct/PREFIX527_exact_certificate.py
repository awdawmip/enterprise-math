#!/usr/bin/env python3
"""PREFIX-527 exact symbolic BRC--aAc joint renewal / extremal gate certificate.
Exact signed-X6 discrete combinatorics; no trigonometry or numerical physics.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict, Counter
from math import comb
import json
import sympy as sp

STARS=[(0,2,5),(0,3,4),(1,2,4),(1,3,5)]
def nearby(j,c):
    return [-(1 if c>0 else -1)*(a+1) for a in STARS[j] if a!=abs(c)-1]
def successor(s):
    j,p,c=s
    k=next(i for i,v in enumerate(STARS) if i!=j and abs(c)-1 in v)
    return [(j,c,v) for v in nearby(j,c) if v!=p]+[(k,c,v) for v in nearby(k,c)]
S=[(j,p,sign*(a+1)) for j in range(4) for a in STARS[j]
   for sign in (-1,1) for p in nearby(j,sign*(a+1))]
I={s:i for i,s in enumerate(S)}
NEXT=[[I[v] for v in successor(s)] for s in S]
T=I[(0,1,-3)]
assert len(S)==48 and all(len(a)==3 for a in NEXT) and T not in NEXT[T]
assert sum(T in z for z in NEXT)==3
sgn=lambda x:1 if x==1 else -1 if x==-1 else 0
q,u,z=sp.symbols('q u z')
P=[i for i,s in enumerate(S) if (s[2]>0)==(S[T][2]>0)]
pidx={i:j for j,i in enumerate(P)}
assert len(P)==24 and T in P
B=sp.zeros(24)
for s in P:
    for mid in NEXT[s]:
        for dst in NEXT[mid]:
            assert dst in P
            B[pidx[dst],pidx[s]] += q**(int(abs(S[mid][2])==1)+int(abs(S[dst][2])==1))
ix=pidx[T]
cp=sp.Poly(B.charpoly(z).as_expr(),z)
cp2=sp.Poly(B.minor_submatrix(ix,ix).charpoly(z).as_expr(),z)
def reciprocal(poly):
    return sp.Poly(sum(c*u**(poly.degree()-exp[0]) for exp,c in poly.terms()),u).as_expr()
D_full=sp.expand(reciprocal(cp))
N_cofactor=sp.expand(reciprocal(cp2))
assert sp.expand(D_full.subs(u,0))==1
assert sp.expand(N_cofactor.subs(u,0))==1
Kernel=sp.cancel((N_cofactor-D_full)/(4*D_full))
kn,kd=map(sp.expand,sp.fraction(Kernel))
D1=1+2*u-3*q*u**2
D2=1+(4+2*q)*u**2-(12*q+4*q**2)*u**3+9*q**2*u**4
D3=1-u-(12+30*q)*u**2-(36+126*q+36*q**2)*u**3-(324*q+243*q**2)*u**4-729*q**2*u**5
D=sp.expand(D1*D2*D3)
assert sp.degree(D,u)==11
assert sp.cancel(Kernel*D).is_polynomial(u,q)
assert sp.cancel(sp.denom(Kernel)/D).is_number
assert sp.gcd(kn,kd)==1
assert sp.gcd(kn,D)==1
assert sp.cancel(Kernel.subs(q,1) - ( (1-5*u-21*u**2-75*u**3-108*u**4)/(1-5*u-26*u**2-78*u**3-135*u**4+243*u**5)-1)/4)==0

loops=Counter({(T,0):1})
R={}
for m in range(0,15):
    if m%2==0 and m>=4:
        dist=Counter()
        for (i,k),n in loops.items():
            if i==T:
                assert k%2==0
                dist[k//2] += n*2**(m-2)
        R[m]=dict(sorted(dist.items()))
    nxt=Counter()
    for (i,k),n in loops.items():
        for j in NEXT[i]:
            nxt[(j,k+int(abs(S[i][2])==1)+int(abs(S[j][2])==1))]+=n
    loops=nxt
assert R[4]=={1:20} and R[6]=={1:288,2:160} and R[8]=={1:7168,2:11840}
Rrat=sp.factor(Kernel.subs(u,4*u))
rnum,rden=map(lambda x:sp.Poly(sp.expand(x),u),sp.fraction(sp.cancel(Rrat)))
rc={}
for m in range(0,8):
    val=sp.expand((rnum.nth(m)-sum(rden.nth(j)*rc[m-j] for j in range(1,m+1) if m-j in rc))/rden.nth(0))
    rc[m]=val
    if 2*m in R:
        assert sp.expand(val-sum(v*q**p for p,v in R[2*m].items()))==0
    else:
        assert m<2 and val==0 or (m==1 and val==0)

states={(i,i,2,0,0):1 for i in range(48)}
F={}
Hhist={}
for d in range(0,16):
    observed=defaultdict(int)
    moments={k:defaultdict(int) for k in range(1,5)}
    for (start,end,prev,K,hits),n in states.items():
        delta=sgn(S[end][2])-sgn(S[start][2])
        assert (K-abs(delta))%2==0 and K>=abs(delta)
        pair=(K-abs(delta))//2
        observed[(hits,pair)]+=n
        for k in moments:
            if hits>=k: moments[k][pair]+=n*comb(hits,k)
    Hhist[d]=dict(sorted(observed.items()))
    F[d]={k:dict(moments[k]) for k in moments}
    assert sum(observed.values())==48*6**d
    if d==15:break
    updated=defaultdict(int)
    for (start,end,prev,K,hits),n in states.items():
        for dst in NEXT[end]:
            nk=K+int(abs(S[end][2])==1)+int(abs(S[dst][2])==1)
            for branch in (0,1):
                h=hits+int(prev==0 and branch==0 and dst==T)
                updated[(start,dst,branch,nk,h)]+=n
    states=updated

def convolution(a,b,maxd):
    out={}
    for d1,ap in a.items():
        for d2,bp in b.items():
            d=d1+d2
            if d>maxd:continue
            dest=out.setdefault(d,Counter())
            for p,an in ap.items():
                for pp,bn in bp.items():dest[p+pp]+=an*bn
    return out
maxd=15
J={d:Counter(F[d][1]) for d in range(maxd+1)}
Rdict={m:Counter(x) for m,x in R.items() if m<=maxd}
powR={0:Counter({0:1})}
for k in range(1,5):
    pred=convolution(J,powR,maxd)
    for d in range(maxd+1):
        assert dict(pred.get(d,{}))==dict(F[d][k]) ,(d,k,pred.get(d,{}),F[d][k])
    powR=convolution(powR,Rdict,maxd)

primitive_checks=0
for i in range(48):
    frontier=[(i,i,(),(),0)]
    for d in range(5):
        for start,end,bs,word,hits in frontier:
            if d>=1:
                chars=['a' if k==1 else 'A' if k==-1 else 'c' if abs(k)==3 else '_' for k in word]
                h=sum(chars[j:j+3]==['a','A','c'] for j in range(len(chars)-2))
                assert h==hits
                K=sum(abs(k)==1 for k in word)
                p=min(sum(k==1 for k in word),sum(k==-1 for k in word))
                delta=sgn(S[end][2])-sgn(S[start][2])
                assert p==(K-abs(delta))//2
                primitive_checks+=1
        if d==4:break
        nextfront=[]
        for start,end,bs,word,hits in frontier:
            for dst in NEXT[end]:
                for branch in (0,1):
                    a,b=-S[end][2],S[dst][2]
                    w=word+(a,b) if branch==0 else word+(b,a)
                    nextfront.append((start,dst,bs+(branch,),w,hits+int(len(bs)>0 and bs[-1]==0 and branch==0 and dst==T)))
        frontier=nextfront
assert primitive_checks==48*(6+36+216+1296)

for k in range(1,5):
    for extra,mult in [(0,9),(1,108)]:
        d=4*k-2+extra
        if d>15:continue
        expected=mult*20**(k-1)
        top={pair:v for (h,pair),v in Hhist[d].items() if h==k}
        assert top=={k:expected},(k,d,top,expected)
        assert all(h<=k for h,p in Hhist[d])

out={
 'verdict':'ALL_CHECKS_PASS','date':'2026-11-06',
 'model':'PREFIX-518/522/525 signed-X6 four-STAR path, typed BRC pair observer',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phase_states':len(S),'phase_parity_block':len(P),
 'two_step_denominator_degree_u':11,'full_t_recurrence_order':22,
 'even_subsequence_order':11,'gcd_numerator_denominator':'1 in Q(q)[u]',
 'D_factorization':list(map(str,[D1,D2,D3])),
 'renewal_first_terms_t':{str(m):{str(p):str(n) for p,n in dist.items()} for m,dist in R.items() if m<=12},
 'joint_factorial_moments_checked_d':15,'joint_factorial_orders_checked':[1,2,3,4],
 'native_word_direct_checks':primitive_checks,
 'maximal_gate_diagonals':'For k>=1: at d=4k-2, (H,p1)=(k,k) has 9*20^(k-1) histories; d=4k-1 has 108*20^(k-1).',
 'top_hit_sample':{str(d):{f'{h},{p}':str(v) for (h,p),v in Hhist[d].items() if h==max(x[0] for x in Hhist[d])} for d in [2,3,6,7,10,14,15]},
 'renewal_formula':'P(t,q,z)=P0(t,q)+(z-1)J(t,q)/(1-(z-1)S(t,q))',
 'moment_formula':'sum_d sum_w binom(H(w),k) q^p t^d=J(t,q)*S(t,q)^(k-1), k>=1',
 'scope':'author-proved formula, executed exact integer/symbolic certificate; independent review and admission pending'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
