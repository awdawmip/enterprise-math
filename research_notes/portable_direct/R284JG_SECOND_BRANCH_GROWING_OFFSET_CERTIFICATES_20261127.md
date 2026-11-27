# R284JG — Second-branch growing-offset pole certificates
2026-11-27. Author proof, exact rational replay, NOT_REVIEWED. Auxiliary binary-tag joint-count observer; no native spatial transfer. Existing directed independent activity RA-B82240E8488EF5A1DA5186C4, own registered session recovered (no runs); no shared task claim or owner mutation. Current owner query r1-20261127-0900-owner RUNNING at prepublication observation. Frozen science:
- JF df5cac5b9a78bc685dc792efa70c847d75e74704:research_notes/portable_direct/R284JF_OFFSET_ADAPTIVE_HEIGHT_AND_LOCAL_EXCEPTION_BUDGET_20261127.md (blob 84c9353a56cea033d4d3114b228fc68ed661eecc).
- JB e92de4ef4680b68015e53c4c702fbf929dada0a0:research_notes/portable_direct/R284JB_FIXED_OFFSET_INTERIOR_POLE_FAMILY_20261127.md (blob 9ac16b9644637a8416a050c701568463acb70248).
P000 V5, ACTIVE worldview and joint observer contract consulted. JF's first-branch certificates remain unchanged.

## 1. Second-branch pole reduction (all 3<=r<d)
Use JB's full observer: q>=64, d>=2, d^2<=4q, u=q+d, m=2q+d, R_n(k)=prod_(i=0..k-1)(n-i)/(n+i+3). With l=d-k, a_k=(k+1)(l+1)R_u(k)R_m(l), b_k=(k+1)l R_u(k)R_m(l-1) for l>=1, zero otherwise; v_k=(u-k)(u+k+2)/(2u(2u+1)). V=sum a, Q=sum b, A=sum v(a+b), E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/(2u(2u+1)(4m+2)). W=A+E, Z=qA+Q+V. Y=q(4q+3d+1)^2 WQ/[(3q+d+1)Z^2]; C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. Z>0 on primal domain by JB.

Define j=d-r, N=2q+2d-r+2=m+j+2, T=R_m(j). For p|N, p>4d+6 and t=v_p(N), set q0=-d+(r-2)/2, u0=(r-2)/2>0, m0=-j-2. Only the second-branch denominator at index j-1 is a nonunit. At the formal pole, all other raw denominator factors and exterior denominators (clearing 2 where necessary) are nonzero integers of magnitude <=4d+6; second-branch numerator factors are nonzero and of magnitude <=2d+1. First-branch numerator zeros are allowed (not used as units). Thus v_p(T)=-t. For h>=0, the regular ratio R_m(j+h)/T at q0 is c_h=(-1)^h binom(2j+h+1,h), via the exact consecutive-product recurrence. For l<j the normalized second branch vanishes mod p.

The reduced fiber is k=0..r, l=d-k, h=r-k, U_k=R_{u0}(k),
a*_k=(k+1)(l+1)U_k c_h,
b*_k=(k+1)l U_k c_(h-1) for h>=1, else 0,
v*_k=(u0-k)(u0+k+2)/(2u0(2u0+1)).
V*=sum a*, Q*=sum b*, A*=sum v*(a*+b*), E*=0, Z*=q0 A*+Q*+V*.
Here E is regular before normalization and E/T=0 mod p, not an assumption that E vanishes for primal q or higher jets.
Then (V,Q,A,E,Z)/T reduces componentwise to (V*,Q*,A*,0,Z*) mod p. Consequently C/T^2 reduces to
G2_r(d)=3q0(4q0+3d+1)^2 A*Q* -32(3q0+d+1)(Z*)^2.
If G2_r(d) !=0 mod p then Y!=32/3, even if Z* vanishes. Cost O(r) modular operations given the prime, not a bound for finding primes. When r is even, u0=r/2-1 is a nonnegative integer; U_k=0 for k>=r/2, so only r/2 fiber positions survive. For odd r the U_k may change sign but are all defined. r=1,2 are excluded because exterior denominators may couple to the pole; r=1 is JA's already established coupled certificate, r=2 remains separate.

## 2. Uniform positivity for growing second-branch offsets
For d>=30, 3<=r<=floor(d/10), G2_r(d)>0. Proof:
|c_(h-1)/c_h|=h/(2j+h+1)<=1/18. |U_(k+1)|<=|U_k| by |u0-k|/(u0+k+3)<=1. Put B_k=v*_k U_k; then
B_(k+1)=B_k (u0-k-1)/(u0+k+2),
an exact identity also at zeros, since it follows by product multiplication without dividing by B_k. Hence |B_(k+1)|<=|B_k|. Each of the four sums V*, Q*, Av=sum v*a*, Aq=sum v*b* has successive term absolute value at most 1/9 of its predecessor (factor (k+2)/(k+1)<=2, l or l+1 decreases, c ratio <=1/18; zero tails persist). Each differs from its first term by at most 1/8 of that first term's absolute value. V* has sign (-1)^r, Q* has sign (-1)^(r-1). B_0=v0=(u0+2)/(2(2u0+1))>0; Av and Aq have opposite signs, and |Aq_first|/|Av_first|=d|c_(r-1)|/((d+1)|c_r|)<=1/18. Therefore
(-1)^r A*>0, |A*| >= (7/8-9/(8*18)) v0(d+1)|c_r| = (13/16) v0(d+1)|c_r|;
|Q*| >= (7/8)d|c_(r-1)|.
Now q0<0, 3q0+d+1<0, 4q0+3d+1=-d+2r-3 !=0. A*Q*<0 makes the first term of G2 strictly positive, and its second term nonnegative. This is independent of E's sign in the first-branch proof. The contrast is structural: here the A* and Q* joint signs alone suffice because E is regular at this pole. No signed mass has been replaced by unsigned mass; absolute bounds only pay the tail of the actual signed sums.

## 3. Small-offset denominator and height
Let L(n)=lcm(1,...,n), D=4(r-2)(r-1)L(3r+2). For every k<=r, den(U_k)|L(3r+2). If r is even, U_k=0 for k>u0 and otherwise the two consecutive integer intervals in R have equal lengths; counts of multiples of p^a differ by at most one. If r is odd, use U_k=prod_(i<k)(r-2-2i)/(r+4+2i); all factors odd and nonzero; for odd prime powers the arithmetic progressions of step 2 again have counts differing by at most one. Denominator factors are positive <=3r+2. Thus any denominator exponent is at most floor(log_p(3r+2)); this proves divisibility including prime 2. The additional v denominator divides 4(r-2)(r-1), so D clears V*, Q*, A*, E*. Use Dbar=2D to also clear Z*=q0 A*+Q*+V* when q0 is half integral. This clears all six outputs including W*. P=2 Dbar^2 G2 is a positive integer (the coefficients of G2 have denominator at most 2), with no denominator prime >4d+6.

Since log L(3r+2)=O(r) by the elementary Chebyshev estimate, log Dbar=O(r+log r). The tail estimates in section 2 imply |V*|,|Q*|,|A*|=O(d |c_r|) uniformly, |Z*|=O(d^2 |c_r|). Thus 0<G2=O(d^5 c_r^2). As |c_r|=binom(2d-r+1,r)<=(e(2d+1)/r)^r, log P=O(r log(ed/r)+log d). The number of primes p>4d+6 that divide P is O(1+r log(ed/r)/log d). This supplies the JF-quality exception budget for an independent second-branch family with lower prime threshold. The denominator itself has log-height O(r), independent of d for fixed offset. For r even, exact numerator zeros give further truncation; no division by a zero first-branch factor is used.

Correction to the optional stronger D assertion: only Dbar is used in the proof; finite checks below happen to show D clears Z for the tested cases, but no general claim about that smaller denominator is needed. Reported P bit lengths use the tested D, not Dbar; Dbar changes P by factor 4.

## 4. Consequences and limitations
For fixed d large and q in an arbitrary interval of length O(d), q comparable to d^2, choose R=Theta(d/log d) with sufficiently large constant. The coordinates N=2q+2d-r+2 for 3<=r<=R are consecutive; JE's deterministic binomial window lemma (as used in JF) yields Omega(R) coordinates with p>B for B a suitable constant times d greater than sqrt(max N),4d+6. For fixed r and exceptional p>B the congruence 2q+2d-r+2=0 mod p has O(1) solutions in that interval. Sum the section 3 budget over r and divide by a fixed positive fraction of R as in JF: all but O(d log log d/(log d)^2) q have Omega(d/log d) surviving certificates in this second family. This is an independent local family, not a proof of smaller intersection of first/second failure sets. The same argument for the common band around floor(s sqrt q), shifting r by 2(d-d0), gives JF's global exception order O_s((k+1) X log log X/(log X)^2) for k<=R/8 and R=Theta(sqrt X/log X). Distinct coordinates at one q are charged to distinct (q,d,r) failure triples. No independence assumed.
Open: exploit exact compatibility between the two families' exceptional divisibility (including r=2 exterior coupling), determine whether first/second failure sets intersect at all on the critical band; all-budget equality exclusion and inverse-polynomial real separation remain unresolved.

## 5. Executed exact checks
Python Fraction, math.comb/lcm and sympy.primerange. Uniform triangle d=30..200, 3<=r<=floor(d/10): 1548 checks, plus four large cases. P=2D^2G2 bit lengths for (d,r)=(1000,100):2068; (10000,1000):20087; (10^30,40):8607; (10^60,60):25055. Full original observer crosscheck d=5..23, 3<=r<d, primes 4d+6<p<500, N in {p,2p,p^2} with correct parity and q legal: 20728 comparisons of all six normalized outputs; 115 zero mod-p cross-residues (not equality). All assertions passed. Unbounded conclusions use the analytic proof. Exact replay:
```python
from fractions import Fraction as F
from math import comb, lcm
from sympy import primerange

def rr(n,h):
    a=[F(1)]
    for k in range(h): a.append(a[-1]*(n-k)/(n+k+3))
    return a

def residue(d,r):
    j=d-r; q=F(r-2,2)-d; u=q+d; m=2*q+d
    c=[(-1)**h*comb(2*j+h+1,h) for h in range(r+1)]
    U=rr(u,r); V=Q=Av=Aq=F(0)
    for k in range(r+1):
        l=d-k; h=r-k
        a=(k+1)*(l+1)*U[k]*c[h]
        b=(k+1)*l*U[k]*c[h-1] if h else F(0)
        v=(u-k)*(u+k+2)/(2*u*(2*u+1))
        V+=a; Q+=b; Av+=v*a; Aq+=v*b
    A=Av+Aq; Z=q*A+Q+V
    G=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
    return (V,Q,A,F(0),Z,G),U,Av,Aq,c

def full(q,d,r):
    q=F(q); u=q+d;m=2*q+d; U=rr(u,d); M=rr(m,d); T=M[d-r]; V=Q=A=F(0)
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*M[l]; b=(k+1)*l*U[k]*M[l-1] if l else F(0)
        v=(u-k)*(u+k+2)/(2*u*(2*u+1)); V+=a;Q+=b; A+=v*(a+b)
    E=U[d]*(u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2)/(2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
    return V/T,Q/T,A/T,E/T,Z/T,G/T**2

def mod(x,p): return x.numerator*pow(x.denominator,-1,p)%p

def check(d,r):
    (V,Q,A,E,Z,G),U,Av,Aq,c=residue(d,r); u=F(r-2,2); v0=(u+2)/(2*(2*u+1))
    assert (-1)**r*V>0 and (-1)**(r-1)*Q>0 and (-1)**r*A>0 and G>0
    assert abs(A)>=F(13,16)*v0*(d+1)*abs(c[r])
    assert abs(Q)>=F(7,8)*d*abs(c[r-1])
    L=lcm(*range(1,3*r+3)); D=4*(r-2)*(r-1)*L
    assert all(L%a.denominator==0 for a in U)
    assert all((D*x).denominator==1 for x in (V,Q,A,E,Z))
    P=2*D*D*G; assert P.denominator==1 and P>0
    return int(P).bit_length()

if __name__=='__main__':
    count=0
    for d in range(30,201):
        for r in range(3,d//10+1): check(d,r);count+=1
    print('uniform checks',count)
    for d,r in [(1000,100),(10000,1000),(10**30,40),(10**60,60)]: print('large',d,r,check(d,r))
    count=exc=0
    for d in range(5,24):
        for r in range(3,d):
            a=residue(d,r)[0]
            for p in primerange(4*d+7,500):
                for N in (p,2*p,p*p):
                    if (N-2*d+r-2)%2: continue
                    q=(N-2*d+r-2)//2
                    if q<64 or d*d>4*q: continue
                    b=full(q,d,r)
                    assert [mod(x,p) for x in a]==[mod(x,p) for x in b],(d,r,p,q)
                    count+=1;exc+=mod(a[-1],p)==0
    print('full crosschecks',count,'zero residues',exc)
```
