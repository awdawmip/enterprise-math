# R284JQ — Simple p-adic root lifting, local obstruction and cross-window finite closure
2026-11-27. Author proof and exact Python computation; NOT_REVIEWED. Existing Activity RA-B82240E8488EF5A1DA5186C4; recovered own RESEARCHER session MCP-8cd6c4fa26b9459d923ff73ba0082220, original registration open, no formal runs, researcher EM-DIRECT-0C386E / TASK_RESEARCH. Corrected recovery request r1-20261127-1855-recovery-correct-sid succeeded (first request used researcher ID rather than SID). Current LEASED inventory r1-20261127-1855-leased-read RUNNING at observation; no Task acquisition or ownership mutation. Global canonical entry blobs verified at 3092af0acc00508f3d66d25f69ec6301aa286bea. P000 V5, ACTIVE worldview, joint observer and residual contracts, portable and current research method consulted. Auxiliary arithmetic observer, not native spatial dynamics.

Frozen scientific inputs:
- JP a1d1eac1c1df905c12c4e7ebb7f41c9a995a7ee7:research_notes/portable_direct/R284JP_BUDGET_ZERO_FIBER_AND_PADIC_JETS_20261127.md (full read; original zero-budget classification independently replayed below).
- JH decfd2e7f01e53d1036716b13efda9bf1bb36e87:research_notes/portable_direct/R284JH_SECOND_BRANCH_REMOVABLE_POLE_AND_HALF_WINDOW_20261127.md (r=2 certificate).
- JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9:research_notes/portable_direct/R284JO_FULL_JOINT_BLOCK_TRANSFER_20261127.md (all second offsets, including edge, and exact signed observer).
Original observer and endpoint E preserved throughout.

## 1. The exact local obstruction: simple roots persist to every order

Use JP's primal functions for q>=64, d>=3, d^2<=4q:
u=q+d, m=2q+d, R_n(k)=product_{i<k}(n-i)/(n+i+3), l=d-k,
a=(k+1)(l+1)R_u(k)R_m(l), b=(k+1)l R_u(k)R_m(l-1) (zero at l=0),
v=(u-k)(u+k+2)/(2u(2u+1)), V=sum a, Q=sum b, A=sum v(a+b),
E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)),
W=A+E, Z=qA+Q+V,
C(q,d)=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2.
Equality qK=32/3 implies C=0. All rational denominators are p-units on q in p Z_p for prime p>2d+2. (At zero, 4m+2=2(2d+1).)

Interior gap 3d+5<=p<=4d+1: JP shows v_p(Z(0))=1, W(0),Q(0) divisible by p. If there is an unresolved first-jet class s0 (1<=s0<p), at q*=p s0 both Z and at least one of W,Q have valuation >=2, and Z'(0) is a unit. Write q=q*+p^2 h and F(h)=C(q*+p^2 h,d)/p^4. This is a restricted power series over Z_p, i.e. coefficients integral and tending to zero. Proof: expand the finite rational functions at q*; inverse of each denominator has integral Taylor coefficients since the constant denominator is a unit. Substitution of p^2 h makes each coefficient of degree n divisible by p^(2n). Thus Z/p^2, the degenerate factor W/p^2 or Q/p^2, the other factor /p, and q/p have integral restricted expansions. Their products in C/p^4 give the assertion. The actual reduction of F is JP's quadratic
f(h)=3s0(3d+1)^2(L0+L1 h)-32(d+1)(z2+z1 h)^2,
with z1=Z'(0) mod p a unit. In particular this is not an arbitrary function with only pointwise p^4 divisibility.

For every simple root h0 of f in F_p there exists exactly one alpha in Z_p with alpha=h0 mod p and F(alpha)=0. Proof without an external analytic premise: if h_n is the unique root lift modulo p^n, then F(h_n+p^n t)=F(h_n)+p^n t F'(h_n) mod p^(n+1). The derivative is congruent to the nonzero f'(h0), so the next digit is uniquely -[F(h_n)/p^n]/f'(h0) mod p. The lifts converge in Z_p and the restricted series is continuous. For any h=h0 mod p, factor F(h)-F(alpha) by h-alpha termwise; the quotient is congruent to f'(h0) and is a p-unit. Hence, with beta=q*+p^2 alpha,
v_p(C(q,d))=4+v_p(h-alpha)=2+v_p(q-beta)
on that residue ball (including infinite valuation at the root). Distinct initial roots yield distinct beta. For N>=3, if these are all the initial roots and they are simple, the condition v_p(C)>=N+2 on q in p Z_p is equivalent to q lying in the corresponding lifted classes mod p^N. For N=3 this uses JP's prior exclusion of the other s classes. If a quadratic has a repeated root, this theorem does not settle it.

Boundary p=4d+3 prime: JP gives W(0),Q(0) units, v_p(Z(0))=1, and t=v_p(q)=1 or >=3 always certified. For q=p^2 h, F_b(h)=C(p^2 h,d)/p^2 has a restricted integral power series, with reduction a linear polynomial having nonzero slope and constant term:
3(3d+1)^2 W(0)Q(0) h -32(d+1)(Z(0)/p)^2.
The same proof gives exactly one alpha_b in Z_p, a unit, and beta_b=p^2 alpha_b; for q in its original residue ball, v_p(C)=v_p(q-beta_b). Thus for N>=3, v_p(C)>=N on q in p Z_p is equivalent to q=beta_b mod p^N.

**Consequence for strategy.** For each simple-root fiber, higher jets cannot remove the entire p-adic fiber: the full original C actually has a zero in Z_p. They do compress undecided *integer budgets* to one class per root at every depth. This is a scope-specific obstruction, not an integer equality example. The positive next step is to intersect the exact lifted classes with the other certified arithmetic coordinates or a bound on q, not try to force a nonexistent no-root theorem at the same p.

## 2. Sparse representative cross-window closure

For each fixed d and p in the tested range, a remaining simple root gives exactly one representative q in [0,p^N) at depth N. Instead of enumerating q, evaluate only those representatives with the independent second-branch witnesses. The whole zero-budget background is retained by the partition into certified complement and exact remaining classes.

Independently replayed JP for d=3..500, all interior gap primes: 17579 pairs; 12 zero Z slope, 17546 third-order closures, 21 fourth-jet cases, 9 with no roots and 12 with two roots. Exact list:
(8,29,22,[4,26]), (27,89,33,[1,87]), (46,173,29,[25,41]), (77,293,180,[58,150]), (94,337,13,[95,151]), (101,317,48,[61,276]), (281,1093,693,[203,466]), (311,1049,362,[208,234]), (323,1021,416,[439,661]), (404,1429,1271,[424,505]), (445,1433,347,[110,1214]), (493,1597,1287,[1378,1480]).
Each root is simple. Boundary primes 4d+3: 153. Total 24+153=177 branches. Lift every branch from modulus p^3 through p^6, checking exact original C at each lifted representative and a neighboring digit to verify slope. For an interior branch C mod p^(N+2)=0; boundary C mod p^N=0. For each of the 708 representative evaluations (177 per N, not all distinct integers), apply the r=2 certificate p'|q+d, p'>2d+1, H(d) nonzero mod p', where H=64d^6-61d^5+13d^4+61d^3-29d^2+16, or the full second-branch certificate for r>=3 (p'|2q+2d-r+2, p'>4d+6, G nonzero). Use largest prime factor as a sufficient witness; failed factor candidate does not imply equality.
Results:
N=3: interior 24/24 r2; boundary 146 r2 + 7 r>=3.
N=4,5,6: each interior 24/24 and boundary 153/153 r2.
All 708 certified, 701 by r2, 7 by other offsets. Minimum original undecided interior representative q=4002; boundary q=4761. Minimum q/d^2 across all 177 initial representatives is 10858/729 (d=27,p=89,q=10858). This ratio statement is finite, not uniform beyond d=500.
Example d=8,p=29,s0=22,h0=4: slope 8 mod 29; q representatives mod p^3,p^4,p^5,p^6 are 4002,516171,3345295,146923338. At q=4002 the r2 witness is p'=401 with H(8)=349 mod 401. At h0=26 slope 21 mod 29, representatives 22504,266394,266394,369467076; r2 witness at q=22504 is p'=67, H(8)=6 mod 67. Example d=27,p=89,s0=33,h0=1: representatives 10858,38079184,38079184,38079184; zero higher digits are retained, not treated as closure.

**Finite-domain theorem (implicit large q coverage).** For all integers 3<=d<=500, q>=64, d^2<=4q, if there exists a prime p|q with p>2d+2 and q<p^6, then qK(q,d)!=32/3. Proof: outside gap and boundary JP's zero-order certificate applies for all eligible p; in the gap the independently replayed finite classification and lift theorem leave only the 24 reps at N=6; at the boundary only 153 reps; the complete computed r2 certificates exclude every one. In particular it holds for every such d,q with q<(2d+3)^6 and a prime divisor >2d+2. The proof uses no probabilistic independence and does not enumerate q in that range. Smooth budgets without an eligible large prime and the unbounded d question remain open. No claim that Hensel roots are integer or rational.

## 3. Exact reproducibility (combined replay)
Python 3 with SymPy, integer modular arithmetic only; no float, and denominators inverted only on the proven unit fibers. The following combines the executed recheck, lift and witness routines, preserving the same formulas and scopes.

```python
from sympy import primerange, isprime, factorint
from math import comb
from collections import Counter

def obs(q,d,m):
    u=q+d; n=2*q+d
    def R(t):
        a=[1]
        for i in range(d):
            a.append(a[-1]*(t-i)*pow(t+i+3,-1,m)%m)
        return a
    U,M=R(u),R(n); V=Q=A=0
    iv=pow(2*u*(2*u+1),-1,m)
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*M[l]%m
        b=(k+1)*l*U[k]*M[l-1]%m if l else 0
        V=(V+a)%m; Q=(Q+b)%m
        A=(A+(u-k)*(u+k+2)*iv*(a+b))%m
    E=U[d]*(u-d)*(2*d+3)*(n+2)*pow(2*(2*u+1)*(4*n+2),-1,m)%m
    return (A+E)%m,Q,(q*A+Q+V)%m
def primal(q,d,m):
    W,Q,Z=obs(q,d,m)
    return (3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2)%m
def classify():
    stats=Counter(); pairs=[]
    for d in range(3,501):
        for p in map(int,primerange(3*d+5,4*d+2)):
            a=obs(0,d,p*p); b=obs(p,d,p*p)
            assert all(x%p==0 for x in a) and a[2]//p
            sl=[(y-x)//p%p for x,y in zip(a,b)]; stats['gap']+=1
            if not sl[2]: stats['zero slope']+=1; continue
            s=-(a[2]//p)*pow(sl[2],-1,p)%p; assert s
            W=(a[0]//p+s*sl[0])%p; Q=(a[1]//p+s*sl[1])%p
            if W and Q: stats['third']+=1; continue
            stats['degenerate']+=1
            q=p*s; a=obs(q,d,p**3); b=obs(q+p*p,d,p**3)
            z0=a[2]//(p*p); z1=(b[2]-a[2])//(p*p)%p
            assert a[2]%(p*p)==0 and z1
            if not W and Q: l0=a[0]//(p*p)*Q; l1=(b[0]-a[0])//(p*p)*Q
            elif not Q and W: l0=a[1]//(p*p)*W; l1=(b[1]-a[1])//(p*p)*W
            else: l0=l1=0
            rt=[h for h in range(p) if (3*s*(3*d+1)**2*(l0+l1*h)-32*(d+1)*(z0+z1*h)**2)%p==0]
            stats['roots '+str(len(rt))]+=1
            if rt: pairs.append((d,p,s,rt))
    print(stats,pairs); assert len(pairs)==12
    return pairs
def lift(d,p,base,step,scale,h,N=4):
    def f(x,n):
        z=primal(base+step*x,d,p**(scale+n))
        assert z%p**scale==0
        return z//p**scale
    der=(f(h+p,2)-f(h,2))//p%p
    assert der and f(h,1)==0
    vals=[h]
    for n in range(1,N):
        t=f(h,n+1); assert t%p**n==0
        h+=(-(t//p**n)*pow(der,-1,p)%p)*p**n
        assert f(h,n+1)==0
        assert f(h+p**n,n+1)==der*p**n%p**(n+1)
        vals.append(h)
    return der,vals
def second(d,r,p):
    u=(r-2)*pow(2,-1,p)%p; q=(u-d)%p; j=d-r
    U=1; B=(u+2)*pow(2*(2*u+1),-1,p)%p
    V=Q=A=0; c=(-1)**r*comb(2*j+r+1,r)%p
    for k in range(r+1):
        l=d-k; h=r-k; nxt=-c*h*pow(2*j+h+1,-1,p)%p
        a=(k+1)*(l+1)*c; b=(k+1)*l*nxt
        V=(V+U*a)%p; Q=(Q+U*b)%p; A=(A+B*(a+b))%p
        if h:
            U=U*(u-k)*pow(u+k+3,-1,p)%p
            B=B*(u-k-1)*pow(u+k+2,-1,p)%p; c=nxt
    Z=(q*A+Q+V)%p
    return (3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2)%p
def witness(q,d):
    H=64*d**6-61*d**5+13*d**4+61*d**3-29*d**2+16
    p=max(factorint(q+d))
    if p>2*d+1 and H%p: return (2,p,H%p)
    for r in range(3,d+1):
        p=max(factorint(2*q+2*d-r+2))
        if p>4*d+6:
            G=second(d,r,p)
            if G: return (r,p,G)
    return None
def main():
    pairs=classify(); counts=Counter(); rows=[]; failures=[]
    def take(kind,d,p,base,step,scale,h):
        der,vals=lift(d,p,base,step,scale,h)
        for N,x in enumerate(vals,3):
            q=base+step*x
            if q<64 or d*d>4*q: continue
            w=witness(q,d); counts[kind,N,'tested']+=1
            if w: counts[kind,N,'r2' if w[0]==2 else 'r>=3']+=1
            else: failures.append((d,p,N,q))
            rows.append((d,p,N,q,w))
    for d,p,s,hs in pairs:
        for h in hs: take('interior',d,p,p*s,p*p,4,h)
    for d in range(3,501):
        p=4*d+3
        if not isprime(p): continue
        z0=primal(0,d,p**3)//p**2; z1=(primal(p*p,d,p**3)//p**2-z0)%p
        assert z0 and z1
        h=-z0*pow(z1,-1,p)%p
        take('boundary',d,p,0,p*p,2,h)
    print(sorted(counts.items()),failures)
    assert not failures and len(rows)==708
    import json
    with open('r284jq_witnesses.json','w') as f: json.dump(rows,f,separators=(',',':'))
if __name__=='__main__': main()
```

## 4. Frontier
The simple-root obstruction makes infinite local jet escalation unproductive for these fibers. Study the r2 coordinate on the lifted family q=p s0+p^2 h (or p^2 h on boundary) with the exact residue h mod p^n, derive a deterministic cross-coordinate relation or a rigorous condition on large factors of q+d. For d>500, repeated-root cases (if any), smooth q, and integer equality outside the finite implicit coverage remain open. Real inverse-polynomial separation remains open. Retain original C, all prime factors as potential observers, and exact root digits; no independence assumption. No formal result, admission or task closure claimed.


## 5. Additional exact witness primality audit and final owner observation
The 708 witness primes were explicitly rechecked, as were divisibility, threshold and nonzero residue. There is one witness beyond 2^64, so the probable-prime branch of factorint/isprime alone would not suffice for the finite proof. For d=476,p=1907,N=6 the surviving representative is q=46812701342323511291, and the r2 witness l=q+d=46812701342323511767 with H(d) mod l=742936331645841664. Full factorization l-1=2*3^2*73*35626104522316219, all factors strictly below 2^64 and prime by deterministic-range SymPy isprime. With a=5, a^(l-1)=1 mod l and gcd(a^((l-1)/t)-1,l)=1 for each distinct prime t dividing l-1, verified by exact modular arithmetic. This is an elementary full-order primality proof: for every prime divisor b of l the order of a mod b divides l-1 and cannot divide (l-1)/t for any t, hence equals l-1, forcing b>=l. The other 707 witness evaluations use primes below 2^64. Maximum q among the 708 evaluations is 56693385334078500954. Additional actually executed audit (using routines and JSON above):
```python
import json, math
from sympy import isprime
rows=json.load(open('r284jq_witnesses.json'))
big=0
for d,p,N,q,(r,l,z) in rows:
    if l<2**64: assert isprime(l)
    else:
        big+=1
        assert l==46812701342323511767
        fac={2:1,3:2,73:1,35626104522316219:1}
        assert math.prod(k**e for k,e in fac.items())==l-1
        assert all(k<2**64 and isprime(k) for k in fac)
        assert pow(5,l-1,l)==1
        assert all(math.gcd(pow(5,(l-1)//k,l)-1,l)==1 for k in fac)
    if r==2:
        H=64*d**6-61*d**5+13*d**4+61*d**3-29*d**2+16
        assert (q+d)%l==0 and l>2*d+1 and H%l==z!=0
    else:
        assert (2*q+2*d-r+2)%l==0 and l>4*d+6 and second(d,r,l)==z!=0
assert len(rows)==708 and big==1
```
All checks passed. The final owner inventory original request r1-20261127-1855-leased-read SUCCEEDED: as-of 2026-11-27T10:57:24.281527+00:00, source 6cdc7b061d6579d6993f2fbc30d396d9a5c29047, LEASED filter returned no tasks. No shared owner changes.
