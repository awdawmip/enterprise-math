# PREFIX-496 — Dense exact BRC–KMP first-source joint ranking

Date: 2026-11-05 (Asia/Shanghai). Scientific input pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Predecessor: research_notes/portable_direct/2026-11-05_prefix495_exact_brc_fiber_rank_and_joint_streaming.md.

## 1. Domain, observation, and next question

Work within the Heartbeat World native X6 space, restricting the sixth signed axis to zero occupancy; this is a declared X6 path subfamily, not a new independent lower-dimensional world. The remaining signed primitive directions are a,A,b,B,c,C,d,D,e,E. For a path of length n, put y_i=u_i-v_i, p_i=min(u_i,v_i), V=p_b+2p_d+p_e and W=p_c+p_e. Its terminal KMP state for gate g in {aab,aba} is q in {0,1,2,3}. The first source t is N until a b/B or c/C occurs, then permanently B or C according to which occurs first. The output of this certificate is exactly (n,y_a,y_b,y_c,y_d,y_e,V,W,q,t); the permitted future operation appends a single native direction. This does not claim safe erasure of X6 path provenance, physical time or other stronger joint observers.

PREFIX-495 densely ranked the base image x=(y,V,W), with A_n fixed-length base fibers, but allocated a uniform 11 positions per base for aab, or 10 for aba, though not every (q,t) is supported by every base. We construct a dense rank of only realized *joint* states, verify its actual gain and account for its cost.

## 2. Theorem — exact all-n joint reachability and dense ranking

Let D_(g,n) be the set of reachable states (y,V,W,q,t) after n steps, with D_(g,0)={(0,0,0,0,0,0,0,0,N)}. For a signed step epsilon on axis i define delta=1 if and only if epsilon*y_i<0. The exact base observer transition is y'_i=y_i+epsilon, V'=V+c_i*delta, W'=W+d_i*delta, c=(0,1,0,2,1), d=(0,0,1,0,1). Update q by the ordinary prefix-suffix KMP transition and t by the absorbing first-source automaton. Call the resulting map T_g(s,letter). Then, for every n>=0,

    D_(g,n+1) = union_(s in D_(g,n), letter in alphabet) {T_g(s,letter)}.

Proof: every length n+1 path has a length n prefix and last native step, and the specified observer transition is exact; conversely each transition extends an actual realizing path. Induction establishes equality for all n. The induction also shows that the computed first-source supports contain no imaginary states and omit no real states.

Order the exact base image B_n by the PREFIX-495 bijective base rank r_n:B_n->{0,...,A_n-1}. For each base x define C_g(x)={(q,t):(x,q,t) in D_(g,n)} and k_g(x)=|C_g(x)|>=1. Put P_g(n,r)=sum_(j<r) k_g(r_n^{-1}(j)). Order (q,t) in C_g(x) by numeric q, then N<B<C. The joint rank

    R_(g,n)(x,q,t) = P_g(n,r_n(x)) + ord_(C_g(x))(q,t)

is a bijection D_(g,n)->{0,...,S_g(n)-1}, S_g(n)=sum_(x in B_n) k_g(x)=|D_(g,n)|. Each base fiber occupies one consecutive block of exactly k_g(x) positions, and adjacent blocks meet without gaps. Inversion finds the block, applies the already proved base unrank, and indexes its ordered controller support. The minimum fixed-width number of bits to encode all outputs at length n is exactly ceil(log2 S_g(n)), attained by this rank. Because A_n<=S_g(n)<=k_g A_n and A_n=n^7/420+O(n^6), this yields 7 log2(n)+O(1) bits at fixed n, with exact optimality for each finite n. This is a constructive mathematical statement, not a constant-preprocessing-cost claim.

## 3. Exact finite consequences and observer distinction

The accompanying executable Python certificate constructs the reachable sets and dense ranks to n=9 with exact integers. At n=8, A_8=22,275; there are 60,590 actual aab (base,q,t) states and 60,550 actual aba states. Radix capacities are 11*A_8=245,025 and 10*A_8=222,750, so a fixed-length code shrinks from 18 bits to 16 bits for both gates. At n=9, A_9=43,054; the aab and aba actual joint counts are 127,403 and 127,298; the corresponding widths are 19 and 17 bits. The two-bit gains at n=8 and n=9 are exact finite facts. Universal formulas for S_g(n) are still an open question.

At n=8, the same computed full states projected onto (base,q), discarding the actual t value, have cardinalities 39,886 (aab) and 39,887 (aba). This exactly reproduces the PREFIX-493 q-fiber counts. In that earlier observation a source support mask is attached to a (base,q) fiber; it is not an individual first-source t state. Thus full joint state counts above are correctly larger than q-only fiber counts, and the two statements describe different declared observations.

For aab at n=8, the number of base fibers supporting exactly 1, 2, 3, 4 controller states is respectively 4,910, 8,947, 2,289, 3,870; another 2,259 support at least 5 states. For aba these counts are 4,910, 10,102, 1,078, 2,826; another 3,359 support at least 5. In each gate 21 base fibers support all controller states (11 or 10 respectively). The support is genuinely nonuniform, so the uniform radix contains many holes.

## 4. Executed evidence and cost

The program prefix496_dense_joint_certificate.py is dependency-free and uses exact integers. It verifies the PREFIX-495 closed formula for A_n at every n=0..9, checks explicit ranking as a complete bijection with an inverse array for every joint state, and compares (base,q) projection sizes at n=8 to PREFIX-493. Independently, for each gate it enumerates all 11,111 ordered words of lengths 0..4 and compares raw direction occupancies, KMP suffixes and first-source tags to the finite-state transition recurrence. The executed JSON log ends ALL_CHECKS_PASS. Finite tests are implementation checks; the all-n recurrence and rank theorem follow from induction and block partition, not extrapolation.

For a precomputed prefix n<=N, set propagation takes at most O(10*sum_(n<=N)S_g(n)) transition insertions; sorting and building rank indexes takes O(sum S_g(n)*log S_g(n)) comparisons and O(sum S_g(n)*log N) bits of explicit state/index storage. Since S_g(n)<=11*A_n=O(n^7), this auxiliary space can be O(N^8 log N) bits. With a fully materialized hash/rank lookup, streaming state decode/update/re-rank takes expected constant dictionary probes on O(log N)-bit keys; with sorted indexes, logarithmic search is available. In particular this is much more expensive shared preprocessing than the O(N log N)-bit PREFIX-495 base-only prefix table. The two-bit payload savings cannot be advertised as global system memory or latency savings without amortization/compact support formulas. A fresh path from raw symbols still incurs its ingestion cost.

## 5. Next question (PREFIX-497)

Find a compact exact representation for the support set C_g(x), or at least its cardinality k_g(x), using the signed-displacement/cancellation lattice description rather than full D_(g,n) enumeration. Test boundary and interior support patterns for fixed (y,V,W), then build a support-aware fast rank that is compatible with native append and compare complete preprocessing/update costs. Preserve the distinction between current observer sufficiency and stronger provenance/physical-time contracts.
