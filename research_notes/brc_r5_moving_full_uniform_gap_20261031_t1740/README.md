# R5 — Moving FULL support: uniform positive separation over the whole shared-error cube

Date: 2026-10-31 (Asia/Shanghai). Author-side portable research. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## New all-real result

For the original source-positive P/Q two-merger stopping model with alpha_0=1/4 and alpha_1=1/8 (immutable source e7916482f44a925e11ece98e406309f4655fb1f1), use the signed four-coordinate observer J=41 error_Q - 12 T_Q. Assign *common* legal error labels to the eight source/route/action L histories: each STOP label in [0,epsilon], each CONTINUE label in [1-epsilon,1], for 0<=epsilon<=1. FULL has origin/history-dependent policies; seedless LR shares A,D,Y,L keys.

The moving-support minimax, optimizing FULL and LR again after each shared perturbation, is exactly

    min_r (sup_FULL J - sup_LR J)
      = 2 - min(41*epsilon,29)/16
      = 2 - 41*epsilon/16 for 0<=epsilon<=29/41,
        3/16             for 29/41<=epsilon<=1.

Hence four-dimensional convex hulls differ for EVERY legal shared-L-response vector; the full sup gap is >=3/16, yielding an L-infinity FULL-to-LR-hull distance witness >=3/848. This is stronger than the prior *fixed-witness* margin that reached zero at epsilon=151/205. The fixed-witness threshold was not the moving-support threshold.

## Proof nucleus

Put u_i=41*r_(i,Y,STOP)-29 in [-29,41*epsilon-29] and v_i=41*(r_(i,Y,CONT)-1) in [-41*epsilon,0]. Exact Bellman dominance makes D STOP and Y CONTINUE optimal; FULL always continues A only for origin 0 and stops A for origin 1, then chooses the best origin-0 L action. Seedless LR either stops A or continues with one shared L action. Therefore, for all real legal r,

    sup_FULL J = -10 + max(u_0,v_0)/16;
    sup_LR   J = -12 + max(0,(2*u_0+u_1)/32).

The proof in the evidence bundle establishes the exact two-piece minimax by comparing two affine cases and supplies an attaining common response assignment. No full four-dimensional hull equality or native X6 claim is made.

## Complete reproducible evidence

The linked compressed archive is a standard gzip tarball containing the four original NONEMPTY files:
- RESEARCH.md — complete statement, model, all-real proof, assumptions and limits;
- VERIFY.py — actually executed Python standard-library Fraction verifier;
- EXACT_OUTPUT.txt — literal output, final line PASS_EXACT_R5_MOVING_FULL_UNIFORM_J_SEPARATION;
- NEXT_TASK.md — precise continuation and control boundary.

Program checked 1,024 FULL and 16 LR deterministic policy paths with both P/Q normalizations, 30 independently enumerated source-labelled policy-extremum cases, and 256 corners times six exact rational epsilon values. Finite tests are supplementary, not a replacement for the all-real symbolic proof.

Archive Git blob SHA-1: f428dbb19d55e8b483bdfc6a8b89d5d3e1f917bb
Archive SHA-256: 956503692009d0f3fa65bb0e3ab750745a5e1783d9a5824787d6036ce90f904d
Local file SHA-256: RESEARCH 2a974852dbec6e1129908261bb7bba339573628a060cfb0d7072afe61f93bc79; VERIFY 88474bfb1c6ff330c0ddb9ce3da1a6a2984c9de420f24e5249d30e3fd58bb7d2; OUTPUT ab7cbe52b98e7440e15a6625aa8d82e1d9b3d5779b1e1b8a5d55a994b2159fef; NEXT b8d11329710752aef9a033e15f9b6e0b4e433e4650b5ae2033b46bcc28af0436.

Frozen sources: GLOBAL_KNOWLEDGE_V1 main@a8ac2ca67df02b5e1050370145c00ea19607b4d4; Enterprise Math main@cd0d692a5510dddcc42991b056ed032933e0b164; P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (same-snapshot projection match). P000 and ACTIVE worldview are not modified. Native read reported research_authority_granted=false and executor_binding_configured=false; bounded owner inventory yielded CONTROL_QUOTA. This is not a Source CLAIM/Result or independent Driver review.

## Next unit

Change an UPSTREAM information/decision coupling (for example a stage-2 source-sensitive C terminal response), while keeping the strictly positive P/Q transition table. First derive the necessary and sufficient criterion for J-support equality; a zero J gap alone does not establish four-observer hull equality. Then seek exact <=5 LR vertex-mixture certificates for all FULL vertices or Farkas separators. See NEXT_TASK.md inside the archive.
