# R728 supplementary theorem — exact BRC port-edge update and factorial-squared source amplification

Date: 2026-11-12. Companion to R728 port-block proof. Scientific scope: candidate X6 triple-incidence hypergraph, distinct source IDs, finite nonnegative integer BRC counts. Frozen input: a72226e2430ffa4786321ac86e7f0c599d5f0389. This is a proof about typed source branches, not an assertion that a particular port update is a native V29/V39 physical event.

## General exact edge-admission transfer law

Fix a finite set E of allowed three-distinct-axis triples, and one triple T={i,j,k} not in E. Let a=(a_0,...,a_5) be source-family populations with sum a_i=3m, and let L_E(a) count partitions of all individually labeled source IDs into unordered E-admissible triples. Define L_E(0)=1 and L_E(a)=0 whenever no complete partition exists. Denote falling factorial (q)_s=q(q-1)...(q-s+1), with (q)_0=1.

**Theorem.** The exact count after admitting T is

L_(E union {T})(a)
 = sum_(s=0)^K [ (a_i)_s (a_j)_s (a_k)_s / s! ] L_E(a-s*1_T),

where K=min(m,a_i,a_j,a_k), and 1_T has entries one on the three axes of T and zero elsewhere. The term s=0 equals L_E(a); the increase is the sum over s>=1. This update is exact for all nonnegative axis populations and any finite E.

**Proof.** Classify each newly allowed partition by the number s of its triads whose axis-family set is exactly T. Choose s distinguishable source IDs from each of the three families in T. There are binom(a_i,s)binom(a_j,s)binom(a_k,s) such choices. To match the selected IDs into s unlabeled T-triples, fix an arbitrary order of the selected source IDs on axis i; the axis j and k IDs may independently be bijected to that ordered list in (s!)^2 ways. Therefore there are

binom(a_i,s)binom(a_j,s)binom(a_k,s)(s!)^2
 = (a_i)_s(a_j)_s(a_k)_s/s!

ways to make these s source-ID triple branches. The remaining sources must be partitioned using only E, in L_E(a-s*1_T) ways. The decomposition by s is disjoint and exhaustive. Summing proves the formula. QED.

The factor in brackets is an **integer** by the combinatorial count above. This is a provenance-preserving BRC update: the s-th contribution records the exact number of source-ID choices with precisely s uses of the newly admitted port-triple class. For removal of T, read the identity in reverse with E equal to the *remaining* permitted triples; no linear-response approximation is needed.

Equivalently, with P_E(x)=sum_(U in E)prod_(q in U)x_q, adding T replaces P_E by P_E+x_i*x_j*x_k. The binomial expansion of (P_E+x_i*x_j*x_k)^m gives the same identity after multiplying by prod a_l! /m!, in agreement with R728's labeled-branch coefficient formula.

## Unbounded factorial-squared amplification family

Use the R728 six-axis candidate port conflict H excluding all triples that contain both axes 0 and 1. Let T=012, one of the four excluded triples. For any integer m>=1, take the occupation vector

a(m)=(m,m,m,0,0,0).

Before admission, all occupied source axes are {0,1,2}, but H forbids their only possible three-distinct-axis triple. Hence L_H(a(m))=0.

Admitting the **single** candidate port-triple type 012 gives

L_(H union {012})(a(m)) = (m!)^2.

Indeed every labeled partition must match the m distinct axis-1 source IDs and the m distinct axis-2 IDs independently to the m axis-0 IDs, in exactly (m!)^2 matchings. In the transfer formula every term with s<m vanishes because the remaining sources cannot form an H-admissible triple. The only surviving contribution is s=m, equal to [(m!)^3/m!]*L_H(0)=(m!)^2.

For m>=2 the order-s=1 contribution is zero while the order-s=m contribution supplies the **entire** response. The port-edge response therefore has a genuine higher-order cooperative source interaction in this candidate model, of unbounded finite order m. No inference about native energy or time evolution is made.

Exact verified values by independently labeled source-partition recursion for m=1,...,8:

m=1: 1
m=2: 4
m=3: 36
m=4: 576
m=5: 14400
m=6: 518400
m=7: 25401600
m=8: 1625702400

## Future model test

Extract an actual lawful Cell/Link/Port change that adds or removes one verified native triad incidence type T. If such an update exists, use the proven transfer law to compute exact changes in the labeled-source partition observable under that event. Track sign, port, native Cell, ordering and actual TRIADIC_CLOSURE_E certificates separately. A candidate edge transition must first be shown to be a legal native event before transferring any dynamical/physical conclusion.