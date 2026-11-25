# R284HO — Exact fixed-deficit polynomial strips and finite triangular closure

2026-11-25. Author calculation/proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer. Frozen dependency: 90ec11b240d130c8cd2d936b35ba77369751894e:research_notes/portable_direct/R284HN_ALL_SCALE_EVENTUAL_MONOTONICITY_20261125.md, exact port moment identities; HM ee8f08bb614ff06cb63f6e2567d14ead674e42ff supplies prior eventual fixed-deficit result. The following strengthens fixed-deficit eventual signs to all budgets in the stated strips. P000 V5 and ACTIVE worldview read, unchanged. No shared CLAIM or Result. Prior own activity metadata read (RA-B82240E8488EF5A1DA5186C4); current registration capability not reverified. Current LEASED inventory r1-20261125-1256-owner-inventory-read was RUNNING at observation; no inference of empty ownership.

## Exact result

Let d=u-q, x=q, K_d(x)=K(x,x+d). For every integer x>=0:
- K_(d+1)(x)>K_d(x) for 1<=d<=24 (reading-budget direction).
- K_d(x)>K_(d-1)(x+1) for 2<=d<=24 (omission-budget direction).

This is an infinite family of budgets proved by exact finite coefficient certificates, not an asymptotic claim. In addition, all 31,125 adjacent q comparisons with 1<=u<=250 and all 31,125 adjacent u comparisons with 1<=u<=249 are strictly in the stated direction, by exhaustive integer computation. These are explicit parts of the finite complement of HN. The remaining uniform/global proof is open.

## Exact polynomial representation and proof

Use frozen definitions n=x+d, m=2x+d, g=d+1, M_n(k)=(k+1)/(n+1) binom(2n+2,n-k), zero for k>n. Then
M_z(k)/M_z(0)=(k+1) prod_(i=0)^(k-1)(z-i)/(z+i+3).
For each z in {n,n-1,m,m-1}, form a common polynomial denominator D_z=prod_(i=0)^(g-1)(z+i+3) and numerators A_z(k)=(k+1)prod_(i<k)(z-i)prod_(k<=i<g)(z+i+3). These give exact rational weights for every integer x>=0 including support boundaries: if k>z, the numerator contains the zero factor z-z. Keep joint allocation by convolution of the numerator arrays. Write A,a,B,b for z=n,n-1,m,m-1 and ad,aa,bd,bb for their denominators. For arrays define C(A,B,j)=sum_(k=0)^j A(k)B(j-k), zero for j<0. Put rn=n+2,rd=4n+2,tn=m+2,td=4m+2, since M_(n-1)(0)/M_n(0)=rn/rd, etc.
Define
Q=C(A,B,d-1);
S=(C(A,B,d)+Q)aa rd + x rn (C(a,B,d)+C(a,B,d-1))ad;
P=sum_(j=0)^3 binom(3,j) C(a,b,d+1-j).
The exact ratio from HN is K_d(x)=N/D where
N=P Q rn tn (3n+x+1)^2 ad aa rd bd,
D=S^2 td bb (n+2x+1).
Indeed original normalized Q,S,P have denominators ad bd, ad aa bd rd, aa bb respectively, with P carrying rn tn/(rd td); cancellation yields this expression. Every common denominator is strictly positive at x>=0, and S>0 from the positive Q port. Reduce N,D by their polynomial gcd over the integer polynomial ring. For each d in the declared range, the resulting denominator and the adjacent denominator have all strictly positive coefficients, so the sign of the comparison is exactly the sign of the cross polynomial. All nonzero (indeed every coefficient including constant) coefficients of the following cross polynomials are strictly positive in the executed scope:
F_d=N_(d+1)D_d-D_(d+1)N_d,
G_d=N_d(x)D_(d-1)(x+1)-D_d(x)N_(d-1)(x+1).
The certificate below computes every coefficient exactly. This proves the result for all real x>=0 for the rational polynomial extension, and for integer x>=0 for the original counts. It does not assume any continuous extension of the original binomial counting model.

## Executed symbolic certificate (Python/SymPy)

```python
import sympy as s
from math import comb
from functools import lru_cache
x=s.Symbol('x')
@lru_cache(None)
def port(a,b,g):
 z=a*x+b
 den=s.prod(z+i+3 for i in range(g))
 arr=[s.Poly(s.prod(z-i for i in range(k))*s.prod(z+i+3 for i in range(k,g))*(k+1),x) for k in range(g+1)]
 return arr,s.Poly(den,x)
@lru_cache(None)
def K(d):
 u=x+d;m=2*x+d;g=d+1
 A,ad=port(1,d,g);a,aa=port(1,d-1,g);B,bd=port(2,d,g);b,bb=port(2,d-1,g)
 def C(a,b,g):return sum((a[k]*b[g-k] for k in range(g+1)),s.Poly(0,x)) if g>=0 else s.Poly(0,x)
 rn=s.Poly(u+2,x);rd=s.Poly(4*u+2,x);tn=s.Poly(m+2,x);td=s.Poly(4*m+2,x)
 Q=C(A,B,d-1);S=(C(A,B,d)+Q)*aa*rd+s.Poly(x,x)*rn*(C(a,B,d)+C(a,B,d-1))*ad
 P=sum((comb(3,j)*C(a,b,d+1-j) for j in range(4)),s.Poly(0,x))
 N=P*Q*rn*tn*s.Poly((3*u+x+1)**2,x)*ad*aa*rd*bd
 D=S*S*td*bb*s.Poly(u+2*x+1,x)
 G=s.gcd(N,D);return N.exquo(G),D.exquo(G)
def shift(p):return s.Poly(p.as_expr().subs(x,x+1),x)
for d in range(1,25):
 N,D=K(d);a,b=K(d+1);F=a*D-b*N
 G=None if d==1 else N*shift(K(d-1)[1])-D*shift(K(d-1)[0])
 assert min(D.all_coeffs())>0 and min(b.all_coeffs())>0
 print(d,N.degree(),D.degree(),F.degree(),min(F.all_coeffs()),None if G is None else (G.degree(),min(G.all_coeffs())),flush=True)
```

Executed output summary: d=1..24; 24 F and 23 G cross polynomials; all printed minima strictly positive. Selected rows (d,N degree,D degree,F degree,min F,(G degree,min G)):
```
1 9 10 21 89600 None
2 11 12 28 2222080 (21, 89600)
6 27 28 58 1029439488000 (51, 789007564800)
12 49 50 102 13337607182053539840 (95, 104858029496729600)
18 71 72 146 4533492925206097821696000 (139, 225049211128997121884160)
24 93 94 190 23272068827363207307602165760 (183, 251911783755725553008640000)
```
Every intermediate row also had positive minima; reproducible by the code. Observed matching adjacent minima in F/G does not alone establish a structural identity.

## Exact finite triangular check

Executed Python arbitrary integer version, no floating point or asymptotic approximation:
```python
from math import comb
from functools import lru_cache
@lru_cache(None)
def moments(n):
 a=[comb(2*n+2,n)//(n+1)]
 for k in range(n):
  v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert r==0;a.append(v)
 return a
def K(u,d):
 q=u-d;m=u+q
 A,a,B,b=(moments(n) for n in (u,u-1,m,m-1))
 def C(a,b,g):return sum(a[k]*b[g-k] for k in range(max(0,g-len(b)+1),min(g+1,len(a))))
 Q=C(A,B,d-1);S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1));P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
 return P*Q*(3*u+q+1)**2,S*S*(u+2*q+1)
def gt(a,b):return a[0]*b[1]>b[0]*a[1]
prev=[];bad=[];nq=nu=0
for u in range(1,251):
 cur=[K(u,d) for d in range(1,u+1)]
 for d in range(2,u+1):
  nq+=1
  if not gt(cur[d-1],cur[d-2]):bad.append(('q',u,d))
 for d in range(1,u):
  nu+=1
  if not gt(cur[d],prev[d-1]):bad.append(('u',u-1,d))
 prev=cur
print(nq,nu,bad[:100],len(bad))
```
Observed: `31125 31125 [] 0`. A subsequent attempt at u<=500 timed out; no additional range is certified by that attempt.

## Next

Seek a symbolic certificate uniform in d rather than repeating independent fixed-width polynomial scans. The numerator arrays retain each joint allocation and may permit a positive convolution/transport decomposition of the cross products. Alternatively derive an explicit effective bound in HN and then cover the residual finite region using exact comparison plus certified paid bounds. No native physical attribution or independent review is claimed.
