# R284JD — Density-one simultaneous non-equality certificates by linear-window amortization

2026-11-27. Author proof, exact finite denominator replay, NOT_REVIEWED. Auxiliary binary-tag joint-count observer; not a native spatial transfer. Independent continuation of the existing direct research line (RA-B82240E8488EF5A1DA5186C4); original session metadata recovered, no runs/claims. No shared task mutation or formal Result/Review. Frozen scientific inputs:
- JC f4abd4b538f733777dc34f187b5236916806a72c:research_notes/portable_direct/R284JC_UNIFORM_GROWING_OFFSET_CERTIFICATES_20261127.md, blob d1ff271ebe73d9ec1f1509eea29459d1b128efa7.
- JB e92de4ef4680b68015e53c4c702fbf929dada0a0:research_notes/portable_direct/R284JB_FIXED_OFFSET_INTERIOR_POLE_FAMILY_20261127.md, blob 9ac16b9644637a8416a050c701568463acb70248.
Use exactly the full original joint observer V,Q,A,E,Z,W,C,Y in JB §1 and its normalized residue G_r(d) in §2. Use JC §1–2 for uniform positivity; no dropping E. P000 V5, joint observer, ACTIVE worldview, portable protocol and current method consulted. External input: Matomäki and Radziwiłł, Multiplicative functions in short intervals, Annals of Mathematics 183 (2016), 1015–1056, DOI 10.4007/annals.2016.183.3.6; arXiv:1501.04585v4 (2017-10-15), Theorem 1 pp. 1–2, verified original statement at https://arxiv.org/pdf/1501.04585 and https://annals.math.princeton.edu/2016/183-3/p06 . This is a new application to the retained observer, not a new proof of the external theorem.

## 1. Main theorem
Fix 0<s<2 and a finite real K>=1. For each positive integer budget q define the band D(q)={integer d: |d-floor(s sqrt(q))|<=K}. For all sufficiently large q all such d are legal (q>=64, 10<=d<=2sqrt(q)). There are constants c>0 and X0 depending on s,K such that, for X>=X0, except O_{s,K}(X/(log X)^(1/50)) integer q in [X,2X], at least c sqrt(X) distinct integers N simultaneously certify Y(q,d)!=32/3 for EVERY d in D(q). Each witness is a common composite coordinate N=q+2d-r_d+2 with 1<=r_d<=floor(d/10), and a prime p|N, p>100 sqrt(X), for which G_{r_d}(d) is a p-unit (nonzero mod p). In particular all candidates in any fixed bounded band around the critical scale are simultaneously certified for a set of budgets of natural density one; possible equality budgets in that band are O_{s,K}(X/(log X)^(1/50)) up to X by dyadic summation. The bound concerns explicit arithmetic certificates, not sign, real gap size, factor discovery runtime or the set of all d in the full legal range.

## 2. New BRC denominator compression and exceptional-prime budget
Let j=d-r, q0=-2d+r-2, u0=-j-2, m0=-M=-3d+2r-4. In the JC uniform region d>=10, 1<=r<=d/10, retain c_h=(-1)^h binom(2j+h+1,h) and every reduced fiber a_h,b_h,v_h,E*. The signed products use
R_{-M}(l)=binom(M+l-1,l)/binom(M-3,l), 0<=l<=r.
This follows by the rising/falling products; M-3>=r. For integer n>=1 every binom(n,l) divides L(n)=lcm(1,...,n): Legendre's formula gives v_p binom(n,l) as a sum of floor differences, each 0 or 1 and vanishing for p^a>n, hence <=floor(log_p n)=v_p L(n). Therefore each raw R denominator divides L(M-3), without multiplying all the consecutive factors. Set
D'=2u0(2u0+1)(4m0+2)L(M-3).
D' clears V*,Q*,A*,E*,W*,Z* simultaneously, by the exact JB/JC formula for the exterior observer and residual. D' is a p-unit for p>20d+20. By JC positivity P'=D'^2 G_r(d) is a strictly positive integer. The Chebyshev bound log L(n)=psi(n)=O(n) gives log |D'|=O(d). Also |c_h|<=2^(2d+1), R_{-M}(l)<= (4/3)^l by JC, and all observer coefficients and the number of terms have at most polynomial growth in d; hence log(1+|G|)=O(d) uniformly. Thus log P'=O(d) and
# {p>20d+20 : p | P'} = O(d/log d)
uniformly for the ENTIRE linear offset triangle. This improves JC's O(r) budget in the linear-r regime. It does not claim an improvement for small fixed r (use min of the two bounds there). This compression is for the exact rational normalized cross-observer only; all original fibers remain the source.

## 3. Amortized exceptional-incidence lemma
For q in [X,2X] and d in D(q), d is comparable to sqrt X and the possible q for any fixed d lie in an interval of length O_{s,K}(sqrt X). For each admissible pair (d,r), the exceptional primes from §2 exceed 20d+20, hence each hits q+2d-r+2 in O_{s,K}(1) such budgets. There are O(sqrt X) possible d, O(sqrt X) possible r per d and O(sqrt X/log X) exceptional primes per pair. Consequently the total number of triples (q,d,r) with any such exceptional prime dividing the coordinate is O_{s,K}(X^(3/2)/log X). This counts incidences rather than discarding a whole budget because one coordinate is bad. By Markov, only O_{s,K}(X/log X) budgets can have more than any fixed positive multiple of sqrt X bad triples. For an arbitrary growing window R=o(sqrt X) the older JC O(r+1) bound alone also suffices: total bad incidences O(sqrt X R^2), and losing a fixed fraction of an R-window costs O(sqrt X R)=o(X) budgets. This improves the older union bound restriction R=o(X^(1/4)) when the goal is existence of a valid witness, not absence of every exceptional coordinate.

## 4. Large-prime witnesses in almost all common windows
Set d0=floor(s sqrt(q)), k=ceil(K), R=floor(s sqrt(X)/40). For large X, R<=d/10 for every d in D(q). Take the common interval of integers
I_q={q+2d0-r+2 : 2k+1<=r<=R-2k}.
It has H=R-4k consecutive integers, with left end x_q=q+2d0-R+2k+2. For d=d0+e, the same N is represented by r_d=r+2e in [1,R]. Thus a single integer N and its prime factor can serve every candidate. x_q is strictly increasing, x_q=q+O(sqrt X); only O(sqrt X) q can have x_q outside [X,2X]. This permits direct transfer of a short-interval exceptional set without an independence assumption.

Choose a fixed B=100 sqrt(X), larger than 20d+20 and sqrt(2X+O(sqrt X)) for large X. Define f_X(n)=1 if every prime factor of n is <=B (including n=1), otherwise 0. This is a completely multiplicative real function with values 0,1. On [X,2X] an integer has at most one distinct prime >B. The fraction of integers there having a prime >B equals log 2+O(1/log X), by counting multiples of primes p in (B,2X], with total rounding error O(pi(2X)) and the prime reciprocal estimate sum_{B<p<=2X}1/p=log(log(2X)/log B)+O(1/log X). The long mean of f_X is 1-log 2+o(1).
Apply Matomäki–Radziwiłł Theorem 1 with h=H-1, f=f_X, delta=1/10. Crucially the theorem is uniform in f,h,delta; f_X can vary with X. Their estimate gives |short mean-long mean|<=delta+O(log log h/log h), outside O(X[(log h)^(1/3)/(delta^2 h^(delta/25))+1/(delta^2(log X)^(1/50))]) start integers in [X,2X]. The inclusive endpoint convention h vs h+1 changes the average by O(1/h). Since h is comparable to sqrt X, the exceptional count is O_{s,K}(X/(log X)^(1/50)); for all other q at least H/2 integers N in I_q have a prime >B, once X is sufficiently large (log 2>0.6). For each such N that fails the common certificate for at least one d, choose one failing d. The associated triple (q,d,r_d) is an exceptional incidence from §3; different N at fixed q cannot map to the same triple. Excluding O_{s,K}(X/log X) budgets, at most H/4 N are spoiled. Hence >=H/4 valid common witnesses, proving §1. The big-O constants and onset are not small numerical predictions; the external theorem is asymptotic.

For arbitrary R=R(X)->infinity with R=o(sqrt X), the identical proof with the original JC O(r+1) bound gives at least (log 2-o(1))R common witnesses outside o(X) budgets: choose delta tending slowly to zero (e.g. (log h)^(-1/200)), and apply Markov to total incidences with threshold R times a slowly vanishing relative tolerance. The linear-window result also has this concentration lower bound by Markov with tolerance (log X)^(-1/2). We only count the chosen threshold B, not all available certificates.

## 5. Executed finite replay
Python exact Fraction, integers, comb and lcm. All d=10..150 and r=1..floor(d/10) (1065 pairs) and four larger cases checked: R quotient identity, each denominator divides L(M-3), D' clears all six joint quantities, D'^2 G positive integral. Bit lengths (P', reduced G numerator, |D'|):
(300,30): 2867,653,1247
(1000,100): 9385,2208,4107
(3000,300): 27712,6358,12137
(10000,1000): 92265,21296,40453.
Reproducible core (no floating arithmetic):
```python
from fractions import Fraction as F
from math import comb,lcm
def check(d,r):
    j=d-r;q=-2*d+r-2;u=q+d;m=2*q+d;M=-m
    R=[F(1)]
    for l in range(r):
        R.append(R[-1]*F(m-l,m+l+3))
    L=lcm(*range(1,M-2));D=2*u*(2*u+1)*(4*m+2)*L
    V=Q=A=F(0)
    for h in range(r+1):
        k=j+h;l=r-h;c=(-1)**h*comb(2*j+h+1,h)
        assert R[l]==F(comb(M+l-1,l),comb(M-3,l))
        assert L%R[l].denominator==0
        a=(k+1)*(l+1)*c*R[l]
        b=(k+1)*l*c*R[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=a;Q+=b;A+=v*(a+b)
    c=(-1)**r*comb(2*j+r+1,r)
    E=c*F((u-d)*(2*d+3)*(m+2),2*(2*u+1)*(4*m+2))
    Z=q*A+Q+V;W=A+E
    G=3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
    P=D*D*G
    assert all((D*x).denominator==1 for x in [V,Q,A,E,Z,W])
    assert P.denominator==1 and P>0
    return P.numerator.bit_length(),G.numerator.bit_length(),abs(D).bit_length()
n=0
for d in range(10,151):
    for r in range(1,d//10+1):check(d,r);n+=1
print('exhaustive',n)
for d,r in [(300,30),(1000,100),(3000,300),(10000,1000)]:
    print(d,r,*check(d,r))
```
No finite distribution experiment claimed. Density proof uses the published uniform short-interval theorem and frozen author-proved JC/JB, whose independent review remains pending. No RH or probabilistic independence assumed. Next: exploit additional quantitative short-interval results or explicit deterministic long-window constructions to control the remaining sparse budgets; attempt all-budget exact equality exclusion, not merely density one; separate prime discovery and real residual magnitude from arithmetic existence.
