# X6 layer replacement for Fibonacci — Frobenius multiresolution factorization frontier

Status: `RESEARCH NOTE / FINITE EVIDENCE + EXACT DERIVATIONS / NO FOUNDATION PROMOTION / NO GENERAL FACTORING BREAKTHROUGH CLAIM`
At: `2026-09-06T12:25:00+08:00`
Mode: `TASK_RESEARCH`
Repository snapshot before write: `main@5a50e3b5e942c8c79921835b7acc9af87a2257b6`
Global journal frontier before mirror: `awdawmip/chatgpt-global-knowledge@fd4ad4ae07d5343a35e58403456d6f6c801da25c`

## 1. Research question and BRC typing

The original proposal was to replace Fibonacci accumulation/deletion weights by the native Enterprise-coordinate layer structure when filtering or factoring semiprimes.

The useful replacement is **not one scalar per layer**. The retained object is the layer-internal path/BRC field. For the positive X6 layer of radius `N`, with

`a=(a_1,...,a_6)`, `a_i>=0`, `sum_i a_i=N`,

define the shortest-path multiplicity

`M_N(a)=N!/(a_1!...a_6!)`.

BRC population = layer-N path branches/endpoints; branch identity = exact coordinate composition; observer = divisibility/gcd/support after explicitly declared quotient; future operation = Frobenius/cyclic reduction or factor witness extraction. Any compression that discards position/provenance is treated as unsafe unless an operation-safe quotient is proved.

## 2. Scalar layer replacements are negative baselines

The full signed X6 L1 shell cardinality is

`S_6(r)=4r(2r^4+20r^2+23)/15` for `r>=1`.

It is polynomial (`Theta(r^5)`) and every positive shell size is divisible by 4, so whole-shell cardinalities are not a Zeckendorf-like universal scalar basis.

The positive-axis total shortest-path count is exactly `6^r`. The full signed path total is a linear combination of `1^r,...,6^r`; for a prime modulus `p>6` its period is governed by

`lcm(ord_p(2),...,ord_p(6))`,

placing the scalar-period route in the multiplicative-order / Pollard-p-1 family rather than creating a new factor invariant.

Conclusion: `FIBONACCI_SCALAR -> X6_SCALAR_LAYER_COUNT` is rejected. The surviving object is the internal coefficient/path field.

## 3. Exact first path-defect factor criterion

On the two-axis boundary endpoint

`d_{N,k}=(N-k,k,0,0,0,0)`,

one has

`M_N(d_{N,k})=C(N,k)`.

If `p` is the least prime factor of composite `N`, then

- `N | C(N,k)` for every `1<=k<p`;
- `gcd(N,C(N,p))=N/p`.

Hence the first divisibility defect locates the least factor. This is classical binomial divisibility arithmetic, retyped here as a native X6 shortest-path/BRC defect; it is not claimed novel as an arithmetic theorem.

A stronger prefix identity used in this research is

`G_N(m)=gcd(C(N,1),...,C(N,m))=N/gcd(N,lcm(1,...,m))`.

Thus `G_N(m-1)/G_N(m)` jumps precisely at prime-power divisors of `N`. But this compression collapses the layer field to the classical LCM/factorial/product-tree structure, so it does not provide a new factoring complexity.

## 4. Primitive-layer exact bridge

In a centered 3-axis native slice, the number of primitive L1-shell endpoints for `n>1` is

`P_3(n)=4 J_2(n)`.

For a distinct-prime semiprime `N=pq`,

`J_2(N)=(p^2-1)(q^2-1)=(N+1)^2-(p+q)^2`.

Therefore exact knowledge of `P_3(N)` yields

`p+q=sqrt((N+1)^2-P_3(N)/4)`

and hence factors from the quadratic. This is an exact reduction, not an efficient algorithm; exact primitive counting is factor-equivalent on this family.

## 5. Lucas defect sublattices inside one X6 layer

For a prime `ell`, multinomial Lucas implies

`M_N(a) != 0 (mod ell)`

iff the six coordinate digits add to the base-`ell` digits of `N` without carry. If

`N=sum_j N_j ell^j`,

then the number of nonzero X6 layer cells modulo `ell` is

`A_ell(N)=prod_j C(N_j+5,5)`.

For `N=pq`, `p<q`:

- modulo `q`, the nonzero locus is the `q`-scaled 5-simplex of compositions of `p`, with size `C(p+5,5)`;
- modulo `p`, the nonzero locus is a Lucas digit fractal determined by the base-`p` digits of `q`.

Thus a semiprime appears as two distinct factor-scale defect sublattices in the same X6 layer. This is the strongest native geometric interpretation found in this branch.

## 6. Frobenius prior-art boundary and the s-branch support law

The cyclic-polynomial route overlaps known Frobenius-map semiprime factorization (Agrawal–Saxena–Srivastava, MFCS 2016). Their two-term support quantity for `q=sum_i a_i p^i` is

`|q|_{p,2}=prod_i(a_i+1)`.

For an `s`-term sparse seed, the direct multinomial generalization is

`|q|_{p,s}=prod_i C(a_i+s-1,s-1)`.

Therefore adding branches does not automatically make Frobenius support sparser; the support upper bound grows with `s`. In particular, six-axis expansion by itself is not a factorization advantage.

Finite seed tests did show that some sparse multi-term seeds can beat the simplest binomial `x+1` at fixed finite layer width, but blind tests did **not** support a stable claim that `s=3` is uniquely optimal or that triadic balance proves an algorithmic optimum. Keep only the weaker finite engineering observation.

## 7. Compression no-go and higher correlations

For cyclic convolution over a finite field with sufficiently large field size, an observer that must preserve exact future zero-hole detection under **arbitrary future convolution kernels** cannot substantially compress a coefficient vector: apart from global nonzero scalar and cyclic shift symmetries, distinct vectors can be separated by a future kernel. Thus a universal exact small state is unavailable for that future-operation lease.

Higher cyclic correlations are nevertheless algebraically closed under convolution. For

`C_k^a(t_1,...,t_{k-1})=sum_x a_x a_{x+t_1}...a_{x+t_{k-1}}`,

one has

`C_k^{a*b}=C_k^a * C_k^b`

on `(Z/rZ)^(k-1)`.

But low orders are not sufficient: a finite `F_3, r=6` witness was found with

`a=(0,0,1,1,2,2)`, `a'=(0,2,1,0,2,1)`,

having the same value histogram and all 2-point and 3-point cyclic correlations, while convolution with

`b=(0,0,0,0,1,2)`

produces a hole pattern for one and full support for the other. Complete high-order correlation tensors scale too quickly to be a useful compression baseline.

## 8. N-only adaptive layer-width scheduling loses factor-ratio provenance

For a candidate prime cycle width `r`, the relative Frobenius orientation is

`rho_r = p q^{-1} (mod r)`.

If `n_0=N mod r` and `p=u mod r`, then

`rho_r=u^2 n_0^{-1} (mod r)`.

Thus `N mod r` determines only the quadratic-residue coset of the hidden ratio and leaves roughly `(r-1)/2` possible orientations. Legendre-symbol and `ord_r(N)` scheduling therefore cannot recover the missing factor-ratio provenance; finite tests showed only weak/inconsistent constant effects.

## 9. Positive result: one fine layer gives all divisor quotient layers

This is the main reusable result of the branch.

If `r | R`, then

`x^r-1 | x^R-1`.

Compute once

`P_R(x)=f(x)^N mod (x^R-1,N) = sum_{k=0}^{R-1} c_k x^k`.

The quotient map to the `r`-cycle is exact. Its coefficients are

`c'_j = sum_{k == j (mod r)} c_k`,

and the resulting polynomial is exactly

`P_r(x)=f(x)^N mod (x^r-1,N)`.

Therefore **one expensive fine-layer exponentiation supplies every divisor layer `r|R`**. No extra exponentiation is required for those coarser resolutions.

Define the multiresolution factor-defect spectrum

`D_R(N)={r|R : exists j with 1<gcd(N,c'_j)<N}`.

BRC interpretation: fine-layer branch provenance is retained first; each divisor layer is an explicit operation-safe quotient for its declared cyclic observer. Coarse recoalescence can expose modular cancellation that is invisible coefficientwise at the fine level; it does not create information.

Finite blind experiments showed substantial complementary gains from the divisor family versus testing only the fine layer. Example finite observations from this research include roughly:

- `R=120`: fine-layer success near 11% in one development batch; all divisor layers near 20%; a separate blind timing batch gave about 22% multiresolution success;
- `R=180`: about 16% -> 28% in development, and about 30% in a blind batch;
- `R=240`: about 20% -> 37% in development, and about 39% in a blind batch.

These are finite experiment summaries, not asymptotic guarantees.

## 10. Cyclotomic coordinate family is complementary

Because

`x^R-1 = product_{d|R} Phi_d(x)`

and

`sum_{d|R} phi(d)=R`,

the same fine-layer state can also be projected to all cyclotomic components with total coordinate dimension `R` and no new `N`-exponentiation. When `gcd(N,R)=1`, the full cyclotomic family is essentially a change of coordinates of the same fine state.

Blind finite observations:

- `R=120`: divisor-layer observer about 19.4%, divisor + cyclotomic about 26.9%;
- `R=240`: about 33.2% -> 42.9%.

Arbitrary large families of Hadamard/random linear changes were **not** retained as an Enterprise-specific gain: random linear combinations reproduced the same high-hit curves, consistent with simply making many independent-ish gcd attempts whose baseline single-attempt probability is approximately `1/p+1/q`.

## 11. Hot-cell compression is not position-specific

At `R=256`, selecting only 8 or 16 coefficient positions could retain a large fraction of successful cases while compressing over 90%, but random-position controls performed similarly. The cause was clustering of mismatch cells, especially for near factors, not intrinsically privileged Cell addresses.

Finite stratification showed that small `q-p` produces large defect clusters and high success, while for `q-p>R` successful cases often have only a few mismatched cells. Thus sparse coordinate sampling mostly retains already-easy near-factor cases and is not a generic factorization breakthrough.

## 12. Scale wall and generic-factorization verdict

Finite scale experiments indicate that constant-success cyclic width grows approximately linearly with the smaller factor:

`(p,R) ~ (2600,360), (26044,5040), (128589,20160)`.

A three-point log-log fit gave an empirical exponent near `1.04`, consistent with

`R = Theta(p)`

for ordinary balanced semiprimes. This is finite evidence, not an asymptotic proof, but it also agrees with the known Frobenius support mechanism where deterministic separation requires cycle width tied to factor gap.

For balanced semiprimes `p~sqrt(N)`, even quasi-linear polynomial arithmetic therefore leaves this route around `~O(p)=~O(sqrt(N))` unless the `R~p` wall is broken. Pollard rho has expected factor-finding scale `O(sqrt(p))=O(N^(1/4))`.

A finite Brent/Pollard-rho control at factor scale about `10^3..5*10^3` averaged roughly 143 modular multiplications and about 7.4 gcds (median roughly 93 modular multiplications), far below the cyclic-polynomial fine-layer workload in the tested implementation.

**Verdict:**

`GENERAL_SEMIPRIME_FACTORING_BREAKTHROUGH = REJECTED_AT_CURRENT_FRONTIER`.

`MULTIRESOLUTION_FINE_LAYER_REUSE_FOR_SPECIAL_FROBENIUS / NEAR-DEPENDENT FACTOR FAMILIES = RETAIN`.

Reopen the generic factoring claim only if a new X6/BRC observer achieves total work `o(sqrt(p))` or otherwise breaks the observed `R~p` scale wall.

## 13. Current durable frontier

Retain as the main algorithmic object:

`ENTERPRISE MULTIRESOLUTION FACTOR OBSERVER`

with state/observer chain

`fine cyclic layer P_R`
`-> divisor quotient layers r|R`
`-> cyclotomic coordinate components Phi_d, d|R`
`-> gcd factor witnesses`.

Do not spend further research budget on scalar Fibonacci/X6 layer codes, total path periods, prefix-gcd compression, arbitrary large linear-observer stacks, or claims that one specific triadic seed is universally optimal unless new evidence changes the frontier.

Next useful work, if this branch is reopened, is to toolize the multiresolution observer and benchmark special factor-dependency families under equal-operation budgets against the 2016 Frobenius baseline, Fermat for near factors, and Pollard rho. Generic factoring should stay closed unless the scale wall is broken.

## Persistence note

This note is intentionally stored in the Enterprise Math repository itself, in addition to the account-level global research journal, following the user's explicit instruction that Enterprise Math research progress should also be written to `awdawmip/enterprise-math` rather than existing only in the global knowledge repository.
