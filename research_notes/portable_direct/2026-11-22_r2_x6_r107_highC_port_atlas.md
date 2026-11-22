# X6 R107 — Exact high-C Port transition atlas for the four-positive-weight six-pair BRC observer

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_RATIONAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Mode: independent auxiliary TASK_RESEARCH. Author identity inherited from the **verified original Source** registration `EM-DIRECT-894DDE` (session `MCP-9f342cda939b4be69352afbffbe73ece`, Activity `RA-1BEEF6E61AB30E813F55307E`). This is not a CLAIM on the native X6 Task.

Scientific foundation pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. The statement is conditional on the R104–R106 four-channel positive-weight BRC **observer**, not a physical native Cell/Link/time-dynamics identification.

## Model

For a nonzero `a=(x,y,z) in Z^3`, identify `a~-a`. Put

`q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0)))`;
`u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z`.

For `w_C=(9,1,C,41)`, define

`F_C(a)=max(|u|/10,|v|/(C+9),|h|/50,|v-u|/(C+1),|h-u|/42,|h-v|/(C+41))`

and `eta_p(C)=min{F_C(a):a!=0,q(a)<=p}`; `N_p(C)={±a:q(a)<=p, F_C(a)<3 eta_p(C)/2}`.

All parameters here are **real C >= 59** and **integer p >= 11**.

Define these disjoint direction collections (the indicated integer is the exact minimum Port budget `q`):

**E8, upper wall C=62:**

| Direction | q |
|---|---:|
| (1,0,0) | 1 |
| (5,-4,1) | 6 |
| (9,-5,1) | 10 |
| (15,-9,2) | 17 |
| (19,-10,2) | 21 |
| (23,-14,3) | 26 |
| (25,-14,3) | 28 |
| (29,-18,4) | 33 |

**E3, upper wall C=89:** `(10,-5,1):11`, `(14,-9,2):16`, `(34,-19,4):38`.

**E1, no finite upper wall:** `(24,-14,3):27`.

These are precisely the twelve R106 strict-near directions at `C=59`.

## Theorem — sharp high-C classification

For every `C>=59` and every `p>=11`,

`eta_p(C)=1/10` if `11<=p<=26`, and `eta_p(C)=6/(C+1)` if `p>=27`.

Write `E[q<=p]` for filtering by the displayed Port budget. The **complete** strict `3/2)-near-optimal set is

`N_p(C)=(E8 union {(10,-5,1),(14,-9,2)})[q<=p]` when `11<=p<=26`;

and, for `p>=27`,

- `59<=C<62`: `N_p(C)=(E8 union E3 union E1)[q<=p]`;
- `62<=C<89`: `N_p(C)=(E3 union E1)[q<=p]`;
- `C>=89`: `N_p(C)=E1`.

At **C=62** and **C=89**, equality with the strict threshold excludes the directions leaving the set. For `p>=38` the multiplicity is exactly 12, 4, or 1 in those respective C regions. For `C>=89` the increment `p=26 -> 27` makes the multiplicity drop sharply from **8 to 1**.

Combined with R106's proven `157/3<C<59` chamber, twelve strict-near directions exist for `p>=38` throughout `157/3<C<62`. This enlarges the previously certified C-interval and determines its upper endpoint.

## Proof

**1. Source baseline.** R105/R106 proves at `C=59`: `eta_p=1/10` for all `p>=11`, and the complete near set is the twelve rows above filtered by q. Its exhaustive integer-moment proof uses the necessary congruences

`v=0 mod 3,` `h-u=0 mod 6,` `h-u-6v=0 mod 12`

and the exact inverse

`x=(h+19u-8v)/2, y=(-h-14u+7v)/3, z=(h+11u-6v)/12`.

The 945-point moment box `|u|<=1, |v|<=10, |h|<=7` covers every strict `F_59<3/20` candidate; it contains 32 nonzero oriented congruent vectors, and exactly twelve unoriented vectors meet that strict bound. The accompanying checker independently repeats this finite reduction.

**2. Monotone ratio bound for C>=59.** Set `k=60/(C+1)`. The six pair denominators at 59 are `(10,68,50,60,42,100)`; at C they are `(10,C+9,50,C+1,42,C+41)`. Each ratio (old denominator / new denominator) is at least k. The only nontrivial checks reduce to `8C>=472` and `40C>=2360`; equality holds at `C=59`. Hence for **every integer direction**, irrespective of its Port,

`F_C(a)>=k F_59(a)`.

For `p>=27` this gives `eta_p(C)>=k/10=6/(C+1)`. The direction `t=(24,-14,3)` has `(u,v,h)=(0,-6,0)`, `q(t)=27`, and `F_C(t)=6/(C+1)`: equality follows. Moreover, for `p>=27`,

`F_C(a)/eta_p(C)>=F_59(a)/eta_p(59)`,

so **no direction outside the twelve-row R105 set can enter** as C grows.

**3. The low-Port minimum and complete low-Port set.** If `u !=0`, then `F_C>=1/10`. If `u=0,h!=0`, integrality forces `h-u` to be a nonzero multiple of six, hence `F_C>=6/42>1/10`. If `u=h=0`, the inverse map forces `v=6j`, giving `a=(-24j,14j,-3j)` and `q=27|j|`; thus no nonzero such direction is feasible for `p<=26`. The direction `s=(10,-5,1)` attains `1/10` at `q=11`.

For any `p<=26`, every strict-near direction must satisfy the **C-independent** necessary inequalities `|u|<=1, |h|<=7, |h-u|<=6` (using the three fixed denominator observers). Since `|z|<=26`, the inverse also gives `|v|<=55`. Exhausting only these finite bounds, the displayed congruences, integrality and `q<=26` yields exactly eight directions:
`(1,0,0),(5,-4,1),(9,-5,1),(10,-5,1),(14,-9,2),(15,-9,2),(19,-10,2),(23,-14,3)`.
They already satisfy the strict bound at `C=59`. As C increases, `F_C` is nonincreasing while `eta_p=1/10` stays fixed; all eight persist. This proves the low-Port classification.

**4. Sharp upper walls for p>=27.** With `eta_p(C)=6/(C+1)`, each reference candidate must satisfy `F_C(a)<9/(C+1)`. Direct substitution into all six observers gives sharp upper wall `C<62` for each of E8, `C<89` for each of E3, and no upper wall for E1. The C-dependent edge inequalities are included in these exact comparisons: all candidates have `|v-u|<9`, while the inequalities from `|v|/(C+9)` and `|h-v|/(C+41)` impose no stronger cutoff for `C>=59`. Thus the displayed lists are exhaustive, including their endpoints. QED.

## Verification and dependencies

The companion exact `Fraction` checker:
- independently enumerates the full 945 moment-triple reference box and verifies its 32/16/12 counts;
- enumerates the proven finite low-Port limiting candidates and finds exactly eight directions;
- derives all twelve sharp upper walls from their six exact score inequalities;
- checks 8 rational C samples crossed with 12 Port budgets, including both transition endpoints.

Scientific evidence is **author proof + exact arithmetic**, independent review pending. Source references: R105 @ `6b1f16d63230f69190423dfbdafd1cba37122025`, R106 @ `61dab37160586686f00234ef79f7b51712b2ca92`; the status/notation follows these exact predecessors. No R063 native six-file event benchmark was run in this unit.

**Next question:** Outside the proven 12-direction ray/chamber, decide whether 13 strict `3/2)-near-optimal directions are achievable for any positive quadruple. A second independent direction is to establish faithful native P000 Cell/Link/Port/heartbeat observer lifts for this reduced BRC score without erasing branch or path provenance.
