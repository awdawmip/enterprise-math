# S23/AV: 181 exact capacity plateaux (20–200) with a finite symbolic lattice certificate

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_RATIONAL_CERTIFIED_THEOREM; independent mathematical review pending. Scientific input remains frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Theorem and complete range

In the frozen two-point iid S23/AV auxiliary likelihood-sign observer with one-step laws `P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)` on labels (1,3,4), keep the joint label-1/label-4 counts and neutral label-3 padding. Put `T_h={10^j/7^s:0<=j<=s<=h}`. Let `N(h)` be the least common padded observation length allowing an attainable prefix score in **every** open threshold cell of `T_h`, including both exterior cells.

Define, for each integer `i>=1`,

```
r = ln(7)/ln(10/7)
epsilon = 79*r - 431
d = 2074774 - 380295*r
a_i = floor(i*d/epsilon)
V_i = 380295*i + 79*a_i
K_i = 2074774*i + 431*a_i
H_i = V_i + 510
M_i = K_i + V_i - (V_(i-1) + 1)
```

**For every integer `20<=i<=200` and every integer `V_(i-1)+511 <= h <= V_i+510`,**

```
N(h) = M_i.
```

This determines the exact capacity on **68,841,769 consecutive integer horizons**, from `h=7,226,985` through `h=76,068,753`. The final exact plateau has `N(h)=415,385,600` on `75,688,380<=h<=76,068,753`.

The previous nineteenth plateau ended at 7,226,984. The sequence 20–200 is contiguous because the next plateau starts at `V_i+511=H_i+1`.

## Lower bound: existing universal first-entry theorem

The earlier proved scaled-gap first-entry law is documented in `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at immutable commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`. For every `i>=1`, the translated adjacent cell `J_t` with `t=V_(i-1)+1` first receives a prefix of length exactly `K_i+V_i-t=M_i`, and occurs among the `T_(t+510)` cells. Consequently `N(V_(i-1)+511)>=M_i`. The original proof is an exact unimodular decomposition, not an extrapolation from the data of this batch.

## Universal upper-bound construction for each endpoint

For a fixed `i`, put `H=H_i`, `M=M_i`, `D_H={(v,j) in Z^2_{≥0}:v+j<=H}`, and thresholds `t(v,j)=r*v-j`. The integer basis `U=(79,431)`, `W=(11,60)` has determinant `-1`. Every difference between thresholds has unique integral coefficients `(dv,dj)=aU+bW`, width `x=dv*r-dj=a*epsilon+b*eta`, `eta=11*r-60`. The exact integer coefficient `b` obeys `b=79*x-epsilon*dv`.

For `0<x<epsilon`, `|dv|<=H` implies `|b|<epsilon*(H+79)`. Use a certified rational upper enclosure `EU/Q` of `epsilon`, `Q=10^26`, and set the integer `B=floor(EU*(H+79)/Q)+1`. It suffices to examine the **complete finite list** `b` with `-B<b<B`, `b!=0`. For fixed nonzero `b`, `0<a*epsilon+b*eta<epsilon` has at most one integral `a`; the checker determines it by a strictly validated quotient floor. Keep only displacements whose minimum triangle embedding cost is `<=H`. At every one of the 181 endpoints, the retained candidate displacements have both coordinates positive or both negative, which allows the following exact admissibility test.

For each `1<=s<=i` the translated witness `(K_s,V_s)` has offset `delta_s=K_s-rV_s in (0,epsilon)`. At a left threshold point `p=(v,j)`, the corresponding prefix is `(k,ell)=(K_s-j,V_s-v)`. It falls strictly in the immediately following open cell and within the allowed length `M` if:

```
v <= V_s
j <= K_s
v+j >= K_s + V_s - M
no outgoing threshold displacement from p has width <= delta_s
```

All outgoing differences of width less than `epsilon` occur among the complete finite list above. For positive-coordinate displacements `(dv,dj)`, it is feasible at `p` iff `v+j<=H-(dv+dj)`; for negative-coordinate displacements, iff `v>=-dv` and `j>=-dj`. A width `<=delta_s` blocks that candidate. Width ordering against every `delta_s` is certified with strict, adverse rational interval endpoints (and exact equality handled explicitly).

Partition the full integer population of left endpoints with `v<=V_i` at every transition for the witness conditions, and for the narrow-displacement conditions. Equivalently split the three integers `v,j,z=v+j` at all relevant threshold cuts. On each resulting rectangular critical cell `v in [v0,v1]`, `j in [j0,j1]`, `z in [z0,z1]`, all witness and obstruction predicates are **constant**, and the cell contains an integer left endpoint iff

```
max(v0+j0,z0) <= min(v1+j1,z1).
```

This equivalence is exact because every integer between `v0+j0` and `v1+j1` is a sum of integers from the respective coordinate intervals. Therefore checking one Boolean predicate set for each *feasible critical cell* establishes full integer coverage, regardless of the number of thresholds. `VERIFY_PLATEAUX20_200.py` enumerates these cells for **every i from 20 to 200**, fails on any uncovered feasible cell, and confirms that at least one candidate witness enters the cell with length `<=M`.

For the remaining `V_i<v<=H` top 510 rows, `j<=509`. The exact `gamma=eta-epsilon` gap lemma in `PROOF.md` proves every positive outgoing gap is at least `gamma` in this domain. For the smallest `m in {1,...,6}` with `L=V_i+68+79m>=v`, choose `K=K_i+371+431m`; the program certifies `0<K-rL<gamma`, admissibility, and prefix length `<=M`. Both exterior cells use the explicit prefixes `(0,floor(H/r)+1)` and `(floor(rH)+1,0)`, with strict length/ordering checks. Thus `N(H_i)<=M_i`. Together with the sharp lower bound and monotonicity of `N(h)`, the theorem follows for all integers in every plateau interval.

## Exact rational certificate and observed evidence

`VERIFY_PLATEAUX20_200.py` uses only Python standard-library `fractions.Fraction` and integers. Forty-five terms of the rational atanh series and a strict geometric remainder establish `LO/Q<r<(LO+1)/Q`, where `LO=545569623581288298975349314`, `Q=10^26`. Its `enc(A,B)` gives rigorous lower/upper integer numerators for `A+B*r`; all comparisons (including floor quotient uniqueness, positive gap width, obstruction order, top-row intervals and exterior strict inequalities) are proved through those adverse bounds. Each integer `i` is checked separately under its own valid finite coefficient bound; no generalization to untested `i` is assumed.

Actual execution returned `PASS_S23_AV_ANALYTIC_PLATEAUX_20_TO_200 certified 181 last_H 76068753 last_N 415385600 max_critical_cells 19266 max_narrow_types 60`. The 181 finite symbolic endpoint checks cover up to **19,266 complete critical integer cells** at a single endpoint and up to **60 embeddable narrow displacement classes**. `RUN_PLATEAUX20_200.txt` contains the actual compact checkpoint stdout and final PASS. At `i=20` the certificate uses 194 cells; `i=21` uses 209. All conditions are checked by a standalone executable; the preceding mathematical argument proves their sufficiency for the declared domain.

## Provenance, BRC scope and next question

The observation carrier is the **joint** label-1 and label-4 count, plus neutral label-3 padding, preserving relevant joint information under the BRC observer. This is a theorem for the frozen two-point auxiliary experiment and retains P000/ACTIVE native Heartbeat X6 premises. The six-source/ten-label mother-model lawful transfer and full four-observation minimax error remain separate mathematical work. The result is author-side research material in Draft PR #1777; independent review, formal Task/Result freeze and Foundation admission have their own authorities.

Next: study the first new behavior for `i>200` and whether the bounded critical-cell certificate can be proved *uniformly* over an infinite family, instead of checking individual finite endpoints. In parallel, investigate the lawful six-source bridge and four-observation minimax delta4, which are independent of further capacity staircase extension.
