# R284JM — Resonance coefficient triple and disjoint large-prime degeneration

2026-11-27 · directed independent continuation · EM-DIRECT-0C386E / TASK_RESEARCH · NOT_REVIEWED.
Frozen scientific input: e700b37ddcbcd90bf7ae887bea7d3f2795c6df9c:research_notes/portable_direct/R284JL_RESONANT_MOMENTS_AND_ENDPOINT_CHARACTER_CERTIFICATES_20261127.md (read in full); its signed W weights, Newton basis and exact T,H representation are used unchanged. No formal Task claim or acceptance. The owner inventory r1-20261127-1504-owner was still RUNNING on last observation; this independent note changes no shared ownership.

## Theorem (exact resonance threshold and coefficient triple)

Take integers d>=r>=3, j=d-r, w=(r-2)/2, b=2j+2, q0=w-d. Use JL's t_k, P_h(k)=(k-w) rising h, T=t_(r+1), H=sum_(k=0)^r 1/(k+w+2). Each signed observer is L+BT+CH; write C_V,C_Q,C_A for the H coefficients of V*,Q*,A*, and C_Z=q0 C_A+C_Q+C_V. All coefficients and both residual coordinates remain in the original exact representation.

For even r, all four H coefficients vanish because P_r(0)=0. For odd r, all four vanish iff r>2j+3. In the active odd region r<=2j+3, set
 x=b+r/2, t=b-r+1=2j+3-r>=0,
 C=(w+2) P_r(0)(j+1)/(2 (r-1)!),
 F(x,k)=binom(x,k)+2 binom(x+1,k)+binom(x+2,k) for k>=0, F(x,k)=0 for k<0.
Then the EXACT formulas are
 C_V=-C F(x,t), C_Q=C F(x-1,t), C_A=C F(x,t+1),
 C_Z=C [q0 F(x,t+1)-F(x-1,t-1)].
In particular V,Q coefficients have opposite sign, Q,A have the same sign, Z,A have opposite sign (all statements about H coefficients, not total observers). This closes JL's finite observation with a uniform proof.

Proof. Define S_(n,a)(y)=binom(n-w+y+a-1,a-1)+binom(n-w+y+a-2,a-1), y=w-k, s=(-1)^r. JL's three polynomial weights become s(j+1)(r/2-y)S_(r,b+1)(y), -s(j+1)(r/2-y)S_(r-1,b+1)(y), and s(j+1)(r/2-y)y(r-y)S_(r,b)(y)/[(r-2)(r-1)]. The Newton coefficient a_r in P_r(k) is (-1)^r Delta^r W(w-y)|_(y=0)/r!; multiply by (w+2)P_r(0) for H. Here Delta is forward difference in y. The signs s cancel. Pascal identity gives Delta^h binom(z+y,k)=binom(z+y,k-h), including zero for negative lower index. For any polynomial S, discrete product rule yields
 Delta^r[(r/2-y)S(y)](0)=-(r/2)[Delta^(r-1)S(0)+Delta^(r-1)S(1)].
For the cubic factor use falling factorials y_(ell):
 (r/2-y)y(r-y)=y_(3)-3(r-2)y_(2)/2+(r-1)(r-2)y/2.
 Since Delta^r[y_(ell)S](0)=r_(ell) Delta^(r-ell)S(ell), the bracket after extracting r(r-1)(r-2) equals
 (1/2) Delta^(r-1)S(1)-(3/2) Delta^(r-2)S(2)+Delta^(r-3)S(3)
 = (1/2)[Delta^(r-3)S(1)+Delta^(r-3)S(2)].
The last identity follows by expanding the two differences in the first line. Thus division by (r-2)(r-1) gives the stated C_A. Substitution of the two adjacent binomial tops gives F(x,t), F(x-1,t), F(x,t+1); the difference F(x,t)-F(x-1,t)=F(x-1,t-1). If r odd and t<0 then t<=-2, so all coefficients vanish by degree. In active region C is nonzero because w is a half-integer, all three F values are strictly positive by their product expressions (all factors positive), and q0<0 with F(x-1,t-1)>=0 proves the sign and nonvanishing of Z. For even r, (-w) rising r contains zero, independently of degree. QED.

## Theorem (three quadratic carriers, pairwise disjoint large-prime zeros)

In the active odd region, let
 N_V=4d^2+18d-3r+18,
 N_Q=4d^2+10d-3r+6,
 N_A=4d^2+14d-3r+12.
The exact factorization
 F(x,k)=binom(x+2,k) N(x,k)/[(x+2)(x+1)],
 N(x,k)=k^2-4kx-5k+4x^2+12x+8
 follows by converting the two shifted binomials to binom(x+2,k). Substitution of (x,t),(x-1,t),(x,t+1) gives N_V,N_Q,N_A respectively. These are an arithmetic progression in the order Q,A,V, with step 4d+6.

For every prime p>4d+6, the common factor C and the three binomial prefactors (including their denominators) are units in Z_(p). Indeed, w and x are half-integers, their doubled factors in P_r(0) and binomial products have absolute value strictly between 0 and p; largest binomial top doubled is 2(x+2)=4d-3r+8<=4d-1. The factorial denominators have indices <p, and w+2,j+1,2 are units. Hence C_i=0 mod p iff p divides N_i. Since adjacent differences are 4d+6 and outer difference is 2(4d+6), no eligible prime can divide two of them. Moreover 0<N_i<(4d+6)^2 for d>=r>=3, so each individual coefficient has at most ONE eligible exceptional prime. All three together have at most three distinct exceptional primes. At any eligible prime at least two of C_V,C_Q,C_A survive. This applies also at the exact resonance threshold t=0 (then N_V and N_Q may have small factors but their full prefactors are units). It does NOT assert that G(T,H) is nonzero mod p, nor that these are exceptions of G. It gives a structural obstruction to removing the resonant coordinate by simultaneous vanishing of the three linear observers.

Interpretation: JL's H coordinate is necessary in the active odd region for this observation family; its sensitivity cannot disappear simultaneously even modulo any large eligible prime. All signed terms, T,H, and G's cross terms remain present. The three quadratic integer carriers are a compact prime-degeneration test; no calculation of H or T is needed for THIS test. Evaluating the carriers takes O(1) integer arithmetic operations on O(log d)-bit inputs, not a claim about the cost of computing full G or discovering p.

## Actual exact replay (Python 3, Fraction, SymPy factorint)
The executed scope was every 3<=r<=d<=60, using direct r-th differences of JL weights vs closed coefficients and all eligible prime divisors of the three carriers. Observed 1711 pairs: 590 active odd, 841 even, 280 inactive odd. All closed formulas and sign/zero assertions matched. Eligible exceptional-prime incidences among active pairs: V=406,Q=382,A=384; all pairwise disjoint at fixed pair and prime. First respective witnesses (d,r,p,N): (4,3,29,145), (4,3,101,101), (4,3,41,123). These are formal coefficient-degeneration samples, not G=0 or primal q equality. Unbounded claims follow from the algebra above, not samples.

```python
from fractions import Fraction as F
from math import factorial
from sympy import factorint

def bc(x,k):
    if k<0:return F(0)
    v=F(1)
    for i in range(k):v=v*(x-i)/(i+1)
    return v

def rise(x,k):
    v=F(1)
    for i in range(k):v*=x+i
    return v

def W(n,a,k):return (k+1)*(bc(n-k+a-1,a-1)+bc(n-k+a-2,a-1))
def direct(d,r):
    w=F(r-2,2);j=d-r;b=2*j+2;s=(-1)**r
    rows=[[s*(j+1)*W(r,b+1,w-i) for i in range(r+1)],[-s*(j+1)*W(r-1,b+1,w-i) for i in range(r+1)],[s*(j+1)*W(r,b,w-i)*i*(r-i)/(2*w*(2*w+1)) for i in range(r+1)]]
    for h in range(r):rows=[[y-x for x,y in zip(row,row[1:])] for row in rows]
    c=(-1)**r*(w+2)*rise(-w,r)/factorial(r)
    return tuple(c*row[0] for row in rows)

def FF(x,k):return bc(x,k)+2*bc(x+1,k)+bc(x+2,k)
def closed(d,r):
    w=F(r-2,2);j=d-r;b=2*j+2;x=b+F(r,2);t=b-r+1
    if t<0:return (F(0),)*3
    c=(w+2)*rise(-w,r)*(j+1)/(2*factorial(r-1))
    return -c*FF(x,t),c*FF(x-1,t),c*FF(x,t+1)

def carriers(d,r):return (4*d*d+18*d-3*r+18,4*d*d+10*d-3*r+6,4*d*d+14*d-3*r+12)
count=active=even=inactive=0;exceptions=[0,0,0];witness=[None]*3
for d in range(3,61):
    for r in range(3,d+1):
        c=closed(d,r);assert c==direct(d,r),(d,r,c,direct(d,r));count+=1
        t=2*(d-r)+3-r
        if r%2==0:even+=1;assert not any(c);continue
        if t<0:inactive+=1;assert not any(c);continue
        active+=1;v,q,a=c;z=F(r-2,2)-d;z=z*a+v+q
        assert v*q<0 and q*a>0 and z*a<0
        x=2*(d-r)+2+F(r,2);nv,nq,na=carriers(d,r)
        for i,(xx,tt,N) in enumerate([(x,t,nv),(x-1,t,nq),(x,t+1,na)]):
            assert FF(xx,tt)==bc(xx+2,tt)*N/((xx+2)*(xx+1))
            assert 0<N<(4*d+6)**2
            pp=[int(p) for p in factorint(N) if p>4*d+6]
            assert len(pp)<=1
            for p in pp:
                assert c[i].numerator%p==0 and c[i].denominator%p!=0
                assert all(c[k].numerator%p!=0 and c[k].denominator%p!=0 for k in range(3) if i!=k)
                exceptions[i]+=1
                if witness[i] is None:witness[i]=(d,r,p,N)
        assert nv-na==na-nq==4*d+6
print(count,active,even,inactive,exceptions,witness)
# Observed: 1711 590 841 280 [406, 382, 384] [(4, 3, 29, 145), (4, 3, 101, 101), (4, 3, 41, 123)]
```

## Next
Use the normalized resonance vector and its nondegenerate modular differences to eliminate H from selected linear combinations without dropping it from the full quadratic G. In particular investigate the quadratic-in-H discriminant and the compatibility with the actual T class; no general nonvanishing of G follows from coefficient nondegeneration alone. Preserve the exact H term for subsequent operations. All-budget equality exclusion, cross-window exceptional intersection, and real inverse-polynomial separation remain open. Independent review pending.
