# X6 candidate signed-rotation: 32-chart moving diagonal quotient

Date: 2026-11-17. Task: RS-X6-NATIVE-ROTATION-DYNAMICS, publication TP2-6A1F9D8C2047E3B51C01. This is a self-contained **algebraic** construction in the signed native-axis lattice; native Cell/Port/three-force event and time-law admissibility remain to be established. It preserves and cites earlier 23040-element group and fixed-quotient memory results, rather than repeating them.

## Statement

Let L=Z^6, D=(1,1,1,1,1,1), m a positive integer, and H=(C2)^6 ⋊ A6, the previously derived group of signed monomial maps with even unsigned permutation, |H|=23040. Let V={v in {±1}^6}/(v~-v). This set has 32 unoriented sign-line classes. Define K_[v]=m Z v, Q_[v]=L/K_[v], and the disjoint union E_m = ⨆_[v] Q_[v].

For every g in H define G_g([v],[z]_{K_v})=([gv],[gz]_{K_gv}). For every signed primitive letter s=±e_i define translation T_s([v],[z]_{K_v})=([v],[z+s]_{K_v}).

**Theorem 1 (equivariant bundle).** These formulas give genuine invertible H actions and well-defined signed-letter translations on E_m for arbitrary m≥1, with G_g G_h=G_gh and G_g T_s=T_(gs) G_g. Hence every finite alternating word of candidate frame transformations and signed elementary path steps acts consistently on the moving-chart bundle, without lifting the discarded common-depth integer. The *operation word itself* remains retained for source/branch provenance.

Proof: if z and z+mk v represent the same point in Q_[v], their images under g differ by mk gv, which lies in K_[gv]. Thus G_g is well-defined with inverse G_(g^-1). For two transformations, gh K_[v]=K_[ghv], so composition follows; translation preserves each quotient kernel and conjugacy follows from g(z+s)=gz+gs. Induct on word length.

**Theorem 2 (sharp minimum number of chart types).** H acts transitively on V. The stabilizer of [D] consists of the 360 even unsigned permutations with a uniform sign ±, so its cardinality is 720. Therefore the orbit of K_[D]=mZD has 23040/720=32 distinct kernels. Every H-closed family of distinct rank-one quotient kernels containing mZD must contain that entire orbit; hence 32 is minimal *in this kernel-family category*. This says nothing about minimum total memory in bits.

**Explicit exact chart codec.** Normalize v to v6=+1. Record five integers r_i=z_i-v_i z6 (i=1,...,5) and one residue t=z6 mod m. This gives Q_[v] ≅ Z^5×(Z/mZ), with canonical representative z_i=r_i+v_i t (i≤5), z6=t, 0≤t<m. To apply g or a signed step, map this representative and re-encode under the transformed normalized chart; the outcome is independent of representative lift. Five chart bits encode the 32 possible sign lines. The integer common depth remains discarded.

**Why this differs from the fixed-observer obstruction.** On a single fixed quotient L/(mZD), a mixed-sign g fails to descend since gD≠±D; the older theorem also gives the sharp finite-horizon extra depth-bit requirement and an infinite-input no-finite-tag obstruction. Here the quotient kernel is transported from mZD to mZgD, so the output is in a *different* observer chart. No recovery of the original fixed-chart reading is asserted. Prior signed-path lift and finite-depth results remain unchanged.

## Exact reproducibility

The companion Python checker enumerates 32 chart types and runs 1,920 deterministic integer sample cases across m=1,2,3,5,7. It checks alternate full lifts, two generator compositions, covariance with signed elementary translations, and |V|=32, |H|/|V|=720. On Python standard library the reported outcome is PASS for all 1,920 cases. The proof above supplies the all-m, all-group statement; tests check the implementation.

## Required next native test

Construct an actually licensed native Cell/Port/TRIADIC_CLOSURE_E event square and determine whether transporting the observer kernel is an admitted update, retaining signed source, branch, phase and native time observables. If the target's interface requires one fixed observer chart at both ends, retain the earlier infinite-depth obstruction. This proof does not equate signed-frame algebra with physical native rotation.

## Reused fixed sources

- cc0d2f61bbf5516bd06f32c2714d2b2a7e0cc986:research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-c618a61189764f23846a391a08518a1a/c1c9e1128e090ca4c3a7/X6_ORIENTED_TRIAD_SIGNED_C6_GROUP_AND_PATH_ACTION.md
- 704829bb9c00998b4d0a19bd1a1341babde48bab:research_notes/driver/2026-11-12_x6_finite_depth_signed_brc_cover_rotation_descent_and_minimum_memory.md
- TP2-6A1F9D8C2047E3B51C01 immutable task publication; prior 2026-11-16 Burnside/Stirling signed-word orbit checkpoint retained independently.
