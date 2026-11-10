# R5: An exact lawful 11-arc Blackwell minimum and a five-dimensional local stratum

Date: 2026-11-10 (Asia/Shanghai). Mode: author-side exact rational result, not independent review or canonical Source Result.
Frozen scientific sources unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

## Precise model and dependencies

Continue the seven-likelihood-ratio P/Q–BRC statistical Blackwell transport of PR #1950 (`c8a0ade3904507cf4dda38bfa888bdb490b1ea87`), with 14 physical strategy parameters, five affine equalities, 26 capacity slacks, 30 allowed nonnegative transport arcs, all 21 martingale/marginal equations and the frozen eight-parameter family `p(z)=p0+P*(tstar+z)`. Reuse the 13-edge exact result of PR #1963 (head `a7808fdc1c5715bc2a8859278d0f6b85750811fa`) only at its exact certified definitions and frozen inputs. The accompanying `VERIFY_11.py` reconstructs these quantities **self-contained** and validates all proof-critical conditions using exact SymPy rationals / Python Fraction.

These 30 edges are positive statistical transfer branches. The eight auxiliary parameter coordinates and five-dimensional stratum do not change the P000 native six-dimensional spatial structure or the independent time dimension.

## Exact 11-edge physical witness

Define

```
R = 49948501046391 / 3920403670319950000
zc = R*(-1,1,1,-1,-1,-1,-1,1)
alpha = 53523764802790621389 / 287880142016181828437500
z13 = zc - alpha*e5 - (293725/3287440)*alpha*e7
k5 = (14343940/34101, 0, 0, -260, 0, 0, 0, 1)
h = -2110010319589186676373085701 / 21647807832978109719298700000000
z11 = z13 + h*k5
```

Here `e5,e7` are zero-based basis vectors in the **auxiliary physical eight-parameter family**. At this rational `z11`, two distinct edges of the previous 13-edge basis, `(0,2)` and `(3,2)`, simultaneously have weight zero. Exactly eleven remaining edges have positive rational masses:

```
F9 = ((0,0),(0,1),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
S2 = ((2,1),(0,3))
E11 = F9 + S2
```

All five original physical equalities and all 26 physical inequalities hold. The only zero physical slacks are indices 4,15,19,23; the other 22 are strictly positive. All **21 original Blackwell equalities**, not merely a reduced system, hold with the listed eleven edges. Exact positive margins:

```
min_positive_transfer = 51197529884140057879542511669 / 7326950343469514058839560000000
min_positive_physical_slack = 3862165470441621676320701979 / 666086394860864914439960000000
```

## Proof of global minimality for this exact physical point

Let `C` be the rank-15 rational reduction of the full 21-row system, `q=q(z11)`, and let `x>=0` be *any* solution to the full 30-edge system. For each of the nine listed `F9` arcs, `VERIFY_11.py` gives a fully explicit rational vector `y_e` and checks against **all 30 columns**

```
C^T*y_e <= indicator(e),       y_e^T*q > 0.
```

Consequently `x_e >= y_e^T*q > 0`. These nine arcs are **forced in every coupling** (not just in the constructed basis). Every hypothetical coupling with at most ten positive edges would have only at most one additional arc among the remaining 21. After quotienting out the nine forced columns using the exact 6-by-15 left annihilator `L9`, the checker exhausts all 21 singleton candidates and verifies

```
rank([V_j | L9*q]) > rank(V_j)      for every j in {1,...,21}.
```

These rank obstructions exclude all <=10-edge couplings, including smaller supports by extension. Together with the explicit eleven strictly positive masses:

```
N_min(z11) = 11.
```

A second exact exhaustion of all `binom(21,2)=210` possible two-extra-arc supports shows **exactly one** quotient support contains `L9*q`, namely `((2,1),(0,3))`, which is the displayed positive solution.

## Five-dimensional local stratum and its scope

The eleven-column reduced matrix `M11` has rank 11 and a 4-dimensional left nullspace `N11`. The induced physical observation derivative `G=N11*T` has exact rank **3** in the eight-parameter physical family. Thus the affine parameter locus on which the eleven named columns solve the complete constraints is `z11+ker(G)`, of dimension **5**.

The eleven weights, nine forcing-dual lower bounds and 22 nonstructural physical slacks are all strictly positive at `z11`. They remain so on a sufficiently small relative-open neighborhood inside this affine five-plane. The 21 singleton and 209 other doubleton support spans are finitely many closed subspaces excluding the exact right-hand side at `z11`; therefore one common ambient neighborhood excludes every alternative <=11-edge support. In this neighborhood the exact lawful minimum-11 locus is **precisely the relative-open part of the displayed five-plane**, with the unique eleven-edge support `E11`.

This is an author-side exact theorem about the original fixed *auxiliary statistical* model, with a finite exhaustive checker. It neither changes P000 nor claims any untested global lower bound across other legal physical strategies.

## Actual execution and evidence

Run `python VERIFY_11.py` with Python 3 and SymPy; the script is stand-alone, reconstructs the frozen numerical input, checks 5+26 physical conditions and 21 transport equations, validates 9 complete duals and exactly 21+210 finite rank candidates, checks rank 3 and emits exact fractions. `EXACT_OUTPUT.txt` records a local **actual execution of this exact self-contained script**, including the PASS line; no floating-point acceptance is used.

Researcher-ID at this run: `EM-DIRECT-0F9746 / TASK_RESEARCH`; native activity `RA-FC85051BCB10301EC4E3E7F2`, registered in canonical EM main `ccb636c9e667e5818720e7e1940bcdc1f5feb232`. Current canonical task dispatch chose `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, not R5; **no R5 CLAIM, freeze, Result, or independent Review** is asserted. This research branch is separately attributable, author-side evidence.

## Next discriminating experiment

Search within the five-plane for a lawful simultaneous vanishing of one more edge, and test exact <=10 support feasibility with all surviving full-model forced-arc duals, accounting for their changing positivity. Also investigate whether 11-edge support can occur on other affine sheets outside this local chamber, preserving true physical capacity and full observation constraints. Formal independent mathematical examination and Source Result intake remain separate.
