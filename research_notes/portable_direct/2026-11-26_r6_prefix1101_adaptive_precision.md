# PREFIX-1101 — Adaptive centered BRC moment recurrence and polynomial-margin bit complexity

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_COMPUTATION / NOT_REVIEWED. Independent continuation of the frozen R6 Stage46 observation, not a new shared Task, CLAIM, Result or review. Original own registration receipt r6-20261123-2358-session-start-own-v1 returned SUCCEEDED/error=null in this run; Activity RA-0ABD84561C86E53067DB0322 identifies EM-DIRECT-780BBE / TASK_RESEARCH. Fresh owner query r6-20261126-1150-owner-read-v1 last observed RUNNING (no claim authority inferred); no shared task mutation.

Frozen inputs unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint-observer/time/residual companions. Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full signed/phase/ordered-multiplicity six-axis BRC carrier retained. Only the exact radial observer D_m(k)=L[x^m(1-x)^k] and its existing normalized auxiliary Beta representation are used; no new native propagation or classical physical comparison.

Immutable sources:
- 60f5d76fb61beaefbd9c479a0e96c9429c379513:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.md
- 74b507708fa98cca4031924c9344e663f217ac0f:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.py
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md

## 1. Exact centered recurrence and a uniform moment bound

In the existing positive auxiliary Beta observer set a=m+1, S=m+k+2, mu=a/S, and M_n=E[(X-mu)^n]. Then M_0=1,M_1=0, and for n>=1,

  (S+n) M_(n+1) = n [mu(1-mu) M_(n-1)+(1-2mu) M_n].

Proof: integration by parts of x(1-x) times the normalized Beta density gives E[X(1-X) f'(X)]=S E[(X-mu) f(X)]. Boundary terms vanish for a>0 and S-a>0. Substitute f=(X-mu)^n and X(1-X)=mu(1-mu)+(1-2mu)(X-mu)-(X-mu)^2. This is an exact identity within the already-proved BRC radial observation bridge, not a replacement of the native signed object. It reduces the n-term binomial reconstruction of each centered moment to two previous moments. Signed odd moments are retained. 

For S>=1, induction gives |M_n| <= n! S^(-ceil(n/2)) for every n>=0. In the induction, the smaller of the two predecessor ceiling exponents is ceil((n-1)/2); adding one gives ceil((n+1)/2). The coefficient bound n[(n-1)!/4+n!]=(n+1/4)n! <=(n+1)! suffices. In particular 0<=M_(2r)<= (2r)!/S^r. This is a uniform fixed-order bound; not a sharp estimate for all r.

Use the adaptive exact rational radial center R0=36mu in PREFIX-1100. For any fixed positive integer r with J=2r-1 admissible for the denominator geometric majorant, its centered error payment is
  G(R0,J) E[(36X-R0)^(2r)] <= G(R0,J) 36^(2r) (2r)!/S^r.
On the declared cone 8/5<=36mu<=161/100, T=13/10, all denominator constants for J>=7 are bounded uniformly: q_4<=161/239, q_16<=161/1439 and q_d (J+4)/(J+2)<1. For fixed J the uniform numerator absolute norm is finite by the parent Frobenius bound on T^2<2. Hence this error is O_r(S^-r), without the floor caused by the fixed R0 in 1100. The previous center is not necessarily worse at small S; even the mean is not asserted to minimize the eighth moment.

The half-integer moment channel also admits a shrinking rational-square center. Let L=ceil(log2 S), h=2^L, r0=floor(sqrt(floor(a h^2/S)))/h. This is computed by integer square root, not by approximate transcendental functions. Then 0<=sqrt(mu)-r0<1/h, 0<=mu-r0^2<=2/S. On the cone, for sufficiently large S, r0 has a uniform positive lower bound. For u=(X-r0^2)/r0^2,
  E[u^(2r)] <= 2^(2r-1) r0^(-4r) [M_(2r)+(2/S)^(2r)] = O_r(S^-r).
Use the inherited 1098 odd binomial-order sqrt remainder with l=2r-1 and retain its single shared signed coefficient as in 1100. Thus its error likewise has no fixed-center floor. To evaluate exactly, shift centered moments with sum_j binom(n,j) M_j (mu-r0^2)^(n-j), rather than subtracting rounded large raw moments.

## 2. Exact finite evidence

Local Python Fraction check passed 2448 comparisons of all centered moments n=0..16 over a,b=1..12 (144 input pairs), each against exact raw rising-factorial moments and the factorial bound. The following four actual rows reuse the already saved last-negative endpoint integers; this is a new calculation of the two error-payment ingredients, NOT a fresh proof of the signs or the whole oracle. Old centers R0=160427545/10^8 and r0=19/90; new centers as above. All quantities were computed as exact rational numbers; rounded display only:

m | old/new M8 ratio | old/new U16 ratio | new M8 | new U16
1e5 | 0.9999749375 | 1.004167863 | 3.838626682e-17 | 1.410011003e-34
1e9 | 1.0000000008 | 40253.05496 | 3.839093065e-33 | 1.407585795e-66
1e20 | 97.13512235 | 1.630433582e90 | 3.839093112e-77 | 1.407585543e-154
1e22 | 500528756.7 | 1.630433582e106 | 3.839093112e-85 | 1.407585543e-170

U16 here is E[((X-r0^2)/r0^2)^16]. The prefactors G and r0 may change, so these are moment-payment comparisons rather than the total certificate radius or measured runtime. The earlier small-scale row shows a slight increase of M8 after recentering. No new whole-oracle execution; the large-scale total error remains dominated by anchor/series terms, not these tiny moment ingredients.

## 3. Arbitrarily accurate anchor supply with controlled growth

This addresses the other load-bearing term of the precision-versus-scale problem without simply extrapolating past numerical radii. In the exact six-mode representation of 1095, the first component y0 of each of the four base modes is f_lambda(R)=R^lambda (ell_lambda+O(R)), lambda in {0,1/2,1,2}, ell_lambda nonzero by the listed eigenvectors. The two homogeneous mixed modes have zero y0. Let anchor k_i=t_i K, t_i=4^i, i=0..3; mixed anchors at K. K is a positive integer anchor scale, unrelated to the fixed normalizer K in 1100. Let A denote the four-by-four exact local integral matrix on [0,1].

  lim_(K->infty) K^(lambda+1) A_(i,lambda)
    = ell_lambda * t_i^(-lambda-1) * integral_0^infty z^lambda exp(-z/36) dz.

Proof: change variable R=z/K. On 0<=z<=K, (1-z/(36K))^(t_i K)<=exp(-t_i z/36). The analytic factor of f_lambda is bounded on [0,1]. Extend by zero to z>K; dominated convergence applies. The constants multiplying each column are nonzero; no evaluation of these auxiliary integrals is required, and this is not a native reference calculation. The remaining limit matrix is an ordinary Vandermonde in nodes 1/4,1/8,1/16,1/64. Exact determinant 945/536870912 !=0. Hence the rescaled A is eventually invertible with bounded inverse, and ||A^-1||=O(K^3). The same nonzero-rank argument works for distinct positive t_i by the generalized Vandermonde property; no need to change actual anchor selection yet.

For the six-by-six matrix use the block form [A 0; C D]. The mixed rows contain R times base mixed functions, each O(R^lambda) on [0,1], so C=O(K^-2). The homogeneous block D is diagonal with J_1(K),J_2(K), where J_j=int_0^1 R^j(1-R/36)^K dR = Theta(K^(-j-1)) by the same proof. Therefore ||D^-1||=O(K^3), and the off-diagonal inverse block -D^-1 C A^-1 is O(K^4). Full inverse norm O(K^4). This is an asymptotic conditioning bound, not a computed finite threshold or a claim that 64K anchors are practical.

The parent scaled Frobenius recurrence has a fixed contraction bound after n=200. Extending that same exact recurrence to truncation N>=200 gives uniform tails O(2^-N) on [0,1], including mixed modes (the fixed constants in 1095 suffice); the global moment tails are O((35/36)^K). Set N>=K+200, and either exact rational integration or round each term on a dyadic grid of O(K) bits paying O(N 2^-cK). Truncated local matrices differ exponentially from the exact matrices; Neumann's inequality transfers the O(K^4) inverse bound for sufficiently large K. Since the six true coefficients are already enclosed in |theta_i|<1, the 1100 dual/coordinate residual payment yields anchor error O(K^4 exp(-c0 K)) for some c0>0. In particular, to certify p bits of coefficient accuracy, K,N and rounding precision O(p+1) suffice asymptotically. The constant and startup scale are not computed. Doubling K and checking the actual rational error certificate terminates at O(p+1) scale for large p. This is a proof of asymptotic anchor supply, not an actual execution of the new large-anchor regime. Direct exact rational recurrences for the parent BRC grouped moments, local incomplete Beta integrals, and basis coefficients have fixed dimension, O(K+N) index lengths (the largest anchor is 64K), and polynomial bit size: step divisors are polynomial in index with fixed rational denominators, so product of all step denominators has O((K+N) log(K+N)) bits per recurrence; numerator growth is bounded by a product of polynomial-sized step factors. Exact moment finite differences use O(K) rational/integer terms and factorial normalization of O(K log K) bits. Integration products and sums and fixed six-dimensional inversion still have polynomial bit size, even without optimal shared denominators. This proves a coarse polynomial preprocessing cost, not its practical exponent or timing.

## 4. Precision versus scale theorem (polynomial margin only)

Fix A>0 and a cone as in section 1. For sufficiently large m, k, S comparable to m, the entire inherited normalized observation can be enclosed with absolute radius <= S^(-A), with polynomial bit cost in log S, conditional on the already saved exact radial correspondence and all parent certificate hypotheses. The ingredients are:

* choose fixed r>A (and r>=4) for both adaptive centered errors;
* choose p and the numerator cutoff O(log S). The numerator series truncation on 0<=t<=T is bounded by a constant times (169/200)^cut (times fixed exponent factors), from 1095; rounding on a dyadic grid of O(log S) bits suffices including the finite polynomial norm. Use section 3 for anchor supply to this precision. The six-mode dual uses bounded target integrals since the local polynomial coefficients are uniformly absolutely summable at T for fixed J and cone. The sqrt coefficient evaluated in full Beta moments can also be bounded by a polynomial in S: at degree O(log S), monomial moments are <=36^j, and the coefficient growth is at most exp(O(log S)). If necessary choose larger fixed r depending on A and the cutoff constant, or use the same tail localization on this channel; specifically the odd-polynomial part at T has uniformly bounded absolute coefficient sum divided by T, and its full expectation with shifted half-integer Beta parameters has exponentially small upper tail for degree O(log S). This gives a uniform bound on the actual shared sqrt coefficient. No independent unsigned payment of individual BRC residual terms is needed.
* outside tail as in 1100 is exponentially small uniformly in this cone. Here is a concrete coarse domination: mode z=m/(m+k), choose u=z +/- 1/m. For m>=1e5 these lie in [1/25,1/20], and s=(1299/1000)^2/36 exceeds z by >=1/1000. log f(x)=m log x+k log(1-x) has derivative zero at z, second derivative <=-m; between z and u its absolute second derivative is <=700m (k<=22m on this cone for large m). Thus f(s)/f(u)<=exp(-m/(2*10^6)+350/m)<=2*2^(-floor(m/(2*10^6))). The normalized tail ratio rho of 1100 is <=m*2^(-floor(m/(2*10^6))). The parent polynomial factors and order-3 derivative estimates grow polynomially in S; degree O(log S) satisfies the parent monotonicity inequalities eventually. Pay this tail at finite dyadic precision by clipping the enormous exponent down to the desired p+O(log S) bits before constructing a power of two. This is a rational upper bound; no numerical exp/log reference needed.
* ordinary and half-integer rising-factorial recurrences at degree O(log S) have denominators with O((log S)^2) bits from products of O(log S) factors of O(log S) bits. Exact centered recurrences, rational shift, polynomial multiplication, 6x6 inversion, and dyadic integer square root all have polynomial bit cost in log S. The outside factor can be bounded without constructing giant powers or factorials. For target accuracy use strict rational certificates or allocate each component a fixed fraction of the requested radius.

The preceding statement is about a requested polynomial absolute error, not a uniform sign oracle. If a specific normalized observation has |D_m(k)/(K_normalizer B)| >= S^(-A0), taking A>A0 certifies its sign at sufficiently large S. With PREFIX-1097 monotonic suffix and endpoint signs, any adjacent pair satisfying such a margin certifies the full last-negative integer. If all queried midpoints satisfy a polynomial margin, binary search takes O(log m) calls, with anchor preprocessing reusable at fixed accuracy. No unconditional polynomial margin is proved. Exact zeros, superpolynomially close integer edges, and explicit finite startup constants remain unresolved; the fixed cutoff outside payment cannot by itself resolve arbitrarily tiny signs at a fixed scale. Do not claim unconditional polylogarithmic K_last, or a new integer endpoint. The previously certified 18 rows remain unchanged.

## 5. Reproduction of executed finite experiment (Python 3 standard library)

```python
from fractions import Fraction as Q
from math import comb, factorial, isqrt, prod

def centered(a,S,n):
    mu=Q(a,S); v=[Q(1),Q(0)]
    for j in range(1,n):
        v.append(Q(j,S+j)*(mu*(1-mu)*v[j-1]+(1-2*mu)*v[j]))
    return v[:n+1]

def raw(a,S,n):
    u=[Q(1)]
    for j in range(n): u.append(u[-1]*Q(a+j,S+j))
    return u

def shift(v,delta,n):
    return sum(comb(n,j)*v[j]*delta**(n-j) for j in range(n+1))

def dyadic_root(a,S):
    L=(S-1).bit_length(); den=1<<L
    return Q(isqrt((a*den*den)//S),den)

checks=0
for a in range(1,13):
    for b in range(1,13):
        S=a+b; mu=Q(a,S); v=centered(a,S,16); u=raw(a,S,16)
        for n in range(17):
            assert v[n]==shift(u,-mu,n)
            assert abs(v[n])<=Q(factorial(n),S**((n+1)//2))
            if n%2==0: assert v[n]>=0
            checks+=1
print('exact raw/centered comparisons and bound checks:',checks)
nodes=[Q(1,4),Q(1,8),Q(1,16),Q(1,64)]
det=prod(nodes[j]-nodes[i] for i in range(4) for j in range(i+1,4))
assert det!=0
print('scaled Vandermonde determinant:',det)
rows=[(10**5,2144102),(10**9,21440036819),
      (10**20,2144003672040464398426),(10**22,214400367204046439832847)]
for m,k in rows:
    a=m+1;S=m+k+2;mu=Q(a,S);v=centered(a,S,16)
    oldR=Q(160427545,10**8);newR=36*mu
    assert Q(8,5)<=newR<=Q(161,100)
    oldM=36**8*shift(v,mu-oldR/36,8);newM=36**8*v[8]
    r=dyadic_root(a,S);assert 0<=mu-r*r<=Q(2,S)
    newU=shift(v,mu-r*r,16)/r**32
    oldU=shift(v,mu-Q(19,90)**2,16)/Q(19,90)**32
    assert min(oldM,newM,newU,oldU)>0
    assert newM<=Q(36**8*factorial(8),S**4)
    print(m,float(newR),float(oldM),float(newM),float(oldM/newM),
          float(oldU),float(newU),float(oldU/newU))
```

Next: quantify the finite anchor condition/startup constants or use adaptive exact checks with practical closely spaced k_i; then test a full variable-precision oracle (not only the moments). Investigate integer-edge separation or zero decision, full spectrum sign classification and c2=0. Mother B_fix,odd(32), global p,d remain open. Independent mathematical review and Activity observation audit pending.
