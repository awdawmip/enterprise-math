# PREFIX-996 — X6 Stage46 outer-grade collision law and sharp polynomial decay

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable research; no formal Task CLAIM or Result.

## Frozen inputs and observation

The P000 V5 scientific input is pinned to `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`, together with the native six-axis X6 and joint-relation-preservation contracts. The exact local BRC Stage46 candidate is `research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md`, with signed port scattering coefficient `C[h,j]=1/6-1[h=j]` on twelve signed native neighbour ports. The initial preparation is one normalized directed incoming edge `x0-e_i -> x0`, with negative incoming-neighbour label.

PREFIX-995 (immutable `660533de7ad0ee5e783d371c83b8c69c312a5d37`) established for any nonnegative raw relative X6 displacement `k=(k1,...,k6)`, `sum k_i=n>=1`, that the full unrestricted signed Stage46 candidate has exact outer positive-grade Cell probability

`P_n(k) = 36^(-n) sum_{j:k_j>0} N_j(k)^2`,

where `N_j(k)=(n-1)!/((k_j-1)! product_{a!=j} k_a!)` counts positive named paths with the declared endpoint and terminal port. Each positive named path has amplitude `6^(-n)`, but coherent addition is allowed only in the **same endpoint and terminal incoming-port fiber**. The grade `ell=sum_i k_i` increases by +/-1 per primitive signed step. Thus every n-step path at grade n is positive, and this is exactly the boundary of the full twelve-direction walk, not a separately normalized positive-only walk.

## Theorem 996.1 — Exact six-category collision identity (all n)

For `n>=1`, write `M_n=sum_{k in Z_{>=0}^6, sum k_i=n} P_n(k)` for the total Stage46 probability on the extreme positive-grade Cell boundary. Define

`A_d(m)=sum_{r_1+...+r_d=m} (m!/(r_1!...r_d!))^2`.

Then, for every n,

`M_n = 6*A_6(n-1)/36^n = A_6(n-1)/(6*36^(n-1))`. **(1)**

Let `U,V` be independent uniform words of length n-1 over six axis labels, and let `H` be the letter-count vector. Equivalently,

`M_n = (1/6) Pr[H(U)=H(V)]`. **(2)**

The integers have a quadratic-cost in n exact recurrence (for fixed d):

`A_1(m)=1`, `A_d(m)=sum_{r=0}^m binom(m,r)^2 A_(d-1)(m-r)`. **(3)**

**Proof.** Fix a final port j. Deleting the final letter gives a bijection from all n-step positive named paths with final j to arbitrary (n-1)-step positive words. Summing `N_j(k)^2` across endpoints equals the square-multinomial collision count `A_6(n-1)`, independent of j. There are six final ports; the denominator is `36^n`, proving (1). Two independent uniform prefixes have the same six-component count vector with probability `A_6(n-1)/36^(n-1)`, yielding (2). Splitting the count of one label gives (3). The earlier grade lemma excludes every negative step from the boundary, proving exactness for the unrestricted Stage46 candidate. QED.

## Theorem 996.2 — Sharp asymptotic with explicit constant

The all-length aggregate outer-grade mass has the exact leading asymptotic

`M_n ~ [9/(8*pi^(5/2))] n^(-5/2)`, as `n -> infinity`. **(4)**

**Proof.** Put `m=n-1`. For each word position t, let `U_t,V_t` be independent uniform labels in {1,...,6}, and encode the sixth label by 0 in Z^5. The difference of count vectors is a sum of m independent random increments `Z_t=e_(U_t)-e_(V_t)` in Z^5. Its characteristic function is

`phi(theta)=|(1+sum_{j=1}^5 exp(i theta_j))/6|^2`.

Fourier inversion gives

`Q_m:=Pr[H(U)=H(V)]=(2pi)^(-5) integral_{[-pi,pi]^5} phi(theta)^m dtheta`. **(5)**

The modulus `phi=1` occurs at a unique torus point: equality in the triangle inequality forces all six unit complex phases, including the fixed sixth phase 1, to agree. Outside a small neighbourhood of 0 the integrand is bounded by `(1-epsilon)^m`. Its covariance is `Sigma=2[(1/6)I_5-(1/36)J_5]`, with eigenvalues `1/3` (multiplicity 4) and `1/18` (multiplicity 1). Thus `det Sigma=1/1458` and

`log phi(theta)=-theta^T Sigma theta/2+O(||theta||^4)`.

Scaling `theta=u/sqrt(m)` in (5), the Gaussian integral and the exponentially small complementary region yield

`Q_m ~ [1/sqrt(det Sigma)](2pi m)^(-5/2) = [27/(4*pi^(5/2))]m^(-5/2)`.

Finally `M_n=Q_(n-1)/6`, proving (4). QED.

For comparison only, the same argument applies to an **auxiliary** d-positive-axis, 2d-valent reflection kernel `C=J_(2d)/d-I_(2d)`: `M_(d,n)=A_d(n-1)/d^(2n-1)` and `M_(d,n) ~ d^(d/2-1)(4pi)^(-(d-1)/2)n^(-(d-1)/2)`. P000 itself remains six-dimensional.

## Exact integer verification

The companion Python program `PREFIX996_R6_OUTER_GRADE_COLLISION_CHECK.py` evaluates recurrence (3) exactly for `m=0,...,60` using built-in integer binomial coefficients. As an independent check, it enumerates all six-letter positive named words, groups by exact endpoint and final port and squares the multiplicity only within each fiber. All word lengths n=1,...,7 pass (335,922 enumerated words altogether).

Selected exact probabilities: `M_1=1/6`, `M_2=1/36`, `M_3=11/1296`, `M_4=83/23328`; the coherent pair numerator over `36^7` at n=7 is `53,089,416`. Independently computed asymptotic ratios `M_n / ((9/(8pi^(5/2)))n^(-5/2))` are about 1.10226459 at n=20 and 1.03157633 at n=61. Numerical convergence is illustrative; the preceding Fourier argument proves the arbitrary-n result.

The total probability therefore has a polynomial tail despite each individual positive path amplitude decreasing exponentially. This is a quantified role of BRC joint endpoint/terminal-port information: independent path-probability addition or premature endpoint-only coherent squaring would compute different observers.

Status: author analytical proof; exact integer verification on the stated finite window; no independent review, new native BRC engine run, physical heartbeat law or Task promotion claimed. Link/Port interactions beyond the source-defined free Stage46 candidate are not included.

## Next question

Compute the next signed grade `ell=n-2`: each length-n path has exactly one negative primitive step, whose immediate-reversal factors may be `-5/6`. Retain full ordered source, endpoint and terminal incoming-port labels to derive a closed exact contribution and its asymptotic relative to (4), then test any proposed compression under actual occupancy and field couplings. The mother objective `B_fix,odd(32) in {19,20}` remains open.

Source provenance: P000 V5 frozen `f42f2906`; Stage46 author source; PREFIX-995 `660533de`. Research mode: independent portable TASK_RESEARCH. Historical Researcher `EM-DIRECT-FBEA5D` is provenance, not a present session capability.
