# R5 next frontier: integrate four-parameter q=1 and chart-specific sharp boundary

**Frozen source pins:** Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged. Current control/normative snapshot is separate from scientific pins.

**Verified completed new units (do not redo):**
1. `RESEARCH.md`, `VERIFY.py`: For source `x(q)=(1,0,1,0,9/160,21q/80,0)`, a nonnegative Blackwell kernel on common face `C_(3/4)` exists iff `q∈[0,1343/1589]`; exact stopping-time separator, 12-edge and 13-edge endpoint witnesses, 1001 exact regressions. This is strictly fixed-face; on C_(1/4) the source itself is seedless even at q=1.
2. `Q1_PRISM.md`, `VERIFY_Q1_PRISM.py`: Three-dimensional full `(t,p,q)` box at `theta=1/4,kappa=3/4`, `t∈[0,1/5]`, `p,q∈[0,1]`. Exact 8 corners, 37 transport edges at 4 nontrivial corners, 601 tests.
3. **Stronger latest**: `THETA_PRISM.md`, `VERIFY_THETA_PRISM.py`: All real `t∈[0,1/5],p,q∈[0,1],theta∈[0,3/4]`, fixed `kappa=3/4` have a seedless target on one common C_(3/4) face and a calibrated Blackwell transport. Proof uses 16 exact corners (4 nontrivial t=1/5,theta=0 corners with 37 positive transfer edges), multi-affinity and 601 exact regression tests. This **subsumes unit 2**. Signed residual `9t(theta-3/4)/10` is nonpositive, negative in its interior.

**Next discriminating target**: Extend the current four-dimensional prism across varying `kappa` (positive-residual region) and/or `theta∈(3/4,1]` while retaining full `p,q∈[0,1]`. At fixed `t=1/5,p,q∈{0,1}`, test `theta=1,kappa=3/4` on charts `C_(1/4),C_(1/2),C_(3/4)`; use one exact rational feasible kernel or an exact Farkas separator for each selected face. A true global counterexample requires excluding **all** lawful seedless targets, not just one face. Separate LP float discovery from Fraction certificate construction.

**Source status**: GitHub author-side mathematical proof only, independent review/admission pending. Native active owner/claim/unshared task authority not inferred. No edits to P000, protected worldview, Result/Review or frozen task scientific pins.
