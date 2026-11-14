# R762AI — An exact optimal codec for named source BRC fibers of sliding bursts

Status: AUTHOR-SIDE CONDITIONAL THEOREM, EXACT CODE VALIDATION, NOT_REVIEWED (2026-11-14).
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R762AH, Draft PR #2401, immutable 1d6edba581242c1adde59f56d053a2bb71b87d84. This is an auxiliary source-blind Cell/Port star observer, not an admitted native force dynamics.

## Problem

Fix integers 2 <= B <= m. There are m occupied unit-capacity outer ports with distinct source quanta 0,...,m-1, and a central buffer of capacity B. Each token enters once (I_i); each destination j receives one token (O_j), never from its own original source j. The public log preserves all ingress/egress ports and event order, but removes the source name at egress.

Consider the R762AH sliding log tau_(m,B): ingest I_0,...,I_(B-1), then perform O_j followed by I_(B+j) when available, for j=0,...,m-B, and finally O_(m-B+1),...,O_(m-1). Let F_(m,B) be the set of compatible bijections from output ports to source names; f_(m,B)=|F_(m,B)|. The question is the exact amount of lossless repair information needed to recover the complete hidden named provenance of a *fixed known log*.

## AI1. A terminal matching formula

Suppose n distinct sources and n output ports remain after the final ingress. Let k be the number of source labels that also occur among the n output labels. Every common label creates exactly one forbidden self-return match, and all k forbidden pairs are disjoint. Hence

\[
E(n,k)=\sum_{r=0}^k(-1)^r\binom{k}{r}(n-r)!.
\]

Proof: select r forbidden pairs and fix them; (n-r)! permutations remain. Inclusion–exclusion completes the proof. For an R762AH terminal window bitmask S, the n=B-1 remaining destination labels and the active window sources have exactly |S| common labels; therefore t_B(S)=E(B-1,|S|). For B=3 this gives t_3=(2,1,1,1), independently confirming the former terminal vector.

## AI2. A bijective, optimal fixed-length source-provenance codec

Theorem. For every 2 <= B <= m, the following Rank and Unrank algorithms establish a lexicographic bijection

\[
F_{m,B}\longleftrightarrow\{0,1,\dots,f_{m,B}-1\}.
\]

Both sender and receiver know (m,B,tau_(m,B)). Thus the exact minimal number of *fixed-length binary bits* needed to distinguish every compatible named source history is

\[
\ell_{m,B}=\lceil\log_2 f_{m,B}\rceil,
\]

with zero bits for a singleton fiber.

Proof and construction. Write q=m-B+1. R762AH supplied an integral transfer matrix T_B indexed by the 2^(B-1) bitmasks S describing which of the most recent B-1 source labels remain unused. The older unused labels are strictly less than the next output index and cannot violate any *future* self-return condition; their multiplicity is recorded by T_B.

Form backward completion values

\[
C_q(S)=E(B-1,|S|),\qquad
C_j(S)=\sum_{S'}T_B(S,S')C_{j+1}(S')\quad(j=q-1,\ldots,0).
\]

The existing R762AH exact transfer proof gives C_0(S_full)=f_(m,B) for S_full=2^(B-1)-1.

To Rank, retain the *actual* unused named source set U (not only the compressed mask). At each main output O_j, first add the incoming source j+B-1; examine every available source i except i=j, sorted increasingly. For each individual i, compute the resulting mask S'_i and its precise suffix count C_(j+1)(S'_i). An older identity i<j contributes exactly one such suffix count: it is essential not to multiply by the total older-source multiplicity a second time. Add the counts of choices preceding the actual source i to the running rank, remove i, and advance.

After the last ingress, at output O_j and a proposed source i, there remain n=m-j-1 further outputs and some set U' of remaining source labels. Its exact suffix count is E(n, |U' intersection {j+1,...,m-1}|), by AI1. Continue lexicographic accumulation until all outputs are assigned.

To Unrank an integer r in [0,f), examine source choices in the same order. Their positive completion counts form consecutive disjoint integer intervals. Select the interval containing r, subtract preceding interval lengths, and recurse to the next output. The AI1 tail and R762AH transfer recurrence prove by induction that the intervals partition the exact remaining matching set at each stage. Therefore Rank and Unrank are inverses, each entire fiber is attained exactly once, and all source-to-port allocations and their intermediate named hub histories are reconstructed.

The lower bound follows from the pigeonhole principle: b fixed bits distinguish at most 2^b distinct hidden source assignments, while the permitted future operation may inspect their different final named placements. Rank achieves that lower bound by using the padded binary representation of r.

Counting all suffixes takes O(m B 2^(B-1)) exact integer operations and O(m 2^(B-1)) stored integer entries. With standard small set/sort operations, a single Rank or Unrank after precomputation uses O(m B log B+B^3) basic arithmetic operations, including the final explicit forbidden-diagonal matching counts. For fixed B, arithmetic operation count is linear in m, while integer bit complexity is retained separately (the counts have O(m log B) bits). This algorithm is for the restricted sliding-source permanent, not for an arbitrary permanent.

## AI3. Exact asymptotic repair density when B=3

R762AH already proved the positive transfer matrix T_3 has characteristic polynomial

\[
p(x)=x^4-2x^3-x^2-x-1.
\]

The matrix is primitive, and its Perron eigenvalue is the positive real root lambda=2.59205279238617... . Because initial and final vectors couple positively to its Perron eigenvectors, f_(m,3)=c lambda^m(1+o(1)) with c>0, whence

\[
\ell_{m,3}=m\log_2\lambda+O(1),\qquad
\lim_{m\to\infty}\frac{\ell_{m,3}}m
 =\log_2\lambda=1.3740951019177958\ldots.
\]

This is the source-identity repair rate *for this observer and conditional model*, not a physical entropy or a native force amplitude.

## Reproducible exact verification

The accompanying Python 3 standard-library verifier independently enumerates every compatible permutation (without transfer DP) for B=2 and m=2..10, B=3 and m=3..10, and B=4 and m=4..8. It checks the exact source-fiber count and every ordinal rank/round-trip against this oracle: 22 exhaustive (B,m) cases and 5091 named histories. Twenty additional (B,m) cases at B=2..6 and m=9,14,18,32 sample first, last, and quantile ranks; the R762AH quartic recurrence is also rechecked with exact integers through m=32.

For B=3 and m=3..12, the exact fiber sizes are 2,6,15,39,101,262,679,1760,4562,11825; fixed-length repair bits are respectively 1,3,4,6,7,9,10,11,13,14.

The Python source and JSON evidence are deposited alongside this proof. All tests completed successfully in the local Python 3 runner, and the JSON report preserves each tested (B,m), fiber size, verified code count and requested bit width.

## Relation to P000 and further research

This theorem concerns positive integer BRC source-provenance branches in an auxiliary hub with unit-capacity ports and no-home-return egress. P000 still fixes six native spatial axes, a three-dimensional research slice and primitive three-force stable closure. The auxiliary hub's occupancy and ingress/egress schedule have not been admitted as TRIADIC_CLOSURE_E.

The next native step is to derive actual Cell/Link/Port force-event incidence and admitted repeatability. Intersect the present fiber with that exact typed event alphabet, then recompute the source repair rank while retaining V29 PASS versus TRANSFER, V17 frame action, V39 holonomy, signed branch structure and the observer/future-operation scope. Separately, R762AH's assertion that the sliding word maximizes a general B=3 complete-log fiber has only been verified through m=10 and remains open.

P000 and frozen task inputs are unchanged; formal Result and independent Driver acceptance require their own actual authority and review.