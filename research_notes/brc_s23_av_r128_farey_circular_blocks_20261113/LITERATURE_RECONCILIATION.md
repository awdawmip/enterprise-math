# R128 literature reconciliation and novelty classification

Date: 2026-11-13. Companion to `PROOF.md` at the same research branch. This was checked **after** the local derivation and before final reporting.

## Prior art verified

Anna E. Frid and Damien Jamet, **“The number of binary rotation words”**, *RAIRO — Theoretical Informatics and Applications* **48** (2014), 453–465, DOI **10.1051/ita/2014019**, [journal record](https://www.numdam.org/item/ITA_2014__48_4_453_0/), [arXiv preprint](https://arxiv.org/abs/1302.3722).

The published abstract explicitly reports an exact formula for the number of binary words obtained by coding rotations with a partition of the circle into two intervals, and sharp growth `Theta(m^4)`. This is the same *general free-rotation word counting class* as R128's `U_m` (up to exchange of bit names/orientation and the endpoint convention for finite words). Therefore the universal fourth-order growth, general rotation-word counting problem, and prospect of an exact formula are **prior published mathematics**, not a novel R128 theorem.

The local Farey-sector proof is retained as an independently derived constructive enumeration/certificate specifically adapted to the present S23 feasibility input. Its simple explicit upper bound is not claimed to improve the 2014 literature. The verified journal abstract suffices to establish the prior-art overlap and sharp asymptotic; the published exact formula was subsequently checked term by term against the count table (see below).

## Actual project-specific contribution

R126 had an exact fixed-three-integer feasibility reduction **for one prescribed m-bit S23 signature**. R128.3 connects its witness-preserving S23 feasibility filter to a finite list of all free rotation words: use the Farey-sector construction to generate candidates, retain the original signed S23 coefficients and frozen science, then test each candidate via the R126 exact predicate. This yields an explicit `O(m^7)` **count of 3-integer ILP instances** for full S23 signature enumeration (assuming `|P_m|=O(m^3)`), with no exponential enumeration of all `2^m` bit strings. This cost is an algorithmic corollary/composition under existing fixed-dimension ILP theory; no independent novelty or asymptotic improvement over every published rotation-word algorithm is claimed.

The exact Fraction generator and S23 sampling/checks are concrete reproducible integration artifacts. The exact published Frid–Jamet Theorem 1 formula has now been transcribed and evaluated independently: all `m=4..13` local exact counts and nine paper Table 1 entries agree. See [LITERATURE_FORMULA_CROSSCHECK.md](LITERATURE_FORMULA_CROSSCHECK.md) and [check_r128_lit.py](check_r128_lit.py).

## Revised research direction

Rather than seeking `o(m^4)` for the **free rotation family**, which would contradict the known `Theta(m^4)` result, investigate **S23's correlated one-parameter phases** `({x+A*theta},{d*theta},{E*theta})` and whether a smaller coefficient-sensitive bound or direct enumeration algorithm is available. Also implement the actual fixed-3D ILP backend, with strict boundary witnesses, branch provenance and full coefficient bit-costs.

## Evidence status

Bibliographic overlap and sharp asymptotic: independently verified from the 2014 journal abstract on 2026-11-13. Constructive local proof and exact finite tests: author-side R128 files. Novelty/admission: independent review pending; no formal CLAIM or native X6 promotion.
