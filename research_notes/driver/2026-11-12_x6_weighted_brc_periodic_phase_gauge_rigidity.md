# X6 / Weighted-BRC: periodic phase gauges, monodromy completeness, and cone-rigid recovery

Status: DRIVER_MATHEMATICAL_AUDIT / EXACT_SCOPED_THEOREM / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Parent: RS-X6-NATIVE-ROTATION-DYNAMICS / PO-X6-UPPER-STRUCTURE-20260906
Provenance: new Driver derivation in a shared, nonblind X6 context, extending the exact four-origin transfer tomography and full-period collisions already published by this lane. Earlier signed Cell, C6/C12 and Weighted-BRC authorship remains unchanged.

## 1. Exact finite-phase mathematical model

Fix an integer n >= 1 and positive rational numbers t_1,...,t_n, indexed cyclically. At phase j let

    T(t_j) = [[1,t_j],[1,0]] in GL_2(Q).

The entries model the pre-existing two-state, non-immediately-backtracking candidate weighted branch transfer. Their orientation uses the already declared O/I boundary-state convention. The ordered one-period monodromy is

    M(t) = T(t_1) ... T(t_n).

For each registered starting phase j let B_j(t)=T(t_1)...T(t_{j-1}), with B_1=I, and P_j(t)=B_j(t)^(-1) M(t) B_j(t). Thus P_j is the period transfer in the registered phase-j state frame.

A *periodic phase gauge* is a family of invertible rational matrices G_1,...,G_{n+1}, with G_{n+1}=G_1, relating two transfer laws u,v by

    T(v_j) = G_j^(-1) T(u_j) G_{j+1}.

This is a conditional state-frame equivalence of the two-state transfer model; it does not assert that arbitrary GL_2(Q) frame changes are physically allowed for native X6 Cells.

## 2. Exact classification under arbitrary rational phase gauges

**Theorem A (monodromy classification).** For any two positive rational laws u,v of the same period n, a periodic rational gauge exists if and only if M(u) and M(v) are conjugate in GL_2(Q). Equivalently, because these monodromies are nonscalar 2-by-2 rational matrices, a gauge exists exactly when

    tr M(u) = tr M(v)  and  det M(u) = det M(v).

*Proof.* Multiplication of the n phase equations telescopes to M(v)=G_1^(-1) M(u) G_1, proving necessity. Conversely, choose G_1 with that conjugacy and define

    G_j = B_j(u)^(-1) G_1 B_j(v),       1 <= j <= n+1.

Then G_j^(-1)T(u_j)G_{j+1}=T(v_j) by cancellation of adjacent prefixes; the conjugacy equation gives G_{n+1}=G_1. Every T(t) is invertible (det=-t). For n=1, T(t) is nonscalar, while for n>=2 each entry of M is strictly positive, hence M is nonscalar. A nonscalar 2-by-2 rational matrix has minimal polynomial equal to its characteristic polynomial and admits a rational cyclic basis; two such matrices with the same characteristic polynomial are rationally similar. This proves the trace/determinant equivalence. QED.

**Corollary (unregistered phase observations).** If an observer retains each P_j only up to a separately unknown invertible rational phase-frame change, then even the complete family of all n phase origins cannot recover the phase weights in general. The full gauge-invariant content of these phase-period matrices is the conjugacy class of M, represented here by its trace and determinant. By contrast, the preceding four-origin theorem assumes each complete P_j is available in a shared registered O/I convention, and that assumption is essential.

## 3. Exact collision and explicit periodic gauge

The previously verified distinct positive six-phase laws are

    u=(1/2,1/2,1/2,1/2,2,2)
    v=(1/2,1/2,1,2,1/2,1).

Their exactly equal monodromy is

    M(u)=M(v)=[[37/4,15/2],[27/4,11/2]].

Taking G_1=I gives the following full periodic gauge, obtained from the prefix formula:

    G_1 = I
    G_2 = I
    G_3 = I
    G_4 = [[1,0],[0,2]]
    G_5 = [[2,0],[-2,4]]
    G_6 = [[2,-1],[0,1]]
    G_7 = I.

Direct exact rational multiplication verifies all six identities
T(v_j)=G_j^(-1)T(u_j)G_{j+1}. Therefore the collision persists through every observation invariant under these independent periodic GL_2(Q) phase changes, including phasewise conjugacy classes, repeated-period traces, and determinants. Several displayed G_j have negative entries, which matters for the next theorem.

## 4. The positive-state-cone boundary restores weight rigidity

An invertible real matrix G is an automorphism of the standard nonnegative two-state cone if both G and G^(-1) have nonnegative entries. In two dimensions such a G is a positive monomial matrix (a positive diagonal matrix possibly followed by a coordinate swap).

**Theorem B (cone-rigid canonical transfers).** Suppose u_j,v_j>0 are real, all transfers have the canonical normalized form T(t)=[[1,t],[1,0]], and a periodic family G_j satisfies

    T(v_j)=G_j^(-1)T(u_j)G_{j+1}

with G_j and G_j^(-1) entrywise nonnegative. Then u=v and every G_j is the same positive scalar multiple of the identity.

*Proof.* Canonical T(t) has precisely one zero entry, at (2,2), and its other three entries are strictly positive. Under left and right multiplication by positive monomial matrices, the zero position changes exactly by the respective row and column permutations. To remain at (2,2), neither permutation can swap either axis. Thus every G_j is diagonal, say diag(a_j,b_j) with positive entries. Comparing the (1,1) and (2,1) entries in the displayed identity yields a_{j+1}/a_j=1 and a_{j+1}/b_j=1. Cyclically, a_j=b_j=a for one positive constant a. Comparing the (1,2) entries then gives v_j=u_j for every j. QED.

This yields a precise type choice for any future physical or computational lift: allowing arbitrary two-state linear re-registration gives monodromy-only reconstruction, while preserving the labelled nonnegative O/I state cone and its canonical transition normalization rules out those nontrivial gauges. A native-X6 claim must first specify which boundary-state transformations are admissible; no physics or new spatial axis follows automatically.

## 5. Reproducible exact check and relation to prior source

The six-phase matrices and G_1,...,G_7 above were independently evaluated with Python fractions.Fraction, using exact 2-by-2 multiplication and determinant-based inversion. Results:

    M(u)==M(v): True
    G_7==G_1==I: True
    for each j=1,...,6, inv(G_j)*T(u_j)*G_(j+1)==T(v_j): True

These finite checks corroborate the written algebraic proof and are not the source of its universal quantifiers.

Existing exact source links:
- research_notes/driver/2026-11-12_x6_cyclic_phase_transfer_sharp_four_start_tomography.md, commit 30afe94772306113ea7a03cd455e6fc1663d890c, blob 69a2ebeb54f4ee352644e1b4416a3aaba6648cfa.
- research_notes/driver/2026-11-12_x6_weighted_brc_full_period_transfer_matrix_nonidentifiability.md, commit 0d5e4cacb6b9d79f1977b83f88f23b192ae58a2f.
- Frozen native spatial definition at a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md (the signed spatial torsor, primitive steps and typed Path-formal/Weighted-BRC hierarchy).
- Current Heartbeat World typed constraints at definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json.

Review status and next unit: Scoped exact rational/positive-real algebra, hand proof plus exact checked collision, shared-context Driver contribution; not independently reviewed/accepted as a native Result. For native rotation dynamics, test whether the O/I branch-state cone, phase registration, and temporal update are preserved by the proposed Cell/path composition. Only then apply the sharp four-origin theorem or the arbitrary-gauge quotient in the relevant observer type. Existing researcher owner/CLAIM and Foundation authority remain separate.
