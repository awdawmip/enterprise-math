# R752 — Exact C3/C12 semiconjugacy strata for R748 fixed-source versus V1R signed-frame law

Date 2026-11-12. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS. Original Run RUN-aea48b2b684b1204bf7fd828, generation 2 revision 5 at start. Original CLAIM MCP-aa543cb564e2a231d3fe6017. Frozen P000 @a72226e2430ffa4786321ac86e7f0c599d5f0389.
Status: author-side exact theorem and full 960-frame finite check, not native event permission or mathematical acceptance.

## Source and type discipline
R748 actual PR #2163 (research_notes/R748_X6_SIGNED_PAIR_BRC_SPECTRUM_THEOREM_20261112.md) defines directed-edge signed-Port states, each corresponding to a signed triad with a distinguished cyclic phase; its fixed-source C1 shift cycles three *identical signed ports*, with period three. Resampling is a different kernel A/16.
V1R research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md defines ordered axes a=(a0,a1,a2), ordered signs s=(s0,s1,s2), with R_can(a,s)=(cyc(a),-s), where signs are negated in the same slot positions, NOT cyclically permuted with axes. Its internal state has SHELL/CLOSURE mode, and T^2=(R_can, mode unchanged). R750's correction of R749 theorem 2 remains binding.
The signed-Port triple associated to a frame is p(F)=((a0,s0),(a1,s1),(a2,s2)). R748 C3 shift C(p0,p1,p2)=(p1,p2,p0).

## Theorem A: abstract cycle factor exists, but does not establish signed-source compatibility
Every V1R orbit has length 12; every R748 fixed-source orbit has length 3. Abstract equivariant maps of a V1R 12-cycle onto any selected R748 3-cycle exist, by sending phase k modulo 12 to phase k modulo 3. This requires an arbitrary choice of cycle origin and target signed source. It is NOT a canonical source-preserving map, nor a native Cell/Link/Port event license. Conversely a full 12-cycle cannot be injectively represented by only three phases.

## Theorem B: sharp signed-source compatibility for T^4 and T^8
Let F have distinct axes and signs s. V1R T^4 applies R_can^2: it shifts axes twice and leaves the sign tuple in the SAME slots. R748 C^2 shifts the three entire signed ports twice, including signs. Equality p(T^4 F)=C^2 p(F) holds iff s0=s1=s2. Similarly p(T^8 F)=C p(F) iff s0=s1=s2. Exactly 2*6*5*4=240 of 960 signed frames satisfy either identity. On the remaining 720 mixed-sign frames both identities fail.

Proof: equality forces the original sign tuple to equal its nontrivial cyclic rotation, hence all three signs equal. Conversely homogeneous signs make the two constructions identical. T^12 is the identity on all frames. For every F, T^2 flips all signs and therefore changes the signed-port source; there is no universal one-step signed-source-preserving identification of V1R T with R748 C.

## Theorem C: a valid restricted intertwining
Restrict to homogeneous-sign frames and the 4-step sampled V1R operation T^4, with either fixed mode. This is closed on the homogeneous-sign subspace and has exact period 3. The canonical map p to the signed-Port ordered triple intertwines T^4 with R748 C^2, and T^8 with C. For each fixed mode the restricted carrier has 240 frames; the two modes give two separate copies. This is a genuine signed-Port/source-preserving exact relation for the *sampled* dynamics. It does not assert the intermediate T,T^2,T^3 steps preserve signed source, and it is not a native event authorization.

## Theorem D: universal obstruction at intermediate steps
For all 960 frames, T^2 sends each signed port sign to its negative (at permuted axes), and the resulting signed-Port source cannot equal the original source under an odd three-port sign-flip cycle with all distinct axes. T^4 returns to the same signed source only for homogeneous-sign frames. Therefore a universal, instantaneous source-preserving conjugacy from V1R's full single-step T to R748's fixed-source shift cannot be obtained simply by forgetting SHELL/CLOSURE mode and reading the current signed-Port frame.

## Finite verification
R752_C3_C12_SIGNED_SOURCE_VERIFY.py enumerates 960 frames, checks T^n at n=1,2,4,8,12 and exact signed-source equality. Expected result:
{"status":"PASS","frames":960,"R748_shift_compatibility_counts":{"1":0,"2":0,"4":240,"8":240,"12":960},"signed_source_preserved":{"2":0,"4":240,"8":240,"12":960},"homogeneous_sign_frames":240,"native_event_permission":false}.
The checker uses integer tuples and finite permutations only. Proofs above are universal within the exact finite V1R carrier and do not depend on numerical approximations.

## Next
1. Test a signed-frame gauge transport that maps mixed-sign V1R paths to a *twisted* R748 source-memory connection, retaining gauge provenance; do not silently equate different signed sources.
2. Investigate whether a declared native Cell/Link/Port guard admits any sampled T^4 coupled PASS event. R748 and V1R alone do not.
3. For a full event-level comparison, retain mode, sign-gauge and dependency history; source-preserving observer quotient must be explicitly scoped.
