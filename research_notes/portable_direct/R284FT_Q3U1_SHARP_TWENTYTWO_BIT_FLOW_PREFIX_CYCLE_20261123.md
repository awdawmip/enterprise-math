# R284FT — All-code sharp 22-bit cycle for omission q=3 and read noise u=1

Date: 2026-11-23 (Asia/Shanghai).
Status: AUTHOR_EXACT_FINITE_PROOF / INDEPENDENT_REVIEW_PENDING.
Scope: informed portable TASK_RESEARCH, auxiliary four-phase binary observer; frozen R284CO scientific inputs, P000, X6/Heartbeat ontology and all earlier author attributions unchanged. No formal CLAIM, Result or independent mathematical Review.

## Theorem

In the inherited R284FM/R284FR/R284FS fixed-four-code model, the writer cycles c0->c1->c2->c3->c0 and attempts each nominally changed bit at most once in a fixed order, with up to q=3 omitted writes at every publication. Omitted residuals can persist through arbitrarily many generations. Each stateless read may flip up to u=1 bit; stable reads must name the true generation, a non-atomic prefix must not report a third generation, and independent reads while a prefix is paused must not return a newer success followed by an older success.

For arbitrary fixed distinct binary labels and arbitrary per-edge write orders, **the exact minimum tag width is**

    n_min(3,1) = 22.

This is a model-typed capacity theorem, not a new primitive X6 spatial theorem.

## New exact prefix-distance flow lemma

Let S_i be the complete all-history stable-state set at phase i. R284FM's all-history reachability lemma gives its exact description: c_i may be flipped in an arbitrary subset of up to q coordinates **in each last-nominal-change group**, independently. On phase edge i->t, fix a subset T of successfully attempted changed coordinates; let W(T) be the physical prefix words obtained by overwriting the coordinates T of an arbitrary s in S_i with the target bits of c_t.

For an arbitrary target stable phase j, construct an integral demand network:
- A non-overwritten coordinate k with c_i[k] different from c_j[k] produces one unit of demand assignable either to the left vertex L_(ell_i(k)) or right vertex R_(ell_j(k)).
- An overwritten coordinate k with c_t[k] different from c_j[k] produces one unit assignable **only** to R_(ell_j(k)). A bit overwritten to the j target creates no demand.
- Every one of the four left and four right last-change group vertices has capacity q. Ordinary demand units may be matched to either eligible end, and right-only units to their single eligible group. All matching is integer.

If D is the total number of demand units, and nu is the maximum integral flow, then

    min_{w in W(T), s in S_j} d_H(w,s) = D - nu.           (FT1)

Proof: on each nominally differing coordinate, either an allowed omission error on the source side (when the bit was not overwritten) or an allowed omission error in j's stable state makes the two physical values agree. An unassigned differing coordinate contributes exactly one Hamming mismatch. The source and target phase errors have separate per-group capacities q. Hence every legal pair of stable states induces a feasible assignment with one match per corrected bit, and every integral assignment is realized by selecting the indicated errors in the relevant independent last-change groups. Overwritten coordinates cannot be altered by source errors, explaining their right-only edges. Thus maximizing corrected coordinates exactly minimizes Hamming distance. No floating-point, finite history cutoff or implicit per-group observation-flip budget is used.

The formula generalizes R284FM's stable-to-stable min-cut: set T empty. In particular, two independent radius-u readings can share an observed word between the prefix and stable phase j **if and only if** the distance in (FT1) is at most 2u, by splitting the differing coordinates into two flip sets of size at most u.

## A necessary no-rollback prefix test

For every attempted-prefix T0, every omission subset M of T0 with |M|<=q, and actual successful bits T=T0\M:
1. For j outside {i,t}, require dist(W(T),S_j)>2u. Otherwise some legal physical prefix can force forbidden third-phase success.
2. If |T|<=2u, additionally require dist(W(T),S_t)>2u. Otherwise choose w in W(T) within 2u of S_t; phase t is forced by some noisy reading, while the original source stable word used to form w is at Hamming distance at most |T|<=2u from w, forcing phase i on a subsequent noisy reading at the **same physical prefix**. This is forbidden new-then-old success.

These conditions are necessary, not sufficient. To exclude an encoding it is enough to show there exists no monotone path of attempted-prefix counts through nodes passing the test. Equal column patterns are permutation-equivalent for both the physical model and choice of attempted-bit orders, so a finite count lattice in the seven nonconstant patterns exhausts all orders.

## Exhaustive all-code obstruction

Complement each coordinate to set c0=0. Constant coordinates can be deleted without reducing decoding capability; in a putatively optimal code all columns have one of seven nonconstant patterns p=(c1,c2,c3), where c1 is the least significant bit. Thus a width-n candidate is uniquely represented up to coordinate permutation by nonnegative counts x1..x7 summing to n, giving binomial(n+6,6) cases.

Apply all four necessary adjacent codeword distances 2q+4u+1=11, the two opposite distances 2(q+u)+1=9, then all six exact R284FM stable-observer flow cuts (there must be a vertex subset U with |E(U)|>q|U|+2u). For surviving histograms run the prefix-flow necessary test above with exact integer max-flow and exhaustive attempted-count-lattice BFS, first on edge 0->1, then on 1->2.

| Width | Seven-pattern histograms | Six distance tests pass | All six stable cuts pass | Safe path edge 0->1 | Safe path edges 0->1 and 1->2 |
|---|---:|---:|---:|---:|---:|
| 20 | 230230 | 4005 | 10 | 1 | **0** |
| 21 | 296010 | 10421 | 97 | 10 | **0** |

For width 20 the unique first-edge survivor is (0,0,0,0,11,9,0). For width 21 exactly ten first-edge survivors occur; they are asserted explicitly in the checker. Every survivor fails its second edge. These computations exclude all widths 20 and 21, including every possible writing order, not merely Gray codes or separable designs.

R284FP had already established n>=4q+5u+3=20 for q>=2u+1, u>=1; its proof therefore excludes widths below 20 at (3,1). The existing R284FE two-group repeated-Gray construction with group size 2q+4u+1=11 supplies a correct 22-bit protocol. Both sides match, proving the theorem.

## Reproduction and evidence

File in this directory: R284FT_q3u1_22bit_flow_checker.py, standard-library Python. Execute it without arguments. It checks the table, the full explicit set of ten 21-bit first-edge survivors, that no candidate passes the second-edge necessary test, and that the known 22-bit Gray repeated-group histogram passes this **necessary** prefix test. All assertions passed in the author execution.

The exact matching-flow oracle was separately compared against direct enumeration of physical source/target stable states and fixed overwrite operations on 43,200 small-model cases, with zero discrepancies. This small-model verification supports implementation correctness; (FT1) has the general integral-flow proof above. Neither test is a formal independent mathematical review.

Earlier immutable frozen sources:
- R284FM flow-cut and all-history S_i: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9.
- R284FP high-omission all-parameter lower bound: enterprise-math@de49ae0239abee14619a730fe6ea60614a2cde5b.
- R284FE repeated-Gray group upper construction: enterprise-math@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0.
- R284FS 17-bit finite obstruction at q=2,u=1: enterprise-math@aa9bd1a7aa77adb171978f03b99eeeac2405dcf0.

Next: test whether the flow-prefix obstruction supports a symbolic q-family at u=1, especially n=4q+8u+1, without introducing finite search conclusions as universal claims. Separately audit R284FM's all-history group product and (FT1), and extend the observer to bank-data writes and H-stale readers with provenance retained.
