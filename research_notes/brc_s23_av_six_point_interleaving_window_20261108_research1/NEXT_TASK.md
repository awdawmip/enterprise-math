# Continuation after third S23/AV inversion window

Date: 2026-11-08; frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Latest proof: `PROOF.md` in this directory; prior four-point proof: `c43c0279fb4b53b7b7e0d53b1ae4836994fa382b`; PR #1777.

New exact frontier: for `9820786<=H<=9821295`, true threshold order is a disjoint union of `T(H-9820786)` six-point interleavings, `T(H-7365717)-2T(H-9820786)` four-point rotations, and the **H-invariant** `2455069^2=6027363794761` isolated swaps. This is a constant-time pointwise correction of the old integer-key rank/select, with full symbolic proof and finite exact checks.

**Next discriminating unit:** at H=9821296, handle the newly feasible `2q2=2u+4w` inversion (K=2) and its interaction with adjacent-key local blocks. Derive a new disjoint finite local permutation or a concrete obstruction/counterexample; check a scaled unimodular model first, then prove full exact H window.

**Independent active unit:** H=2455579 global changed-gap prefix occupancy, to settle N(H). This question is independent of exact threshold ordering.

BRC relation carrier: retain joint (1,4) counts and padding, preserve provenance and future observation, and treat these as order/readout results only. Native owner/CLAIM and independent mathematics review require current Source receipts; this author proof makes no such authority claim.
