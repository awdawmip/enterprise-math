# EC49FXP — Exact phase-histogram sufficient statistic for arbitrary Farey–CRT observer phases

Date: 2026-11-23 (Asia/Shanghai). Scientific pin: **BRC16943**, unchanged.
Direct parent: EC49FXO at `18a1adbe6f7f3d017923c7d3fb5b4806635ead01`, PR #2991.
Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Model, type and result

We continue exactly the frozen auxiliary double-channel *whole-activation symbol-distance* model. Let physical sites be `t∈Z/110`. For a finite nonempty relative phase set `D⊆Z/110`, a selected site set `S⊆Z/110`, support color `i∈Z/5` and missing column `j∈Z/11`, let

\[
G_S(d,i,j)=\sum_{t\in S}{\bf1}\{(t\bmod5=i\ \land\ t\bmod11\ne j)\ \lor\
((d-t)\bmod5=i\ \land\ (d-t)\bmod11\ne j)\}.
\]

The OR is taken *inside* each physical site's contribution; two channel differences in one activation count once. Write `N_r(D)=min |S|` under `G_S(d,i,j)≥r` for all `(d,i,j)∈D×Z/5×Z/11`.

Let `A={d mod55:d∈D}` and define the five **distinct-phase occupancy counts**

\[
h_a=|\{d\in A:d\bmod5=a\}|,\qquad a\in\mathbb Z/5.
\]

**Theorem (sharp arbitrary-phase histogram law).** Assume `h_a≥1` for all five colors. For each integer `4≤r≤20`,

\[
\boxed{
N_r(D)=5r+
\sum_{a=0}^{4}\mathbf1\!\left\{h_a\ge12-\left\lceil\frac r2\right\rceil\right\}
+\sum_{a=0}^{4}\mathbf1\{h_a\ge22-r\}.
}
\]

For every `r≥21`, no qualifying site set exists. Thus *all* eligible phase sets with identical five-count histograms have identical sharp optimal activation cost, regardless of which precise phase residues occur inside a color. This is a cost-observer sufficient statistic, **not** a complete dynamic phase state and **not** a promise of identical optimal layouts.

The formula generalizes EC49FXO from the 51 intervals `{0,...,k-1}` to every set hitting all five mod-5 classes, including disconnected and nonuniform sets. The frozen support/missing-column universal quantifiers remain independent. No assertion about which phases arise on native same-anchor Farey trajectories is made.

## Proof

**1. Phase quotient.** Every residue appearing in the definition of `G` is taken modulo 5 or 11. Consequently, for every `S,i,j,d`, `G_S(d+55,i,j)=G_S(d,i,j)`. Quantifying over `D` is therefore equivalent to quantifying over the distinct residues `A` modulo 55. The proof below may use `A⊆Z/55` without discarding native branch/anchor provenance.

**2. Five independent forced self-color rows.** Partition `S` by `t mod5=i`; let `m_i` be the corresponding cardinality. Because each phase color occurs in `A`, for every `i` there is at least one `d∈A` with `d mod5=2i`. At that phase only the sites of color `i` can contribute to `G_S(d,i,j)`; hence `m_i≥r`.

For each `x∈Z/55` with `x mod5=i`, let `n_x∈{0,1,2}` count how many of its physical lifts `x,x+55` are selected. Define the unsafe groups `U_i={x:x mod5=i,\ 2x mod55∈A}` and the safe groups `T_i={x:x mod5=i}\setminus U_i`. Because doubling is a bijection modulo 55 and sends color `i` onto phase color `2i`, we have `|U_i|=h_{2i}`, and `s_i:=|T_i|=11-h_{2i}`.

In a self-color row, a site fails to distinguish the candidate exactly when *both* channels' residues fall in the missing column `j`. That requires `t mod11=j` and `d=2j mod11`, i.e. `d=2x mod55` for the unique group `x` with `x mod5=i, x mod11=j`. Exactly its `n_x` selected lifts are deleted. For every unsafe group this phase is present in `A`. Therefore all self-color inequalities are **equivalent** to

\[
m_i-\max_{x\in U_i}n_x\ge r.
\]

The maximum is over a nonempty set under the stated five-color assumption.

**3. Optimal local occupancy.** Put `s=s_i`. If `m_i=r`, the unsafe maximum must be zero, so one may use only the `2s` safe lifts; this is possible precisely if `2s≥r`. With `m_i=r+1`, unsafe groups may have occupancy at most one, so capacity is `2s+(11-s)=11+s`; this is feasible if `r+1≤11+s`. In every remaining case `r+2≤22`; selecting `r+2` distinct lifts always succeeds because each unsafe occupancy is at most two. These cases give the sharp per-color minimum

\[
f_r(s)=r+\mathbf1\{s<\lceil r/2\rceil\}+\mathbf1\{s<r-10\},
\qquad 4\le r\le20.
\]

Explicit attainment: list the safe and unsafe groups in ascending order. If `2s≥r` choose the first `r` safe lifts. Otherwise, if `11+s≥r+1`, choose the first `r+1` sites from all safe lifts followed by one lift per unsafe group. Otherwise take the first `r+2` lifts from all 11 groups. Each case meets its exact minimum.

**4. The other rows automatically hold.** When `d mod5≠2i`, the left and right channels use the distinct physical site colors `i` and `d-i`. In each color at most two physical lifts lie in a given mod-11 column. Hence

\[
G_S(d,i,j)\ge(m_i-2)+(m_{d-i}-2)\ge2r-4\ge r
\]

for `r≥4`. Thus the per-color lower bounds can be attained simultaneously, with no additional cross-color cost. Summing `f_r(11-h_{2i})` over the five values of `i` and using that `i↦2i` permutes `Z/5` proves the boxed law.

**5. Sharp upper limit.** Fix any phase `d∈A`, choose its unique self-color `i=d/2 mod5`. Of its 11 mod-55 groups, at most two lifts can be selected in each. The exact bound follows from the three occupancy cases: if all unsafe occupancy is zero then `m_i≤2s_i≤20` (since `h_{2i}≥1`); if the unsafe maximum is one then `m_i≤11+s_i≤21`, and so `m_i-1≤20`; if the unsafe maximum is two then `m_i≤22`, and `m_i-2≤20`. This rules out `r≥21` for every color and completes the proof.

## Two exact limitations of cardinality-only compression

Take

\[
D_A=\{5,10,15,20,25,30,35,40,45,50,1,2,3,4\},
\quad
D_B=\{0,10,15,20,25,30,35,40,45,50,1,2,3,4\}.
\]

Both have `|D|=14` and histogram `(10,1,1,1,1)`; the interval `I_{14}={0,...,13}` has histogram `(3,3,3,3,2)`.

- At `r=4`, `N(D_A)=N(D_B)=21`, but `N(I_14)=20`.
- At `r=20`, `N(D_A)=N(D_B)=102`, but `N(I_14)=110`.

Thus equal phase-set size alone neither determines optimal cost nor fixes which distribution is more costly uniformly in `r`.

Moreover, an attaining `r=4` layout for `D_A` uses in color zero the sites `0,55,5,10,15`, together with four safe sites in each other color (see the exact script's 21-site output). Under `D_A`, all sampled rows have minimum distance 4. Under `D_B`, row `(d,i,j)=(0,0,0)` loses both `0,55` and has distance exactly 3. Hence even equal full histograms **do not preserve a particular optimal physical layout**. This is an explicit observer-relative information-loss witness: the five-count summary is sufficient for the *minimum cost number* but the detailed residue set is necessary to select/transfer an actual layout.

## Executed exact verification

The accompanying dependency-free JavaScript checker was executed in the current V8 tool runtime with all assertions passing. It verifies 187 local occupancy optima through an independent finite DP on `n_x∈{0,1,2}`; constructs 550 deterministic mixed/disconnected phase sets with seed 4923, checks 683,815 direct `G_S(d,i,j)` integer inequalities, tests the `d→d+55` quotient and validates the `D_A/D_B/I_14` witness including its exact failing row. A separate local Python implementation also checked 550 generated cases, all passing. The JS output file records the actual executed results; the scripts cover finite samples while the argument above proves the quantified theorem.

## Native-transfer question

Next derive the actual reachable **joint** `(phase,support color,missing column,anchor,branch,height)` data from pinned same-anchor Farey evolution. The five-count compression is exact only for the frozen *universal independent* `i,j` auxiliary observer cost. If the trajectory correlates those variables, its admissible row family changes; preserve the full phase and provenance until a new lossless observer map is proved. Native X6 requires an explicit three-dimensional slice, third-coordinate meaning, readout and update preservation. P000 and ACTIVE worldview are unchanged, and no formal Claim/Result/Review is asserted.
