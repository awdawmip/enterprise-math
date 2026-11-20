# R284BN — Connectedness is necessary and sufficient for three-vertex editable-Port determinant identification

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Independent portable research; no native CLAIM or review asserted.

## Exact predecessor and problem

This is an algebraic continuation of R284BM at `a2537fde3598cef07a8a31eca0b0a676d143f29e:research_notes/portable_direct/R284BM_CONNECTED_EDITABLE_PORT_GRAPH_MINIMUM_20261120.md`, with its frozen R284BJ/R284BL-FX1 observer scope. R284BM proves that disconnected editable-Port support graphs have exact binary gauge collisions, and that a full outgoing star is sufficient. The remaining small-dimensional question was whether other orientations of a spanning tree are also sufficient.

For a directed edge set E on V={0,1,2}, let

```text
F_C^E(d,z) = det(diag(d)-C-sum_{(i,j) in E} z_ij E_ij).
```

Here C has strictly positive rational entries and all controls are independent formal variables. Let U(E) be the underlying undirected graph.

## Theorem BN1 (complete three-vertex graph criterion)

For n=3, the map C↦F_C^E is injective on strictly positive rational 3×3 matrices **if and only if** U(E) is connected. The same criterion holds for the full bounded positive integer population {1,…,H}^{3×3}, H≥2.

**Necessity.** If U(E) is disconnected, the exact {1,2}-matrix pair constructed in R284BM has identical formal determinant responses. This refutes injectivity for every H≥2.

**Sufficiency.** Every connected U(E) contains two distinct undirected edges spanning all three vertices. Retain one editable orientation per chosen edge, set all other editable variables to zero, and write the resulting directed two-edge tree as T. It suffices to reconstruct C from F_C^T. Up to vertex relabeling, there are three orientation patterns:

1. **Two edges directed outward from the middle vertex.** This is precisely the full outgoing star of R284BM, which has explicit injective coefficient reconstruction.
2. **Two edges directed inward to the middle vertex.** Transposition gives `F_C^T(d,z)=F_(C^transpose)^(T^transpose)(d,z)`; the transposed graph is an outgoing star, so the same reconstruction applies.
3. **One directed path u→v→w.** The coefficients `[prod_{k!=i} d_k]F=-C_ii` determine all diagonal entries, while `[d_k]F=C_ii C_jj-C_ij C_ji` (where {i,j,k}={u,v,w}) determines all three reciprocal off-diagonal products `P_ij=C_ij C_ji`. Each editable arrow i→j gives `[z_ij d_k]F=-C_ji`, hence the two arrows determine C_vu and C_wv; dividing P_uv and P_vw determines C_uv and C_vw. Finally, the single coefficient `[z_uv z_vw]F=-C_wu`: the only determinant term using both arrows is the directed three-cycle u→v→w→u, with permutation sign + and three negative factors. Thus C_wu is known, and `C_uw=P_uw/C_wu`. All divisions are valid by strict positivity.

All matrix entries are therefore recoverable. Retaining any additional editable variables cannot remove this injectivity, since setting them to zero recovers the tree observer. QED.

The n=2 analogue is also exact: one directed edge makes U(E) connected and the two-vertex outgoing-star proof of R284BM applies after relabeling. For n≥4, connectedness remains a proved necessary condition; its sufficiency for every graph/orientation is an open question under these sources.

## Finite exact check

The companion standard-library checker imports R284BM's integer-polynomial Leibniz determinant routine. For all 12 oriented spanning trees on three labeled vertices, it computes the complete coefficient dictionary of F_C^T and verifies that no two C have the same signature:

- H=2: 12×512 = 6,144 exact signatures; no collision.
- H=3: 12×19,683 = 236,196 exact signatures; no collision.

These exhaustive finite tests independently exercise the orientation classification in small integer populations. The algebraic proof above covers every strictly positive rational C at n=3.

## Information and native interpretation

The formal polynomial retains named directed Port identities. The obstruction arises from an exact diagonal-similarity fiber, while the connected three-vertex construction has a separating observer. This is a typed auxiliary determinant experiment; no conversion of a two-coordinate representation into a native X6 three-dimensional slice, no BRC amplitude cancellation, and no physical sensor feasibility are inferred. No change to P000, frozen science, or existing review state occurs.

## Next unit

Test the connectedness conjecture in n=4 (first for mixed-orientation spanning trees with positive integer populations), then seek a general constructive coefficient-recovery theorem or an exact positive-matrix counterexample. For a single finite-field scalar, combine the graph criterion with the Schwartz–Zippel existence argument from R284BM, keeping instrument cost and noise threshold separate.
