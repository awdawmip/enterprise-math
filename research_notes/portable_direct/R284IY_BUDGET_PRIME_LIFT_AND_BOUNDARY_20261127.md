# R284IY — Complete budget-prime lift dichotomy and boundary-prime pole
2026-11-27. Author analytic proof and executed finite tests; NOT_REVIEWED. Auxiliary binary-tag joint-count observer, no native spatial/dynamics promotion. Frozen input IX@011395eccc729879500146ebe1eae29d7ac1f73d:research_notes/portable_direct/R284IX_BUDGET_PRIME_COMMON_CERTIFICATE_20261127.md (blob f1deff6f24c8b9fac0036d40f1fd8a0a321cdc19), retaining its IV/IW pins. P000 V5 and global V4 projection, ACTIVE worldview, joint observer, heartbeat companion, research method and portable contract consulted. Own recovery of session MCP-8cd6c4fa26b9459d923ff73ba0082220 returned original successful registration; RA-B82240E8488EF5A1DA5186C4. Owner inventory r1-20261127-0057-owner-inventory last observed RUNNING at scientific preparation; no shared Task/CLAIM/Result or owner mutation. Preserve V,Q,A,E including E even when its zero-order value vanishes.

## 1. Setup and new all-order dichotomy
Use the exact IX definitions: u=q+d, m=2q+d, l=d-k, R_n(j)=product_(i=0)^(j-1) (n-i)/(n+i+3), w0=(k+1)(l+1)R_u(k)R_m(l), w1=(k+1)l R_u(k)R_m(l-1) (zero at l=0), v=(u-k)(u+k+2)/(2u(2u+1)), V=sum w0, Q=sum w1, A=sum v(w0+w1),
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)],
Y=qK=q(3u+q+1)^2(A+E)Q/[(u+2q+1)(qA+Q+V)^2].
Physical domain integers q>=64, d>=1, d^2<=4q. Rational functions at q=0 or p-adic arguments are auxiliary residues only. Put W_d(x)=A(x,d)+E(x,d), P_d=2(d+1)^2+1, C=W_d(0), D=W_d'(0). For a prime p>4d+3 with p|q put t=vp(q). Then:
- If p does not divide P_d: vp(Y)=t.
- If p divides P_d and D=0 mod p: vp(Y)=t+1 for EVERY q divisible by p.
- If p divides P_d and D !=0 mod p: a unique alpha in p Z_p has W_d(alpha)=0, vp(alpha)=1, and vp(Y)=t+vp(q-alpha). In particular if t>=2 then vp(Y)=t+1, in either derivative branch. If t=1, extra valuation above t+1 occurs exactly when q=alpha mod p^2 in the simple branch.
Thus no derivative nondegeneracy conjecture is required to classify all eligible budget-prime lifts. The actual existence of singular pairs is still open.

Proof: all defining denominators are p-units throughout p Z_p (their constants are bounded by 4d+2 in factors, or the smaller exterior factors listed in IX). W has a convergent power series there with coefficients in Z_p, by expanding each inverse linear factor as a geometric series; products and finite sums preserve this. IX proves vp(Y)=t+vp(W_d(q)), and its diagonal formula C=B P_d/[3(d+1)(2d+1)], B=((d+1)/binom(2d+2,d))^2 binom(4d+2,d), with prefactor a unit. Since 0<P_d<(4d+3)^2<p^2, an exceptional p has vp(C)=1 EXACTLY. In the singular case W(x)=C+xD+O_p(x^2) gives vp(W(x))=1 on p Z_p. In the simple case Hensel's lemma gives unique alpha in that ball. For x,y in p Z_p the divided difference (W(x)-W(y))/(x-y) is congruent to D mod p, since each degree >=2 contributes a multiple of p. Hence vp(W(x))=vp(x-alpha), including equality with infinity at the root. Evaluating at x=0 gives vp(alpha)=1. For actual positive q, W>0 (A positive, E nonnegative) so infinite valuation does not arise. This proof retains the complete W=A+E; replacing it by A alone is not justified for the first jet.

## 2. Exact joint first-jet algorithm
Write r_j=R_d(j), J_j=sum_(i=0)^(j-1) [1/(d-i)-1/(d+i+3)], J_0=0. At q=0 the weights are a_k=(k+1)(l+1)r_k r_l, b_k=(k+1)l r_k r_(l-1) (zero at l=0). Their first derivatives are a_k(J_k+2J_l), b_k(J_k+2J_(l-1)), respectively. This follows by differentiating each nonzero factor; m has slope two, u slope one. Put N_k=(d-k)(d+k+2), H=2d(2d+1). Then
v_k=N_k/H, v'_k=((2d+2)H-(8d+2)N_k)/H^2,
E'(0)=r_d (2d+3)(d+2)/[4(2d+1)^2].
The E formula follows from the explicit factor u-d=q; the bracket at zero equals d(2d+3). The exact derivative is
D=E'(0)+sum_k [v'_k(a_k+b_k)+v_k(a_k(J_k+2J_l)+b_k(J_k+2J_(l-1)))],
omitting the b-term when l=0. No division by N_k at k=d. This computes the required first jet in O(d) modular arithmetic operations (including inverses; actual bit cost includes modulus and input lengths). It does not imply a polynomial-in-log d algorithm or solve prime discovery.
The first lifted residue is alpha/p = -(C/p) D^(-1) mod p. Each next digit is obtained from W evaluated at the previous representative and the same unit derivative.

## 3. New boundary pole at p=4d+3
Assume d>=2 and p=4d+3 is prime dividing q. This was NOT included in IX. All original observer denominators remain p-units; in the IX diagonal formulas B,Q0,A0 and 3d+1,d+1 are units (3d+4<p, and P_d=9/8 mod p). But Z=qA+Q+V has Z(0)=B*4p/[3(3d+4)] of exact valuation one. Consequently
vp(Y)=t-2vp(Z).
For t=1 this is negative; for t>=2, vp(Z)=1 since q=0 mod p^2, giving vp(Y)=t-2. Thus for t=1 or t>=3, Y !=32/3. For t=2 let h=q/p^2, a p-unit. Reducing the exact IX rational leading coefficient after cancellation of p^2 gives
Y = h * d(3d+1)^2(3d+4)^2 P_d/[4(d+1)^3(2d+1)] = (33075/256) h mod p.
The last equality substitutes d=-3/4 mod p; all factors are units for p>=11. Hence equality is excluded also for t=2 unless h=8192/99225 mod p. This last congruence is necessary only, not sufficient.
In a fixed critical family d=s sqrt(q)+O(1) with s>1/4, p>=4d+3 implies p^2>q eventually, so t=1 always. The new boundary branch gives a valid pole-based certificate for every such boundary prime. This is a genuine distinct mechanism from IX's positive valuation, not a claim of improved asymptotic density (one boundary integer per d). At d=1,p=7 the simplification has a different denominator and is excluded from the boundary statement.

## 4. Executed finite evidence and reproducibility
Python exact fractions, modular integer arithmetic and SymPy factorint/isprime (small integer domains). Exhaustively factored P_d for 1<=d<=3000: 1997 eligible (d,p) pairs, all nondegenerate in this finite range. This is not a proof of universal nondegeneracy. For 1<=d<=100, 63 pairs, 189 successive Hensel digits verified through modulus p^4, with first-jet finite differences and perturbation tests. First examples (d,p,D mod p,alpha mod p^4): (2,19,8,57722), (5,73,41,10012461), (7,43,18,803025), (8,163,63,510481933), (9,67,55,14601310). Boundary: all primes p=4d+3 for 2<=d<=40, q=h p^t, h=1,2,3, t=1,2,3 satisfying physical domain. Exact Fraction tests: 136 cases (28,54,54 by t), all pass, including residue at t=2. No real residual lower bound, large-q real K rerun, or independent review.

Reproduction:
```python
from sympy import factorint,isprime
from fractions import Fraction as F

def jet(d,p):
    def div(a,b): return a*pow(b,-1,p)%p
    R=[1]; J=[0]
    for i in range(d):
        R.append(R[-1]*div(d-i,d+i+3)%p)
        J.append((J[-1]+div(1,d-i)-div(1,d+i+3))%p)
    A=D=0; den=2*d*(2*d+1)
    for k in range(d+1):
        l=d-k; w0=(k+1)*(l+1)*R[k]*R[l]%p
        w1=(k+1)*l*R[k]*R[l-1]%p if l else 0
        dw=w0*(J[k]+2*J[l])+(w1*(J[k]+2*J[l-1]) if l else 0)
        num=(d-k)*(d+k+2); v=div(num,den)
        dv=div((2*d+2)*den-num*(8*d+2),den*den)
        A=(A+v*(w0+w1))%p; D=(D+dv*(w0+w1)+v*dw)%p
    E1=R[d]*div((2*d+3)*(d+2),4*(2*d+1)**2)%p
    return A,(D+E1)%p

def obs(q,d,M=None):
    def div(a,b):return F(a,b) if M is None else a*pow(b,-1,M)%M
    def red(a):return a if M is None else a%M
    u=q+d;m=2*q+d
    def R(n):
        z=[1]
        for i in range(d):z.append(red(z[-1]*div(n-i,n+i+3)))
        return z
    P,S=R(u),R(m);V=Q=A=0
    for k in range(d+1):
        l=d-k;w0=(k+1)*(l+1)*P[k]*S[l];w1=(k+1)*l*P[k]*S[l-1] if l else 0
        v=div((u-k)*(u+k+2),2*u*(2*u+1))
        V=red(V+w0);Q=red(Q+w1);A=red(A+v*(w0+w1))
    E=red(P[d]*div((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2)))
    return V,Q,A,E

def vp(x,p):
    x=F(x);a,b=abs(x.numerator),x.denominator
    if not a:return float('inf')
    t=0
    while a%p==0:a//=p;t+=1
    while b%p==0:b//=p;t-=1
    return t

def W(q,d,M):
    _,_,a,e=obs(q,d,M);return (a+e)%M

def Y(q,d):
    v,Q,a,e=obs(q,d);u=q+d
    return q*(3*u+q+1)**2*(a+e)*Q/((u+2*q+1)*(q*a+Q+v)**2)

n=0;sing=[]
for d in range(1,3001):
    for p0 in factorint(2*(d+1)**2+1):
        p=int(p0)
        if p<=4*d+3:continue
        a,j=jet(d,p);assert a==0;n+=1
        if not j:sing.append((d,p))
print(n,sing) # 1997 []
count=0;examples=[]
for d in range(1,101):
    for p0 in factorint(2*(d+1)**2+1):
        p=int(p0)
        if p<=4*d+3:continue
        _,D=jet(d,p);assert D
        assert ((W(p,d,p*p)-W(0,d,p*p))//p)%p==D
        assert W(0,d,p*p)%p==0 and W(0,d,p*p)!=0
        alpha=0
        for j in range(1,4):
            z=W(alpha,d,p**(j+1));assert z%p**j==0
            alpha+=(-z//p**j*pow(D,-1,p)%p)*p**j
            assert W(alpha,d,p**(j+1))==0
            if j<3:
                q=alpha+p**j
                assert W(q,d,p**(j+1))%p**j==0 and W(q,d,p**(j+1))!=0
            count+=1
        if len(examples)<5:examples.append((d,p,D,alpha))
        assert W(p*p,d,p*p)!=0
print(count,examples) # 189
count=0;levels={}
for d in range(2,41):
    p=4*d+3
    if not isprime(p):continue
    for t in (1,2,3):
        for h in (1,2,3):
            q=h*p**t
            if q<64 or d*d>4*q:continue
            y=Y(q,d);v=vp(y,p)
            assert (v<=-1 if t==1 else v==t-2)
            if t==2:assert (y-F(33075*h,256)).numerator%p==0
            if t!=2:assert y!=F(32,3)
            count+=1;levels[t]=levels.get(t,0)+1
print(count,levels) # 136 {2:54,3:54,1:28}
```

Next: exploit other exterior pole/zero coordinates or internal multiple-pole regions; analyze whether the critical interval meets the single high-lift residue and whether a closed jet simplification can remove the O(d) evaluation. Universal IW second-endpoint derivative nondegeneracy, real separation and worst-case fast sign determination remain open. No theorem acceptance or task completion asserted.
