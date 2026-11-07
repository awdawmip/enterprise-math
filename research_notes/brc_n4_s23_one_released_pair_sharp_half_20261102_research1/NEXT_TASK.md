# Next research unit

Mother question: joint optimization of ten randomized decoder kernels for all eleven real lawful BRC N4 S23 controls with original six-source mixing; previous global minimax bracket [1/2,2/3].

Completed local sharp result: for each h=1..8, freeing Dh in addition to D9,D10 gives exact 1/2 seven-witness minimax (rather than exact 4/7 with two free kernels). The same explicitly given Dstar works for every h; read PROOF.md and VERIFY.js.

Action A (discriminating exact test): keep D1..D8 except one h, insert Dstar,D9,D10, scan all 3^11 ternary lawful policies using the original M20 and shared a_A,a_B,b_U,b_AV,b_BV,c* mapping. Record the worst target(s), loss fractions and active decoder. Compare across h; identify new controls that witness a loss above 1/2. Finite ternary results are candidate frontier, not a continuous certificate.

Action B (continuous analytic route): for the best candidate bank, derive a rigorous sign-cell / multi-affine parameter-domain covering bound on all [0,1]^11, preserving shared b_U and each of six preparations; attempt a certified full-domain <2/3 upper improvement or a specific counterexample.

Independent complementary route: find a finite legal witness set forcing error >1/2 for arbitrary jointly redesigned ten kernels, or a proof that this threshold is globally sharp.

Native authority: do not borrow earlier author/session IDs or issue authenticated CLAIM/Result/Review under the read-only gateway. Author-side results remain UNREVIEWED / NOT_ADMITTED pending current owner/Driver decisions.

## Update: exact whole-domain trial-bank counterexample (2026-11-02)

The proposed Action A test was completed with exact integer arithmetic across all 3^11=177147 ternary lawful policies for each of h=1..8. Every proposed bank (original seven pairs + D9,D10,Dstar) attained max loss 1. More decisively, the *same* lawful vertex `Z=(0,1,0,1,0;1,1,0,0,0,0)` forces every one of the eleven candidate kernels to incur TV loss exactly 1 by explicit prepared-row disjoint atoms. See COUNTEREXAMPLE.md, VERIFY_COUNTEREXAMPLE.js and RUN_COUNTEREXAMPLE.json in this directory.

Next independent unit: reoptimize the three free stochastic kernels jointly on **eight** strategies W,J,A,B,C,X,Y,Z with each one of eight frozen-pair releases; determine exact minimax and whether the former 1/2 obstruction persists. Explicitly include six prepared rows and causal b_U. A second independent unit is bank-independent witness or real-domain certificates to improve the global jointly optimized ten-label bound; do not reuse a full-domain upper claim for the refuted trial bank.
