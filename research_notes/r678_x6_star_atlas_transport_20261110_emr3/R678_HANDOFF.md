# R678 研究交接｜移动四 STAR 支撑图册的 15/30 态定理

Date: 2026-11-10 Asia/Shanghai. Task RS-X6-NATIVE-ROTATION-DYNAMICS; science frozen a72226e2430ffa4786321ac86e7f0c599d5f0389; predecessor R677 same branch / Draft PR #1904.

**Theorem R678-A (support-atlas stabilizer).** Original FCC four STAR support triples are precisely the four vertex stars of K4 on six edge labels. Each original axis is the unique intersection of two STARs. Hence the unlabeled 4-STAR atlas set stabilizer in S6 is isomorphic to S4, order24, and its induced edge permutations are all even.

**Theorem R678-B (orbit and predictive quotient).** In S6 there are 30 distinct transported 4-STAR support atlases, split into two disjoint A6 orbits of 15 each. R677's three-STAR signed C6 candidate group G=(C2)^6⋊A6 has signed support stabilizer order1536 and reachable support-atlas orbit15. The full B6 signed permutation group has orbit30. For a future language querying the current exact 4-STAR support set and applying arbitrary group elements before re-query, the coarsest state quotient has exactly 15 (respectively30) atlas states; support atlas must be transported as α←gα.

**Counterexample**: g_136 maps original STAR {1,4,5} to {3,4,5}, outside the fixed four-STAR atlas. Thus a fixed-atlas-only realized-support interface does not implement all of G on that representation.

**Verification**: R678_VERIFY.py exhaustively checks all 720 unsigned permutations, equal-size disjoint parity orbits 15+15, stabilizer24, generator orbit15, and the concrete counterexample. All assertions pass; exact JSON evidence R678_EVIDENCE.json. Pass marker R678_SIGNED_C6_STAR_ATLAS_15_30_FRAME_PASS.

**Next**: construct typed transport of ordered chirality, OUTER C12 primitive trace and source/target signed BRC path words between atlas frames; prove local event availability covariant under moving α or give minimal failure witness and add necessary residual. The 15-state claim pertains to support-atlas queries only, not to complete original native dynamics; preexisting source four FCC STAR charts do not automatically imply full physical carrier realization for every transported α.

Author-side exact research / Driver unreviewed / no Result or Foundation promotion. Source artifacts in research_notes/r678_x6_star_atlas_transport_20261110_emr3/, alongside R677; no frozen scientific input mutation.
