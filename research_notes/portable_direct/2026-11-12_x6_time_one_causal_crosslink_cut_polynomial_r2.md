# X6 native-time cut observers II: one declared causal cross-link and exact cut compression

Date 2026-11-12; Researcher EM-DIRECT-403AAA; own activity RA-3CCFD886BD2BFF49E8A49CB9. Parent task RS-X6-NATIVE-TIME-DYNAMICS (publication TP2-91D4A7C2F63805BE21A3; frozen P000/task science @a72226e2430ffa4786321ac86e7f0c599d5f0389). Companion predecessor: research_notes/portable_direct/2026-11-12_x6_time_cut_lattice_and_C12_winding_residual_r2.md. Status: scoped author-side exact combinatorial conditional theorem, integer verifier, no independent review, no admission of a physical Cell/Link/Port coupling event.

## Setup

Two typed local V1R C12 components have chains of a and b forward internal updates, indexed A_1<...<A_a and B_1<...<B_b, respectively. Assume 0<=a,b<=11 so all local decorated states at different local indices are distinct. Initially cross-component actions are endpoint-commuting on the declared domain, with resource/future-language independence actually certified **only when appropriate**. Add one explicit **hypothetical causal link** A_r<B_s for 1<=r<=a and 1<=s<=b; take the transitive closure. This edge is a mathematical dependency constraint, not by itself an already admitted native physical Link or force law. The resulting finite causal poset is a well-defined combinatorial test for what a future valid native coupling might enforce.

Each event prefix ideal is determined by local completed counts (i,j). The chain constraints demand 0<=i<=a, 0<=j<=b. The cross dependency is respected exactly when j<s OR i>=r: if B_s has occurred, A_r must already have occurred.

## Theorem: closed exact k-cut distribution and reduction from independent product

The generating polynomial of the possible k-event causal-cut ideals is

    C_(a,b;r,s)(x)
    = (sum_(i=0)^a x^i)(sum_(j=0)^b x^j)
      - (sum_(i=0)^(r-1) x^i)(sum_(j=s)^b x^j).

Coefficient [x^k] C counts exactly the legal order ideals with k event occurrences. The total number of distinct ideals is

    C(1) = (a+1)(b+1) - r (b-s+1).

For a,b<=11 each ideal yields a distinct tuple of complete V1R decorated states; hence at k it is also the exact number of possible decorated k-cut states in the **conditional two-chain-plus-one-link model**. Where the coefficient is N>0, identifying the chosen global serialized k-cut from k and initial states requires ceil(log_2 N) bits of additional cut-selection information. The terminal full state remains unique under the declared deterministic local updates.

**Proof.** An order ideal contains initial segments of both chains; it violates A_r<B_s iff its B prefix has length j>=s yet its A prefix has length i<r. The illegal pairs form the rectangle i in [0,r-1], j in [s,b]. Subtract their bivariate univariate-counting monomial polynomial from the unconstrained product. Evaluate at x=1 for the count. Each legal ideal extends to a linear extension of the whole poset, so every counted prefix is actually reachable. When local lengths<=11 the exact V1R period 12 makes the progress-to-state encoding injective, proving the decorated-state formula. QED.

## Exact linear-extension count as a second independent certificate

A sequence interleaving a A's and b B's respects A_r<B_s iff in its first r+s-1 positions there are at least r A's. Count by choosing j A positions in that prefix and a-j in the remainder:

    L_(a,b;r,s)
       = SUM_(j=r)^min(a,r+s-1)
         binom(r+s-1,j) binom(a+b-r-s+1,a-j),

where binomial terms with impossible parameters are zero. This is an exact second invariant, independent of the cut polynomial. It can be checked against enumeration of all binom(a+b,a) possible serializations. It is **not** a physical probability unless a sampling law on serializations is supplied.

## Small examples and sharp effects

* a=b=3, r=s=2: independent product has 16 ideals, degree-k histogram [1,2,3,4,3,2,1], peak four states at k=3. The causal link excludes four ideals, leaving 12 with histogram [1,2,2,2,2,2,1]. Exactly 10 of 20 serializations remain; the maximal cut ambiguity drops from 2 bits to 1 bit.
* a=b=2, r=2, s=1: A_2<B_1 forces a full chain A_1<A_2<B_1<B_2, giving one possible state at every cut and one linear extension. No extra cut-choice bits are required.
* a=b=3, r=1, s=3: 15 ideals, histogram [1,2,3,3,3,2,1], and 19 of 20 linear extensions.
* a=b=4, r=3, s=2: 16 ideals, histogram [1,2,2,2,2,2,2,2,1], and 17 linear extensions.

Thus one precisely located causal link may change intermediate-state observability dramatically without changing either component's local C12 update rule. The required observer memory is a property of the **event dependency relation**, not only the number of Cells or their individual periodic modes.

## Computational evidence

Python standard-library integer checker: research_notes/portable_direct/x6_single_crosslink_cut_verify_20261112.py. Verified for all 100 tuples (a,b,r,s) with a,b=1..4, 1<=r<=a, 1<=s<=b: explicit all-pairs ideal count, polynomial subtraction, closed total, exact complete serial-word enumeration, and closed linear-extension sum. Output: research_notes/portable_direct/x6_single_crosslink_cut_results_20261112.json. All checks PASS; this finite exhaustive suite verifies 100 specified models while the algebraic proofs establish the general theorem in the stated scope.

## Frontier and source discipline

Neither the algebraic cross-link A_r<B_s nor an endpoint-commutation certificate is presumed to be admitted by P000 or the current X6 Cell/Link/Port system. Where future queries inspect order/provenance, cross-component swaps require fresh V2 operation-safe certification even if endpoint updates commute. This theorem provides a concrete quantitative target for such a permission predicate: the guard must specify the added dependency edge(s) and the horizon/observer lease. A physical duration does not follow without a separately calibrated event duration map.

Next discriminate: find an actual lawful native pair of adjacent Cell triadic updates, identify one explicitly sourced causal resource overlap and its event guard, then compute whether the observed serializable k-cut family matches the one-link polynomial; if it does not, locate additional hidden dependencies or retained path/force source state instead of falsifying P000 or inventing a native no-go.
