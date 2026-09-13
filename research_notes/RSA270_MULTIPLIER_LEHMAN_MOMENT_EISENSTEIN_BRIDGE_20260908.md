# RSA-270 continuation: multiplier-collision closure and BRC moment–Eisenstein bridge

Status: `RESEARCH NOTE / EXACT THEOREMS + NEGATIVE PREDICTOR RESULT / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T00:13:30+08:00`  
Parent: PR #1331 salvage/continuation branch.

No RSA-270 factor is obtained.

Tool reuse resolution: `T0_BRC -> REUSE_APPLIED`; `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA -> REUSE_APPLIED`. No new top-level tool family is introduced.

## 1. Multiplier boundary defect is exactly rational-approximation / Lehman geometry

Let `N=pq`, and for positive integers `a,b` define

`x_(a,b)=a p + b q`,  `y_(a,b)=|a p-b q|`,  `k=ab`.

Then

`x_(a,b)^2-y_(a,b)^2=4abN=4kN`.

Hence the distance of the exact factor endpoint from the Fermat starting surface is

`x_(a,b)-2 sqrt(kN) = y_(a,b)^2 / (x_(a,b)+2 sqrt(kN))`.

Also

`y_(a,b)=bp |a/b-q/p|`.

Therefore a small multiplier/Fermat step is precisely a good rational approximation `a/b ~= q/p`; the proposed multiplier-boundary near-collision search is not a new asymptotic mechanism by itself. This is the same geometry used by Lehman's variation of Fermat: systematic multiplier/Farey coverage obtains the classical `O(N^(1/3))` regime, while a better complexity would require an N-only method that selects the good rational approximation without scanning the usual multiplier family.

This identifies the correct novelty gate:

`NEW BRC ADVANTAGE != EXISTENCE OF GOOD MULTIPLIER`;

`NEW BRC ADVANTAGE -> N-ONLY PREDICTOR OR COMPACT PROVENANCE OBSERVER THAT SELECTS/ENCODES THE GOOD MULTIPLIER`.

Classical prior-art boundary: R. S. Lehman, *Factoring Large Integers* (1974); later expositions and generalizations explicitly describe the search as finding `a/b` approximating the unknown factor ratio and testing values near `2 sqrt(abN)`.

## 2. N-only first-layer predictor benchmark: negative at increasing scale

For each odd `k<=1000`, define

- `x0(k)=ceil(sqrt(4kN))`;
- `d0(k)=x0(k)^2-4kN`;
- normalized shell phase `rho=d0/(2x0-1)`;
- normalized nearest-square defect of `d0`;
- hidden target `j*(k)=min_(ab=k) [ap+bq-x0(k)]`.

A fixed reproducible benchmark used 12 balanced semiprimes at each factor size 16, 20 and 24 bits. The two normalized N-only features were compared against `log(1+j*)` by Spearman rank correlation and by top-5% multiplier overlap.

Results:

| factor bits | rho corr | rho top-5% overlap | sq-defect corr | sq-defect top-5% overlap |
|---:|---:|---:|---:|---:|
| 16 | 0.0075 | 0.0567 | -0.0140 | 0.0633 |
| 20 | 0.0398 | 0.0600 | -0.00018 | 0.0467 |
| 24 | 0.0102 | 0.0500 | -0.00224 | 0.0433 |

Random top-5% overlap baseline is 0.05. At the largest tested scale both normalized features are effectively at the random baseline and rank correlation is approximately zero.

Interpretation: this finite experiment does **not** prove an impossibility theorem, but it rejects the specific shortcut that the first shell residual or its nearest-square phase cheaply predicts the good Lehman/BRC multiplier. Earlier small-scale apparent enrichment is not scale-stable in this benchmark.

## 3. Generalized two-form Plücker determinant identity

For two boundary forms

`x1=a p+b q`,  `x2=c p+d q`,  `Delta=ad-bc`,

we have exactly

`d x1-b x2 = Delta p`,

`a x2-c x1 = Delta q`,

and hence

`(d x1-b x2)(a x2-c x1)=Delta^2 N`.

If `Delta=+-1`, two correctly labelled exact boundary observations recover `p,q` immediately. Thus the multi-multiplier boundary cloud is a rank-2 determinant network. The remaining difficulty is observation/extraction, not algebraic recovery.

## 4. Hyperbolic transform of the exact BRC profile

For odd `n`, let

`P_n(u)=sum_(d|n) W_((d+n/d+2)/2)(u)`

with

`W_s(u)=sum_(j=0)^(s-2) u^(2-s+2j)`.

Put `u=e^z` and

`h_d=(d+n/d)/2`.

Then the geometric progression gives the exact transform

`W_s(e^z)=sinh((s-1)z)/sinh(z)`,

so

`Phi_n(z):=P_n(e^z)= [1/sinh(z)] sum_(d|n) sinh(h_d z)`.

This is an even analytic function at `z=0` after the removable singularity is filled.

For a distinct odd semiprime `N=pq`, `S=p+q`, the transform collapses to

`Phi_N(z)=2 [sinh((N+1)z/2)+sinh(Sz/2)] / sinh(z)`.

After subtracting the known outer term,

`(sinh z / 2) Phi_N(z)-sinh((N+1)z/2)=sinh(Sz/2)`.

This is a rigorous replacement for the over-broad SG1/SG3 language in PR #1330: the **exact semiprime profile transform** is a one-parameter analytic family indexed by `S`.

Consequences within this explicitly defined family:

- any exact real evaluation at fixed `z!=0` is injective in positive `S` and therefore factorization-equivalent;
- at `z=2*pi*i/m`, the unknown term is periodic in `S mod 2m`;
- the r-th z-derivative at such a torsion point is a degree-r polynomial in `S` times a periodic sine/cosine phase. Thus the entire derivative ladder is an exact quasi-polynomial family, not merely a finite experimental observation.

No claim is made that these evaluations are cheaply computable from N.

## 5. BRC moment -> odd divisor-sum theorem

Define the even coefficient moments

`mu_(2r)(n)=sum_e e^(2r) P_n[e]=Phi_n^(2r)(0)`.

For one block of length `h`, the exponent set is

`{1-h, 3-h, ..., h-1}`.

Its `2r`-th power sum is an odd polynomial in `h` of degree `2r+1` with leading term `h^(2r+1)/(2r+1)`.

For the divisor-pair heights,

`H_(2m+1)(n):=sum_(d|n) h_d^(2m+1)`

satisfies exactly

`H_(2m+1)(n)
 = 2^(-2m) sum_(j=0)^m binom(2m+1,j) n^j sigma_(2m+1-2j)(n)`.

Therefore the moment vector

`(mu_0,mu_2,...,mu_(2r))`

and the odd divisor-sum vector

`(sigma_1,sigma_3,...,sigma_(2r+1))`

are related by an invertible triangular rational transformation. The diagonal coefficient of `sigma_(2r+1)` in `mu_(2r)` is

`1 / ((2r+1) 4^r) != 0`.

Thus the two finite towers contain exactly the same arithmetic information.

First formulas:

`mu_0 = sigma_1(n)`;

`mu_2 = [sigma_3(n)+(3n-4)sigma_1(n)]/12`;

`mu_4 = [3sigma_5 +(15n-40)sigma_3 +(30n^2-120n+112)sigma_1]/240`;

`mu_6 = [3sigma_7 +(21n-84)sigma_5 +(63n^2-420n+784)sigma_3 +(105n^3-840n^2+2352n-1984)sigma_1]/1344`.

The attached verifier checks these formulas directly on odd composites `15,35,45,105,143,225,315`.

## 6. Eisenstein-series interpretation

The classical Eisenstein series have nonconstant Fourier coefficients proportional to `sigma_(k-1)(n)`. Therefore the BRC even-moment tower is, after the explicit triangular change of basis above, exactly the ordinary odd-divisor-sum / even-weight Eisenstein coefficient tower:

`mu_0 <-> sigma_1` (weight-2/quasimodular boundary),

`mu_2 <-> sigma_3` (weight 4),

`mu_4 <-> sigma_5` (weight 6), etc.

For `N=pq`, every `sigma_m(N)` is a polynomial in `N` and `S` because

`p^m+q^m = S(p^(m-1)+q^(m-1))-N(p^(m-2)+q^(m-2))`.

Hence **all unweighted exact profile moments stay inside the same scalar S-wall**.

This clarifies why the character-weighted line already developed on PR #1331 is structurally different. Ordinary/unweighted differentiation produces the ordinary Eisenstein divisor-sum tower; retaining a faithful factor-residue split requires branchwise character weighting before BRC provenance is erased, leading instead to twisted divisor sums / weight-1 Eisenstein data.

## 7. Updated frontier

The multiplier-collision route is now classified:

1. exact boundary identities are useful;
2. near-collision = rational approximation of the factor ratio;
3. systematic coverage reproduces classical Lehman/Farey geometry;
4. tested first-layer N-only shell features do not select good multipliers at scale;
5. two exact boundaries would recover factors immediately by the determinant identity, so extraction remains the wall.

The strongest new reusable result of this round is the **BRC moment–odd-divisor-sum triangular equivalence** and its Eisenstein interpretation.

Next high-value target:

- do **not** enlarge raw multiplier scans;
- use the hyperbolic/moment bridge to prove a separation theorem between unweighted profile differential observables and provenance-sensitive character-weighted observables;
- then search only for a compact BRC construction that computes the existing faithful twisted coefficient `A_e(N)=sum_(d|N) chi_e(d)` (or an equivalent low-width trace) **before** factor provenance is collapsed.

That is the first route in the current portfolio that is not already explained by ordinary Lehman geometry or the unweighted `S`-only profile algebra.
