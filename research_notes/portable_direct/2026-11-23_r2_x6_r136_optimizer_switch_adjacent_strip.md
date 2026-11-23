# X6 R136 — exact two-parameter optimizer-switch strip and complete Port-10 strict-near atlas

Date: 2026-11-23. Scientific status: **AUTHOR EXACT FINITE/ALGEBRAIC PROOF, 82 FULL-LATTICE FRACTION REPLAYS PASS; INDEPENDENT REVIEW PENDING**.

## Scope, preserved assumptions and upstream frontier

This continues R134–R135 past their upper D=220 rectangle, across a genuine optimum-branch switch. It is the **conditional four-positive-weight, six-pair BRC observer on a declared X6 three-axis slice**, not native six-axis time dynamics or a modification of P000. Frozen scientific inputs are:
- R121: `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`;
- R122: `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`;
- R134: `awdawmip/enterprise-math@f1b00131adf435d400d1486652c4635bdba01772:research_notes/portable_direct/2026-11-23_r2_x6_r134_two_parameter_nonradial_stability_polygons.md`;
- R135: `awdawmip/enterprise-math@7c6ed9aa64cd19fe60549ca2922a5f83e74668ce:research_notes/portable_direct/2026-11-23_r2_x6_r135_complete_two_rectangle_membership_atlas.md`.

For nonzero `a=(x,y,z) in Z^3`, identify `a` with `-a` only; positive multiples remain distinct. Set
`q(a)=max(sum_i max(a_i,0),sum_i max(-a_i,0))`,
`h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`,
`g_ij(a)=abs(h_i-h_j)`, `s_ij=w_i+w_j`,
`F_w(a)=max_{i<j} g_ij(a)/s_ij`, `eta=min_{0<q(a)<=10} F_w(a)`,
`N={a modulo sign:0<q(a)<=10, 2F_w(a)<3eta}`.
All six joint pairs (01,02,03,12,13,23) remain present.

## Theorem — full closed strip in D, positive-open strip in B

For **every real** `0 < B <= 20`, `220 <= D <= 500`, with
`w=(136,B,176,D)`, the exact optimum is

```
eta_10(136,B,176,D) = min(3/(136+B), 6/(B+D)).
```

The optimizer branch switches **exactly** at `D = 272+B`, including an equality tie there.

Define the four permanent near directions
`C = {(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}`,
the two individually disappearing directions
`v=(4,-4,1)`, `u=(6,-1,0)`,
and the paired directions
`E={(1,3,-1),(7,-1,0)}`.
Then the **complete** strict-near set is

```
N_10 = C
      union ({v} if D < 396 + 5B/4 else empty)
      union ({u} if D < 408 + 2B else empty)
      union (E if B < 20 and
                  D < min(306 + 5B/4, 312 - B) else empty).
```

Equivalently,
`|N_10| = 4 + [D<396+5B/4] + [D<408+2B] + 2*[B<20 and D<min(306+5B/4,312-B)]`.
**Equality at each membership wall excludes its direction**, as required by the strict `3/2` condition.

For `0<B<20`, vertical motion from `D=220` to `500` has exactly `8 -> 6 -> 5 -> 4` members. The pair-exit wall is `D_E=min(306+5B/4,312-B)`, whose formula switches at `B=8/3`. The other exit walls are `D_v=396+5B/4` and `D_u=408+2B`, always in this order. At `B=20`, the paired directions are absent throughout and the count is `6 -> 5 -> 4`. In every vertical slice, the optimizer switch at `272+B` precedes the membership exits, so the optimal witness changes **without** a strict-near membership change.

Example `B=8`: optimizer switches at `D=280`; near counts at `D=220,280,304,406,424,500` are respectively `8,8,6,5,4,4`.

## Proof — finite integer coverage and affine polygon certification

The admissible unoriented Port-10 population is exactly 1,935 integer triples. Partition the parameter strip into the two closed polygons

```
P0: (0,220), (20,220), (20,292), (0,272)
P1: (0,272), (20,292), (20,500), (0,500)
```

with `B=0` used solely as a closure vertex. On `P0`, the candidate optimum is `3/s01`; on `P1` it is `6/s13`.

For each of **all 1,935** integer directions `a`, the accompanying checker finds a fixed pair `j(a)` for which `g_j(a)*s01 >= 3*s_j` at every vertex of `P0`, and a fixed pair for which `g_j(a)*s13 >= 6*s_j` at every vertex of `P1`. Both are affine inequalities in `(B,D)`; four-vertex positivity thus proves the lower bounds over the full polygons. In the first polygon `(6,-1,0)` attains `3/s01`, and in the second `(1,0,0)` attains `6/s13`: all six upper-witness inequalities hold at every vertex. This proves the optimizer expression for all real parameters.

For each of the other **1,927** integer directions outside the eight above, the checker finds one of six pairs violating strict nearness throughout each polygon: `2g_j(a)*s01 >= 9*s_j` on `P0` and `2g_j(a)*s13 >= 18*s_j` on `P1`. Both hold at the corresponding four vertices and hence throughout by affinity. The same pair can serve as a witness on both polygons for every outsider. Thus no unlisted direction can enter anywhere in the full strip; this certificate keeps all six pair observations.

Only the remaining 8 directions need membership analysis. On `P0`, all their strict inequalities have positive affine slack on the closure except the `02` pair for the two directions in `E`, with slack `360-18B`. On `P1`, the four core directions have all six slacks positive on the closure. The potentially active comparisons are:

| Direction(s) | Necessary active strict forms on P1 | Simplification |
|---|---|---|
| `(1,3,-1),(7,-1,0)` | `10B-8D+2448`, `5616-18B-18D`, `8B-10D+3168` | `D<min(306+5B/4,312-B)` |
| `(4,-4,1)` | `5616-12B-12D`, `10B-8D+3168` | `D<396+5B/4` |
| `(6,-1,0)` | `12B-6D+2448`, `5616-12B-12D` | `D<408+2B` |

The third form in the first row is implied by the first for `0<=B<=20`: `316.8+0.8B >= 306+1.25B`. The second form in the last two rows is implied by the other form since `468-B >= 396+1.25B` and `468-B >= 408+2B` on the same B-range. Every other comparison is strictly positive at all polygon vertices. Applying strictness and combining the two polygons yields the claimed full formula, including ties, endpoints and `B=20`.

This is a finite integer proof with **global continuous-parameter coverage** because each relevant signed comparison is affine after clearing positive pair capacities. Merely sampling parameter values would not establish the theorem.

## Reproduction, evidence and limitations

The complete standard-library checker is
`research_notes/portable_direct/x6_r136_adjacent_optimizer_strip_verify.py`.
It enumerates the 1,935 directions (modulo sign only), verifies all integer witnesses at the 4+4 polygon corners, checks the eight surviving directions' active affine forms and dominance of secondary bounds, and independently evaluates the exact optimum and **full** near set at 82 rational `(B,D)` configurations including exact wall equalities.

Observed exact local output:

```
R136 CERTIFICATE PASS
port10_unoriented_directions 1935
optimizer_lower_pair_at_each_polygon 1935 x 2
excluded_outsiders 1927 x 2; common_pair_witnesses 1927
exact_full_direction_replays 82
anchor_switch D=272+B; paired departure D=min(306+5B/4,312-B)
remaining departures D=396+5B/4, D=408+2B
sample B=8: D=220,280,304,406,424,500 counts [(220, 8), (280, 8), (304, 6), (406, 5), (424, 4), (500, 4)]
```

Scope is the declared frozen conditional observer and the stated compact parameter strip. The new result extends R135 beyond its D=220 bound; **author proof/checker verified, independent mathematical review pending**. Native X6 time dynamics, formal CLAIM/Result and P000 promotion are separate.

## Next discriminating problem

Extend `D>500` until the next optimizer branch or first genuine outsider entry; detect and classify a **nonmonotone** near-set trajectory if any. Alternatively vary `B>20` across the strict paired-direction loss wall, with all candidate and optimizer branches re-evaluated. Keep immutable R121/R122 pins and observer semantics; do not infer a global four-weight atlas from this strip.
