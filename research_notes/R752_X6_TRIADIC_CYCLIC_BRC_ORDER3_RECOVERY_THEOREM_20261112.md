# R752 — Exact third-order BRC recovery of the hidden global source sign

**Scope:** six native X6 axes; 320 *syntactic* oriented, equally quantized, three-distinct-axis signed Port triads. **Researcher:** EM-X6-0E46B2; native Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, claim `MCP-0dcdd94fe2451fb0cbb7cb29`, run `RUN-14a5d6f361d4bb24a99a717a`. **Scientific input:** frozen `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` and R751 immutable proof `6cf3423394a85f14f471c7f6e13222a557c1c86c`. **Status:** author-proved finite theorem and complete exact Python verification; not a native V29/V39 event, physical law or independently admitted result.

## Problem

R751 proves that the marked-free second-order signed exterior observer S on three cyclical Port branches has 160 fibers, each exactly `{(p,q,r),(-p,-q,-r)}`, while retaining their common cyclic orientation. Does an *actual signed Path-formal word statistic* of the next degree split these two-element fibers, with no arbitrary externally supplied Port sign? What is the smallest degree in this precise iterated-subword hierarchy that accomplishes it?

## Definitions

Let `i<j<k` be three distinct X6 axes, `p=s_i e_i, q=s_j e_j, r=s_k e_k` where the three `s` are ±1. A state is the cyclic-order class `[p,q,r]`, orientation `ε=+1` for `(p,q,r)` and `ε=-1` for `(p,r,q)`; the class contains exactly three cyclic marks.

For each cyclic mark `(a,b,c)`, let `W(a,b,c)=(a,b,c,-a,-b,-c)`. This is a six-step **coordinate-return witness**, not an assertion that a three-force Port closure is a Cell-coordinate return. Retain the three branch words as separate signed Path-formal BRC objects. For a signed primitive word `U=(u_1,...,u_m)`, define the integral ordered-subword moments
```
J_{ab}(U) = sum_{t<v} (u_t)_a (u_v)_b,
M_{abc}(U) = sum_{t<u<v} (u_t)_a (u_u)_b (u_v)_c.
```
Define cyclic unmarked totals `J=Σ_{3 marks}J(W)` and `M=Σ_{3 marks}M(W)`. Their components use *integer signed letter contributions*, not positive BRC masses, probabilities, a continuous physical area or a classical propagator. Both are computed from the retained 3 Path-formal branches; neither is asserted to be an already installed project API. Under a permutation `g∈S6`, the full tensors transform by relabeling axes: `J(gx)=g^{⊗2}J(x)`, `M(gx)=g^{⊗3}M(x)`.

## Theorem (exact minimal third-order lift)

For all `i<j<k` and all eight signings and both cyclic orientations:

1. The degree-0 branch count equals three. Degree-1 totals vanish, because all three W are coordinate-return paths. Degree-2 signed subword data `J` have **exactly 160 values with two source states per value** in X6; their nonzero antisymmetric components reproduce R751 `S_{ab}=J_{ab}-J_{ba}`. They are invariant under simultaneous global sign reversal of all three primitive Ports.
2. The following *single order-three coefficient* has the uniform exact decoding formula:
   `M_{iji}([p,q,r]) = -ε s_j`.
   In particular, the coefficient is always ±1 and reverses sign under the global simultaneous Port sign flip, while S and ε stay fixed.
3. Consequently `(J,M)` is injective on all 320 states. In fact `(S,M_{iji})`, where `i<j<k` is decoded from support of S, is already injective: S decodes the axes, ε and pairwise source-sign products; `s_j=-ε M_{iji}` then decodes `s_i` and `s_k`. In the specified integral iterated-subword hierarchy, degree three is minimal: every observation through degree two is identical on global-sign pairs, whereas the displayed degree-three coefficient separates them.
4. More generally for every integer `d≥3` with `d` signed native-axis labels in the same formal construction, there are `16 binom(d,3)` oriented candidate states; degree two has `8 binom(d,3)` double fibers; degree three separates all candidate states. `S_d` covariance holds under axis permutations (not an assertion of all physically legal rotations).

**Proof of the cubic coefficient.** In each marked word W, the subsequence relevant to `(i,j,i)` sees only its two i-letters and two j-letters. If the positive/negative paired i-source is earlier than the paired j-source in the first half, the projected four-letter word is `(+s_i i,+s_j j,-s_i i,-s_j j)`, giving exactly one indexed i-j-i subsequence with signed weight `-s_j`. If j is earlier, its projection is `(+s_j j,+s_i i,-s_j j,-s_i i)`, giving `+s_j`. In the forward cyclic class with sorted starting order `(i,j,k)`, two of the three cyclic marks put i before j, and one puts j before i: the total is `-s_j`. Reversing the cyclic order switches that 2:1 count to 1:2 and gives `+s_j`. This proves `M_{iji}=-εs_j`. The sign pairs and orientation recovered by S are those explicitly proved in R751. All lower degree moments are even or zero under global inversion, proving degree-minimality. Finally, letter relabeling commutes with each ordered-subsequence sum, establishing permutation covariance.

## Exact finite validation and independent evidence

A standalone Python standard-library checker exhausts 20 axis triples × 8 signs × 2 orientations = 320 states, their 960 six-step closed nonbacktracking branch words, all degree-2/3 moment coefficients, and all 720 label permutations on each state (230,400 exact covariance checks). It verifies `M_{iji}=-ε s_j`, the R751 antisymmetric coefficients, the 160 × 2 degree-2 fibers, the 320 × 1 degree-(2,3) fibers, and full tensor equivariance. Expected/observed certificate: `R752_X6_TRIADIC_CYCLIC_BRC_ORDER3_EXACT_PASS`. The combinatorial argument proves the arbitrary-d statement; only d=6 is exhaustively checked here.

**Important boundary:** 320 is a syntactic Port-incidence candidate class, not a verified set of native legal `TRIADIC_CLOSURE_E` events. The theorem does not show that V29 PASS or V39 reads M, that a signed-Port reversal is legal under a particular actual update, or that the smaller observer is dynamically sufficient. P000 primitive force arity remains three; six refers only to the coordinate-return witness length. Native source/legal-event extraction and fiber-constancy for the actual following update remain unresolved.

## New research direction

The exact degree-three residual is **not an arbitrary hand-added sign bit**; it is a computable signed Path-formal BRC ordered subword coefficient. Read exact frozen V29 PASS/V39 event and its actual Cell/Link/Port permission predicate. For a legal pair of global-sign-opposite input states, determine whether the native update descends through S; if not, test whether `(S,M_{iji})` is sufficient for this specified update and downstream observables. Do not assume this candidate event family is legal merely because its path witnesses close.
