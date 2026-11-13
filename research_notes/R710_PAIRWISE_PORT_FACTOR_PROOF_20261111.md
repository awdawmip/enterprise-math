# R710 — Pairwise-factorized port eligibility forces a full triadic cover

Date: 2026-11-11 Asia/Shanghai. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389. Continuation of R709 in Draft PR #2047.

## Model and theorem

At one X6 Cell, take one individually labeled equal-positive-q signed primitive token from each of six native axes. Preserve sign and source identity. Define a hypothetical **pairwise-factorized** triad eligibility model by a simple graph G on axis labels V={0,1,2,3,4,5}: an axis triple T is allowed precisely when all three two-axis pairs are edges of G. Write H(G)={T in C(V,3): C(T,2) subset G}. This is a candidate independent pairwise permission model, **not** an identification with actual native X6 Link/Port occupancy or V29/V39 dynamics.

Fix R709's Pasch family P={012,034,135,245}; each is an unordered triple. For every simple graph G satisfying P subset H(G), the four complementary triples {345,125,024,013} also belong to H(G). Consequently H(G) contains four exact disjoint complementary pairs and the labeled-triad cover count for n=(1,1,1,1,1,1) satisfies

    D_H(G)(1,1,1,1,1,1) >= 4.

Hence the R709 four-triple fractional-cover/no-integral-cover state H=P cannot arise within this pairwise-factorized candidate class.

## Proof

The union of the pair edges in P is exactly the twelve-edge set

    R=C(V,2) minus {05,14,23}.

The three omitted pairs form a perfect matching. If G contains P as triangles, it must contain all twelve edges R. The triangles of the minimal graph R are exactly the sets containing one endpoint from each of the three omitted pairs. There are 2^3=8 such triangles. They are the four triples P plus their four distinct complements, arranged into four complementary pairs. As H(R) subset H(G), each complementary pair gives an exact partition of all six individually labeled tokens into two 3-axis triads, proving at least four distinct sources. QED.

## Classification and unary comparison

All graphs G containing P as triangles equal R union X for a subset X of {05,14,23}. Hence there are exactly eight such graphs. Full enumeration gives their integral cover-count distribution: four graphs with 4 covers, three graphs with 6 covers, and one graph with 10 covers. Every one of the 2^15=32768 simple graphs on six labeled axes was checked independently.

If eligibility is instead based on unary axis gates (a triad is permitted iff its three axes are each individually enabled), P forces all six axes open; all 20 triples are then eligible and yield 10 unordered complementary-pair covers.

## Interpretation and native bridge

R709 gives a minimum obstruction for genuinely ternary eligibility H. R710 proves that factorization into pairwise graph-clique eligibility automatically supplies four integral repairs. Thus realizing exactly P requires a contextual three-way gate, port/address ordering, or further state/source dependence. Whether the *actual* X6 native admissibility relation belongs to either class remains to be determined by frozen Cell/Link/Port, V29 PASS/TRANSFER, V39 loop-flow j and the real triadic rotation generators. No classical vector-sum force cancellation, trigonometric operator or non-BRC physical propagator is used.

## Exact executed verification

The independently run Python standard-library checker experiments/R710_PAIRWISE_PORT_FACTOR_VERIFY_20261111.py enumerates all 32768 six-vertex graphs, tests the forced twelve edges, the eight minimal triangles, four complementary pairs, and the 4/6/10 cover histogram. Its executed stdout was:

    R710_PAIRWISE_PORT_FACTOR_EXACT_PASS 15 8 12 8 4 {4: 4, 6: 3, 10: 1}

General conclusion follows from the proof; enumeration supplies finite exact corroboration and JSON evidence.

Next smallest unfinished research unit: derive actual native typed H(Cell,state,time,source) and determine its factorization; construct a reachable event and verify TRIADIC_CLOSURE_E, conservation, BRC provenance and rotation covariance.