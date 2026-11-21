# R284DF — Two bits of nonlinear winning-arc provenance are necessary and sufficient

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scientific input: the original frozen R284CO 34-bit Port auxiliary observer; no altered model or native X6 transfer.

## Problem

For the frozen 65,536 distinct Port residues `X` and 64 labeled integer circular arcs `A_j`, let `D(x)=max_j dist_circle(x,A_j)` and let `L(x)` be the label of its unique maximizing arc. R284DD established that `L(x)` is defined at every frozen site; R284DE classified the collisions when only `D` is retained.

**How little information derived solely from the winner label L must accompany D to distinguish every frozen codeword?** A `q`-symbol label encoder is any map `c:{0,...,63}->{0,...,q-1}`, used through the observation `(D(x),c(L(x)))`. The encoder is fixed globally and does not inspect the source word or D.

## Sharp finite theorem

**Four symbols are necessary and sufficient.** Equivalently, **two bits of arbitrary (generally nonlinear) winner-label side information** make the observation injective on all frozen 65,536 sites; no one-bit label-only encoding can do so.

Furthermore:

1. The scalar `D` has exactly **65,139** distinct values and **420** unordered pairs of distinct sites with equal D.
2. All 420 colliding pairs have different winning labels. Thus the richer observation `(D,L)` is injective.
3. The graph `H` on 64 arc labels, with an edge `{u,v}` if some two distinct sites with the same D have winners u,v, has exactly **84 distinct edges**.
4. `H` contains the four-clique `{1,8,62,63}`, proving at least four colors are required. Its six edges have actual equal-D site witnesses and are recorded in the accompanying JSON certificate.
5. An explicit four-color assignment, indexed by arc label 0 to 63, is

```text
2,0,2,0,0,1,2,2,1,3,1,0,1,0,0,1,
0,0,0,1,1,0,0,0,0,0,2,0,0,1,1,0,
2,0,1,0,2,1,0,0,1,0,0,0,0,1,0,3,
3,1,0,0,0,1,1,2,0,0,1,0,2,0,2,3
```

Directly checking all 84 edges shows every edge has differently colored endpoints. Hence the 4-color code `c` is sufficient, and the lower bound is sharp.

**Nonlinear refinement:** No affine two-output-bit code on the *six binary digits of L* achieves this. Exhaustively testing all `63 choose 2 = 1,953` unordered pairs of distinct nonzero parity masks yields zero valid label codes. Such mask pairs exhaust rank-two linear maps `F_2^6 -> F_2^2` up to row permutation, and adding a fixed affine offset does not change which labels collide. Lower-rank maps have fewer than four values and fail the clique bound. Thus a shortest encoder must be nonlinear as a function of the six label bits.

## Proof and exact evidence

For a proposed code c, a collision of `(D,c(L))` between two *different* frozen sites occurs exactly when their D values agree and their label colors agree. The checker enumerates all 65,536 frozen sites, regenerates the 64 arcs and evaluates the fully attributed farthest envelope. For independent validation it also calculates all **4,194,304** integer distances and confirms the entire distance/argmax-label pair for every site.

Grouping by D yields exactly 65,139 fibers, with 420 unordered intra-fiber pairs. The checker confirms different winner labels for every pair and records 84 distinct unordered winning-label conflicts. A q-symbol label encoder makes the observation injective **if and only if** c is a proper coloring of this finite conflict graph H. The six observed conflicts among labels `1,8,62,63` give a `K_4` and force `q>=4`. The explicit 64-entry color table is then checked against every conflict edge and all 65,536 reconstructed `(D,color)` pairs, giving `q<=4`.

Finally, every binary linear two-bit label encoder has outputs `(parity(a & L),parity(b & L))` for two nonzero distinct six-bit masks a,b, up to swapping rows. There are 1,953 such unordered pairs; all are checked against the 84 distinct conflict edges. None is valid, proving the stated linear/affine obstruction.

The K4 witnesses in the certificate permit independent spot-checking of the lower bound without trusting graph-coloring software. The upper bound is a complete explicit finite check, not a heuristic chromatic estimate. The theorem concerns the **additional symbol carried with D** and does not assert that the whole original 34-bit state has been compressed into two bits, nor that arbitrary future native operations preserve this quotient.

## Source pins and continuation

Original frozen checker: `enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`, ordered word SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The R284DD attributed-envelope source and R284DE graph census are reused with original evidence strength.

Next research question: is there a low-degree nonlinear algebraic description of the two-bit label encoder, avoiding a 64-row lookup, and how does the minimum color count change under frozen-admissible source mutations, input subsets, or alternative observer families? Distinguish snapshot injectivity from operational residual fidelity under subsequent transformations.

Historical researcher/Activity references remain provenance only; this artifact does not create a formal task CLAIM, Activity event, accepted Result or independent review.
