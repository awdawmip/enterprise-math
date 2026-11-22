# CBRC F7 r472 — quadratic-density obstruction for global and finite-box low-error tails

Date: 2026-11-22 (Asia/Taipei). Role/source: existing RESEARCH_DRIVER logical lane `EM-DVR-DEBB5E`. Original F7 researcher and scientific ownership: `EM-CBRCF7-83A1D4`. This is a **new mathematical corollary and exact witness audit** extending the Driver's existing r471 axis-to-axis identity. It is not a native independent review, Result acceptance, or original-author attribution change.

## Frozen model

For `z=(a,b,c,d)∈Z^4` let `k=a-2b-c+2d` and
```text
D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
```
Retain first-coordinate evenness, `q(0,0)=0`, `q(x,0)=1` for every nonzero integer `x`, the off-axis bound `q(x,y)≥1/2` for `y≠0`, and the two original fixed marked values `q(2,1)=q(-1,-1)=1/2`. The argument below actually needs only the nonzero-axis values, and thus is valid for every original admissible `q`.

For `B≥3`, define `E_B(q)=max_{z∈[-B,B]^4∩Z^4}|D_q(z)|`. Set `N=floor(B/3)`, and the *tilted original-coordinate window*
```text
P_N = { (2r-u, r-u) : r,u∈{-N,…,-1,1,…,N}, r≠u }.
```
The integral coordinate map `(r,u) ↦ (2r-u,r-u)` has determinant `-1`, and hence is injective. Therefore `|P_N|=(2N)(2N-1)=4N²-2N`.

## Theorem (exact pair covering, density and mass requirements)

Suppose `q` is original-admissible and `E_B(q)≤ε<1`. Then:

1. The involution `T(x,y)=(x-3y,-y)` partitions `P_N` into exactly `2N²-N` disjoint two-point orbits. For every such orbit `{p,Tp}`,
   ```text
   2-ε ≤ q(p)+q(Tp) ≤ 2+ε .
   ```
2. At least `2N²-N` distinct points in `P_N` satisfy `q(p)≥1-ε/2`. In particular, any low-error solution must modify the half-valued off-axis baseline at **quadratically many** points in every growing tilted window.
3. The total excess over that baseline obeys the exact finite-box inequality
   ```text
   Σ_{p∈P_N}(q(p)-1/2) ≥ (1-ε)(2N²-N).
   ```
   No upper bound on `q` is required.

The same conclusions hold for all `N≥1` for any function with `E_∞(q)≤ε<1`, regardless of any finite-box restriction. For `ε=4/7`, the high-value threshold is `5/7` and the lower bound on total excess is `(3/7)(2N²-N)`. For `ε=1/2`, at least `2N²-N` points in each `P_N` satisfy `q≥3/4`.

### Proof

Fix `r,u∈{-N,…,-1,1,…,N}` with `r≠u`, and put
```text
p = (2r-u, r-u),      p' = (2u-r, u-r).
z = (2r-u, r-u, 2u-r, u-r).
```
Because `|2r-u|,|2u-r|≤3N≤B` and `|r-u|,|u-r|≤2N≤B`, the input `z` is inside the full `B` box. Direct substitution gives `k=u-r`, `(a+k,b+k)=(r,0)`, and `(c-k,d-k)=(u,0)`. Since `r,u≠0`, the two transformed axis values are both one, yielding
```text
D_q(z) = 2 - q(p) - q(p').
```
Thus `|D_q(z)|≤ε` proves the two-sided pair sum inequality. The inverse coordinate map is `r=x-y`, `u=x-2y`; exchanging `r` and `u` sends `p=(x,y)` to `p'=(x-3y,-y)`. Since `r≠u`, these are distinct and `T²=identity`. Every unordered `{r,u}` gives one distinct orbit, of which there are `(2N choose 2)=2N²-N`.

For each orbit at least one of its two values is at least `(2-ε)/2=1-ε/2`. The orbits are disjoint, proving the count. Subtracting one from each pair-sum inequality and summing the `2N²-N` pairs gives the mass bound because the two points of each orbit each contribute a baseline `1/2`. For the global claim, take arbitrary `N` and `B≥3N`. QED.

## Scoped computational audit of the frozen r469 table

For context, the existing B14-optimal quarter-valued `q_*` is frozen at

- Source: `awdawmip/enterprise-math@ba281507cfcba49b9fb592c0e7f98b5a4ccd5621:research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json`
- Blob: `81afd124e5d9faaa877f8cbffd4bdb25a377b10b`.
- Off-axis representation: `4q_*(x,y)=2+n(|x|,y)` with `n=0` outside the frozen 1,190-row table.

A fresh exact JavaScript read/evaluation of the immutable GitHub table checked every unordered nonzero-distinct pair `{r,u}` with `|r|,|u|≤N`:

| N | two-point orbits | q≥3/4 point count | minimum pair sum (4q units) | pair sums below 6 | total excess (4q units) |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 6 | 0 | 2 |
| 2 | 6 | 12 | 6 | 0 | 12 |
| 3 | 15 | 29 | 6 | 0 | 30 |
| 4 | 28 | 52 | 6 | 0 | 56 |
| 5 | 45 | 86 | 6 | 0 | 90 |

For `N≤5`, each pair is **exactly saturated**, with `q(p)+q(Tp)=3/2`, so the quadratic total-excess lower bound is attained on the entire `P_5` window. `N=5` uses inputs within B15, not necessarily B14. For `B=15`, `N=5` is within the box, yet r469's known B15 full-box failure comes from other mixed-input configurations. Thus the new necessary condition is not asserted sufficient for B15.

## Scientific scope and continuation

This strengthens r471's *escaping-ray* necessity to a precise **positive planar density and quadratic integrated excess** necessity, including an exact finite-box version. The new condition is a structural filter for proposed infinite-tail constructions or purported sparse corrections: if `ε<1`, `o(N²)` non-baseline support on `P_N` is impossible. It does not improve `1/2≤E_∞^*≤4/7`, close unrestricted `B=15`, or imply accepted Result status.

Next valuable question: test whether the axis-pair saturated `P_N` constraints, together with first-coordinate evenness and other fiber constraints, yield a stronger finite-box infeasibility criterion or guide a non-sparse global construction. Preserve original F7 ownership, source pins, and current official review gates.

Prior work:
- r471 exact fiber and axis-to-axis theorem: `research_notes/driver/2026-11-22_f7_r471_exact_fiber_swap_global_quarter_audit.md` at `013c38ab95d45a1c5fc6f3e583d6e62e688395f7`.
- r469 finite B14 witness and proof: `research_notes/driver/2026-11-22_f7_r469_exact_B14_quarter_minimax_certificate.md` at `9711c93649a16eade31dc35f339c9501d255dd71`.
