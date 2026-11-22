# X6 R105 — The factor 3/2 is sharp in the actual six-pair BRC family; complete Port-threshold spectrum for the R104 witness

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Direct dependency: R104 `research_notes/portable_direct/2026-11-22_x6_r104_thirteen_class_robust_gap_and_finite_box.md`. Same conditional auxiliary positive-count **BRC star-gap** observer, not a statement that native X6 Cell/Link/triadic events or heartbeat trajectories are modeled faithfully. P000 and ACTIVE worldview are unchanged.

## Definitions

For a nonzero integer vector (a=(x,y,z)), up to sign, let
[
q(a)=max(sum_i a_i^+,sum_i(-a_i)^+),quad
u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z.
]
Use the R104 six-pair norm at **fixed** (w=(A,B,C,D)=(9,1,59,41)):
[
F(a)=max{ |u|/10, |v|/68, |h|/50,|v-u|/60, |h-u|/42, |h-v|/100}.
]
Let (eta_p=min_{a
e0,q(a)le p}F(a)), (p) any integer (ge11). Let
(N_p={{pm a}:q(a)le p, F(a)<3eta_p/2}) and
(C_p={{pm a}:q(a)le p, F(a)le3eta_p/2}).

## Theorem R105 — exact entire Port spectrum

For **every integer** (pge11), (eta_p=1/10).
The entire set (igcup_{pge11} C_p) is the following **14** unoriented directions; each enters both sets, where applicable, precisely at the displayed Port cost. The scores are exact.

| Direction | q | F |
|---|---:|---:|
| (1,0,0) | 1 | 1/7 |
| (5,-4,1) | 6 | 1/7 |
| (9,-5,1) | 10 | 1/7 |
| (10,-5,1) | 11 | 1/10 |
| (14,-9,2) | 16 | 1/10 |
| (15,-9,2) | 17 | 1/7 |
| (19,-10,2) | 21 | 1/7 |
| (23,-14,3) | 26 | 1/7 |
| (24,-14,3) | 27 | 1/10 |
| (25,-14,3) | 28 | 1/7 |
| (29,-18,4) | 33 | 1/7 |
| (33,-19,4) | 37 | 3/20 |
| (34,-19,4) | 38 | 7/60 |
| (39,-23,5) | 44 | 3/20 |

Consequently, for all (pge11):
[
|N_p|=4+[pge16]+[pge17]+[pge21]+[pge26]
+[pge27]+[pge28]+[pge33]+[pge38],
]
[
|C_p|=|N_p|+[pge37]+[pge44].
]
The complete minimizer directions are (10,-5,1) for (pge11), (14,-9,2) additionally for (pge16), and (24,-14,3) additionally for (pge27).

For all (pge38), (|N_p|=12), permanently. For all (pge44), (|C_p|=14), permanently. Thus the **thirteenth and fourteenth** feasible order statistics in the score, for (pge44), are both exactly (3/20=(3/2)eta_p).

**Sharpness corollary.** R104 proved (|{F<3eta_p/2}|le13) for *all* positive BRC weights and (pge11). The present single BRC example has **14** directions at (Fle3eta_p/2) for (pge44). Therefore, for every (lambda>3/2), the claimed uniform bound (|{F<lambdaeta_p}|le13) is false within this same BRC family. The constant (3/2) is a sharp universal cutoff, not merely a limitation of the R104 residue proof. No conclusion is drawn here about whether 13 can occur **strictly** below the sharp cutoff.

## Proof

First (s=(10,-5,1)) has (q(s)=11), moment triple ((1,0,1)), and (F(s)=1/10), so (eta_ple1/10).
For any nonzero (a), if (u
e0), then (F(a)ge|u|/10ge1/10).
If (u=0) and (h
e0), the exact lattice congruence (h-uequiv0pmod6) yields (|h-u|ge6), hence (F(a)ge6/42>1/10).
If (u=h=0), nonzero (a) implies (v
e0) (the moment matrix is invertible); (vequiv0pmod3) and (h-u-6vequiv0pmod{12}) give (vin6mathbb Z), hence (F(a)ge|v|/60ge1/10). This proves (eta_p=1/10) simultaneously for all (pge11).

Next if (F(a)le3/20), its first three summands force
[
|u|lelfloor10(3/20)floor=1,quad
|v|lelfloor68(3/20)floor=10,quad
|h|lelfloor50(3/20)floor=7.
]
All integer moment triples are therefore contained in an **unconditional finite box of 945 triples**, independent of Port. By the exact inverse
[
x=(h+19u-8v)/2,quad y=(-h-14u+7v)/3,quad z=(h+11u-6v)/12
]
and congruences (vequiv0pmod3, h-uequiv0pmod6, h-u-6vequiv0pmod{12}),
there are exactly **32** nonzero *oriented* integral candidates in that box. Direct exact evaluation of all six rational summands at threshold (3/20) eliminates four oriented candidates, leaving **28 oriented =14 unoriented**. The complete directions, their scores and their exact Port costs are the displayed table; the companion JavaScript checker verifies every integer congruence, inverse, score, count and row of the finite exhaustive step without floating point.

Since (eta_p) is already fixed and the exhaustive closed sublevel set is independent of Port, intersection with (qle p) gives exactly the displayed indicator formulas for every (pge11). Two boundary vectors enter at Port 37 and 44; strict sublevel vectors stabilize at Port 38. The sharpness claim follows at once. QED.

## Verification scope and next question

The symbolic reduction to the 945-element moment box is valid on the entire infinite integer lattice. The finite check proves coverage of the last 14 cases by exact integer arithmetic, not by a bounded-Port guess. We make no claim of independent scientific review, formal verification or native physical realization.

Remaining: determine whether **13 strict** (3/2)-near-optimal vectors can occur for *any* positive four-weight BRC norm and any Port; if not, prove the stronger uniform bound 12. An exact parameter-chamber feasibility certificate or structural obstruction distinguishing this six-pair norm from a generic cube norm would settle the question. Separately retain P000 observer-fidelity and original R063 native benchmark obligations.
