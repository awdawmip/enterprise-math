# R749S — Exact signed-Port graph spectrum, source-loop BRC coefficients and two-defect repair

**Date:** 2026-11-12  
**Research type:** Author-side exact finite/proved extension; independent from the currently leased native X6 triadic-closure Task (no CLAIM, native event permission, formal Result or review).  
**Scientific input:** R749N PR #2167, exact science commit `awdawmip/enterprise-math@e8c5c874aca5b7098acfdbaf8fadb8ad64a1506f`; ancestral R749 PR #2165, R748 PR #2163; original P000/Task science pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Behavioral norms use current canonical source, not a re-pin of scientific inputs.  
**Verified method:** direct signed-Port incidence decomposition, positive BRC closed-walk enumeration, full 960-state and exact rational integer checker `R749S_SPECTRAL_BRC_LOOP_CHECK.py`.

## 1. Finite typed carrier

Let `S={(i,σ):i=0,...,5; σ∈{−1,+1}}` have twelve **signed labels** (not signed amplitudes). Let `V` be the 60 unordered two-label subsets with distinct axes. For `u,v∈V`, write `u~v` when they share one **identical signed Port** and together use exactly three distinct axes. The simple undirected graph `G=(V,E)` is 16-regular. The 960 oriented edges form `D={(u,v):u~v}`.

If `(u,v)∈D`, let `w=u△v` be symmetric difference of the two signed two-port sets, a valid vertex. The `C1` source-successor permutation is `F(u,v)=(v,w)`, with `F³=1`. Define the 0–1 alternative transition operator `B` to send `(u,v)` to all 15 states `(v,x)` with `x~v` and `x≠w`. For `p∈[0,1]`, set

```
q=(1+15p)/16,     r=(1-p)/16,     P_p=q F + r B.
```

Here `F,B` are adjacency matrices of **individual branches**; all weights are nonnegative. This is precisely R749N's source-retention probabilistic candidate. It is an observer/branch model, not an admitted native Cell/Link/Port event dynamics.

## 2. Theorem A — complete 60-state adjacency spectrum and p=0 mixing

For the undirected adjacency matrix `A_G` of the 16-regular graph `G`,

```
spec(A_G) = 16(1), 8(6), 4(5), 0(15), −2(24), −4(9).
```

Parentheses denote multiplicity. In particular, this is the **exact integer spectrum**, including the zero sector; all 60 dimensions are accounted for.

**Proof by signed-axis Fourier components.** Write each function on a vertex with axes `i<j` and signs `s,t` uniquely as `a_ij+b_ij s+c_ij t+d_ij st`. Independent sign flips of each of the six axes commute with adjacency, so the spaces with character support size 0,1,2 are invariant and mutually disjoint.

* Empty character, dimension `C(6,2)=15`: the operator is `2 J(6,2)`, where `J(6,2)` is the adjacency of the Johnson graph on the fifteen axis pairs. Its eigenvalues are `2·8=16` (once), `2·2=4` (five times), `2·(−2)=−4` (nine times). Directly: `(Jc)_ij=R_i+R_j−2c_ij`, where `R_i=Σ_{j≠i}c_ij`. The constant sector has 8; the five-dimensional row-difference sector has 2; the nine-dimensional kernel `R_i=0` has −2.
* One-axis character, one 5-dimensional block for each `i`: its axis-partner coefficients obey `2(J_5−I_5)`, which has 8 once and −2 four times. Across six choices: `8(6),−2(24)`.
* Two-axis character, one dimension for each `{i,j}`: the sign-product component `st` cancels when the neighbor's other sign is summed; it has eigenvalue 0, 15 times.

All eigenvectors lie in the stated direct sum, proving the spectrum.

At `p=0`, the observed vertex walk is `T=A_G/16`, so its exact nonzero eigenvalues are `1(1),1/2(6),1/4(5),−1/8(24),−1/4(9)`. The graph is connected and has triangles, hence this walk is mixing. For any starting vertex and integer `n≥1`, the exact chi-square distance to uniform on 60 vertices is

```
χ²(T^n(v,·) || Uniform(V)) = 6/4^n + 14/16^n + 24/64^n.
```

Indeed the graph is transitive under signed axis permutations; the diagonal of each spectral projector is its multiplicity divided by 60. Consequently the mean-zero L² spectral radius is `1/2` and the total variation is bounded above by half the square root of the displayed exact chi-square distance.

**Exact edge-return formula at p=0.** For every oriented source edge `e∈D`, `n≥1`,

```
Pr_0(E_(t+n)=e | E_t=e)
 = [1 + 6·(1/2)^n + 5·(1/4)^n + 24·(−1/8)^n + 9·(−1/4)^n] / 960.
```

To see this, `tr(P_0^n)=tr((A_G/16)^n)`: cyclic walks in the edge-lift correspond bijectively to rooted vertex closed walks, with common weight `16^(−n)`. The signed-axis group acts transitively on `D`, so every diagonal edge-return probability is `tr(P_0^n)/960`. Exact values at lengths 2,3,4 are `1/256,7/4096,49/32768`, respectively. The limit is `1/960`.

## 3. Theorem B — a precise BRC closed-source weight polynomial

For `n≥1`, let `c_(n,k)` be the number of **individual length-n branch words** starting and ending at a fixed `e∈D` and containing exactly `k` retained `F` transitions and `n−k` alternative `B` transitions. Each `B` transition has fifteen distinguishable actual next-state choices. By signed-axis transitivity, `c_(n,k)` is independent of `e`. Then

```
W_n(q,r) = Pr_p(E_(t+n)=e | E_t=e)
         = Σ_(k=0)^n c_(n,k) q^k r^(n−k).
```

All coefficients are nonnegative integers and record the exact positive-weight BRC histogram of retained-vs-alternative labels; no branch multiplicity or signed-Port identity is silently canceled.

For every `n≥1`:

1. `c_(n,n)=1` iff `3|n` and otherwise zero.
2. `c_(n,n−1)=0` (one alternative event cannot leave and return to the same forced C3 orbit).
3. For `n≥2`, the **exact two-defect coefficient** is

```
c_(n,n−2) =
   5 n(n−3)/2,    n ≡ 0 (mod 3);
   n(n−1)/6,      n ≡ 1 (mod 3);
   n(n+1)/6,      n ≡ 2 (mod 3).
```

The right-hand values are nonnegative integers on their stated integer congruence classes. These identities apply for arbitrarily large `n`, not merely a finite experimental window.

**Proof of the two-defect formula.** Write `e=(u,v)`, `w=u△v`. Its forced orbit is `e,F(e)=(v,w),F²(e)=(w,u)`. A `B` event departing any forced orbit cannot land in the same forced orbit: the sole transition from a forced orbit state with the correct next first component is its excluded `F` successor. Thus a closed word has no single `B` event.

For two alternatives with exactly `a∈{0,1,2}` forced steps between them and `b∈{0,1,2}` forced steps after the second to the target, modulo three, define
`M_(a,b)=#{e→B x→F^a y→B z→F^b e}`. A local enumeration **valid for every e** yields the full nine-case table:

```
          b=0  b=1  b=2
a=0        1    0    0
a=1        0    1    0
a=2        0    0   15
```

Here is the explicit local argument, not a mere machine assumption. After the first alternative, `x=(v,t)` with `t~v,t≠w` (15 choices). The successive forced states are `x=(v,t)`, `Fx=(t,v△t)`, `F²x=(v△t,v)`. The required target immediately after the second alternative is `F^(−b)e`, respectively `(u,v),(w,u),(v,w)` for `b=0,1,2`. Its first component must equal the second component of `F^a x`. For `a=0` this forces `t=u` only when `b=0`; for `a=1` it forces `t=u` only when `b=1`; for `a=2` it forces `b=2` while **all 15** alternatives `t≠w` work. This proves the matrix.

Place the first `B` at step `i` and second at `j>i`; let `d=j−i`. Rotating the forced starting phase, the local table indices are `a≡d−1` and `b≡n−d−1` (mod 3), independent of `i`. Thus the number of closed words for a fixed gap is 15 when `n≡d≡0` (mod3), one when `n≡1,d≡2` or `n≡2,d≡1`, and zero otherwise. There are `n−d` position pairs with gap `d`. Summing `(n−d)` over the permitted gaps gives the displayed three congruence formulas, for every `n≥2`.

This captures an exact *source-defect repair law*: away from lengths divisible by 3, a closed source loop requires at least two alternative branch events.

## 4. Exact small-length weighted counts and verification

Direct, independent typed enumeration of the full 960 edge carrier gives

```
W_2 = r²
W_3 = q³ + 6 r³
W_4 = 2 q² r² + 24 q r³ + 72 r⁴.
```

For `W_3`, the forced triangle gives `q³`; there are exactly six other common neighbors `{a,d}` with a remaining signed axis `d`, each giving three alternative steps. The `W_4` coefficients arise from exact finite typed enumeration.

The companion **standard-library only** Python checker `R749S_SPECTRAL_BRC_LOOP_CHECK.py` constructs the complete 60/960 states; verifies `F³=1`, all 9 local two-defect table entries for **every 960 source edges**, the three congruence formulas for lengths 2–12, exact positive-branch closed-loop histograms through length 12, and graph trace moments `tr(A_G^n)` for lengths 1–10 against the complete proved spectrum. It also checks exact rational probabilities for `p=0,1/2,1` and the graph/edge trace identity. `R749S_SPECTRAL_BRC_LOOP_RESULTS.json` is its captured output.

The universal spectrum and two-defect coefficient theorem are proved above; finite checks are fault-detection evidence, not a substitution for the all-n proofs.

## 5. Scientific continuation

The graph admits a complete exact Fourier decomposition at `p=0`, while the all-`p` signed-source loop polynomial retains nontrivial C3 provenance. A valuable next question is to factor the **full** `960×960` positive-branch transition `P_p=pF+(1−p)P_0` into sign-character blocks with exact eigenvalue/minimal-polynomial data for `0<p<1`, to obtain sharp source-memory mixing rather than just the `p=0` vertex rate. A separate native-source interface test remains needed before applying this candidate to triadic closure or native PASS events. Existing X6 Task CLAIM ownership is unchanged.
