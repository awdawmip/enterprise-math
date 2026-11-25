# R284HY — Capacity-increment coupling and effective square-root-domain monotonicity

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer; same scope as HX, no native physical attribution. Frozen scientific inputs: HX at 1aebe9404d585d9573188649d124a802181131f3:research_notes/portable_direct/R284HX_PARABOLIC_BASELINE_AND_LOGARITHMIC_RESIDUAL_20261125.md; HP at 3a29820d72c053c4a5a71e303244ce747a08be38:research_notes/portable_direct/R284HP_EXACT_TILTED_PORT_COUPLING_20261125.md; HT at d9a5329739c288770a164382c7b8b1992d886c65:research_notes/portable_direct/R284HT_TERMINAL_PORT_EXACT_REDUCTION_20261125.md. HU exact K identity retained through HX. Global canonical main entries read at 8aa98b1afbd406b2c5a45ad80b755062ae23a00b; current EM continuation/portable/method, P000 V5, Heartbeat, ACTIVE worldview, joint preservation and residual policy read. Own session recovery r1-20261125-2255-own-recovery: original RESEARCHER registration SUCCEEDED, open, metadata only, RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Original inventory r1-20261125-2255-owner-read SUCCEEDED, as_of 2026-11-25T14:56:41.737718Z, Source 817b1405a3350c5b1cb904c2b591611d009903b1, no LEASED entries in the returned snapshot; Source changed by completion. No shared CLAIM or Result mutation.

## Main theorem

For integer u,q with 0<=q<u and d=u-q, if d^2>=441u, both true ratios K(q,u+1)/K(q,u) and K(q,u)/K(q+1,u) exceed 1+1/[8(u+1)]. The condition implies u>=441 and d>=441? Only d>=21 sqrt(u)>=441, so the neighbor is valid. In the direct band d<=u/100 the stronger margin 1+1/[2(u+1)] holds. This removes the logarithmic factor in HX's sufficient boundary for the true K, with an explicit square-root constant 21. Remaining smaller-deficit band is open as an effective uniform proof problem, apart from existing fixed strips and finite verification. A second result improves the signed residual bound in the parabolic baseline region to 16 exp(-36d^2/(625u)), rather than a prefactor growing like u^2/d^2.

## Definitions and exact factorization

M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n, zero otherwise. C_(n,m)(g)=sum_k M_n(k)M_m(g-k). At (U,Qp) let n=U, m=U+Qp, h=U-Qp, Q=C_(n,m)(h-1), V=C_(n,m)(h), A=C_(n-1,m)(h)+C_(n-1,m)(h-1), E=M_(m-1)(0)[M_(n-1)(h)+M_(n-1)(h+1)], L=(3U+Qp+1)^2/(U+2Qp+1). HX/HU give K=L (A+E)Q/(Q+V+Qp A)^2. Set b=V/Q, alpha=A/(Q+V), e=E/A. Then exactly

K=L * [1/(1+b)] * [alpha/(1+Qp alpha)^2] * (1+e).

Introduce the joint law of (k,l,z), z in {0,1}, k+l+z=h, proportional to M_n(k)M_m(l). This is the true joint population for Q+V, not an independent product after conditioning. Since

M_(n-1)(k)/M_n(k)=v_n(k)=((n+1)^2-(k+1)^2)/(2n(2n+1))

including zero at k=n, alpha is exactly E[v_n(k)] under this law. The extra boundary E is retained, not absorbed into this observation.

## Proof 1 — exact capacity-increment coupling

Every port sequence M_n has positive integer-interval support and decreasing consecutive ratios [(k+2)/(k+1)] [(n-k)/(n+k+3)]. A convolution of two such log-concave sequences with interval support is log-concave. For completeness, the Toeplitz matrix with entries a_(j-i) has nonnegative 2x2 minors: the diagonal subscripts lie between the off-diagonal subscripts and their sums agree; monotone successive ratios give the product inequality, also with interval-support zeros. The product of the two Toeplitz matrices gives the convolution, and the 2x2 Cauchy-Binet formula is a finite sum of nonnegative products for these finite sequences. This also applies to convolution with the dummy sequence (1,1).

For a conditioned pair with masses M_n(k) B(h-k), where B is any nonnegative log-concave interval-support sequence, let mu and nu be the laws at n and n+1, fixed h in the old support. On common positive support

M_(n+1)(k)/M_n(k)=2(n+1)(2n+3)/[(n+1-k)(n+k+3)]

is increasing in k, while

M_(n+1)(k+1)/M_n(k)=2(n+1)(2n+3)(k+2)/[(k+1)(n+k+3)(n+k+4)]

is decreasing in k. Also B(h-k-1)/B(h-k) is decreasing in k. Thus nu(k)/mu(k) is increasing, whereas nu(k+1)/mu(k) is decreasing (normalizations are constant). The supports are intervals; the lower endpoint of nu is the same as mu, the upper endpoint grows by at most one. For the shifted law nu(k+1), the endpoints instead move left by at most one. The single-crossing likelihood ratio argument in HP yields F_mu(k-1)<=F_nu(k)<=F_mu(k) for every integer cut. Using one uniform quantile gives K_new-K_old in {0,1} almost surely. This is exact even at support boundaries. The same proof as HP for increasing h by one uses the increasing likelihood ratio B(h+1-k)/B(h-k) and the reverse-port order to obtain the same coupling; this requires only log-concavity and interval support, not the particular M sequence.

For the three-port law above, use B=M_m*(1,1) to couple the k marginal when n or h increases. When m increases, couple the l marginal using B=M_n*(1,1); l increases by 0 or 1. Given l, the conditional pair (k,z) has masses M_n(k) times the dummy, with sum h-l. Couple these conditional pairs by the adjacent-sum rule. Consequently k decreases by 0 or 1 in the m-increment step. This preserves the relevant joint conditional laws. By composing the three transitions, on the read step (n,m,h)->(n+1,m+1,h+1), the k coordinates differ by at most 2; on the omit step (n,m,h)->(n,m+1,h-1), k decreases by 0,1 or 2. In particular alpha on the omit step is nondecreasing. This extends HP's total-resource coupling to actual capacity shifts; it supplies a direct adjacent bound without paying two unrelated absolute moments.

## Proof 2 — improved weighted-tail payment

Reuse HT's signed-extension identity with N=a+1, M=b+1, S=2(N+M), j=a+b-g. Let J be the first-class count in a uniform j-subset of a population with class sizes 2N,2M. The signed weight is w=(1-J/N)(1-(j-J)/M); the real count truncates to J<=N-1 and j-J<=M-1. R=binom(S,j) f(S,g), f=[4(g+2)^2-S]/[S(S-1)], and C-R equals the omitted negative mass with its sign reversed. Let X=J-EJ, p=(g+2)/(N+M), so the two factors are p-X/N and p+X/M. On every omitted nonzero branch one factor is negative, and p<=|X|/min(N,M). In the three HX locations (u,q), (u+1,q), (u,q+1), assume u>=64, d>=36, d^2>=16q. Then d^2>=11u, since u=q+d<=d^2(1/16+1/36)=13d^2/144<d^2/11. For each of the four convolution terms of Q,V,A, min(N,M)>=u, N+M<=3u+3, S<=7u, 0<=j<=25u/8, g+2>=d. Thus f>d^2/(17u^2). The distance from either class mean to its first forbidden layer, even minus one, is >=[u/(3u+3)]d-1>=(3/10)d; the last follows from u>=64,d>=36.

On an omitted branch, |w|<=2 X^2/u^2: the negative factor has magnitude at most |X|/u, and the other at most 2|X|/u. HX's hypergeometric Hoeffding bound (apply also to the other class) gives Pr(|X|>=s)<=2 exp(-2s^2/j) for j>0; j=0 has no tail. For B=3d/10 the tail-moment identity gives

E[X^2 1_{|X|>=B}] <= 2(B^2+j/2) exp(-2B^2/j).

Indeed integrate the tail of X^2 from B^2, retaining B^2 Pr(|X|>=B). Therefore

0<=C/R-1 <= 68(B^2+j/2)/d^2 * exp(-2B^2/j)
 < 16 exp(-36d^2/(625u)),

using 68(9/100+25/176)<16 and j<=25u/8. This preserves the signed branch weight instead of replacing it by 1; it removes the growing prefactor. For E, HX's port-ratio argument applies since h>=d-1 and 2h^2+6h+3>U-1. If h>U-1 E=0; otherwise E<=2 M_(U-1)(h)M_m(0) (M_(m-1)(0)<=M_m(0) by Catalan ratio). In the convolution C_(U-1,m)(h), that endpoint has second class count M-1 and corresponding factor 1/M<=1/u, with other factor <=1. Its distance above the mean is >=B. The single-tail bound and f give E/A_signed <=34u/d^2 exp(-36d^2/(625u))<16 exp(-36d^2/(625u)).

Let delta=16 exp(-36d^2/(625u)), common to the three locations. All signed counts are positive. With the same rational K0 and parabolic certificate of HX, every true-to-baseline ratio is between (1+delta)^(-2) and (1+2delta)(1+delta). For delta<1/[100(u+1)], the quotient loss is <=(1+delta)^3(1+2delta)<=1+6delta (expand, valid delta<=0.1). HX's baseline margin 1+1/[4(u+1)] then transfers to a true margin >1+1/[8(u+1)]. In particular it suffices that

d^2 >= (625/36) u ln(1600(u+1)), together with u>=64,d>=36,d^2>=16q.

Equality in the logarithmic condition is harmless because the actual payment estimates are strict: one can use the actual common error bound strictly below delta. This is an explicit improvement of HX's logarithmic boundary.

## Proof 3 — direct square-root band, without signed-tail payments

Assume d^2>=441u and d<=u/100; hence u>=(2100)^2=4410000. Write s=sqrt(u). We prove the stronger true margin 1+1/[2(u+1)]. No use of HS eventual onset is required.

First control the boundary e=E/A in all three locations. In each let a=U-1 in {u-1,u}, h=U-Qp in {d-1,d,d+1}, m>=u. Here h<=a because Qp>=1. For each integer j in [ceil(s/3),floor(s/2)], every k from h-j to h-1 satisfies k>=20s and k<=d+1. The same estimate applies to k=h if the following moment is supported. Since a+k+3<=51u/50 and k^2>=400u,

M_a(k+1)/M_a(k)
 <=1+1/(k+1)-(2k+3)/(a+k+3)
 <=1-(100/51-1/400) k/u
 <=1-36/s.

Consequently M_a(h-j)/M_a(h)>=exp(36j/s)>=exp(12). The m port ratio product is M_m(j)/M_m(0)=(j+1) prod_(i=0)^(j-1) (1-(2i+3)/(m+i+3)). The product is at least 1-(j^2+2j)/u>=1/2 by the elementary product inequality. There are at least s/8 such integer j (s>=24), and j+1>=s/3. Summing these distinct actual joint branches gives

A >= C_(a,m)(h) >= (u/48) exp(12) M_a(h)M_m(0).

Since E<=2 M_a(h)M_m(0) as before, we obtain 0<=e<1/(128u) at all three locations (96 exp(-12)<1/128, already (5/2)^12>96*128). This bounds the independent boundary correction absolutely at the required adjacent scale.

Next, b=C(h)/C(h-1). By convolution log-concavity, b decreases when h increases with capacities fixed. By HP's exact mixed transport bound, at h=d a unit capacity increment multiplies b by at most 1+(2d+1)/[(n-d+1)(n+d+3)] <= 1+1/(40u), using n>=u,d<=u/100,u>=1000; the m increment is symmetric. Thus on the read step b_read/b<=(1+1/(40u))^2<=1+1/(16u). It follows that (1+b)/(1+b_read)>=1/(1+1/(16u)). On the omit step b_omit>=b by log-concavity and HP's nonnegative capacity transport. All relevant g=h-1 are interior in these applications.

For alpha, the formula v_n(k)=(1/4+3/(8n+4))-k(k+2)/(2n(2n+1)) shows alpha>=1/5 in all three locations, since k<=d+1 and n>=u. The capacity/total coupling in Proof 1 yields
|alpha_read-alpha| <= (2d+5)/(2u^2)+3/(8u^2)+(d+1)(d+3)/u^3 <1/(60u).
Here the first term is the cost of moving k by at most two using the exact discrete derivative of v; the second is the change in its constant term; the third uses |1/[2u(2u+1)]-1/[2(u+1)(2u+3)]|<=1/u^3. For u>=1000 the displayed sum times u is at most 1/100+1/400+3/8000+143/1000000<1/60. Hence alpha_read/alpha<=1+1/(12u). At fixed q the function H_q(x)=x/(1+qx)^2 decreases for qx>=1 (here q>=99u/100, x>=1/5). If alpha_read<=alpha, H_q(alpha_read)/H_q(alpha)>=1; otherwise it is >=alpha/alpha_read>=1/(1+1/(12u)). The omit coupling gives alpha_omit>=alpha, so H_(q+1)(alpha_omit)<=H_(q+1)(alpha), while
H_q(alpha)/H_(q+1)(alpha)=(1+1/(q+1/alpha))^2>=1+2/(u+5)>1+1/(u+1).

Finally L(u,q)=(3u+q+1)^2/(u+2q+1). At fixed q<=u, its log derivative in x>=u exceeds 1/(x+1): the difference after positive cross multiplication has numerator 4xq+4x-2q^2+8q+4>0. Integrate on [u,u+1] to get L_read/L>1+1/(u+1). At fixed u, L strictly decreases as q increases through the valid range (differentiate). Combine the exact factorization and the three payments:
K_read/K > [1+1/(u+1)]/[(1+1/(16u))(1+1/(12u))(1+1/(128u))]
 > [1+1/(u+1)]/[1+1/(4u)] > 1+1/[2(u+1)].
The denominator bound follows by expansion, using u>=1; the last inequality by cross multiplication for u>3/2. Similarly K/K_omit > [1+1/(u+1)]/[1+1/(128u)] >1+1/[2(u+1)]. This proves the direct band.

## Proof 4 — effective global stitch

If d^2>=441u, then u>=441, d>=441 (since d<=u); in particular the prerequisites of Proof 2 hold. Put U0=4410000. If d<=u/100 use Proof 3. Otherwise d^2/u>u/10000 and d^2/u>=441. For u<=U0, 1600(u+1)<2^33, ln 2<7/10, so (625/36) ln(1600(u+1)) < (625/36)*33*(7/10)<441. For u>=U0, u/10000-(625/36) ln(1600(u+1)) is increasing, by differentiation, and positive at U0. Thus the sufficient logarithmic condition of Proof 2 holds everywhere outside the direct band. The full true K theorem follows. This is a non-asymptotic square-root-domain result, not merely a compact-window limit.

## Executed exact checks (Python 3)

The script below is the locally executed exact-arithmetic replay. All signs and CDF comparisons use integers or Fraction; decimal conversion is only for display. Finite tests do not replace the analytic proof of the direct band (whose minimum u is 4410000).


```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(maxsize=16)
def ports(n):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(n):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3))
        assert r==0
        a.append(v)
    return a

def C(n,m,g):
    a,b=ports(n),ports(m)
    return sum(a[k]*b[g-k] for k in range(max(0,g-m),min(n,g)+1))
def R(n,m,g):
    S=2*(n+m+2); j=n+m-g
    return F(comb(S,j)*(4*(g+2)**2-S),S*(S-1))
def pair(U,q,u,d):
    m=U+q;h=U-q
    triples=[(U,m,h-1),(U,m,h),(U-1,m,h),(U-1,m,h-1)]
    a,b,c1,c2=[C(*t) for t in triples]
    aa,bb,cc1,cc2=[R(*t) for t in triples]
    for n,m,g in triples:
        N,M=n+1,m+1;S=2*(N+M);j=N+M-g-2
        assert min(N,M)>=u and N+M<=3*u+3 and S<=7*u
        assert 0<=j<=F(25,8)*u and g+2>=d
        assert F(min(N,M)*(g+2),N+M)-1>=F(3,10)*d
        assert F(4*(g+2)**2-S,S*(S-1))>F(d*d,17*u*u)
    c,cc=c1+c2,cc1+cc2
    E=ports(m-1)[0]*sum(ports(U-1)[k] for k in (h,h+1) if k<U)
    eps=F(1,100*(u+1))
    residuals=[v/w-1 for v,w in zip((a,b,c1,c2),(aa,bb,cc1,cc2))]+[E/cc]
    assert all(0<=v<eps for v in residuals)
    fac=F((3*U+q+1)**2,U+2*q+1)
    K=fac*F((c+E)*a,(a+b+q*c)**2)
    K0=fac*cc*aa/(aa+bb+q*cc)**2
    assert (1+eps)**-2<=K/K0<=(1+2*eps)*(1+eps)
    return K,K0,max(residuals)
assert F(68)*(F(9,100)+F(25,176))<16
assert F(34,11)<16 and F(36,625)*13>F(7,10)
assert 1+F(7,10)+F(7,10)**2/2+F(7,10)**3/6>2
ncomp=0; maxres=F(0); mn=None
for u in (256,512,1024,2048,4096,8192):
    d0=1+isqrt(13*u*(1600*(u+1)).bit_length())
    for d in sorted({d0,(d0+u)//2,u}):
        if d>u:continue
        q=u-d
        assert d>=36 and d*d>=16*q and d*d>=11*u
        assert d*d>=13*u*(1600*(u+1)).bit_length()
        a,a0,e1=pair(u,q,u,d);b,b0,e2=pair(u+1,q,u,d);c,c0,e3=pair(u,q+1,u,d)
        assert b0/a0-1>F(1,4*(u+1)) and a0/c0-1>F(1,4*(u+1))
        v=(b/a-1)*(u+1);w=(a/c-1)*(u+1)
        assert min(v,w)>F(1,8)
        ncomp+=2;maxres=max(maxres,e1,e2,e3);mn=min(v,w) if mn is None else min(mn,v,w)
        print(u,q,d, float(v),float(w),float(max(e1,e2,e3)),flush=True)
print('comparisons',ncomp,'min_gap',float(mn),'max_relative_residual',float(maxres))

# Exact CDF cuts for the capacity-coupling theorem with a 0/1 dummy port.
def mass(n,m,h,dummy):
    a,b=ports(n),ports(m)
    return [a[k]*sum(b[h-k-z] for z in range(dummy+1) if 0<=h-k-z<=m) for k in range(n+1)]
def cdf(a,k):
    return F(sum(a[:max(0,k+1)]),sum(a))
checks=0;curv=0;ident=0
for n in range(16):
    for m in range(16):
        for dummy in (0,1):
            for h in range(n+m+dummy+1):
                a=mass(n,m,h,dummy); b=mass(n+1,m,h,dummy); c=mass(n,m+1,h,dummy)
                for k in range(-1,n+2):
                    assert cdf(a,k-1)<=cdf(b,k)<=cdf(a,k)
                    assert cdf(a,k)<=cdf(c,k)<=cdf(a,k+1)
                    checks+=2
                if h+1<=n+m+dummy:
                    b=mass(n,m,h+1,dummy)
                    for k in range(-1,n+2):
                        assert cdf(a,k-1)<=cdf(b,k)<=cdf(a,k)
                        checks+=1
                if 0<h<n+m+dummy:
                    assert sum(a)**2>=sum(mass(n,m,h-1,dummy))*sum(mass(n,m,h+1,dummy))
                    curv+=1
                if n>=1 and dummy==1:
                    v=sum(F(((n+1)**2-(k+1)**2)*w,2*n*(2*n+1)) for k,w in enumerate(a))
                    if h<=n-1+m+dummy:
                        assert v==sum(mass(n-1,m,h,dummy))
                    else: assert v==0
                    ident+=1
print('coupling cut pairs',checks,'log-concavity comparisons',curv,'alpha identities',ident)
# Exact constant checks for the analytic direct band and global stitch.
assert F(100,51)-F(1,400)>F(9,5)
assert F(5,2)**12>96*128
assert F(21,1000)/F(99,100)**2<F(1,40)
assert (1+F(1,40))**2<1+F(1,16)
assert F(1,100)+F(1,400)+F(3,8000)+F(11*13,1000**2)<F(1,60)
assert (1+F(1,16))*(1+F(1,12))*(1+F(1,128))<1+F(1,4)
assert 1600*(4410000+1)<2**33 and F(625,36)*33*F(7,10)<441
print('all constant comparisons passed')
# Additional exact true-K comparisons at the new global square-root boundary.
for u in (512,1024,2048,4096,8192):
    d=1+isqrt(441*u);q=u-d
    assert d*d>=441*u and q>=0
    # The global stitch in this range uses the weighted-tail branch, not the huge direct-band threshold.
    assert d*d>=13*u*(1600*(u+1)).bit_length()
    a,_,_=pair(u,q,u,d);b,_,_=pair(u+1,q,u,d);c,_,_=pair(u,q+1,u,d)
    v=(b/a-1)*(u+1);w=(a/c-1)*(u+1)
    assert min(v,w)>F(1,8)
    print('sqrt',u,q,d,float(v),float(w),flush=True)

```

Observed output summary: 36 true neighbor comparisons in the improved logarithmic sufficient domain; minimum scaled gap 1.0000813812438833, maximum observed relative residual 5.859253861633069e-31. 293376 CDF cut pairs (each checks two inequalities), 7425 log-concavity comparisons, 4200 alpha identities. All constant comparisons passed. Additional square-root boundary samples, scaled read and omit gaps:
|u|q|d|read|omit|
|--:|--:|--:|--:|--:|
|512|36|476|1.1582731405360567|27.62380641458014|
|1024|351|673|1.4629880238937436|7.126964624590375|
|2048|1097|951|1.5224949206818723|4.697166060524437|
|4096|2751|1345|1.5317012099737255|3.7652726929379945|
|8192|6291|1901|1.5286717063961976|3.2909296035647846|

Total 46 true neighbor comparisons, all assertions passed. No finite enumeration at u>=4410000 claimed. Scientific proof is the exact coupling, rational inequalities, and the retained residual bound, plus frozen HX's baseline certificate.

## Next

Focus on the complementary d<21 sqrt(u) band. The exact alpha and b decomposition leaves E/A as the main obstruction to making the direct proof work for small d: its adjacent difference, not its absolute mass, should be bounded. The capacity-increment coupling supplies a way to control the endpoint probability jointly; derive an exact adjacent endpoint-ratio formula and use the favorable b and H_q variation to absorb it, possibly proving the entire remaining central strip uniformly. Preserve fixed d<=24, fixed q<=12 and finite-domain results without recomputation. Review remains NOT_REVIEWED.