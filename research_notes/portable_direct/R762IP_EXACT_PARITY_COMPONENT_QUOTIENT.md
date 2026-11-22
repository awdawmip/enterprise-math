# R762IP — exact GF(2) component criterion after inactive-Port filtering

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / BRUTE_FORCE_CROSSCHECKED / NOT_REVIEWED.
Frozen six-axis composite Port-Euler observer pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R762IO corrected inactive-Port census on the same research branch; R762IN and R762IM retained at their exact historical versions.

## Exact all-even-degree feasibility theorem (arbitrary finite event multiplicities)

Fix nonnegative integer counts n_S for each of the 20 three-axis supports and a proposed inactive-Port set M. On each positive support S let A_S be the pair-Ports of S outside M. If any |A_S|<2, no edge assignment avoiding M is possible.

For each positive support with |A_S|=3 and n_S>=2, add the three allowed pair-Port edges to an undirected graph G_free on V=all 15 Ports minus M. Call its connected components C_1,...,C_r, including isolated vertices.

For each positive support with |A_S|=2, there is exactly one allowed edge e_S; put its incidence vector e_S into a fixed GF(2) boundary b when n_S is odd, and put zero when n_S is even. For each full-three-Port support with n_S=1, choose exactly one of its three edge incidence vectors. Let q be the XOR of these chosen vectors and b.

THEN there exists an assignment of EVERY named event to a legal Port edge avoiding M, in which every Port degree is even, if and only if some choices for the full-three-Port n_S=1 supports make

sum_{v in C_i} q_v = 0 (mod 2)   for every component C_i of G_free.

Equivalently, q lies in the GF(2) incidence span of G_free. This is necessary and sufficient for EVEN DEGREE; connectedness and exact activation of all v in V are separate requirements.

Proof for each support. If |A_S|=2 all n_S events must use the same edge, so their boundary is (n_S mod 2) times its incidence vector. If |A_S|=3 and n_S=1, exactly the three nonzero pair-edge boundaries are possible. If |A_S|=3 and n_S=2, using the same edge twice gives zero, and using two distinct triangle edges gives any one of the three edge boundaries. If n_S=3, using all three triangle edges gives zero, and using any one edge three times gives its boundary. Any greater n_S reduces to the n_S=2/3 case by adding repeated parallel pairs, which do not change parity. Thus each full-three-Port support with n_S>=2 supplies independently the entire two-dimensional even-parity space on its triple of Ports. Summing these spaces over all such supports is the incidence span of G_free, exactly the vectors with zero coordinate sum on each component of G_free (proved by a spanning forest). Add the fixed b and one-edge singleton choices to obtain the stated criterion.

Algorithm. Build connected components of G_free once, XOR the fixed support charges, then enumerate at most 3^u singleton choices, where u is the number of supports with multiplicity one and |A_S|=3. For R762IM upper-tail families, u<=3, so at most 27 component-signature trials are needed per (histogram,M), without iterating 3^(sum n_S) assignments. This is a complete mathematical parity test, not a complete Euler feasibility test.

## Exact counterexample to local-incidence sufficiency

Set zero supports Z={134,245}; give each of the remaining 18 supports multiplicity three (54 total events). Specify inactive Ports M={01,24,25,45}. Every positive support has at least two pair-Ports outside M, satisfying the exact R762IO local-incidence criterion F(M) subset Z. The graph of all potentially allowed edges is connected on the 11 proposed active Ports, as verified in R762IO's exhaustive scan.

However Port 14 belongs to only four supports: 014,124,134,145. Support 134 is absent; the other three supports all have count three. Since 01,24,45 are inactive, each of 014,124,145 has exactly one allowable pair-Port edge, respectively 04-14, 12-14 and 14-15. EVERY legal assignment avoiding M therefore gives

degree(14) = 3 + 3 + 3 = 9, odd.

No even-degree assignment exists, hence no legal Euler loop realizes the proposed active Port set. This example proves that a connected potential graph and correct local incidence masks are insufficient for Euler realization; a parity filter is indispensable. It does NOT disprove existence of a legal Euler realization of the same histogram with a different active set.

## Verification and next work

The attached standard-library Python checker implements the quotient criterion and separately brute-forces actual event-to-edge assignments on 1,107 deterministic small instances, comparing the exact yes/no outcomes; all agreed. It independently checks the 54-event forced-odd-degree obstruction. Observed run: PASS R762IP_EXACT_PARITY_QUOTIENT.

Next: use this exact quotient as an early filter for all 14,260,096 R762IO local candidate (histogram,M) pairs; for parity-feasible cases, test exact activeness, connectivity and existence of 52-event support-parity-preserving witnesses. Keep support labels, active Port identity and P000 observer/native distinctions explicit. The R762IM existential high-tail statement remains unverified after its documented completeness gap; review status NOT_REVIEWED.
