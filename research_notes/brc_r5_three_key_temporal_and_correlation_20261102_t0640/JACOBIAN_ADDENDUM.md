# R5 addendum: the actual three-key stopping DAG already has FULL interior rank four

Dated 2026-11-02 (Asia/Shanghai). Supplement to RESEARCH.md at immutable commit dfdb0f5860a473ccb6fa22866c3d2f59ef6bb6ba. Scientific status: exact author-side Jacobian computation, not independently reviewed or admitted. Same frozen scientific inputs.

Let F(x,jB,jI,kC,kI,kBJ,kIJ) be the **actual two-law stopping-DAG four-observer map** in VERIFY.py, not the abstract correlation benchmark. Evaluate all seven FULL behavioral probabilities at 1/2. The four Jacobian columns with respect to (x,jB,jI,kC) are exactly:

    dF/dx  = ( 67/480, -19/240, -55/48,  -103/96)
    dF/djB = ( 23/240, -11/120, -1/3,    -17/48)
    dF/djI = ( 11/240, -23/480, -17/96,  -1/6)
    dF/dkC = ( 1/16,   -3/16,   -5/16,   -7/16)

Every column is computed without numerical differentiation: by multi-affinity it is the difference between the exact physical two-law observation with that coordinate set to 1 and set to 0, holding every other parameter at 1/2. Taking the columns in the listed order gives the exact determinant

    det[ dF/dx, dF/djB, dF/djI, dF/dkC ] = -1/5120 != 0.

Consequently the source-aware FULL real-image of this **genuine 3-key stopping model** contains a nonempty four-dimensional open subset (fix the remaining three parameters at 1/2 and use the inverse function theorem). The seedless LR image is the Lipschitz image of a three-dimensional cube, hence has zero four-dimensional volume. The actual real images therefore differ. In this current model we additionally have an explicit stronger convex-hull separation W and gap 1/6 from the main note.

**Reusable search implication:** the Jacobian-rank half of the proposed equal-hull/different-real-image certificate is already satisfied by a physical stopping architecture, not just by the abstract correlation carrier. Since the determinant is a polynomial/continuous function of the interior natural kernels and branch weights, it stays nonzero throughout some open neighborhood of this physical parameter point. The remaining difficult obligation is to cancel **all** FULL-vs-LR convex-hull support differences while keeping an exact nonzero rank minor. The already identified first facet to repair is n=(0,0,1,-1), with gap 1/6.

The separately saved VERIFY_JACOBIAN.py imports the unchanged verified VERIFY.py, recomputes all four columns from the actual two-law branch evaluator, asserts determinant exactly -1/5120 using fractions.Fraction, and prints PASS_EXACT_R5_THREE_KEY_FULL_JACOBIAN_RANK4. This addendum does not change prior four-file research evidence, P000, ACTIVE worldview or frozen source pins. No native owner or task admission is inferred.