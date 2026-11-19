# R762FX — The four frozen STAR carriers already generate all A6 axis permutations: exact five-step BRC cover

Date: 2026-11-19. Status: EXACT_FINITE_PROOF / INDEPENDENT_LOCAL_INTEGER_RECALCULATION_PASS / NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142.
Frozen base: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Task publication pin @857280d1012943290d141d1317179c40ec3cbdf8. Antecedent: R762FV uniform all-twenty-triads kernel, plus R762FW exact central spectrum.

## Motivation: use only the already realized STAR carrier selections

The frozen Cell-torsor definition distinguishes **20 valid coordinate triple observers** from the **four STAR triples with established complete FCC/K4 carrier-readout realization**; the other 16 are not admitted as equivalent realized carriers. Therefore choose a smaller, better-sourced eight-branch *candidate*: the two oriented three-cycles on each of the four STAR axis triples, with exact positive BRC weight 1/8 per source-named branch.

Label the six axes by the edges of a K4 on vertices 0,1,2,3, ordered as 01,02,03,12,13,23. The four STAR triples in zero-based edge indices are:

\[
 T_0=(0,1,2),\quad T_1=(0,3,4),\quad T_2=(1,3,5),\quad T_3=(2,4,5).
\]

Let C_STAR be the eight directed cycles supported on these four triples, and \(\nu=\frac18\sum_{g\in C_{\rm STAR}}\delta_g\) a positive-rational group convolution kernel on even permutations of the six axis labels. This is a candidate axis-observer kernel; the already established STAR *carrier readout* does not itself grant a signed, physically native Cell/Link/Port triadic update.

## Exact finite theorem

**Theorem.** The eight STAR three-cycles generate the full A6 of size 360. The minimal number of generators required for each element has this exact distribution:

| Minimal word length | Number of A6 elements |
|---:|---:|
| 0 | 1 |
| 1 | 8 |
| 2 | 48 |
| 3 | 182 |
| 4 | 112 |
| 5 | 9 |

Consequently the Cayley word diameter is exactly 5; the number of permutations reachable in exactly h branches is 8,57,239,351,360 for h=1,2,3,4,5 respectively. Every even permutation has at least one representation by **exactly five** branches, while nine require five.

At h=5, all \(8^5=32768\) ordered BRC source words are accounted for. The number \(N_5(g)\) of words ending at a given g satisfies

\[
 \boxed{\min_{g\in A_6}N_5(g)=44,\quad\max_{g\in A_6}N_5(g)=326.}
\]

The exact five-step total-variation distance from uniform U is

\[
 \boxed{\|\nu^{*5}-U\|_{\rm TV}=\frac{28619}{184320}.}
\]

The five-step kernel satisfies the positive minorization

\[
 \nu^{*5}(x^{-1}y)\ \ge\ \frac{44}{8^5}
  \ =\ \frac{495}{1024}\,U(y),\qquad x,y\in A_6,
\]

and hence for all integers k≥0,

\[
 \boxed{\|\delta_x \nu^{*5k}-U\|_{\rm TV}\le(529/1024)^k.}
\]

The group-subset, kernel and resulting class functions are equivariant under the frozen embedded S4 acting by relabeling K4 vertices; this S4 conjugacy action has **22 orbits** on A6.

## Proof by a complete six-axis integer certificate

The attached Python standard-library-only code independently enumerates the 720 permutations of six axis labels and selects the 360 even permutations by inversion parity. It creates the four vertex-incident triples directly from all six edges of K4; for each it forms the two explicit 3-cycles. Each generator is even, so every reachable permutation lies in A6.

Run breadth-first search from the identity under left multiplication by **every one** of the eight generators. Store the first distance for each newly seen tuple. The algorithm terminates because it explores a finite subset of the 720 explicitly enumerated tuples. Every discovered edge is verified by composition, and closure is verified by exhausting the BFS queue. The reached set equals the independently enumerated 360 even tuples, and the five frontier counts are precisely 1,8,48,182,112,9. Therefore the generated group is A6, and the word-length classification is exact. This is a finite exhaustive certificate for these six labels, not an extrapolation to arbitrary dimension.

For any nonempty word ending at depth \(\ell\), replace one three-cycle g with \(g^{-1}g^{-1}=g\); this raises the length by one without changing the endpoint. The identity has expressions of lengths two and three (inverse pair and g³) and hence all lengths h≥2. Thus the BFS length distribution implies the stated exact-depth support.

Independently propagate **integer** word counts by \(N_{h+1}(q)=\sum_{g\in C_{\rm STAR}}N_h(g^{-1}q)\), beginning with \(N_0(e)=1\); all 360 endpoint counts are included at every h. The attached checker calculates exact depths h=1,…,6, independently checks their support against BFS length sets, verifies \(\sum_q N_h(q)=8^h\), and calculates TV as a Fraction. At h=5, direct integer minima/maxima are 44/326 and the TV fraction is 28619/184320. There is no rounding or floating-point tolerance.

Finally every left translate of the kernel has the same minimum, U is stationary for a group convolution kernel, and the standard Doeblin decomposition of the fifth power has uniform mass 495/1024. Iterating its TV contraction proves the displayed all-k bound.

For the S4 claim, generate all 24 permutations of the four original K4 vertices; each induces a six-edge permutation. Exact conjugation of each of the eight generators stays within the generator set. The code enumerates the resulting 22 conjugacy orbits of A6 and checks that each depth-h endpoint count is constant on each orbit.

## Evidence and model boundary

Files: R762FX_VERIFY.py and R762FX_EVIDENCE.json. Exact depth support 8,57,239,351,360,360 for h=1..6; exact TV values at h=3,4,5 are 299/720, 717/2560, 28619/184320. Total domain: all 360 even permutations, 24 embedded S4 relabelings, 22 orbit classes, all eight generators at each BFS/DP step. The finite proof is valid for the declared six-axis candidate. Review remains NOT_REVIEWED.

The four STAR triples are already authorized *carrier-readout configurations*, not authorized primitive balancing rotations. All eight candidate branch identities and complete ordered BRC source paths are preserved beyond the product observer; no claim of physical closure, Source CLAIM/PROGRESS, lossless endpoint compression, or project mathematical review is made.

## Next decisive experiment

Retrieve the actual frozen Cell/Link/Port event-permission predicate (or identify precisely that a transition rule has not yet been defined), then for each STAR triad and orientation test signed incoming axes, port labels, source continuity, Block status and Cell updates. If the resulting legal support differs from the eight candidate cycles, replace the kernel with the actual typed partial transition system and recalculate future-observer/source-fiber separation. This links the reachable group algebra to the original triadic-closure objective instead of silently identifying a carrier realization with an operation permission.