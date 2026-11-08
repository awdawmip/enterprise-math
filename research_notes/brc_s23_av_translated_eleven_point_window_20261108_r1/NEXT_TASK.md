# Continuation: translated eleven-point window, then first eleven-block collision

Date: 2026-11-08. Frozen science is unchanged: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

The new theorem proves the *entire* `H=9,821,296..9,821,805` exact true-threshold ordering by disjoint 11-/6-/4-/2-point blocks. At the right endpoint `H=9,821,805`, the counts are 130,305 eleven-point blocks, 260,100 six-point blocks, 3,016,186,774,585 four-point blocks, and the invariant `M^2=6,027,363,794,761` isolated swaps, with 15,075,927,373,081 inverted pairs. Proof and code: `PROOF.md` / `VERIFY.py`. Direct executed stdout: `RUN_EVIDENCE.txt`.

**Next discriminating question:** at `H=9,821,806=H3+510`, the two eleven-point blocks indexed by `x=0` and `x=u` overlap. Determine their exact union as a consecutive integer-key block, its true-order permutation, and whether all overlaps of translated eleven blocks in the following interval decompose into finitely many disjoint connected components. Start with scaled unimodular models, then prove a bounded global classification. Also inspect when `q5=u+5w` becomes feasible and changes the inversion-type list.

**Independent capacity question:** determine complete changed-gap prefix occupancy at `H=2,455,579`, distinguishing the capacity function `N(H)` from rank/select order.

This is author-side mathematical material in Draft PR #1777; formal task Owner/CLAIM and independent reviewer acceptance require current native Source state. No credentials or execution capabilities are stored.