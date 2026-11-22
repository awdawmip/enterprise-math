# CBRC F7 r477 — rigorous near-half B15 rational upper bound from integer-certified search

Date: 2026-11-22 (Asia/Taipei). Driver mathematical/computational contribution by the existing logical RESEARCH_DRIVER lane EM-DVR-DEBB5E. The F7 original scientist EM-CBRCF7-83A1D4, frozen Result RR-AA38973D56330E59D315, all original credits, and existing Native review/Task authority remain unchanged.

## Original model and theorem

Retain exactly the r476 original F7 class: q: Z^2 -> R, q(-x,y)=q(x,y); q(0,0)=0; q(x,0)=1 for x != 0; q(x,y)>=1/2 for y != 0; q(2,1)=q(-1,-1)=1/2. For k=a-2b-c+2d, set D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d), and e_B=inf_q max_{(a,b,c,d) in [-B,B]^4} |D_q|.

**Certified result** (an exact finite rational upper bound, not exact B15 optimization):

    1/2 <= e_15 <= 200000001 / 400000000 = 0.5000000025.

The lower bound is the existing fixed-marker obstruction; the new upper bound follows from the following explicit finite-precision *rational function*, verified exhaustively by integer arithmetic. A global admissible q is obtained by extending the finite coordinate values with the original baseline beyond the finite evenness-closed support.

## Frozen rational witness and exact check

Use denominator DEN=100000000 and represent every off-axis q(x,y) by an integer Q(x,y)=4*DEN*q(x,y). Axis/mark values are fixed exactly at 0, 4*DEN, or 2*DEN. On the finite transformed-coordinate set, there are 4,730 other evenness-identified (|x|,y) coordinates. Set their Q values in the deterministic r476 q-variable enumeration order to the little-endian signed 32-bit integer array with SHA256:

    f03892d11b67ec8a6a687ae77d3ce24b14fc0d6edabb94d7489687ab5ca25bf1

The array contains 18,920 bytes. It was constructed using SciPy 1.17.0 / HiGHS 1.8.0 numerical `highs-ipm` on the *unmodified* r476 B15 extended system, followed by rounding Q to integers. The numerical solver is **not** the proof; it merely generated the finite integer candidate. The fixed SHA identifies the exact bytes used by the independent full-domain integer checker. The uploaded GitHub reproducer builds the same witness (or accepts a copy through `--verify`), checks its SHA and verifies all required original conditions. The original run was repeated: both regeneration and independent verification of saved bytes returned the same SHA and maximum.

With the integers held fixed, an actual exhaustive loop over **all 31^4 = 923,521 original quadruples**, using the original shear formula and no floating arithmetic, yielded:

- minimum free off-axis Q: 200000000 = 2*DEN, respecting q>=1/2;
- maximum free off-axis Q: 660482273;
- exact maximum |4*DEN*D_q| = **200000001**;
- number of quadruples whose |D_q| strictly exceeds 1/2 for this candidate: **702**;
- one attaining input: (a,b,c,d)=(-15,-5,14,-14).

Thus its exact maximum absolute error is **200000001/400000000**. This finite witness does *not* satisfy the strict B15 half-error system; the exact optimization question e_15=1/2 is still open. The improved upper bound nevertheless shrinks its possible gap over 1/2 from the previously known 1/14 to 1/400000000.

## Reproducibility and proof boundary

Code: `research_checks/CBRC_F7_R477_B15_NEAR_EXACT_RATIONAL_UPPER_20261122.py`, coupled with the previous verified `research_checks/CBRC_F7_R476_FINITE_FIBER_EXTENDED_LP_20261122.py`. Run from `research_checks/`:

    python CBRC_F7_R477_B15_NEAR_EXACT_RATIONAL_UPPER_20261122.py --write F7_R477_B15_q4x1e8_witness.bin
    python CBRC_F7_R477_B15_NEAR_EXACT_RATIONAL_UPPER_20261122.py --verify F7_R477_B15_q4x1e8_witness.bin

A 18,920-byte fixed witness was generated and independently rechecked in this run; the immutable bytes are identified by SHA256, and the source contains a complete deterministic reconstruction/verification recipe. The binary was not separately committed to GitHub in this subunit; retain the original runtime copy for byte-for-byte external auditing. The source script uses floating point only to propose values; all theorem-bearing tests run over Python integers.

No statement about global e_infty follows beyond the pre-existing 1/2 <= e_infty <= 4/7. B15 exact e15 may equal 1/2; neither feasibility at exactly 1/2 nor a positive separating dual certificate has been established.

## Control classification

One independently computed and exactly checked finite rational upper-bound subunit saved. This is not Native Review, Result admission, formal Task completion, global objective completion, author-independent approval of earlier F7 source, or a new CLAIM. Original F7 and T6 real scientific origins are preserved; no schedules or other owners changed.

Previous r476: [exact cubic LP](../driver/2026-11-22_f7_r476_exact_finite_fiber_extended_LP.md). 
