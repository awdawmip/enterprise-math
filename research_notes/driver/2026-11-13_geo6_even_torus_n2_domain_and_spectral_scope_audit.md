# GEO6 second-wave exact-set: even-torus domain and spectral-scope audit (2026-11-13)

**Scope:** Independent, source-bound mathematical correction to the stated *domain* of three torus atoms in frozen Result `RR-B5DB25EC13BF1C42DC9B` (`TP2-B531F3BB4A597B7D3EAF`). Original author, Result bytes, review disposition and historical branches are preserved. This document is an additional Driver audit, not a replacement Result or a new acceptance.

## Verified source comparison

1. The earlier accepted Gen2 Packing Return, `research_returns/GEO6_SPHERE_PACKING_DENSITY_BRIDGE_RESULT_REFREEZE_V2_RETURN_20260830.md` (Git blob `bbe30130dbb998f4af56ff4dad25a3bda7a8337a`), explicitly defines its 12-regular simple torus for **even integers `n >= 4`** (§5, lines 140–160). Its eigenvalue calculation also uses degree 12.
2. One historical prior-art matrix in PR #937 (`claim_source_matrix.json`, Git blob `80a1c75fb73639447b930ea9eced492cf8188fa6`) restates `PCK-05` and `PCK-06` using just “even n”, and `PCK-07` states the degree-12 / least-eigenvalue-minus-12 certificate without retaining the lower bound.
3. The parallel PR #950 matrix (`claim_matrix_v1.json`, Git blob `f056804430e7bed833294a439fa2be5baa2afd70`) explicitly restores `n >= 4` in `P02`.
4. The integrated frozen reconciliation matrix (`reconciliation_matrix_v3.json`, Git blob `c800d221a1f89c3cb1ad96080bf4582800141898`) has canonical atoms `U-P05`, `U-P06`, `U-P07` with the weaker wording “even n” or no `n >= 4` qualifier, and its Return groups the even torus, parity optimum and Hoffman bound together without an explicit lower bound. The frozen Result retains exact historical source provenance and the accepted four selectors.

The reconciled classical **12-regular simple-graph** theorem should therefore state `n >= 4` and `n` even. The omitted qualifier is a **hypothesis-transcription error**, not a counterexample to the correctly stated original Gen2 claim.

## Exact boundary witness at n = 2

Let `T_n` denote the simple undirected conflict graph on `(Z/nZ)^6` where two *distinct* cells are adjacent if they differ by `+e_i` or `-e_i` in one coordinate, for some `i`.

For `n=2`, `+e_i = -e_i` modulo 2. Thus the 12 directed generator expressions give only **six distinct neighbors** per vertex. The simple graph is the 6-dimensional hypercube `Q_6` with `|V|=64`, degree `d=6`, and least adjacency eigenvalue `tau=-6` (the eigenvalues are `6-2k` for `k=0,...,6`). Its parity classes each contain 32 vertices, and the `e_1` perfect matching shows `alpha(T_2)=32`. Hoffman's bound correctly gives `alpha/64 <= 6/(6+6)=1/2`.

Consequently, the unqualified statement “for even n the **simple** torus has `d=12`, `tau=-12`” is false at the valid even input `n=2`. This does **not** invalidate the occupancy equality `alpha(T_2)=2^6/2`: that equality extends to this special case by a different degree/eigenvalue calculation. A 12-regular **multigraph** interpretation counting duplicate `±e_i` edges could also be stated separately, but is not the same simple conflict graph defined above.

For every even `n>=4`, the `+e_i` and `-e_i` neighbors are distinct for each axis; the graph is the ordinary Cartesian product `C_n^{\square 6}`, 12-regular, bipartite, with adjacency eigenvalues `2\sum_{i=1}^6 \cos(2\pi k_i/n)`. The least eigenvalue is `-12` (all `k_i=n/2`), so the original Hoffman ratio `1/2` is valid. A parity class and perfect matching achieve equality.

## Consequence for review and continuation

- Restrict the **joint atom/claim about 12-regular simple torus and spectral certificate** to even `n>=4`, or split out `n=2` with `d=6`, `tau=-6`.
- Preserve the already established finite packing optimum and classical graph-prior-art classification in their respective justified domains. This amendment does not reopen the four surviving P000 semantic selectors or assert a new geometric bridge.
- Retain both original branch citations, original author/Result/Review and `substantive_conflicts=[]` for classification reconciliation. The specific *hypothesis-transcription* gap is distinct from an unresolved prior-art classification conflict.
- If a new controlled native review is ever needed, use the actual current Result bytes, full review set, own Driver authority and contribution disclosures. This note alone does not alter native review state or formal completion.

**Checks performed in this audit:** direct GitHub reads of the Gen2 Return and both origin matrices plus the integrated matrix/Return; exact enumeration of `(Z/2Z)^6` yields 64 vertices, 6 unique neighbors at the zero cell, and 32 even-parity vertices. No numerical approximation or inference from a finite test to a universal theorem was used; the `n=2` result follows from the explicit modular equality `+e_i=-e_i`.
