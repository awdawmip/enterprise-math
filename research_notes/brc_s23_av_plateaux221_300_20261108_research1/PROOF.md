# S23/AV: eighty exact finite observation-capacity plateaux, indices 221–300

2026-11-08 (Asia/Shanghai). Status: **author-side exact-rational finite endpoint proof, subject to the previously established symbolic checker soundness; independent review pending**. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Scope is the two-point iid S23/AV joint-count auxiliary observer, not the unrestricted six-source/ten-label minimax or Heartbeat X6 physical dynamics.

## Statement

The original observation laws on labels (1,3,4) are `P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)`. Observe joint counts of 1 and 4, with neutral 3 padding. As in the predecessor, `N(h)` is the least common padded prefix length required to meet every open threshold cell (including the exterior cells) of `T_h={10^j/7^s:0<=j<=s<=h}`.

Define

```
r = ln(7)/ln(10/7)
eps = 79*r-431
d = 2074774-380295*r
a_i = floor(i*d/eps)
V_i = 380295*i + 79*a_i
K_i = 2074774*i + 431*a_i
H_i = V_i + 510
M_i = K_i + V_i - V_(i-1) - 1.
```

**For each integer 221<=i<=300 and every integer V_(i-1)+511<=h<=V_i+510, the finite certificate proves `N(h)=M_i`.**

These intervals are contiguous and extend the already-certified i=220 endpoint. Thus the exact capacity is newly determined for **30,427,313 consecutive integer horizons**

```
83,675,523 <= h <= 114,102,835.
```

Selected endpoints, all from actually executed exact checks:

| i | H_i | N(H_i)=M_i | narrow displacements | feasible integer cells |
|---:|---:|---:|---:|---:|
| 221 | 84,055,896 | 458,961,026 | 68 | 23,700 |
| 240 | 91,282,370 | 498,386,473 | 74 | 27,965 |
| 260 | 98,889,218 | 539,887,125 | 80 | 32,807 |
| 280 | 106,495,987 | 581,387,267 | 86 | 38,028 |
| 300 | 114,102,835 | 622,887,919 | 92 | 43,635 |

The last new plateau is `113,722,541<=h<=114,102,835` with `N(h)=622,887,919`.

## Proof and completeness of finite certificate

**Lower bound.** The exact unimodular first-entry theorem for the translated adjacent open gap `J_t`, `t=V_(i-1)+1`, at `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` (immutable commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`) gives `N(V_(i-1)+511)>=K_i+V_i-t=M_i` for every positive integer i. No new finite extrapolation is needed for this half.

**Upper bound.** At each endpoint `H=H_i`, reuse the proved integer critical-cell reduction at `research_notes/brc_s23_av_plateau20_20261108_r1/PLATEAUX20_200.md` (commit `19730a65ae527ed19cda441ccc0ed31b9d6f2639`). Its source checker `VERIFY_PLATEAUX20_200.py` (Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`) first establishes `LO/10^26<r<(LO+1)/10^26` using 45-term rational atanh with rigorous tail, then enumerates every narrow admissible lattice displacement by a finite bound on integer `b`. For each potential witness, predicates on `v,j,z=v+j` change only at explicit integer cuts; feasibility of a critical cell is exactly `max(v_lo+j_lo,z_lo)<=min(v_hi+j_hi,z_hi)`. Every feasible cell is tested for a translated prefix with strictly positive cell offset and length <=`M_i`; top 510 rows and both exterior intervals have their own exact checks.

A local independently transcribed implementation preserving those source comparisons was **actually executed** at every index 221 through 300. All returned `PASS`. The full 80-row stdout is in `RUN_EVIDENCE.txt`; 2,651,142 feasible critical cells were checked across all runs. Maximum narrow types at one endpoint was 92; maximum feasible critical cells 43,635. Thus for these 80 particular endpoints, `N(H_i)<=M_i`.

**Interval conclusion.** Because `T_h` is nested and `N(h)` nondecreasing, the established lower bound at the left endpoint and upper bound at the right endpoint give the claimed equality throughout each integer plateau.

The published `VERIFY_RANGE.py` is a small reproducible runner that imports the predecessor exact checker in a repository checkout. The run evidence records the *locally executed transcribed* checker rather than asserting execution of the published wrapper; full local source and unmodified stdout are preserved in this run's companion handoff. Local source SHA256: `7c2f8b905219a173745623a1340ad71f81674f16aadbdcde8808c72114329484`; 80-line raw stdout SHA256: `6d7237c35533f71f5e9efcd373b91b8527ab290c2681d1bf2ff17856605b5288`. These are provenance identities, not a claim of platform-signed execution.

## BRC reuse, status and next unit

BRC carrier: exact **joint** (#label1,#label4) counts and neutral label3 padding; the logarithmic likelihood threshold is a derived observer. The sufficient-statistic and future threshold-cell scope are explicit, without collapsing branch multiplicity or claiming transfer to a native six-axis Heartbeat state. P000 and ACTIVE worldview were read and left unchanged.

This is a finite, author-side result conditional on the inherited soundness proof of its finite checker; independent proof review and formal Task/CLAIM/Result status are separate. Next: check i>=301 and preserve the first uncovered critical integer box/direction if present, or replace per-endpoint enumeration by a uniform-in-i covering theorem. Separately address the lawful six-source/ten-label bridge and full four-observation minimax objective.
