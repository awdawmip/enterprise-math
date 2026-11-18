# An eight-event counterexample: scalar counts conceal both residuals
Date: 2026-11-15. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Scope: derived one-dimensional indexed-center radius-2 observer with original length-3 gap closures; scientific lineage and definitions in companion two-residual theorem, frozen R5 science pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

## Exact certificate
Use eight integer events, original consecutive gaps **(3,3,2,1,2,1,2)**, adjacent selected gap positions a=0,b=1, and K=4 center indices. Coordinates under closure masks empty,a,b,ab respectively are:

- empty: (0,3,6,8,9,11,12,14)
- a: (0,2,5,7,8,10,11,13)
- b: (0,3,5,7,8,10,11,13)
- ab: (0,2,4,6,7,9,10,12)

All four exact optimum nearest-center sums are **6**. Exhaustive enumeration of every 4-subset of eight labeled center indices produces optimizer-family cardinalities

    |O_empty|=1, |O_a|=9, |O_b|=4, |O_ab|=12.

The single-cut intersection surplus is **P={0236,0246}** and the joint-only surplus is **Q={1457,1467}**. In particular, **both residuals are nonempty with equal size two**.

The naive Boolean-diamond cardinality test passes:

    |O_ab| = |O_a|+|O_b|-|O_empty| = 9+4-1 = 12,

yet both Boolean-diamond **family equalities fail**. The correct two-residual equation is

    |O_ab| = 9+4-1-|P|+|Q| = 12.

Thus equal scalar counts alone cannot certify the family-level Boolean diamond; the R5 proof's separate labeled-language intersection check is mathematically load-bearing. The n=8 witness directly exhibits cancellation of positive P and Q.

Moreover the exact max-new/min-old replacement distances to the entire base optimum family are

    H(O_a,O_empty)=2,
    H(O_b,O_empty)=2,
    H(O_ab,O_empty)=3.

So in the **same** witness, scalar counts mask a **strict extra replacement** from joint closure, even though either single closure requires at most two replacements. The complete labeled optimizer families, coordinate arrays, exact costs and residuals appear in the adjacent `N8_SCALAR_CANCELLATION_EXACT_EVIDENCE.json`.

## Reproducibility and boundary

Evaluate `run_case([3,3,2,1,2,1,2],0,1,4)` from `VERIFY_R5_TWO_CUT_RESIDUALS.py` in this directory. The full enumeration checks all 70 four-center subsets of eight event indices per mask using integer distance arithmetic. A second independent JavaScript enumeration was run in the publishing action and confirmed 1,9,4,12 optimizer counts, P/Q sizes 2/2, all four optimal sums 6, and directed distances 2,2,3. This finite model falsifies scalar-count sufficiency in the stated geometric class; it does not change the already checked frozen 954-event special-case diamond. The resulting research question is to compute exact P and Q as **labeled path languages** with rank-aware intersection, not by a single cardinality equation.
