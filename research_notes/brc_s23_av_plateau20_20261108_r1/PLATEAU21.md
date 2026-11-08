# S23/AV: twenty-first exact observation-capacity plateau

Date: 2026-11-08 (Asia/Shanghai). Status: author-side mathematical proof with exact-rational verification; independent review pending. Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Exact theorem

For the same frozen two-point iid S23/AV auxiliary likelihood-sign observer and the definition of `N(h)` in `PROOF.md`, for **every integer** `7,607,280 <= h <= 7,987,653`,

```
N(h) = 43,955,799.
```

Together with `PROOF.md`, the two new consecutive plateaux are:

| Inclusive integer h | Exact N(h) |
| --- | ---: |
| 7,226,985 .. 7,607,279 | 41,880,515 |
| 7,607,280 .. 7,987,653 | 43,955,799 |

## Sharp lower bound

Retain `r=ln7/ln(10/7)`, `eps=79r-431`, `d=2074774-380295r`. The exact scaled-gap first-entry theorem (immutable predecessor `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`) uses `a_i=floor(i*d/eps)`, `V_i=380295*i+79*a_i`, `K_i=2074774*i+431*a_i`. The strict rational interval checker proves `a20=11`, `a21=12`, `(V20,K20)=(7606769,41500221)` and `(V21,K21)=(7987143,43575426)`.

At `t=V20+1=7606770`, the translated original adjacent threshold cell first receives a valid prefix of length `K21+V21-t=43955799`. This cell appears at observation horizon `h=t+510=7607280`. Therefore `N(7607280)>=43955799`.

## Matching upper bound by a complete symbolic partition

Set `H=V21+510=7987653` and `M=43955799`. Adopt the same unimodular basis `U=(79,431)`, `W=(11,60)`, classification and translated-witness lemmas proved in `PROOF.md`. For any difference of threshold values `0<x<eps`, its integral `b` coefficient obeys `|b| < eps*(H+79) < 22`; hence test exactly the **42** nonzero integers `-21<=b<=21`. For each `b` the strict strip `0<a*eps+b*eta<eps` admits at most one integral `a`. `VERIFY_H21.py` certifies each candidate using 45 rational-series terms with a strict remainder and the same `10^-26` enclosure for `r`.

Exactly the same **six** narrow displacement types listed in `PROOF.md` satisfy the triangular embeddability test at `H`; all other positive outgoing differences are at least `eps`. All twenty-one candidate translated witnesses `(K_i,V_i)`, `1<=i<=21`, have certified strict offset `0<K_i-rV_i<eps`. For each candidate the checker identifies the six-vector subset of outgoing displacements with width at most the offset (including exact equalities, which also block strict entry).

As in `PROOF.md`, define `s=v+j` for every integer left endpoint with `0<=v<=V21`, `j>=0`, `s<=H`. Split at *all* threshold crossings for candidate feasibility `v<=V_i`, `j<=K_i`, `s>=K_i+V_i-M`, and the narrow displacement feasibility predicates. The resulting integer interval cuts have **25, 8, 9** endpoints in `v,j,s` respectively. For each product cell, the necessary and sufficient lattice-feasibility test is `max(v_lo+j_lo,s_lo)<=min(v_hi+j_hi,s_hi)`; all width/availability predicates are constant on a cell.

The exact executable certificate finds **209 nonempty critical cells** and gives an admissible translated witness in every one of them; **0 are uncovered**, with 18 distinct witness indices used. This establishes coverage for *all* integer left endpoints `v<=V21`, rather than sampled points.

For the remaining `v>V21` top 510 rows, `j<=509`; the exact gamma gap lemma proved in `PROOF.md` applies unchanged. The six offsets `(K21+371+431m,V21+68+79m)` for `m=1..6` are certified to lie strictly within the universal positive gap lower bound `gamma=eta-eps`, and their prefix lengths do not exceed `M`. The exterior cells are reached at prefix lengths `1,464,095` and `43,578,209`, each less than `M`. Thus `N(H)<=M`.

Monotonicity in `h` between the sharp lower point `7607280` and the fully covered endpoint `7987653` yields the theorem.

## Program, evidence and scope

Run `python3 VERIFY_H21.py` from this directory. All decisions are exact integers or `fractions.Fraction` comparisons, including the strict log enclosure, all 42 coefficient candidates, 21 witnesses, 209 critical cells, top rows and exterior intervals. `RUN_H21.txt` records actual stdout and ends with `PASS_S23_AV_ANALYTIC_PLATEAU_21_CRITICAL_CELLS`.

The carrier retains the joint label-1/4 counts and label-3 padding of the frozen auxiliary observer. The six-source/ten-label lawful bridge, four-observation minimax error, native X6 interpretation, independent mathematical review and formal state-machine admission retain their separate scopes. Next: apply the same compressed classification to `i=22` with actual `H22=V22+510` and explicitly locate any new narrow displacement or uncovered critical cell.
