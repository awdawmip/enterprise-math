# R284HE — Exponentially accurate strip reduction and eventual exact integer transition

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag word-count model only, no new native physical attribution. Original own registration r1-20261124-0256-r284gd-session-v1 returned SUCCEEDED (EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4); own recovery_status confirmed open, metadata only, no runs. Current owner query r284he-20261125-0400-owner-read-v1 RUNNING at observation, no shared CLAIM or formal task mutation. Current GK main e347f36aa5baf89f338c69a503aee6d18f305e9d entries verified; project control snapshot bf6a742b787423c09619371fa5ec6eef9380f019. P000 V5 and ACTIVE worldview unchanged. Frozen scientific inputs: HD 267803d6806a40ffb1570cf98f664f69b1189249:research_notes/portable_direct/R284HD_EVENTUAL_UNIQUE_TRANSITION_AND_INTEGER_ROUNDING_20261125.md, GU f14ef36840c37d78c1537c930f192fdb43d3b094:research_notes/portable_direct/R284GU_UNIFORM_FLEXIBILITY_AND_CRITICAL_SHIFT_20261124.md, HA/HC as pinned in HD. No repinning. HD's eventual global sign-transition theorem is an author-proved dependency, independent review pending.

## Results

For u integer and 0<=q<u use H=u+2q+1, J=3u+q, K=PQ(J+1)^2/(S^2 H) as in HD. For any bounded k=q-6 sqrt(u), uniformly,
K = 1 -(k/3+169/9)/sqrt(u) + (k^2/12+67k/18+17357/54)/u + O(u^(-3/2)).
At k=-169/3 the coefficient of 1/u is 13543/36. Thus an exponentially accurate rational surrogate has its crossing at
q = 6 sqrt(u)-169/3+13543/(12 sqrt(u))+O(1/u).

Combining the expansion with HD gives the following stronger exact integer theorem, for every sufficiently large integer u, with no exceptional set and no tie:
q_max(u) = floor(6 sqrt(u+13543/36)-169/3)
         = (isqrt(324*u+121887)-169)//3.
This is the largest q with K>1. Every larger q in the low-omission domain has K<1. No explicit onset is asserted. Full finite-domain monotonicity remains open.

## Exact strip reduction with exponentially bounded excluded residual

Use the GU corridor for each (A,B,C), e=A-2q, s=2u+1-(C-2q), t=e-s (1 for S, 0 for P,Q), h=B-q-s. Safe path vertices (a,b) obey
[e-a]_+ + [b-q]_+ >= s, b<=h+[a-q]_+.
The orientations are S=(H,J,H), P=(H-1,J+1,H), Q=(H,J+1,H-1).
For q>=1 cut immediately after the q-th B; at that point a=r<=t is necessary (when a>t the lower constraint demands b>=q+1). Prefixes with r A's have multiplicity binom(q+r-1,r), and all are safe for sufficiently large u and q<=u/8 because h grows linearly. For q=0 cut at the initial point only. Remaining inventories are a0=A-r, b0=B-q. Define x=t-r and height of remaining prefixes as x+b'-a'. The stronger corridor requires height >=0 and height <= W=b0-a0+x+t. Endpoint height W-t. It implies both original rules; the two rules coincide with the stronger lower and upper bound respectively except for a>e and a<q. Preserve these two excluded classes, not an assertion that the original paths equal strip paths.

The exact strip count is
L(a0,b0;x,t)=binom(n,a0)-binom(n,a0-x-1)-binom(n,a0-t-1)+binom(n,a0-x-t-2), n=a0+b0.
Proof: kill the nearest-neighbor walk at -1 and W+1; the reflected-image kernel is the sum over j in Z of [binom(n,a0+j(W+2))-binom(n,a0-x-1+j(W+2))]. This follows by Pascal recurrence, zero boundary via reflection and the single initial delta (equivalently odd periodic extension of the initial delta). With q<=u/8 and large u, W+2>a0+x+1 and 2(W+2)>b0+x+1, so only j=0,1 can contribute; complement the binomials at j=1 to obtain the four displayed terms.

For the original safe paths excluded by the strip, a lower violation is possible only after a>e (prefix length at least e-r), and an upper violation only at a<q (reversed suffix length at least A-q). Both lengths are >=u-O(1). Lower violation requires more A than B in the relevant prefix; upper violation likewise requires more A than B in the reversed suffix (initial reversed height t). Under uniform shuffling of the remaining inventory, A-fraction p<=1/3 for all sufficiently large u, q<=u/8. For a prefix/suffix of length l, X number of A, E[2^X] <= (1+p)^l by expanding the product of 1+indicator_A and bounding sampling-without-replacement factorial probabilities by p^j. Markov gives Pr(X>l/2)<=((4/3)/sqrt(2))^l. Sum the geometric tail from u-O(1), and union the two violations: <=C exp(-cu), uniformly in q,r and orientation. The strip count divided by binom(n,a0) is bounded below by a positive constant for large u: its four-term expression tends uniformly to (1-rho^(x+1))(1-rho^(t+1)) with rho=a0/b0 bounded away from 1. Consequently the original safe count = strip count times (1+O(exp(-cu))), even after summing the positive prefix multiplicities. This is an observation-specific approximate BRC positive-branch quotient with explicitly bounded excluded path mass, not a state equivalence or independent endpoint approximation.

Let L as above. Then the three strip sums are exactly
S0=L(H,3u;1,1)+q L(H-1,3u;0,1),
P0=L(H-1,3u+1;0,0), Q0=L(H,3u+1;0,0).
Each is <= its original count, relative error O(exp(-cu)). K0=P0 Q0 (J+1)^2/(S0^2 H) is rational and K=K0(1+O(exp(-cu))).
Eliminate common binom(D,H), D=H+3u. Define R_j(a,b)=product_{i=0}^{j-1}(a-i)/(b+i+1), T(a,b;x,t)=1-R_(x+1)-R_(t+1)+R_(x+t+2). Then normalized strip sums are
s0=T(H,3u;1,1)+q H/D T(H-1,3u;0,1);
p0=H/(3u+1) T(H-1,3u+1;0,0);
q0=(D+1)/(3u+1) T(H,3u+1;0,0).
K0=p0*q0*(J+1)^2/(s0^2 H).
This evaluates with a fixed number of rational operations, no binomial-size integer or convolution loop. Bit cost depends on the integer inputs; this is for the approximate K observer in the stated region only.

## Critical expansion

Set z=1/sqrt(u), q=6/z+k. Expand the rational functions (all denominators have nonzero leading coefficient after scaling; remainders uniform for bounded k):
z*s0=8/9+(4k/27+64/81)z-2696/27 z^2+O(z^3);
p0=4/27-428/27 z^2+O(z^3);
q0=16/27-16/3 z+(-8k/9-8/27)z^2+O(z^3).
Also z^2*(J+1)^2/H=(3+6z+(k+1)z^2)^2/(1+12z+(2k+1)z^2).
Multiplication gives the announced K expansion; the exponential error is smaller than any fixed power. Substitution k=-169/3 gives 13543/36, so the root correction is 13543/12. The rational surrogate has a local smooth root by the implicit function theorem applied in k at z=0 to (K0-1)/z. Exact K is defined only at integer q; no continuous interpolation of K is assumed.

## Removing the integer resonance set

Put C=13543/36, h=6 sqrt(u)-169/3, delta=q-h. For bounded delta, the proved expansion reads
K-1=-delta/(3 sqrt(u))+C/u+O(|delta|/u+u^(-3/2)).
If |delta|>=M/sqrt(u) with a sufficiently large fixed M, the first term dominates both C/u and the remainder, and the sign agrees with q versus h+3C/sqrt(u). In the remaining strip |delta|<M/sqrt(u), define integer
E=324u+121887-(3q+169)^2.
Then E/(324u)=-delta/(3sqrt(u))+C/u-delta^2/(36u), so K-1=E/(324u)+O_M(u^(-3/2)). E is congruent to 2 modulo 3 and cannot be zero. Its absolute value is at least 1, so for sufficiently large u the sign of K-1 is exactly the sign of E. The same sign agreement holds outside the small strip within bounded delta because the linear term dominates. Thus the two integers bracketing 6 sqrt(u+C)-169/3 have strict opposite signs (the real expression is never integral since E cannot be zero). HD's eventual monotone wedge and global upper bound extend those signs to every earlier/later q. No density-zero exceptions remain. Integer evaluation uses isqrt(324u+121887), then subtract 169 and floor-divide by 3. This theorem is asymptotic with an unspecified onset, not a statement for moderate finite u.

## Executed evidence and reproduction

Python exact integers and Fractions: for 8<=u<=64, 0<=q<=floor(u/8), checked all 867 orientation counts against the exact HA moment formula: 867 positive strip counts <= original counts, 171 equal, largest relative excluded fraction 0.000596637412735404. This is a finite check of the reduction, not the exponential proof.
Exact original K and strip K0 at (u,q)=(256,94),(256,95),(1024,168),(1024,169),(4096,344),(4096,345) agree to displayed decimals, with relative K0-K about -9.64e-20,-1.84e-19,-7.25e-156,-3.46e-155 and below floating rendering for the last two. At u=4096 the formula's q=344 is not yet the true boundary (K=0.9770697799681056), so an explicit onset remains important.
Constant-size rational K0 at the predicted boundary q and q+1:
u=65536 q=1484: 0.9995461044145784,0.9981645019189459
u=1000000 q=5944: 1.000259887770165,0.9999209241055578
u=100000000 q=59943: 1.0000260189895527,0.9999926286064439
u=10000000000 q=599943: 1.000002260219811,0.9999989263169281
u=1000000000000 q=5999943: 1.0000002226022282,0.9999998892632003
These last rows are exact rational surrogate values, not evaluated original path counts. Near-resonance finite-size signs can differ before the eventual onset, e.g. u=27781018237,q=1000002 gives E=50 and u*(K0-1)=0.0955197056283156 (leading E/324=0.15432098765); u=27780962678,q=1000001 gives E=-25 and u*(K0-1)=-0.1359854407418194.

```python
from math import comb,isqrt
from fractions import Fraction as F

def strip(a,b,x,t):
    def c(j): return comb(a+b,j) if 0<=j<=a+b else 0
    return c(a)-c(a-x-1)-c(a-t-1)+c(a-x-t-2)
def strip_counts(u,q):
    H=u+2*q+1
    return strip(H,3*u,1,1)+q*strip(H-1,3*u,0,1),strip(H-1,3*u+1,0,0),strip(H,3*u+1,0,0)
def moments(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        a.append(a[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return a
def counts(u,q):
    d=u-q;m=u+q;g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    def C(a,b,g): return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
    Q=C(A,B,d-1);S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1))
    P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
    return S,P,Q
def K_from_counts(u,q,v):
    S,P,Q=v
    return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))
def K0(u,q):
    H=u+2*q+1; D=H+3*u; L=3*u+q+1
    def T(a,b,x,t):
        def R(k):
            p=F(1)
            for j in range(k): p*=F(a-j,b+j+1)
            return p
        return 1-R(x+1)-R(t+1)+R(x+t+2)
    S=T(H,3*u,1,1)+q*F(H,D)*T(H-1,3*u,0,1)
    P=F(H,3*u+1)*T(H-1,3*u+1,0,0)
    Q=F(D+1,3*u+1)*T(H,3*u+1,0,0)
    return P*Q*F(L*L,H)/S**2
def predicted(u): return (isqrt(324*u+121887)-169)//3
if __name__=='__main__':
    n=eq=0;err=F(0)
    for u in range(8,65):
        for q in range(u//8+1):
            for v,w in zip(counts(u,q),strip_counts(u,q)):
                assert 0<w<=v
                n+=1;eq+=v==w;err=max(err,F(v-w,v))
    print(n,eq,float(err))
    for u in (256,1024,4096):
        for q in (predicted(u),predicted(u)+1):
            K=K_from_counts(u,q,counts(u,q))
            assert K0(u,q)==K_from_counts(u,q,strip_counts(u,q))
            print(u,q,float(K),float(K0(u,q)),float((K0(u,q)-K)/K))
    for u in (65536,10**6,10**8,10**10,10**12):
        q=predicted(u);print(u,q,float(K0(u,q)),float(K0(u,q+1)))
```
Symbolic series independently executed with SymPy on these finite rational products, using z=1/sqrt(u), scaling numerator and denominator by z^2, and expanding to order z^2; coefficients are printed above. Can be reproduced by direct substitution or series expansion.

## Continuation

The eventual integer classification is now exact for all sufficiently large budgets; next compute a rigorous effective onset using rational polynomial inequalities, explicit exponential tail constants and congruence gaps, and independently review HD/GU dependencies. Full finite-domain monotonicity and possible moderate-budget exceptions remain open. Preserve original joint path residual for other observers; strip truncation applies to total count only. No formal Result, review, or shared claim is asserted.
