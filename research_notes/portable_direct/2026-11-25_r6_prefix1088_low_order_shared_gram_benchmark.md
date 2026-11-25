# PREFIX-1088 — Exact low-order shared divergence Gram benchmark

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Continuation of PREFIX-1087. Original registration r6-20261123-2358-session-start-own-v1 independently recovered SUCCEEDED, EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Current owner query r6-20261125-2250-owner-read last observed RUNNING, NATIVE_RUNNER; no new CLAIM, no shared Task mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve the complete signed phase-paired Cell/port/ordered multiplicity carrier. CT character variables are auxiliary observations, not native spatial or time coordinates. Native-to-observer correspondence is inherited conditional evidence, not newly validated dynamics.

Parents:
- 2f3bf251ebcd76aa5cbcae50f47c9fe3a861d010:research_notes/portable_direct/2026-11-25_r6_prefix1087_divergence_completeness_and_envelope_floor.md
- 855e604a7ddd689e9aac5b155d9c5db1edc41c6c:research_notes/portable_direct/2026-11-25_r6_prefix1086_ct_divergence_null_controls.md
- 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md

## 1. Low-order exact null family

Retain parent notation R=SB, x=R/36, y=1-x, a=M+2, b=Q-3, w=x^a y^b. For E_i z^v=v_i z^v, define G=sum_i(E_i R)^2. Direct Laurent differentiation gives
    sum_i E_i^2 R = 2(R-6),
    G=B^2 sum_i z_i^2 + S^2 sum_i z_i^(-2) -12R.
Indeed E_i R=z_i B-S/z_i and E_i^2 R=z_i B+S/z_i-2. Apply the PREFIX-1087 divergence identity to V_i=E_i R. Write H_0=36 T_Q(V), so
    H_0=72(R-6)x^2 y^2 + (a+2)G x y^2 -(Q-1)G x^2 y.
For l=1,2,3, apply the product rule to V_i=x^l E_i R:
    H_l=x^l H_0 + l G x^(l+1)y^2.
All four are exactly bin-null. They are symmetric, inversion-even and rational Laurent polynomials. This is a shared basis across the whole infinite tail, with Q dependence explicitly affine, not an independent coefficient fitted at every bin.

A separate vector family V_i=z_i^2 B^2-z_i^(-2)S^2 has
    sum_i E_i V_i=2G+20R,
    sum_i(E_i R)V_i=G_3=B^3 sum_i z_i^3 + S^3 sum_i z_i^(-3)-2R^2.
Consequently its scaled control is
    H_4=36(2G+20R)x^2 y^2 + (a+2)G_3 x y^2 -(Q-1)G_3 x^2 y.
All are real on the unit character carrier after differentiation. No division by x or y is used. For every Q in scope CT[w H_l]=0, by the exact CT divergence product identity. Hence every original signed bin, its multiplicity, and the grouped signed and absolute tail masses are unchanged for any real coefficients; exact rational coefficients are used below.

## 2. Finite exact shared Gram optimization

For Q=k+u and u>=U, weight c_u=binom(u+r-1,r-1), define joint inner product using sum_u c_u CT[w (...)]. Let F denote the full orbit average of the parent carrier, C=<F,F>, B0=<1,1>, v_l=<F,H_l>, K_lj=<H_l,H_j>. For n nested controls, if K is positive definite solve K beta=v exactly. Then residual squared norm is C_n=C-v^T beta and new absolute envelope is
    E_n=c sqrt(B0 C_n)/D_m(k), c=1/(8*36^6).
The finite positive-semidefinite case with redundant modes is handled by restriction to independent modes. Monotonicity follows from the nested minimization. Every signed bin remains exact. Since H_l is S6-invariant, <F,H_l> equals the cross moment using just the original marked pair (no 15-fold orbit expansion). The F^2 term still uses PREFIX-1085's exact three relation types 1,8,6 divided by 15.

For any cross product between terms binom(Q,d) P x^i y^j and binom(Q,e) P' x^i' y^j', put I=i+i', J=j+j'. Use the parent's finite sum L(PP',A,q,h,V)=sum_(l=0)^(h-1) binom(V+l-1,l) CT[PP' x^(A-h+l) y^(q+V)] and the binomial product/Vandermonde identities. The cross-term tail is exactly
    sum_(h=max(d,e))^(d+e) binom(h,d)binom(d,d+e-h)
       sum_(ell=0)^h binom(k,h-ell)binom(r+ell-1,ell)
       L(PP',M+2+I,k+ell-3+J,r+ell,U-ell).
All exponents used in the benchmark are nonnegative, U>=7. The cross terms are integrable: H_0 and H_4 are O(x^2)+O(Q x^3) as x tends to zero (G=O(x), G3=O(x^(3/2))); the weaker bound G3=O(x) suffices, and additional x^l factors only improve the bound. The inherited finite positive moments and binomial weighting justify the finite identities. The scaled controls have no native state erasure.

## 3. Executed benchmark, not a hypothetical Gram correlation

Fixed (m,r,k)=(0,1,115), U=7,20,120. Exact integer occupation recurrence and rational finite Gram sums, 57 shift classes (the SAME class count as the parent orbit benchmark), 367 distinct compressed moment-polynomial coefficient sets including the original D coefficient sequences. N=252, J=N+12. A separate single-control run also passed, digest 768097457a2bc2129123b448d9476b352d2c034f8a2d175353d7d9adbb2c5e9a.

U | zero controls | H0 | H0,H1 | +H2 | +H3 | +H4
7 | 510.5363449582 | 440.3757190608 | 365.9952796799 | 365.9930236844 | 365.3923488301 | 360.2471378031
20 | 362.1618312108 | 312.1016249466 | 258.8821353687 | 258.8802769101 | 258.4697726661 | 254.5080118504
120 | 49.5973038613 | 42.2738754416 | 34.2757766146 | 34.2543960842 | 34.2084967448 | 33.7420547496

The exact fraction of original squared norm removed by all five is about 0.50209355,0.50614715,0.53716423. The two-mode family already removes 0.48607749,0.48902599,0.52240643. Adding the last three to the first two improves absolute envelope by only about 1.56%,1.69%,1.56% respectively. The U=120 signed mass is 0.20462834069258837, so the negative tail upper bound changes from 24.6963377603 (orbit) to 16.7687132045 (five controls), still far above a useful tiny tolerance. This is measured envelope reduction, not measured runtime acceleration. Neither the theoretical inter-bin floor nor the actual true absolute tail is numerically computed here. The small gain of these particular high-order radial multiples does not imply all alternative controls are exhausted.

Exact checks: first eight A_m equal PREFIX-1082, all five controls have exactly zero weighted CT at Q=122,123,135,136,235,236 (30 checks, some repeated in the scalar run), six comparisons of carrier CT with D, three each of A,Z,C tail differences with single-bin values, each 1..5 leading Gram system has strictly positive elimination pivots and its envelope is monotone and above the exact signed tail magnitude. Exact record SHA256 d112f1c1126b96ec514455c2679d8fb5166dfd5be1f5e05cb8a7ed6fbb1e6e9d. Decimal values only for display. No new native enumeration, classical reference arithmetic, formal checker or independent review.

## 4. Reproduction

The following code reconstructs the benchmark with the frozen PREFIX-1082 carrier formula. It preserves the complete six-axis displacement in the CT contraction and combines signed coefficients before norming. The record digest uses JSON compact separators; Fractions are exact. Requires Python and SymPy.

```python
import sympy as sy
from collections import defaultdict
from math import comb
from fractions import Fraction as Fr
import json,hashlib
from functools import lru_cache
S,B,z,c,n,t=sy.symbols('S B z c n t'); R=1-t*S
def H(j):
    b=1/z; cj=b if j==0 else c; delta=int(j==0)
    U=B-6*R*b-36*t; V=B-6*R*cj-36*t
    W=B-6*R*(b+cj)+36*delta*R**2*b-36*t**2*S
    C0=1-6*R*delta-6*t*z
    N=sy.Poly(sy.expand((1-z*t)*U*V+R*t*(36-11*z*t)*W-10*t**2*R**2*C0-390*z*t**3*R**2-390*delta*t**2*R**3),t)
    return sy.expand(sum((n-i-1)*(n-i-2)*N.nth(i)*S**(5-i) for i in range(6)))
def star(h):return h.xreplace({S:B,B:S,z:1/z,c:1/c})
K=sy.expand(H(0)*star(H(0))-H(1)*star(H(1)))
K2=sy.expand(K+K.xreplace({z:1/c,c:1/z}))
def coeffs(poly):
    out=defaultdict(lambda:0)
    for term in poly.as_ordered_terms():
        p=term.as_powers_dict(); key=tuple(int(p.get(v,0)) for v in (S,B,z,c))
        out[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
    return {k:sy.Poly(sy.expand(v),n) for k,v in out.items() if sy.expand(v)!=0}
orig=coeffs(K); sym=coeffs(K2)
assert len(orig)==66 and len(sym)==84
M=1;k=115;r=1;m=0
def embed(P,i,j):
    out={}
    for (u,v,a,b),p in P.items():
        ds=[0]*6; ds[i]=-a; ds[j]=b;out[(u,v,*ds)]=p
    return out
def mul(A,B):
    out=defaultdict(int)
    for a,p in A.items():
        for b,q in B.items():out[tuple(x+y for x,y in zip(a,b))]+=p*q
    return {k:v for k,v in out.items() if v}
def add(*Ps):
    out=defaultdict(int)
    for P in Ps:
        for a,p in P.items():out[a]+=p
    return {a:p for a,p in out.items() if p}
def scale(P,s):return {a:p*s for a,p in P.items() if p*s}
one={(0,)*8:1}
Rpol={(1,1,0,0,0,0,0,0):1}
G=scale(Rpol,-12)
for i in range(6):
    d=[0]*6;d[i]=-2; G=add(G,{(0,2,*d):1});d[i]=2;G=add(G,{(2,0,*d):1})
P=[]
for d in range(4):
    p={(u-2,v-2,a,b):sum((-1)**(d-j)*comb(d,j)*int(f.eval(M+8+j)) for j in range(d+1)) for (u,v,a,b),f in sym.items()}
    P.append({a:v for a,v in p.items() if v})
Fs=[(d,d,3-d,scale(embed(P[d],0,1),(-1)**d)) for d in range(4)]
Hs=[(0,2,2,scale(add(Rpol,scale(one,-6)),72)),(0,1,2,scale(G,M+4)),(0,2,1,G),(1,2,1,scale(G,-1))]
families=[Hs]
for l in (1,2,3):
    families.append([(d,i+l,j,P) for d,i,j,P in Hs]+[(0,l+1,2,scale(G,l))])
G3=scale(mul(Rpol,Rpol),-2)
for i in range(6):
    d=[0]*6;d[i]=-3;G3=add(G3,{(0,3,*d):1});d[i]=3;G3=add(G3,{(3,0,*d):1})
families.append([(0,2,2,scale(add(scale(G,2),scale(Rpol,20)),36)),(0,1,2,scale(G3,M+4)),(0,2,1,G3),(1,2,1,scale(G3,-1))])
def canon(d):return min(tuple(sorted(d)),tuple(sorted(-x for x in d)))
def compress(P):
    out=defaultdict(int)
    for (u,v,*d),p in P.items():
        assert u-v==sum(d)
        key=(u-sum(max(x,0) for x in d),canon(d))
        out[key]+=p
    return tuple(sorted((a,d,p) for (a,d),p in out.items() if p))
Cterms=[]
for d,di,dj,Pd in Fs:
    for e,ei,ej,Pe in Fs:
        pp=add(*[scale(mul(Pd,scale(embed(P[e],a,b),(-1)**e)),wt) for a,b,wt in [(0,1,1),(0,2,8),(2,3,6)]])
        Cterms.append((d,e,di+ei,dj+ej,compress(pp)))
def cross(X,Y):return [(d,e,i+ii,j+jj,compress(mul(P,Q))) for d,i,j,P in X for e,ii,jj,Q in Y]
Aterms=cross(Fs,Hs);Zterms=cross(Hs,Hs)
AF=[cross(Fs,h) for h in families]; ZF={(i,j):cross(h,g) for i,h in enumerate(families) for j,g in enumerate(families) if i<=j}
N=252; J=N+12
origpol=[compress(embed({key:int(v.eval(i+8)) for key,v in orig.items() if v.eval(i+8)},0,1)) for i in range(N+1)]
pols={compress(one)} | {p for d,e,i,j,p in Cterms+Aterms+Zterms+[t for a in AF for t in a]+[t for a in ZF.values() for t in a]} | {compress(p) for d,i,j,p in Fs+[t for h in families for t in h]} | set(origpol)
keys={d for p in pols for a,d,v in p}
assert len(keys)==57 and len(pols)==367
BC=[[1] for _ in range(J+20)]
for i in range(1,len(BC)):
    prev=BC[i-1];BC[i]=[1]+[prev[j-1]+prev[j] for j in range(1,i)]+[1]
Tzero={1:[1]*(J+1)}
for l in range(2,7):Tzero[l]=[sum(BC[j][q]**2*Tzero[l-1][j-q] for q in range(j+1)) for j in range(J+1)]
def calc(d):
    d=[x for x in d if x]; ap=am=0
    if len(d)==6:
        di=d.pop(0);ap=max(di,0);am=max(-di,0);T=[1]*(J+1)
    else:T=Tzero[6-len(d)]
    for di in d:
        pp=max(di,0);mm=max(-di,0);ap+=pp;am+=mm
        T=[sum(BC[j+ap][l+pp]*BC[j+am][l+mm]*T[j-l] for l in range(j+1)) for j in range(J+1)]
    return T
tables={d:calc(d) for d in sorted(keys)}
def ct(i,p):return sum(v*tables[d][i+a] for a,d,v in p if i+a>=0)
As=[ct(i,p) for i,p in enumerate(origpol)]
assert As[:8]==[3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
pow36=[36**i for i in range(N+1)]
def rows(arr):
    out=[]
    while arr:
        out.append(arr[:28]);arr=[36*x-y for x,y in zip(arr,arr[1:])]
    return out
@lru_cache(None)
def mr(p):return rows([ct(i,p) for i in range(N+1)])
def moment(p,i,q):return Fr(mr(p)[q][i],pow36[i+q])
Drows=rows(As)
def D(i,q):return Fr(Drows[q][i],pow36[i+q]*4*36**8)
def nb(p,i,q,r,U):return sum(comb(U+l-1,l)*moment(p,i-r+l,q+U) for l in range(r))
def tail(terms,U):
    total=Fr(0)
    for d,e,i,j,p in terms:
        for h in range(max(d,e),d+e+1):
            for ell in range(h+1):
                total+=comb(h,d)*comb(d,d+e-h)*comb(k,h-ell)*comb(r+ell-1,ell)*nb(p,M+2+i,k+ell-3+j,r+ell,U-ell)
    return total
def binval(terms,Q):return sum(comb(Q,d)*comb(Q,e)*moment(p,M+2+i,Q-3+j) for d,e,i,j,p in terms)
rad=compress(one); den=D(0,k); c0=Fr(1,8*36**6)
assert den>0
records=[]
def solve(A,b):
    A=[row[:]+[v] for row,v in zip(A,b)];n=len(b)
    for i in range(n):
        assert A[i][i]>0
        d=A[i][i];A[i]=[v/d for v in A[i]]
        for j in range(n):
            if i!=j:
                d=A[j][i];A[j]=[v-d*w for v,w in zip(A[j],A[i])]
    return [row[-1] for row in A]
for U in [7,20,120]:
    B0=nb(rad,M+2,k-3,r,U);C=tail(Cterms,U)/15;A=tail(Aterms,U);Z=tail(Zterms,U)
    assert Z>0 and 0<=A*A<=C*Z
    lam=A*A/(C*Z); old=c0*c0*B0*C/den**2; new=old*(1-lam)
    signed=D(0,k+U)/den; assert new>=signed*signed
    Q=k+U
    for Q1 in [Q,Q+1]:
        b=moment(rad,M+2,Q1-3); f=sum(comb(Q1,d)*moment(compress(p),M+2+i,Q1-3+j) for d,i,j,p in Fs)
        h=sum(comb(Q1,d)*moment(compress(p),M+2+i,Q1-3+j) for d,i,j,p in Hs)
        assert h==0 and c0*f==D(M,Q1)
        cc=binval(Cterms,Q1)/15; aa=binval(Aterms,Q1); zz=binval(Zterms,Q1)
        assert zz>0 and cc-aa*aa/zz>=f*f/b
    assert tail(Aterms,U)-tail(Aterms,U+1)==binval(Aterms,Q)
    assert tail(Zterms,U)-tail(Zterms,U+1)==binval(Zterms,Q)
    assert tail(Cterms,U)-tail(Cterms,U+1)==binval(Cterms,Q)
    v=[tail(t,U) for t in AF]; Kmat=[[tail(ZF[min(i,j),max(i,j)],U) for j in range(5)] for i in range(5)]
    assert v[0]==A and Kmat[0][0]==Z
    prev=C
    for n0 in (1,2,3,4,5):
        mat=[row[:n0] for row in Kmat[:n0]];vec=v[:n0];beta=solve(mat,vec)
        res=C-sum(x*y for x,y in zip(vec,beta));assert 0<=res<=prev;prev=res
        sq=c0*c0*B0*res/den**2;assert sq>=signed*signed
        print(U,n0,float(sq)**.5,float(1-res/C))
    for h in families:
        for Q1 in (Q,Q+1):assert sum(comb(Q1,d)*moment(compress(p),M+2+i,Q1-3+j) for d,i,j,p in h)==0
    records.append([U,*map(str,[B0,C,A,Z,signed,old,new]),[str(t) for t in v],[[str(t) for t in row] for row in Kmat],str(res)])
digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
assert digest=='d112f1c1126b96ec514455c2679d8fb5166dfd5be1f5e05cb8a7ed6fbb1e6e9d'
print(digest)
```

## 5. Next

The fixed shared two-control benchmark requested by PREFIX-1086/1087 is now completed; the actual scalar gradient T(E_i F_Q) comparison remains open. Since the two radial controls already capture nearly all the improvement of this five-mode family, investigate shared controls with non-radial joint factors or outer importance weighting and block selection instead of simply increasing radial degree. Quantify actual computational cost before claiming speed. Compute an inter-bin floor estimate using the exact CT bin means; real spectral boundary p, zero multiplicity d, explicit uniform positivity constant, and mother objective B_fix,odd(32) remain open.
