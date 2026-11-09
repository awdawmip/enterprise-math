# BRC-X6: A 9-bit all-positive exact twelve-term native controller and a transport-tree lift obstruction

**2026-11-09 · author portable evidence · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

## Fixed scientific input and native observer

This work continues the frozen BRC-X6 four-source signed preserving-policy polytope, science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. It reuses the original 96-port/six-action transition operator; native source ports are `(6,7,28,29)` with signs `(+,-,-,+)`. All nine frozen roots are zero and ±e₁,…,±e₄; every labeled atom retains next port, six signed reward coordinates and gate K. The exact 38 legitimate preserving deterministic action quadruples are re-enumerated from the original frozen kernel, SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`. No scientific pin, observer, or physical interpretation is changed.

For any legitimate policy x, minSupport(x) is the least number of distinct legitimate deterministic policies with positive real convex coefficients reproducing all 24 original source/action coordinates. All original signed joint observer relations remain valid under mixture because every pure constituent preserves them.

## The new all-positive twelve-term witness

Let the four six-action marginals (source order 6,7,28,29) be `X=N/373` with

```text
N =
 (166, 37,  80, 56, 24, 10)
 (107, 67,  80, 56, 24, 39)
 (110, 11, 180, 37, 32,  3)
 (110, 40, 121, 67, 32,  3)
```

Every row sums to 373 and all 24 integers are positive. A twelve-vertex convex decomposition, using the frozen lexicographic ordering of the 38 legal deterministic policies, is:

```text
vertex index:   24  12   3  19  34  25  17  37   2   5   8   7
integer weight: 20  80  32  46   7   4  10   3  38  67  37  29
```

The weights total 373. The original four-source action quadruples are:

```text
(4,4,0,0) (2,2,0,0) (0,0,4,4) (3,3,2,2)
(5,5,1,1) (4,4,1,1) (3,3,0,0) (5,5,5,5)
(0,0,2,2) (0,1,2,3) (1,0,3,2) (0,5,2,1)
```

Exact checking against the original kernel enumerated all 1,296 possible pure action quadruples, found exactly 38 preserving strategies, verified the 12 selected policies at each of nine roots against the full signed joint observer, and recovered all 24 marginal numerators. Thus minSupport(X) ≤ 12.

## General transport-tree lifting theorem

**Lemma.** Fix two labeled marginal ports with r and s strictly positive action masses and equal total mass, and any finite permitted family of multi-source deterministic policies. Write c*(a,b) for the maximum number of disjoint, nonempty, mass-balanced block pairs of those two marginals. If c*(a,b)=1, an allowed mixture with at most r+s−1 atoms exists if and only if a positive weighted spanning tree on the bipartite action labels lifts edge by edge into the original permitted multi-source deterministic policies, reproducing all remaining source marginals. With integral marginal masses, every edge weight of the tree is integral.

**Proof.** Project a mixture of m≤r+s−1 atoms onto the two selected source labels. Its support graph has r+s nonisolated vertices because each action is positive. Each connected component supplies a nonempty balanced block pair, so c*=1 requires connectivity. A connected graph has at least r+s−1 distinct edges, and at most m distinct projected edges. Hence m=r+s−1, all projected pairs are distinct, and the graph is a spanning tree. Every edge lifts to exactly one original deterministic atom (there can be no positive duplicate of a projected pair). The weight of the unique incident edge at a leaf is forced to equal that leaf marginal. Remove this leaf and subtract its mass at the neighbor; by induction all edge weights are uniquely determined and integral if the marginals are integral. The converse follows by summing the positive lifted policy weights and checking all marginals. QED.

This statement is a general exact obstruction for any finite native multi-source action incidence relation; its following computation uses the original frozen 38-policy BRC-X6 family.

## Exact lower-bound certificate

Use source ports 6 and 29, hence rows 0 and 3 of N:

```text
a=(166,37,80,56,24,10)
b=(110,40,121,67,32,3)
```

Their proper nonempty subset-sum sets respectively contain 54 and 56 **distinct** masses, with empty intersection. If two or more balanced blocks existed, at least one common proper subset mass would exist. Therefore c*(a,b)=1. The established two-port transport theorem gives minSupport(X)≥6+6−1=11.

If an 11-atom mixture existed, the new lemma forces a single connected 11-edge bipartite tree with every edge lifted to exactly one of the 38 legitimate native action quadruples. Complete integer DFS recursively chooses any leaf, forces its incident edge weight to the current leaf action mass, removes the leaf, and subtracts its weight from the marginal arrays at **all four** source ports. Memoization is keyed on the complete four-port integer residual, and repeated leaf orders are deduplicated. Exact run:

```text
distinct recursive residual states: 121983
candidate leaf edges tested:       976415
native pure-lift choices:          1263705
admissible 11-atom completion:     0
```

A second independently coded author-side iterative BFS over exact integer residuals (with its own re-enumeration of legal pure policies) gives the number of unique states at leaf depths 0 through 11:

```text
1, 29, 360, 2459, 10031, 24981, 37327,
31519, 13184, 2049, 43, 0
```

The zero terminal level excludes the eleven-term tree-lift. Since c*=1 already excludes ten or fewer, and the explicit twelve-term mixture is exact, **minSupport(X)=12**. Every action probability is positive and the common denominator is only 373 (9 binary bits), improving on the earlier 155-bit author-side twelve-term construction.

## Verification, scope, preservation

The original reproducibility bundle carries the unchanged frozen Python kernel, `native_12_tree_certificate.py`, `native_12_bfs_crosscheck.py`, two exact JSON certificates and this theorem. Both validation runs execute using Python standard-library integer arithmetic, with no floating-point mathematical inference. A supplemental HiGHS MIP run reported eleven-term infeasibility; it is only exploratory and not part of this rigorous finite certificate. The two implementations share an author/control context and **are not independent Driver review**.

The current BRC proof is author-side portable mathematics; it is not a Source task checkpoint or accepted Result. The D25 native H0/B0 divided-power, Frobenius, kappa and CM experimental frontiers remain separate, uncompleted work. Historical D25 read request `h40-r11-d25-exact-continuation-20261109t0137-read-v1` has SUCCEEDED read receipt with execution_authorized=false. No own valid issued session/claim/open was established; no Source native write is asserted. The old UR V2 four-file original must still be recovered with byte length 94687 and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; no reconstruction is claimed.

**Next mathematical action:** handle a putative 12-atom decomposition when c*=1 and r=s=6: either the two-port support has exactly 11 tree edges with one doubled native lift, or it has 12 distinct edges forming a connected unicyclic graph. Construct and test an exact exhaustive two-case verifier against a known 13-support all-positive witness, aiming for a short exact 13-support certificate. Separately handle original UR V2 writer/provenance once true bytes and authorized native session/claim are available.

**Attribution:** Same author-side TASK_RESEARCH context as previous BRC-X6 portable reports; no new identity, independent credit or review has been inferred. Original D25 authors and preserved Source frontier remain intact.
