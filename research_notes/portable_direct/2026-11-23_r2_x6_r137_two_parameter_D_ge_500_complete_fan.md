# X6 R137 — complete two-parameter Port-10 BRC strict-near fan on the unbounded D halfstrip

Date: 2026-11-23 (Asia/Shanghai). Status: **author analytic/finite certificate; exact local Python Fraction replay PASS; independent mathematical review pending**.

## Scientific scope and frozen inputs

This is a new **two-real-parameter** extension of R136, NOT a new claim about native six-axis heartbeat dynamics. It studies the conditional four-positive-weight, all-six-pair BRC observer on a declared three-axis X6 slice. Preserve the P000 V5/ACTIVE-worldview constraints, all six pair observations, original sign/branch distinctions and original scientific pins:

- R121: `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- R122: `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.
- R136: `awdawmip/enterprise-math@5d4f7cd125bcfd7f7df872054c01add3d6a2a8a3:research_notes/portable_direct/2026-11-23_r2_x6_r136_optimizer_switch_adjacent_strip.md`.
- R129: `awdawmip/enterprise-math@59e7d1e4c4717c0aaa6d5db1f016f62f1180c36d:research_notes/portable_direct/2026-11-23_r2_x6_r129_class_iii_port10_D_ray.md` — previously closed B=8 slice, reused as a crosscheck, not counted as a new one-dimensional theorem.

Set `a=(x,y,z)∈Z³\{0}`, identify only the pair `±a` (positive multiples remain distinct), and

```
q(a)=max(sum(max(a_i,0)), sum(max(-a_i,0)))
h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)
g_ij(a)=|h_i-h_j|,   s_ij=w_i+w_j  for all six i<j
F_w(a)=max_{i<j} g_ij(a)/s_ij
eta_10(w)=min_{0<q(a)<=10} F_w(a)
N_10(w)={a modulo ±: 0<q(a)<=10 and 2F_w(a)<3eta_10(w)}
```

All statements below quantify over **every real** `0<B<=20`, `D>=500`, at `w=(136,B,176,D)`, with integer Port 10.

## Theorem A — complete exact optimizer

For all the above weights,

```
eta_10(136,B,176,D) =
  6/(B+D),     500 <= D <= 528+2B
  2/(B+176),   528+2B <= D <= 1056+5B
  12/(B+D),    D >= 1056+5B.
```

The formulas agree at both shared boundaries. `(1,0,0)` attains the first and second branches; `(6,-4,1)` attains the third. The optimizer changes at both `D=528+2B` and `D=1056+5B`, but only the first also changes strict-near membership.

## Theorem B — exact complete strict 3/2 membership atlas

Define the six unoriented integer directions

```
a=(1,0,0),    b=(5,-4,1),   c=(5,-1,0),
d=(9,-5,1),   e=(4,-1,0),   f=(6,-4,1).
```

For **all** `0<B<=20,D>=500`, the full set is exactly

```
N_10 = {a,b,c}
       union ({d} if D < 528+2B else empty)
       union ({e,f} if D > 704+3B else empty)
       minus ({c} if D >= 1224+8B else empty)
       minus ({a,b} if D >= 1584+8B else empty)
       minus ({e} if D >= 2448+17B else empty).
```

Consequently the exact cardinality is:

| D range (every real B in 0<B<=20) | |N_10| |
| --- | ---: |
| 500 <= D < 528+2B | 4 |
| 528+2B <= D <= 704+3B | 3 |
| 704+3B < D < 1224+8B | **5** |
| 1224+8B <= D < 1584+8B | 4 |
| 1584+8B <= D < 2448+17B | 2 |
| D >= 2448+17B | 1 |

All walls are strictly ordered for `0<B<=20`. At equality, old members exit; `e,f` enter only **strictly to the right** of the second wall. Thus the nonmonotone jump `3 -> 5` is uniform over the **entire open/closed B band**, not a numerical accident at the already-known B=8 slice. Eventually `(6,-4,1)` is the only strict-near direction at every sufficiently large D, with the *sharp B-dependent* threshold `D=2448+17B`.

For B=8, the walls are precisely 544, 728, 1288, 1648, 2584; R129 already classified this slice. Here they are proven as five affine walls for every real B in `(0,20]`.

## Proof: uniform integer witness certificates and affine chamber analysis

**(1) Exhaust the integer domain.** `q(a)<=10` forces all `|a_i|<=10`. Loop all triples in `[-10,10]^3`, retain only `0<q(a)<=10` and lexicographically first-positive representatives of `a~ -a`. Exactly **1,935** directions remain. This search neither identifies positive multiples nor drops any of the six observations.

**(2) Cover the entire unbounded halfstrip by three convex regions.**

- `P0`: closed quadrilateral with vertices `(B,D)=(0,500),(20,500),(20,568),(0,528)`, corresponding to `500<=D<=528+2B`. The line `B=0` is used solely as the closure for checking affine inequalities.
- `P1`: closed quadrilateral with vertices `(0,528),(20,568),(20,1156),(0,1056)`, corresponding to `528+2B<=D<=1056+5B`.
- `P2`: closed unbounded polyhedron with vertices `(0,1056),(20,1156)` and common positive-`D) recession direction `(0,1)`, corresponding to `D>=1056+5B`.

On a region where proposed `eta=K/L`, the universal lower bound `F_w(a)>=K/L` follows if there exists **one same pair index j for each a and region** such that

```
g_j(a)*L(B,D) - K*s_j(B,D) >= 0
```

at all region vertices, and on P2 its recession slope is nonnegative. This is a globally valid affine inequality throughout that region. The independently runnable checker exhaustively finds such a fixed pair for **all 1,935 directions in each of the three regions** (5,805 direction-region certificates). Conversely, all six upper-witness inequalities `g_j(a)*L-K*s_j <=0` hold at the relevant vertices and recession, and one pair is an equality throughout: `(1,0,0)` on P0/P1, `(6,-4,1)` on P2. This proves Theorem A for every real point without sampling extrapolation.

**(3) Uniformly exclude every outsider.** Let `C={a,b,c,d,e,f}`. For each one of the other **1,929** directions and each region, the checker finds one **fixed pair j** satisfying the affine inequality

```
2*g_j(a)*L(B,D) - 3*K*s_j(B,D) >= 0
```

at every vertex and the nonnegative recession slope on P2. Since `eta=K/L`, this one pair establishes `2F_w(a)>=3eta` throughout the region. All `1,929 x 3 = 5,787` outsider-region inequalities pass; moreover every outsider actually has a **common pair witness across all three regions**, a stronger check. Thus the full near set must be a subset of these six vectors everywhere.

**(4) Solve membership of the six survivors exactly.** For each candidate `a` and region, all six strict comparisons reduce after positive-denominator clearing to affine slacks

```
H_j(a;B,D)=3K*s_j(B,D)-2*g_j(a)*L(B,D)>0.
```

Explicit evaluation gives:

- On P0 exactly `a,b,c,d` are near on the interior; `d` reaches equality on the right boundary `D=528+2B`. `e,f` cannot be near there because their (1,3) pair slack is strictly negative.
- On P1, `a,b,c` remain near; `d` has identically zero (1,2) pair slack, hence cannot be strictly near. `e` and `f` each satisfy all six strict comparisons **iff** `D>704+3B`.
- On P2, `f` remains near for the entire unbounded region and `d` does not return. The other survivors have exact one-sided walls: `c` iff `D<1224+8B`, `a,b` iff `D<1584+8B`, `e` iff `D<2448+17B`; each entrance/exit statement is interpreted only within P2. All other pair slacks are implied by these bounds and the region inequalities.

The complete proof therefore requires a finite integer certificate **plus** a finite list of exact affine identities; it extends rigorously to continuous real B and unbounded D. The above strict inequalities resolve all ties and closed endpoints.

## Reproducibility and limits

Executable source: [x6_r137_halfstrip_verify.py](x6_r137_halfstrip_verify.py), immutable published checker commit `42f8104439c66ef30a391657fb26dd1f02329b3c`. Run `python x6_r137_halfstrip_verify.py` with Python standard library only. Its local exact-integer/`Fraction` output:

```
R137 HALFROM STRIP CERTIFICATE PASS
unoriented_population 1935 uniformly_excluded_outsiders 1929
optimizer_lower_checks 5805
outsider_exclusions 5787
rational_full_population_replays 54
optimizer_switches D=528+2B D=1056+5B
near_change_walls 528+2B 704+3B 1224+8B 1584+8B 2448+17B
```

The 54 complete independent full-integer replays use `B=1/2,8,20`, all five walls, immediately neighboring rational points, and representative tail/initial points. Those replays supplement rather than replace the vertex/recession proof. The argument depends on the stated six-pair observer and the exact Port=10 finite population. **Independent mathematical review and project theorem admission remain pending**. No native timing dynamics, BRC–Shor speedup, physical residual attribution, or change to protected P000 is asserted.

## Next scientifically useful questions

Extend B past 20 (R136's paired-direction strict B-wall), recomputing optimizer and outsider exclusion where the current halfstrip witnesses cease to hold. Alternatively classify the nonmonotone `3 ->5` re-entry at `D=704+3B` under simultaneous perturbations of A and C, identifying sharp full four-weight stability facets. Keep frozen R121/R122 pins and distinct source/role/claim authority.
