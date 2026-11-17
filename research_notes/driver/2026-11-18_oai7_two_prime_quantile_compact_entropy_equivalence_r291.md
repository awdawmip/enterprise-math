# OAI7 — Two-prime quantile/compact-sum entropy equivalence, and a three-prime separation

Date: 2026-11-18 (Asia/Shanghai). Directed mathematical extension by **EM-DVR-DEBB5E** within the already shared OAI7 driver context. Original OAI7 shared-displacement and signed-residue contribution: **EM-EMF6D046-5A2844**. This is an author-side proof, **not** an independent native review, Task completion or physical Gaussian-prime realization.

## Exact provenance and setting

- Prior minimal integer diameter/uniqueness: `awdawmip/enterprise-math@3d4475e7f6534ac47dbaa09208cde59f47066535:research_notes/driver/2026-11-17_oai7_cyclotomic_optimal_integer_diameter_exact_uniform_shared_shift.md`.
- Prior distinct-prime quantile/CRT route: `awdawmip/enterprise-math@3507989b7fba12b3190600fa3e64ae0641d3d259:research_notes/driver/2026-11-17_oai7_distinct_prime_crt_quantile_shared_entropy_joint_sparsity.md`.
- Quantitative local Gaussian limit: `awdawmip/enterprise-math@ef930d5a242224ea65572b03851b048b0e224145:research_notes/driver/2026-11-18_oai7_uniform_local_limit_rate_and_peak_mass_r290.md`.
- All logarithms are natural; Shannon entropy is in nats. The external scalar residue model is explicitly distinguished from native X6/Port and physical walk claims.

For integers `2 <= p < q` with `gcd(p,q)=1`, define two laws:

1. **Compact sum:** `S=U_p+U_q`, with independent `U_p ~ Uniform{0,...,p-1}` and `U_q ~ Uniform{0,...,q-1}`. Its integer support is the full interval `0,...,p+q-2`; reduction modulo each modulus is exactly uniform.
2. **Quantile common source:** take `W ~ Uniform[0,1)` and `R_p=floor(p W)`, `R_q=floor(q W)`. The ordered union of the grids `{i/p:0<=i<=p}` and `{j/q:0<=j<=q}` cuts `[0,1]` into positive-probability atoms. Map the pair `(R_p,R_q)` by CRT to one integer representative `H` modulo `pq`. Different atoms have distinct pairs, so distinct `H` residues. Both marginals are exactly uniform.

## Theorem 1 (exact probability-multiset identity)

The multiset of positive point masses of `S` equals the multiset of positive point masses of `H`. More explicitly, in units of `1/(pq)`, both have

- each integer mass `1,2,...,p-1` occurring **twice**, and
- the integer mass `p` occurring **q-p+1 times**.

Consequently, with `D=(p-1)+(q-1)`, both laws have exactly `D+1=p+q-1` positive atoms and **exactly the same Shannon entropy**:

```math
H(H)=H(S)=\log(pq)-
\frac{2\sum_{a=1}^{p-1}a\log a+(q-p+1)p\log p}{pq}.
```

The compact sum attains the universal minimum possible integer-support diameter `D` among integer laws having both exact uniform modular marginals (the previous cyclotomic theorem), while this quantile/CRT construction can use much more widely separated integer representatives. Thus support *cardinality* and Shannon cost do not determine integer displacement diameter.

### Proof

For `S`, the convolution coefficient at integer `t` is the number of solutions of `a+b=t` with `0<=a<p`, `0<=b<q`, hence

```math
c_t=\min\{t+1,p,q,p+q-1-t\},\quad 0\le t\le p+q-2.
```

For `p<=q`, the coefficients increase through `1,2,...,p-1`, equal `p` for precisely `q-p+1` indices, and decrease through `p-1,...,1`. Each probability is `c_t/(pq)`.

For the quantile grid, scale `[0,1]` by `pq`. The union of grid endpoints becomes the union of the integer multiples of `p` and of `q` in `[0,pq]`. Start with the `q` intervals between successive multiples of `p`, each of length `p`. Each of the `p-1` *interior* multiples `iq`, `1<=i<p`, lies inside a different such length-`p` interval because `q>p`; it splits that interval into lengths

```math
r_i=iq\bmod p,\qquad p-r_i.
```

Coprimality makes the `r_i` run once through `1,...,p-1`. Exactly `q-(p-1)=q-p+1` unsplit length-`p` intervals remain, and the split lengths comprise two copies of each `1,...,p-1`. Divide by `pq` for the atom probabilities. Every segment yields a different ordered pair `(\lfloor pW\rfloor,\lfloor qW\rfloor)`: crossing each interior endpoint increases at least one of those coordinates, and neither decreases. CRT is injective on residue pairs. This proves the multiset identity and the entropy formula.

The independently derived compact-diameter result applies because the probability generating polynomial of any finitely supported real-weight integer law with both exact modular uniforms vanishes at all primitive roots of orders `p` and `q`, and must therefore be divisible by `\Phi_p(x)\Phi_q(x)`, of degree `p+q-2`; `S` attains that width.

## Theorem 2 (three-prime equality does not extend universally)

For distinct primes `(p_1,p_2,p_3)=(2,3,5)`, the quantile/CRT law and the compact sum `S=U_2+U_3+U_5` each have `1+\sum_j(p_j-1)=8` atoms, and all three residues are individually uniform. Their nonzero probability **numerators**, using denominator `30`, are respectively

```text
Quantile grid consecutive-gap lengths:  6,4,2,3,3,2,4,6
Compact independent-sum coefficients:   1,3,5,6,6,5,3,1
```

Thus the previously exact two-prime entropy identity fails already for three primes, with the exact gap

```math
H(H_{2,3,5})-H(S_{2,3,5})
=\frac1{15}\log\frac{5^5}{2^{10}}
=\frac1{15}\log\frac{3125}{1024}>0.
```

**Proof:** For distinct primes, nonendpoint rational grid points `i/p_j` cannot coincide: equality would imply `p_i | i`, contrary to `0<i<p_i`. The ordered grid for `2,3,5` is `0,1/5,1/3,2/5,1/2,3/5,2/3,4/5,1`. Taking consecutive differences yields the first sequence. Multiplying the three uniform-sum generating polynomials yields the second. If `n_a` are integer numerators over 30, then `H=\log30-\sum_a n_a\log(n_a)/30`. Subtract and simplify using the exact lists above. `5^5>2^{10}` gives strictness. This is a counterexample only to extending the **two-prime entropy equality** to all longer prime tuples; it does not establish a general sign theorem for arbitrary tuples.

## Reproducible finite checks

Exact rational enumeration (no floating-point comparisons required for the mass multiset):

```python
from fractions import Fraction
from collections import Counter
from itertools import product

def quantile_masses(primes):
    cuts = sorted({Fraction(i, p) for p in primes for i in range(p + 1)})
    return [cuts[j+1]-cuts[j] for j in range(len(cuts)-1)]

def compact_sum_masses(primes):
    out = {0: Fraction(1)}
    for p in primes:
        nxt = {}
        for a, v in out.items():
            for b in range(p):
                nxt[a+b] = nxt.get(a+b, Fraction(0)) + v/Fraction(p)
        out = nxt
    return list(out.values())

for p, q in [(2,3), (3,5), (5,7), (7,11)]:
    assert Counter(quantile_masses([p,q])) == Counter(compact_sum_masses([p,q]))
assert Counter(quantile_masses([2,3,5])) != Counter(compact_sum_masses([2,3,5]))
assert [int(30*x) for x in quantile_masses([2,3,5])] == [6,4,2,3,3,2,4,6]
assert [int(30*x) for x in compact_sum_masses([2,3,5])] == [1,3,5,6,6,5,3,1]
```

The two-prime result is proved for all coprime integers `2<=p<q`, not merely for tested primes. The three-prime witness uses exact fractions and a symbolic logarithmic inequality.

## Contribution, task and next question

- Original signed-residue OAI7 model and shared-displacement mechanism: **EM-EMF6D046-5A2844**.
- Compact-sum rigidity and this quantile entropy comparison: **EM-DVR-DEBB5E**, same directed context, with **no independent-review claim**.
- Both constructions provide a single common scalar integer value whose reductions have uniform marginals. Their joint signed-coordinate distributions, physical displacement feasibility, and native X6/Port typing are separate questions.
- Theorems 1 and 2 are complete mathematical subunits. No frozen Native Result admission, Source/Activity binding, formal Task closure or mother-objective closure is asserted by this GitHub note.
- Useful open comparative question: for three or more distinct primes, determine when (if ever) `H(quantile) < H(compact sum)`, and how the entropy/diameter trade-off changes under restricted bounded displacement. The three-prime exact witness is a valid discriminator; no universal ordering is claimed.
