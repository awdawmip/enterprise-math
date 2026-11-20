# R762HH — Five-axis dual-Euler parity saturation and the exact four-event six-axis obstruction

**Status:** AUTHOR-PROVED (HH1–HH3); EXACT FINITE CHECK (m <= 12 on five axes; m <= 4 on six axes); NOT_REVIEWED.  
**Scope:** signed three-support composite Port candidate language, not an admitted primitive TRIADIC_CLOSURE_E.  
**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / publication TP2-8B7E13C5904A2D6F1142. Original research line EM-X6-3050F6; no new research identity or Result is asserted by this GitHub-only note.  
**Frozen source:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.  
**Direct predecessor:** R762HG, awdawmip/enterprise-math@f19346110bdca4c9aa237ed766fedc612210293c:research_notes/portable_direct/R762HG_HALF_PATH_GRAM_AND_PARITY_SATURATION.md.  
**Original signed model:** six chart-relative X6 coordinate components; unsigned Port transition P -> Q between 2-subsets of {0,...,5} with |P cap Q| = 1; support S = P union Q (three axes); independent signed choice epsilon in {+1,-1} adds epsilon h_S to the chart-relative composite Cell displacement. Each ordered choice remains a named BRC source, including repeated supports. Time/order and Port are retained.

## HH1. All-length saturation for supports avoiding one native axis

Let X={0,1,2,3,4,5}. Fix an axis c, and let S_1,...,S_m be an **arbitrary ordered word** of three-element subsets of X\{c}. The following statements are equivalent:

1. For every axis i in X, its incidence count d_i = #{t : i in S_t} is even.
2. There exist signs epsilon_t in {+1,-1} such that sum_t epsilon_t h_{S_t}=0 in Z^6.

The implication (2)->(1) follows modulo two. For (1)->(2), put Y=X\{c}, so |Y|=5. Each S_t is the complement within Y of a two-element subset E_t=Y\S_t. Regard each occurrence E_t, including repeats, as an individual edge of a loopless multigraph G on five labeled vertices. Because sum_i d_i=3m is even, m is even. For v in Y, the multigraph degree is deg_G(v)=m-d_v, hence even. Thus every nonempty connected component is Eulerian.

Every connected loopless Eulerian multigraph component having an odd number of edges uses at least three vertices: a one-vertex component cannot have an edge, and a two-vertex component consists of an even number of parallel edges. Since G has only five vertices, there cannot be two distinct odd-edge components. Since the total number m of edges is even, there are zero odd-edge components. Every nonempty component therefore has an **even** number of edges.

For each component choose any Euler circuit and alternately color its edge occurrences +,-,+,-,... . In an even-edge Euler circuit, at each vertex every arriving/departing pair of successive edges has opposite colors, including the pair at the basepoint. Hence the signed edge incidence at every v in Y is zero. Each component also has equally many + and - edges, so the total signed edge count is zero. Give S_t the sign of its complementary edge E_t. Then, for every v in Y,

sum_t epsilon_t 1_{v in S_t} = sum_t epsilon_t - sum_{t: v in E_t} epsilon_t = 0-0=0.

The excluded coordinate c is zero automatically. This constructs the required exact sign completion, for **all m**, including the empty word. QED.

Consequently, every parity-zero closed Port history confined to five native axis labels admits a six-axis zero-Cell completion for every even event length. HH1 applies to ordered support words beyond the Port language; it does not collapse BRC provenance, count distinct sign completions, or establish native primitive event admission. It is a new dual to the predecessor HG4 theorem, which instead assumes that all triples **contain** a common axis.

## HH2. Exact shortest obstruction without a five-axis restriction

For unrestricted unordered multisets of three-subsets of the six-axis set, the shortest incidence-even word having no zero-displacement signing has length four. Such a four-occurrence word is unbalanceable **if and only if** its four supports are distinct and any two intersect in exactly one axis: a Pasch configuration. Ignoring order, there are exactly **30** such multisets on six labeled axes.

Proof: An incidence-even word has even length, because the sum of its axis-incidence degrees is 3m; m=2 forces both supports to be identical, which can be signed oppositely. Now take m=4. If an axis appears in all four supports, HG4's common-axis theorem gives balance. Otherwise, each used axis appears exactly twice, and the 12 total incidences force all six axes to appear exactly twice. Make a multigraph on four vertices (one per support occurrence), with each of the six axes represented by an edge joining its two containing occurrences. The graph is loopless and cubic (each support has three axes). Signed zero incidence exactly asks for a proper 2-coloring of its four occurrence vertices, i.e. bipartiteness of this graph.

A nonbipartite loopless cubic multigraph on four vertices must have a triangle. If the triangle edge multiplicities are x,y,z>=1 and the fourth vertex has three incident edges, summing the degree equations gives x+y+z=3; thus x=y=z=1 and every triangle vertex joins the fourth vertex once. The graph is K4. Conversely K4 is nonbipartite. Its six edges are the six distinct axis labels; every pair of support occurrences shares exactly one axis. The distinct unlabeled-occurrence support configurations correspond to bijections from six labeled axes to K4's six edges, modulo relabeling the four support occurrences: 6!/4! = **30**. QED.

One explicit incidence-even but unbalanceable ordered hyperword is the six-bit support masks **[22,25,37,42]**, namely {1,2,4}, {0,3,4}, {0,2,5}, {1,3,5}. Each axis occurs twice and the occurrence-intersection graph is K4; no opposite-sign assignment is possible. **This word is not a Port-admissible history:** consecutive supports of a Port path share at least the two axes of the intermediate Port, whereas every pair in a Pasch configuration shares only one axis. HH2 therefore gives a sharp generic six-axis contrast, not a counterexample to the open all-length Port conjecture.

## HH3. A genuinely five-axis, non-common-axis Port example

Starting with Port {0,1}, the closed Port sequence is

{0,1} -> {0,2} -> {0,3} -> {2,3} -> {1,3} -> {1,4} -> {0,1}.

Its ordered three-axis supports, as six-bit masks, are **[7,13,13,14,26,19]**. Their union is exactly the five axes {0,1,2,3,4}; their common intersection is empty; every axis-incidence count is even. A valid signing is **[-1,-1,+1,+1,-1,+1]**, whose exact six-component sum is zero. This demonstrates that the new avoiding-axis family is not subsumed by the predecessor's common-axis hypothesis.

## Exact checker and recorded results

Source file R762HH_CHECK.cpp is C++17, integer-only, with no floating-point approximation. It enumerates every unordered multiset of length m built from the C(5,3)=10 named five-axis triple types for even m=2,4,...,12, and every multiset of length m=2,4 built from all C(6,3)=20 six-axis triple types. Each incidence-even multiset is checked for sign existence by an exhaustive meet-in-the-middle exact six-coordinate degree split. Six-bit disjoint integer lanes are safe for the tested lengths. Repeated support occurrences remain distinct binary signing choices.

Five-axis m=2,4,6,8,10,12: parity-good multiset counts 10,70,385,1690,6128,19040 respectively, with **zero** unbalanceable. Six-axis m=2: 20 parity-good, zero unbalanceable. Six-axis m=4: C(23,4)=8855 total multisets, 375 incidence-even, exactly 30 unbalanceable; the checker individually checks that each such exception has all six pairwise support intersections of size one. It also checks the HH3 closed Port witness and the HH2 Pasch witness. Observed execution: PASS, author-side. See R762HH_EVIDENCE.json for the full integer table.

This exhaustively checks the stated finite multiset domains; the infinite-length claims HH1–HH2 rest on the proofs above. No independent mathematical review or CI outcome is claimed.

## Open continuation and boundary

The exact unrestricted closed-Port question remains: for any even length, does the six-bit parity criterion suffice for a sign-completable closed walk when all six axes can appear? Previous HG3 proves the result through 12 events; HH1 now proves an unbounded five-axis subfamily. The length-four Pasch hyperword cannot directly occur along a Port walk. A useful next route is to classify how a Port walk might realize a larger connected even-incidence hypergraph with an unavoidable nonbipartite signing obstruction, while respecting the two-axis overlap condition. Keep full Port order, signed multiplicity, Cell displacement, Link and time residuals.

The task's primitive TRIADIC_CLOSURE_E force/Cell/Link/Port/time permission remains open. No physical calibration, formal Result, Review, Foundation promotion, or change to P000 is made.
