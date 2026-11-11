# R5 — a relatively open 12-dimensional triple-exit region

Date: 2026-11-11 Asia/Shanghai. Author-side exact rational construction; independent mathematical review and formal Source Result pending.

## Frozen input and predecessor

Frozen P/Q–BRC Blackwell auxiliary observer, science pins global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e, continued unchanged. The seven target likelihood integers are R=(2,10,15,20,25,30,38). Four dynamic ports j=(1,2,3,5), seven target labels i=(0,...,6), 28 dynamically allocated nonnegative entries in source-major order, two immutable positive singleton arcs, and the same 15 exact observation equalities Ax=b, rank(A)=13. The full physical observer has rank 15.

Direct predecessor: R5 common-C three exits (Draft PR #2088, commit b69383e8665eb0fa71041356b63191661f5d7392). That work exhibited three exits from a single C-support starting transfer but placed the m=4 exit on the exact source-5 compensation-capacity boundary. Earlier R5 four-mask census PR #2063 exhibits a full-positive 27-arc C-face point.

Source-3 masks C={2,3,4,6} and B={2,3,4,5}; the C/B faces have affine dimension 12, by the earlier exact rank and full-support certificates. A six-arc atom H_j(v) adds the three-entry moment-null vector v on source 3 and subtracts v on the compensator port j.

## New theorem — full-dimensional robust triple exits

There exists an explicitly certified rational point Z in the **relative interior of the 12-dimensional C-face** such that, from exactly the same Z, **three different single six-arc port-5-compensated atoms** with target triples {2,5,6}, {3,5,6}, {4,5,6} lead into the **relative interior of the 12-dimensional B-face**. Every connecting segment remains nonnegative and preserves all fifteen observations. The set of such Z contains a nonempty relatively open subset of the C-face. In particular the common-three-exit phenomenon is not restricted to a lower-dimensional boundary witness.

For m=2,3,4, the exit vector on source 3 is v_m(m)=-8, v_m(5)=38-R_m, v_m(6)=R_m-30; its compensator is source 5. If c=X_(6,3)>0, the forced coefficient is t_m=c/(30-R_m). The strict conditions
  X_(m,3) - 8t_m > 0
and
  X_(5,5) - (38-R_m)t_m > 0
together with X in the relative interior of the C-face ensure the endpoint is in the relative interior of the B-face. The two inequalities are affine in X, because t_m is linear in c, so their simultaneous strict solution set is relatively open.

## Explicit construction and exact rational certificate

Start with the exact common transfer C0 printed in the predecessor note, recreated by the accompanying verifier. The m=4 compensator slack at C0 is zero. Apply a fourth, independent, small kernel perturbation on source-3 target triple {2,4,6}:
  u_3=(-13 at 2,+23 at 4,-10 at 6),
  u_5=-u_3,
  epsilon=1/10000.
The mass and moment checks are -13+23-10=0 and -13*15+23*25-10*38=0. The entire segment C0 -> C1=C0+epsilon H_5(u) is nonnegative, has mask C, and retains all observations. The source-3 target-6 mass decreases by 10 epsilon without changing source-5 target-5 mass; hence the previously binding m=4 compensator inequality acquires slack 26 epsilon=13/5000. The other two exit inequalities remain strictly positive (see exact output).

Construct W in the relative interior of the C-face by the already established exact pivot certificate from PR #2063: order dynamic columns by j=1,2,3,5 and i=0,...,6; allowed columns are all except source-3 targets not in C, pivots are (16,1,17,18,0,8,26,27,5,20,13,22,2), and all twelve nonpivot allowed columns have value 1/800. Solve the 15 equations for the 13 pivots over the rational numbers. The verifier checks 25/25 allowed dynamic masses are strictly positive and all equations hold.

Set
  Z=(999/1000) C1 + (1/1000) W.
By convexity Z belongs to the relative interior of the C-face. Exact substitution verifies the strict inequalities for all three m. The minimum of all six source-3 and compensator slack values at Z is
  10065670282659/3907222060000000 > 0.
Therefore each exit reaches a different exact B-mask transfer with all its 25 allowed dynamic arcs strictly positive. Two positive immutable singleton arcs yield 27/27 positive allowed physical arcs at either endpoint. The interior witness and strict inequalities establish the nonempty relatively open region directly.

## Validation and scope

Run Python 3 standard library only:
  python VERIFY_ROBUST_TRIPLE_EXIT.py
The checked output is EXACT_OUTPUT.txt. Every matrix equation, nonnegativity, full-mask and strict exit assertion is exact Fraction arithmetic; the 13-pivot overdetermined rational solve checks the two redundant rows exactly. No numerical LP is needed. This is a conditional-on-the-frozen-auxiliary-model exact constructive theorem, not a claim about native X6 dynamics or an independent formal proof admission.

## Research value and remaining question

The previous boundary construction had three branches from one point. The present lemma supplies a relatively open 12-dimensional family of common-three-exit states, with all three images in the interiors of the B-face. It supports perturbation-stable planning of BRC atomic transfer moves.

Continue the distinct problem of three-step A->B pathways using at most two compensator port labels. The prior restricted 567-case numerical screen found six examples all using three distinct ports; it is not a certified full search. A useful next test is a source-mask/port combinatorial reduction independent of the fixed two-first-triple template, followed by rational primal or dual witnesses.

Provenance: previous R5 #2088 and #2063 are reused at their original immutable science, while current control/normative rules were read from main separately. No shared task ownership change and no independent reviewer identity is asserted.
