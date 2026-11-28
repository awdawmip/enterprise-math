# R284KE — Affine zero fiber, signed derivative, and a new p-adic candidate sieve

2026-11-28. Author proof and executed exact Python computation; NOT_REVIEWED. Auxiliary arithmetic of the R284 observer (no native spatial attribution). Recovered own metadata via r1-20261128-0855-own-recovery: original RESEARCHER registration r1-20261124-0256-r284gd-session-v1 open, no own formal runs; EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4. Owner inventory r1-20261128-0855-owner-inventory-v1 SUCCEEDED, no LEASED tasks as of 2026-11-28T00:56:17.687984Z, source f19e7ddc11152915ff2c73d2ce6332a308e8c709. No task acquisition or shared ownership mutation. Global entries verified at immutable main 3fb0a04910e7deed693b41bcebd727b9d13b19d6; P000 V4/V5, ACTIVE worldview, joint observer and residual rules, current research method and portable protocol consulted.

Frozen inputs:
- JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md — primal rational C and necessary equality, joint polynomial carrier.
- KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md — unique real zero, all legal integer d>=81, scale bracket [3/4,5/4]; KC 52028797f285dc23fcdad50a3f52f9d3d2fa5bea for d>=600 (as pinned by KD). No repeat of finite bridge.
- JP a1d1eac1c1df905c12c4e7ebb7f41c9a995a7ee7 and JQ aaf33a191be38a03736f73654f5f43b4d6dfac5d: zero-budget jets and local lifting obstruction; here a different affine coordinate, 3q+d+1, is used. JO's existing pole-window coordinates remain separate.

## 1. Exact zero fiber and theorems

Keep JR's original definitions: u=q+d, n=2q+d, R_v(k)=prod_{i=0}^{k-1}(v-i)/(v+i+3), l=d-k; a=(k+1)(l+1)R_u(k)R_n(l), b=(k+1)l R_u(k)R_n(l-1) for l>=1 and 0 otherwise, v_k=(u-k)(u+k+2)/(2u(2u+1)). V=sum a, Q=sum b, A=sum v_k(a+b), E=R_u(d)(u-d)(2d+3)(n+2)/(2(2u+1)(4n+2)), W=A+E, Z=qA+Q+V. C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. Equality qK=32/3 implies C=0.

Let d=3m+2, m>=1 an integer, q0=-m-1=-(d+1)/3. At q0 write U=2m+1, n=m. U+m=d-1. The rational functions are regular at q0. R_v(k)=0 when integer v>=0 and k>v; hence V0=0, Q0=(U+1)(m+1)R_U(U)R_m(m)>0 (only k=U, l=m+1 contributes), A0=E0=W0=0 and Z0=Q0. In particular C(q0,d)=0. This is a formal negative-budget root, not a legal equality.

**Theorem A (simple formal root).** For every m>=1, put T=W'(q0)/Q0 (q derivative with d fixed). Then T>0 and
Theta=C'(q0,d)/Q0^2 = -96-3(m+1)(5m+3)^2 T < -96.
Thus C/(q-q0) is a regular rational function nonzero at q0; JR's integer polynomial carrier also has a simple factor q-q0. The proof below retains E and both branches.

**Theorem B (affine large-prime sieve).** For any prime p>2d+2 with p|3q+d+1, all original denominators and Q0 are p-units at the formal fiber. Theta is p-integral. If p does not divide the reduced numerator of Theta then
v_p(C(q,d))=v_p(3q+d+1)
for any legal integer q on this fiber. Hence a legal integer zero requires every prime p>2d+2 dividing 3q+d+1 to divide that particular nonzero numerator. Unlike a generic pole witness this is an exact simple-zero division, followed by a nonzero jet check; no assumption about q's own largest prime factor.

## 2. Signed derivative proof, all m

Use U=2m+1, N=2U+2, M=2m+2. The elementary beta integral B(t,b)=(t-1)!(b-1)!/(t+b-1)! for positive integers gives, for integer v>=1 and t>=1,
R_v'(v+t)/R_v(v)=(-1)^(t-1) B(t,2v+3)
where the derivative is in the branch parameter v (index v+t fixed at its integer value). This follows by differentiating the unique zero numerator factor and multiplying the other numerator/denominator factors. The derivative in q has multiplier 1 for u and 2 for n. Also R_v(v-t)/R_v(v)=binom(2v+2,t), 0<=t<=v.

Split W' at k=U into a central contribution, left signed tail and right signed tail. Normalize by Q0. Central k=U contributes c=(2U+2)/(2U(2U+1)), since v_U=0. For k=U-t, t=1..U, l=m+1+t, the only surviving differentiation is on the m-branch. The ratio of the derivative at l to that at l-1 is -t/(2m+t+3). Their combined weight is
(l+1)*[-t/(2m+t+3)]+l=(m+1)(2m+3+2t)/(2m+3+t).
Use t(N-t) binom(N,t)=N(N-1)binom(N-2,t-1) and B(t,b)*[2-b/(t+b)]=B(t,b)+B(t+1,b). This yields the left tail
L=(2/U) sum_{i=0}^{U-1} (-1)^i (U-i) binom(2U,i)[B(i+1,2m+3)+B(i+2,2m+3)]
=(2/U) integral_0^1 (1-x)^(2m+2)(1+x) P_U(x) dx,
where P_U=sum_{i=0}^{U-1}(-1)^i(U-i)binom(2U,i)x^i. This truncated signed polynomial is the Taylor polynomial through degree U-1 of P(x)=U(1+x)(1-x)^(2U-1). For 0<=x<=1, P^(U)(x)<=0 because U is odd: after factoring (-1)^U U (2U-1)_fall_U (1-x)^(U-1), the remaining factor is (1+x)-(1-x)=2x. Taylor's integral remainder therefore gives P_U>=P>=0, with strict positivity on a nonempty interval. Hence L>0. This is a sign theorem for the actual joint alternating tail, not an absolute-value estimate of the independently large terms.

For k=U+t, t=1..m+1, only the derivative on the u-branch survives. After dividing by Q0 the A contribution is (-1)^t R_t with
R_t = [t(2U+2+t)(U+1+t)/(2U(2U+1)(U+1))] B(t,2U+3) binom(2m+2,t) (2m+3-2t)/(2m+3-t).
Indeed the weights from the m-branch combine as (m+2-t)binom(M,t-1)+(m+1-t)binom(M,t)=(m+1)(2m+3-2t)binom(M,t)/(2m+3-t). This includes l=0 at the last t. The endpoint E derivative has exactly the same sign as that final contribution; its magnitude relative to it is
rho=(2d+3)(m+2)/(2(U+d+2)(d+1)), 0<rho<1.
Thus replace R_(m+1) by (1+rho)R_(m+1), preserving the full endpoint.

For t=1..m the unmodified ratio is
R_(t+1)/R_t = (U+2+t)/(U+1+t) * (2m+3-t)/(2U+2+t) * (2m+1-2t)/(2m+3-2t).
The first factor is <=6/5, the second <1/2, third <1; at t=m the third is 1/3, so even after the endpoint multiplication the final ratio is <2/5. Therefore the modified magnitudes strictly decrease. The entire right tail is >=-R_1. Direct substitution yields
R_1=(2m+3)/(4(m+1)(4m+3)),
c=2(m+1)/((2m+1)(4m+3))>2R_1
(the ratio is 8(m+1)^2/[(2m+1)(2m+3)]>2).
Consequently T=c+L+sum_{t=1}^{m+1}(-1)^t modified_R_t>0. Differentiating C at q0 with W0=0, 3q0+d+1=0 gives C'=3q0(4q0+3d+1)^2 W' Q0-96 Q0^2, and 4q0+3d+1=5m+3. This proves A.

## 3. Exact prime-fiber valuations and second jet

At q0 the positive denominator factors in both R arrays are <=2d+2 (largest is U+d+2); also 2U,2U+1,4m+2 and fixed powers of 2 are units for p>2d+2. Q0 is a p-unit since R_v(v)=1/binom(2v+2,v) and all factorial factors are <=2d+2. Thus C expanded at q0 has p-integral power series coefficients by geometric inversion of these unit-denominator polynomials. Its constant term is zero. For q=q0+h with v_p(h)>=1, the quotient C/h is p-integral and reduces to C'(q0)=Q0^2 Theta. If the derivative is a unit, C/h is a unit, proving B for every valuation of h, without a bound on q.

When p divides Theta's numerator, put B_p=C'(q0)/p mod p and A_p=C''(q0)/2 mod p. These are computed using C'(q0) exactly and C(q0+p) mod p^3:
A_p = C(q0+p)/p^2 - B_p mod p.
All divisions here are on exact p-divisible quantities. For integer t,
C(q0+pt)/p^2 = t(B_p+t A_p) mod p.
For t!=0 mod p this gives at most one surviving t mod p if A_p!=0; no survivor if A_p=0 and B_p!=0; the doubly degenerate case is open to higher jets. For d>=81, KD/KC localize any legal equality to 4d^2/5 <= q <= 4d^2/3. Since p>2d+2, 0<q-q0<p^2 on this bracket (even 4d^2/3+(d+1)/3 < (2d+2)^2), so t is in [1,p-1]. Each nondegenerate exceptional prime therefore supplies at most one actual budget candidate; there is no hidden lift elsewhere in the bracket. This is a deterministic second-jet reduction for the remaining affine prime fibers, not an independence heuristic.

## 4. Actual executed computation and verified scope

Python Fraction, independent product/derivative propagation versus beta-tail expression, exact integer modular calculations. For m=1..66 (d=5,8,...,200), checked all 66 exact jets, including the vanishing at q0, Q0 formula, T equality and positivity. For each such d, all primes 2d+3<=p<=8d+8 (trial division primality), 6336 pairs. For each pair choose first legal q=q0+p*t >=max(64,ceil(d^2/4)) and verify the actual original C mod p^2 equals p*t*C'(q0) mod p^2. 6327 unit-derivative witnesses, 9 exceptional prime fibers. Independently check q=q0+p^2 mod p^3 for first prime per d (66 checks). The second-jet calculation for every one of the 9 exceptions checks t=2,3 directly mod p^3; each has a unique nonzero surviving t and all 9 q candidates are outside KD's root bracket. Exact output:
    {'exact_jet': 66, 'prime_fibers': 6336, 'valuation_1': 6327, 'valuation_2_checks': 66, 'exception': 9}
    exception_fibers [(83, 277), (83, 307), (95, 283), (104, 349), (107, 467), (110, 397), (134, 353), (152, 1039), (155, 499)]
    second_jet_rows [(83, 277, 4, 229, [254], []), (83, 307, 150, 1, [157], []), (95, 283, 168, 264, [128], []), (104, 349, 337, 40, [105], []), (107, 467, 71, 77, [272], []), (110, 397, 114, 370, [313], []), (134, 353, 46, 281, [285], []), (152, 1039, 277, 1038, [277], []), (155, 499, 392, 487, [199], [])]
Rows are (d,p,B_p,A_p,t_survivors,q_survivors_in_bracket). Thus no additional root candidate in the tested affine-prime window. This is a new sufficient certificate mechanism on an unbounded d-family, with a finite validation of its exceptional branch; it does not expand KD's all-integer-budget finite d coverage. No assumption that primes in the tested window always divide 3q+d+1.

Replay (the exact executed script):
```python
from fractions import Fraction as F
from math import comb, factorial, isqrt
from collections import Counter

def beta(a,b): return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))
def formula(m):
    u,d=2*m+1,3*m+2
    L=F(2,u)*sum((-1)**i*(u-i)*comb(2*u,i)*(beta(i+1,2*m+3)+beta(i+2,2*m+3)) for i in range(u))
    R=[F(t*(2*u+2+t)*(u+1+t),2*u*(2*u+1)*(u+1))*beta(t,2*u+3)*comb(2*m+2,t)*F(2*m+3-2*t,2*m+3-t) for t in range(1,m+2)]
    R[-1]*=1+F((2*d+3)*(m+2),2*(u+d+2)*(d+1))
    central=F(2*u+2,2*u*(2*u+1))
    assert L>0 and all(a>b for a,b in zip(R,R[1:])) and central>2*R[0]
    return central+L+sum((-1)**(i+1)*v for i,v in enumerate(R))

def exact_jet(m):
    d=3*m+2;q=F(-m-1);u=q+d;n=2*q+d
    def rr(n,t):
        a=[(F(1),F(0))]
        for i in range(d):
            f=(n-i)/(n+i+3);fp=t*(2*i+3)/(n+i+3)**2
            a.append((a[-1][0]*f,a[-1][1]*f+a[-1][0]*fp))
        return a
    U,M=rr(u,1),rr(n,2);V=Q=A=Wp=F(0)
    for k in range(d+1):
        l=d-k;v=(u-k)*(u+k+2)/(2*u*(2*u+1));vp=(2*u+2-v*(8*u+2))/(2*u*(2*u+1))
        a=(k+1)*(l+1)*U[k][0]*M[l][0];ap=(k+1)*(l+1)*(U[k][1]*M[l][0]+U[k][0]*M[l][1])
        b=(k+1)*l*U[k][0]*M[l-1][0] if l else 0;bp=(k+1)*l*(U[k][1]*M[l-1][0]+U[k][0]*M[l-1][1]) if l else 0
        V+=a;Q+=b;A+=v*(a+b);Wp+=vp*(a+b)+v*(ap+bp)
    assert U[d][0]==0 and V==A==0 and Q==F((int(u)+1)*(m+1),comb(2*int(u)+2,int(u))*comb(2*m+2,m))
    Wp+=U[d][1]*(u-d)*(2*d+3)*(n+2)/(2*(2*u+1)*(4*n+2))
    return Q,Wp/Q

def modC(q,d,power):
    u=q+d;n=2*q+d
    def R(v):
        a=[1]
        for i in range(d):a.append(a[-1]*(v-i)*pow(v+i+3,-1,power)%power)
        return a
    U,M=R(u),R(n);V=Q=A=0;iv=pow(2*u*(2*u+1),-1,power)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l]%power;b=(k+1)*l*U[k]*M[l-1]%power if l else 0
        V=(V+a)%power;Q=(Q+b)%power;A=(A+(u-k)*(u+k+2)*iv*(a+b))%power
    E=U[d]*(u-d)*(2*d+3)*(n+2)*pow(2*(2*u+1)*(4*n+2),-1,power)%power
    Z=(q*A+Q+V)%power
    return (3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2)%power

def prime(p):return p>=2 and all(p%i for i in range(2,isqrt(p)+1))
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p

def main():
    counts=Counter();exceptions=[]
    for m in range(1,67):
        d=3*m+2;q0=-m-1;Q,T=exact_jet(m);assert T==formula(m)>0
        theta=-96-3*(m+1)*(5*m+3)**2*T; assert theta < -96
        counts['exact_jet']+=1
        first=True
        for p in range(2*d+3,8*d+9):
            if not prime(p):continue
            qmin=max(64,(d*d+3)//4);t=(qmin-q0+p-1)//p;q=q0+p*t
            assert q>=qmin and 0<t<p
            cp=mod(Q*Q*theta,p);value=modC(q,d,p*p)
            assert value==p*(t*cp%p)
            counts['prime_fibers']+=1
            if cp:counts['valuation_1']+=1
            else:counts['exception']+=1;exceptions.append((d,p))
            if first:
                assert modC(q0+p*p,d,p**3)==p*p*cp
                counts['valuation_2_checks']+=1;first=False
    print(dict(counts));print('exception_fibers',exceptions)
if __name__=='__main__':main()

def second_jets():
    rows=[]
    for m in range(1,67):
        d=3*m+2;q0=-m-1;Q,T=exact_jet(m);cp=Q*Q*(-96-3*(m+1)*(5*m+3)**2*T)
        for p in range(2*d+3,8*d+9):
            if not prime(p) or mod(cp,p):continue
            b=mod(cp,p*p)//p; val=modC(q0+p,d,p**3);assert val%(p*p)==0
            a=(val//(p*p)-b)%p
            for t in [2,3]:assert modC(q0+p*t,d,p**3)==p*p*(t*(b+t*a)%p)
            ts=[t for t in range(1,p) if (b+t*a)%p==0]
            qs=[q0+p*t for t in ts if q0+p*t>=64 and 4*d*d<=5*(q0+p*t) and 3*(q0+p*t)<=4*d*d]
            rows.append((d,p,b,a,ts,qs))
    print('second_jet_rows',rows)
if __name__=='__main__':second_jets()
```

## 5. Remaining question

Explore uniform bound/structure of the prime divisors of Theta's numerator relative to 3q+d+1, or further affine fibers when d is 0 or 1 mod 3 (then the exact truncation used here does not apply). Combine the new affine certificate with JP/JQ zero-budget and JO pole certificates on the same actual q. The current proof gives an unbounded family of formal simple roots and corresponding sufficient prime certificates, but does not establish that every legal q has an eligible prime, does not exclude doubly degenerate jets uniformly, and does not prove absence of integer roots for d>3000. Preserve the KD real root bracket and JY/JZ sparsity at their original scopes. No formal Result, independent Review, or canonical theorem admission.
