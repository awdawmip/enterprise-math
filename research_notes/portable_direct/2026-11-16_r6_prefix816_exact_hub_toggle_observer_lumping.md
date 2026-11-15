# PREFIX-816 — Exact future-observer lumpability for named BRC hub-cycle toggles

Date: 2026-11-16. Research mode: independent portable TASK_RESEARCH auxiliary mathematics. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Sources: PREFIX-809 named source-cycle moves; PREFIX-811/812 observer-difference fibers; PREFIX-815 exact bounded-hub source fiber and unbounded joint rank. Current method rules were read separately from the scientific pin.

## Question and mathematical model

PREFIX-815 proves a one-edge release can produce arbitrarily large rank in a joint named-source observer. Can the much smaller scalar hub count nevertheless preserve every future observation in a specifically declared branch-toggle language?

Take m>=1 named unfixed spoke branches in the PREFIX-815 integer transportation construction and hub capacity 0<=q<=m. Its legal named source tables are in bijection with subsets S of [m] of size <=q. Here t_i=1 iff i is in S, y_h=|S|, and all other edge values are uniquely reconstructed by the PREFIX-815 equations. The complete state is S; proposed scalar observer U(S)=|S|.

Declare a weighted operation language. A legal elementary residual-cycle toggle adds an inactive branch i if |S|<q (weight alpha_i>=0), or removes an active i (weight beta_i>=0). All weights are nonnegative integers. The weight of a path is the product of step weights, and weights of alternative named paths add. Zero-weight steps contribute zero, including if their underlying combinatorial toggle is feasible. Each toggle is a valid four-edge integer residual cycle of the hub source graph and changes its hub count by exactly +1 or -1.

For initial S, length h>=0 and terminal count l, define P_h(S,l) to be the sum of the weights of all h-toggle paths ending at any named state T with |T|=l. Say the scalar observer is future-sufficient when P_h(S,l) depends only on |S| for every h and l. h counts formal operations; it is not asserted to be native Heartbeat time.

## Theorem 816.1 (sharp all-horizon count-lumping criterion)

Suppose m>=2. The scalar count observer is future-sufficient if and only if:

1. q=0: no restriction on named weights;
2. q=1: beta_1=...=beta_m; the alpha_i may differ;
3. 2<=q<=m: beta_1=...=beta_m and alpha_1=...=alpha_m.

For m=1, count already identifies every named state, so no additional restriction is needed.

Under these conditions, let B be the (q+1) by (q+1) integer matrix indexed by counts k=0,...,q. Its only possibly nonzero entries are

  B[k,k-1] = k*beta       (1<=k<=q),
  B[k,k+1] = (m-k)*alpha (0<=k<q, q>=2),
  B[0,1]   = sum_i alpha_i (q=1).

In the q=0 case B=[0]. For every S with k=|S| and all integers h>=0, the row (P_h(S,0),...,P_h(S,q)) equals row k of B^h, interpreted as exact integer path counting, with B^0 the identity.

### Proof

Let Q(S,T) denote the named one-step weighted adjacency. At count k=|S|, the sum of outgoing weights to count k-1 is D(S)=sum_{i in S} beta_i, and the sum to k+1 is A(S)=1_{k<q} sum_{i not in S} alpha_i. All other count-class row sums are zero. If D and A depend only on k, then the partition by count is weighted equitable. Grouping the intermediate named states in a length-(h+1) path by their count and applying induction proves the B^h formula. Conversely, future sufficiency at h=1 requires D and A to be class-constant.

If q=0 there is just one named state. If m>=2 and q>=1, comparing the singleton states {i} and {j} shows beta_i=beta_j because their downward totals are beta_i and beta_j. At q=1, the unique empty state can add branches with combined weight sum_i alpha_i, whereas singletons cannot add. Uniform beta is therefore sufficient and no equality of alpha is needed.

If q>=2, comparison of singleton upward totals gives sum_{r!=i} alpha_r=sum_{r!=j} alpha_r; hence alpha_i=alpha_j. Conversely, common beta and alpha imply D(S)=k*beta and A(S)=(m-k)*alpha when k<q, as stated. At m=1 no count class has two named states. Boundary counts and zero weights cause no exception. QED.

## Corollary 816.2 (exact compressed path evaluation)

The named legal fiber has N(m,q)=sum_{k=0}^q binom(m,k) states. When the criterion holds, the quotient contains q+1 count states. Constructing its nonzero weights uses O(m+q) integer operations and O(q) storage; propagating a quotient histogram through H formal steps uses O(Hq) integer arithmetic operations. Integer bit lengths depend on H, m and the named weights, so this is an arithmetic-operation rather than universal bit-complexity bound.

At q=1 with nonuniform births but uniform removals, the full (m+1)-state named graph has the exact two-state future-count operator

  B = [[0, sum_i alpha_i], [beta, 0]].

## Corollary 816.3 (typed branch-count carrier)

Partition branch indices into types a such that all members of a type share the same pair of weights (alpha_a,beta_a), and let m_a be their population. The vector c=(c_a), with c_a the number of active branches in type a, is sufficient for weighted future paths observed through the type-count vector. Its only moves are c->c+e_a with weight (m_a-c_a)*alpha_a if sum_a c_a<q, and c->c-e_a with weight c_a*beta_a. Proof: each named state with the same type-count vector has exactly those aggregated row sums, so the same induction applies. This provides an exact intermediate BRC carrier between named branch states and the scalar count.

## Sharp witnesses and residual scope

EXCEPTION AT CAP ONE. Let m=3, q=1, alpha=(1,2,3), beta=(2,2,2). The exact quotient is B=[[0,6],[2,0]]. Every singleton yields precisely the same future count histogram for all h even though its source identity differs.

FAILURE AT CAP TWO. Let m=3,q=2,alpha=(1,2,1),beta=(1,1,1). Initial named states S={1} and S={2} have identical hub readout U=1. The one-step total weight for reaching U=2 is 2+1=3 from {1}, but 1+1=2 from {2}. Thus the scalar quotient fails at h=1.

NAMED-FUTURE DISTINCTION. Even if all weights are uniform, future operations that inspect the named predicate t_i=0, or observe whether pinning a specified branch i at zero is enabled, distinguish {i} from {j} for j!=i. The scalar reduction is exact for the declared weighted toggle and aggregate-observation language; named future tests require richer state. This is an explicit example of observer- and operation-dependent structural residual preservation.

## Exact regression

Executable source: research_notes/portable_direct/PREFIX816_R6_BRC_HUB_LUMPABILITY_CHECK.py.
Structured output: research_notes/portable_direct/PREFIX816_R6_BRC_HUB_LUMPABILITY_RESULTS.json.
Python standard library, no floating point, no randomness. Run:
python research_notes/portable_direct/PREFIX816_R6_BRC_HUB_LUMPABILITY_CHECK.py

Exhaustive domain: every m=2,3,4; every q=0,...,m; every alpha,beta in {0,1,2}^m. A generic enumerator builds named legal states and all named toggle weights independently of the theorem's criterion, computes one-step class totals, and compares to the stated classification. All 35,964 patterns agree: 7,776 lumpable and 28,188 non-lumpable. Per m: 243, 2,916, and 32,805. In deterministic selected lumpable patterns (plus every m=2,q=1 case), the checker independently expands actual named weighted paths and compares them with B^h for h=0,...,4: 2,920 additional exact assertions, all passing. Explicit nonuniform-birth witnesses are separately asserted. General all-m/all-h validity rests on the proof, while these finite checks confirm the implementation in their stated domain.

## Next research question and status

Classify the coarsest observer-safe intermediate quotient under heterogeneous named toggle weights when total count is insufficient; investigate whether further collapses of identical (alpha,beta)-types are possible under q=1, finite horizons, or constrained future tests. Combine the dynamic sufficient-state quotient here with the static integer-lattice results of PREFIX-815 to quantify when large joint source-difference rank coexists with a small future language. Exact native X6 Cell/Link/Port attribution and physical time evolution are separate unproved bridges.

Status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. Independent auxiliary research only: no shared CLAIM, Result, Driver review, or Foundation promotion.