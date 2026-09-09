# Candidate counterexample to an auxiliary even-divisor classification

Author of this audit witness: Driver `EM-DVR-5816EB`. Status: exact polynomial identity checked; a separate [non-author paper review](https://github.com/awdawmip/enterprise-math/blob/61dedaa3528fc32757e1a7c8636b5167da2e959b/research_artifacts/RB_EVEN_DIVISOR_NONAUTHOR_CHECK_20260909_82DF76/REPORT.md) has qualified-passed all six bounded obligations. This is source-exposed review, not a blind reconstruction.

On `C:t²=R³-3R`, let O be infinity, `T0=(0,0)`, and

`U=R³+2Rt+R²-3`.

The identity `R U=(R²+t)²` is checked by formal integer-polynomial rewriting. Replacing U by U+1 leaves residual -R. As a function-field identity, `U=R(R+t/R)²`.

The proposed paper argument is:

- `div(R)=2[T0]-2[O]`, so div(U) is even.
- U is a polynomial in R,t and is finite-regular. At O the terms have pole orders6,5,4,0, so U has exact pole order6 and belongs to L(6O).
- Its square class is [R], which is geometrically nontrivial because T0-O is a nonzero two-torsion divisor class. Otherwise a function with divisor T0-O would give a degree-one map from a genus-one curve to P1.
- U has the nonzero t coefficient2R, so it cannot have form `(R-r)(a+bR)²` for any r in `{0,±sqrt(3)}`. Its nontrivial square class excludes a square from L(3O).
- It is also nonzero at the five finite branch points used by the cited pencil: U(T0)=-3; U(T±)=±3sqrt(3); U(P±)=-7-4t at `R=-2,t=±i sqrt(2)`. The last value cannot vanish because that would require `t=-7/4` and simultaneously `t²=-2`.

The missing allowed half-section is `R+t/R`, which has a pole at T0 compensated by R's double zero. It lies in `L(2O+T0)`, not L(2O). More generally the proposed complete nontrivial type is

`(R-r) L(2O+T_r)²`, where `T_r=(r,0)` and `L(2O+T_r)=<1,R,t/(R-r)>`.

This degree-three basis is already the S=T_r specialization of section5 of the archived empty-fiber paper. The original source's smaller L(2O) space omits it.

Target of the criticism: `payload.exact_reduction.six_block_obstruction` in the raw freeze at `c73816d3552b4247861e12e476101e94a4a2ce5a`, not the later concrete source-exposed map. The original checker checks arithmetic/j values and does not prove the claimed exhaustive even-divisor classification.

Limits: U is one even-divisor member, not a triple `G,G-F,G-lambda F`. It does not solve the full ODE or establish a global six-block map for the frozen lambda. The conclusion sought from the reviewer is that the cited auxiliary classification/proof is incomplete, while the six-block exclusion theorem itself remains undecided by this witness.
