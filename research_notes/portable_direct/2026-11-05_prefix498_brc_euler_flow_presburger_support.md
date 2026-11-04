# PREFIX-498 — Euler-flow Presburger certificate for native BRC–KMP source fibers

Date: 2026-11-05 (Asia/Shanghai). Researcher-ID EM-DIRECT-D2D5D3.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Predecessor: PREFIX-497 @13d7c8c453351605761fb46453e5462c85e47964.

## Precise question and observer

For the ten-direction path subfamily a,A,b,B,c,C,d,D,e,E embedded in the six-axis Heartbeat World, retain length n, five signed displacements y, the BRC cancellation observations V=p_b+2p_d+p_e and W=p_c+p_e, and the complete *set* C_g(n,y,V,W) of possible final KMP/first-source controller pairs (q,t), where g is aab or aba and t is N, B or C. Allowed future operations are native direction appends under the retained observer. The sixth axis is not used in this restricted path family.

The exact five-color quotient from PREFIX-497 is Σ={a,b,B,c,x}; color c combines c/C and x combines A/d/D/e/E. Let Q_g be its reachable deterministic KMP/first-source controller states, with initial s0=(0,N) and transition τ_g. The exact state counts are |Q_aab|=11 and |Q_aba|=10.

## Theorem A: exact transition-flow membership

Fix a five-color count vector k in N^5, terminal controller state f, and n=sum_j k_j. Let z_(s,j) count uses of each transition s --j--> τ_g(s,j). Then a color word with counts k and terminal state f exists **if and only if** the following integer conditions hold:

1. Color totals: sum_s z_(s,j)=k_j for every color j.
2. Directed balance: sum_j z_(v,j) - sum_(s,j : τ_g(s,j)=v) z_(s,j) = [v=s0]-[v=f] for every v.
3. All positive-degree vertices of the undirected support of positive z edges form one connected component containing s0. For n=0, f=s0 and all z are zero.

Proof: an existing word gives counts and a connected trail, hence all conditions. Conversely each z is a multiset of labeled directed controller edges. Balance plus weak connectivity gives a directed Euler trail from s0 to f; reading its colors yields the desired word and preserves the deterministic controller trajectory. For n=0 the empty word is the unique witness. Connectivity excludes disconnected balanced cycles, a genuine counterexample to using flow balance alone.

## Theorem B: exact BRC support with bounded integer dimension

For X=(n,y,V,W), compute m=(n-sum_i |y_i|)/2. Reject when m is not a nonnegative integer. Set d=p_d, e=p_e and derive the only compatible remaining cancellation numbers:
p_a=m-V-W+d+e; p_b=V-2d-e; p_c=W-e.
Require d,e,p_a,p_b,p_c all nonnegative integers. Then the color counts are exactly

k_a=p_a+max(y_a,0);
k_b=p_b+max(y_b,0);
k_B=p_b+max(-y_b,0);
k_c=2p_c+|y_c|;
k_x=p_a+max(-y_a,0)+2(d+e)+|y_d|+|y_e|.

A controller state f belongs to C_g(X) **if and only if** some integer d,e,z satisfies the cancellation constraints and Theorem A's color totals, balances and connectivity.

Proof: the PREFIX-497 cancellation lattice bijection enumerates exactly all ten-direction occupancies with observation X. Its five-color lifting theorem preserves every controller state over all permutations. Theorem A gives precisely the controller endpoints for each lifted count vector. Taking the existential union over d,e gives the assertion, with all boundary cases included.

Connectivity becomes a *fixed finite disjunction* of linear inequalities: select R subset Q_g containing s0 and f; require positive-count edges to have both endpoints in R, each R vertex other than s0 to have positive incident degree, and for every proper cut U subset R containing s0 require at least one edge across U and R\U. The number of subsets and cuts depends only on g, not on n. Thus the existence condition is a finite disjunction of integer linear systems in at most 5|Q_g|+2 <= 57 integer variables, with constants computable from the binary coordinates n,y,V,W.

**Corollary.** For each fixed gate g in {aab,aba}, the exact membership predicate f in C_g(X), and hence the entire support mask, is decidable in time polynomial in the binary input bit length by the fixed-dimensional integer-programming theorem (Lenstra 1983). This is an existence/complexity theorem; the constants from the finite cut disjunction may be substantial. A single-support query no longer mathematically requires the O(n^4) five-color Parikh table and O(n^2) cancellation enumeration used in PREFIX-497. This finite disjunction is also an explicit existential Presburger description of the observation-support relation.

## Executed exact validation

Two independent exact-integer checks were carried out:
(1) An executed JavaScript certificate (published alongside this report) constructs the two native controller graphs, enumerates every five-color word of length 0..6 (19,531 words per gate), checks its flow/weak-connectivity conditions, and reconstructs an Euler trail with matching transition counts and endpoint. Output ALL_CHECKS_PASS.
(2) The extended Python 3 integer certificate independently checked all 111,111 raw native ordered words of length 0..5 per gate and compared all 2,970 corresponding BRC base-observation support sets against the five-color DP plus exact d,e lattice formula; it checked 19,531 five-color word witnesses per gate and 4,300 synthetic transition multisets per gate. Output ALL_CHECKS_PASS. Its full script, trace and SHA-256 manifest are preserved in the companion local research evidence archive; GitHub's executed JS file is a separately run concise witness of Theorem A.

The universal theorem is proved by the two bijections and the directed Euler-trail criterion. The bit-complexity corollary uses Lenstra's fixed-dimensional integer-programming theorem; no implementation or benchmark of that solver was executed this round.

## Relation and next question

BRC typed reuse is COMPOSE_APPLIED: PREFIX-493 append update, PREFIX-495 base rank, PREFIX-496 controller support and PREFIX-497 five-color lifting. Source/provenance is retained for the declared observer and future operation class; P000 and ACTIVE worldview remain unchanged. Research is independent author-side work, not a Result/Review/Admission or a formal claim on another published Task.

Next PREFIX-499: implement a compact exact flow/Presburger support oracle, compare solver preprocessing and query costs with the PREFIX-497 lattice/table, then derive usable prefix-count formulas for PREFIX-496's dense joint rank without enumerating all base fibers. Retain full support masks and account for decoding and append costs.

Reference: H.W. Lenstra, Jr., Integer Programming with a Fixed Number of Variables, Mathematics of Operations Research 8(4):538–548 (1983), DOI 10.1287/moor.8.4.538. Directed Euler-trail theorem is classical.
