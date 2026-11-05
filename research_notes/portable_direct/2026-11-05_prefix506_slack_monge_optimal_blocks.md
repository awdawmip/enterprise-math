# PREFIX-506 — Slack-coordinate Monge optimization for adaptive BRC V blocks

Date: 2026-11-05 (Asia/Shanghai). Independent author-side research on the typed native X6 five-axis signed-path subfamily, with the sixth spatial axis unoccupied. Retained observer: signed displacement, BRC V,W, KMP terminal state q for gates aab/aba, and first B/C source t. Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. The current behavioral policies were read independently on 2026-11-05.

## Theorem

For every integer L>=1, b>=1 and nonnegative integer support vector (k_0,...,k_{L-1}), consider partitions of [0,L) into exactly B=ceil(L/min(b,L)) nonempty blocks of length at most b, minimizing the total workload

    C(i,j)=sum_{i<=v<j} k_v (v-i+1).

This is the exact one-query-per-reachable-controller-state V-row oracle-call objective of PREFIX-505. Let b0=min(b,L), B=ceil(L/b0), r=B*b0-L, so 0<=r<b0. The optimal partition can be constructed in O(L+B*(r+1)*log(r+2)) exact integer operations and O(L+B*(r+1)) integer cells including backpointers, after obtaining the L support weights. Since B*r<2L and B<=L, the uniform upper bounds are O(L log(L+1)) arithmetic operations and O(L) integer cells. On r=0 the feasible partition is unique.

## Proof

Write each block length as b0-delta_a with delta_a>=0. Their total is L exactly when sum(delta_a)=r. Since r<b0, all widths are automatically between 1 and b0. Set cumulative slack s_a=sum_{h<=a}delta_h, so 0=s_0<=...<=s_B=r, and the a-th endpoint equals e_a=a*b0-s_a. This parametrizes every admissible B-block partition bijectively.

Define the exact prefix sums F(j)=sum_{v<j} k_v and T(j)=sum_{v<j}(v+1)k_v. Then C(i,j)=T(j)-T(i)-i(F(j)-F(i)), evaluated in O(1) integer operations.

Let D_0(0)=0, D_0(s>0)=infinity. For a=1,...,B-1 and 0<=s<=r,

    D_a(s)=min_{0<=t<=s} [D_{a-1}(t)+C((a-1)b0-t, a*b0-s)].

For a=B, compute only the terminal state D_B(r). Induction over the final block establishes global optimality; storing winning t yields the exact endpoints.

For a fixed layer define i_t=(a-1)b0-t, j_s=a*b0-s and M(t,s)=D_{a-1}(t)+C(i_t,j_s) on the triangular feasible domain t<=s. Whenever t1<t2<=s1<s2, direct cancellation gives the Monge identity

    M(t1,s1)+M(t2,s2)-M(t1,s2)-M(t2,s1)
    = -(t2-t1) * sum_{v=j_(s2)}^{j_(s1)-1} k_v <= 0.

Feasible candidate sets [0,s] expand with s. The smallest minimizing t is nondecreasing with s by the Monge inequality and the smallest-index tie rule. A divide-and-conquer monotone-minima evaluation therefore computes a full layer in O((r+1)log(r+2)) cost evaluations, each O(1) by F,T. There are B layers; prefix construction takes O(L), and all backpointers use O(B(r+1)) cells. This proves the theorem.

The returned adaptive cuts use the exact PREFIX-505 ranked-prefix and rightmost-feasible inverse unchanged. Thus gapless coding, inverse coding and primitive append-then-reencode remain exact in this declared observer scope; the online support-query upper bound remains min(b,L).

## Exact checks and performance

Extended independent Python 3 certificate: full ten-letter native-state enumeration for both gates at n=0..8, 24,024 quotient-row/width cases with exhaustive admissible partition comparisons for widths 2,3,4,5, complete b=2 rank/inverse checks, and 2,128 additional random/adversarial exact-integer synthetic cases through L=400 (some weights exceed 64 bits). All assertions returned ALL_CHECKS_PASS. The bundled standalone JavaScript file adds 1,364 deterministic safe-integer cases (528 exhaustively compared; 836 against full DP), also ALL_CHECKS_PASS.

At n=8, aab has 60,590 distinct complete native observer states and aba 60,550; there are 1,287 quotient W rows per gate. Across the four tested widths, the optimal partition improves 1,260 of 5,148 aab row-width cases and 1,308 of 5,148 aba cases. For aab, uniform versus optimum aggregate support calls are 64,918 versus 58,371; for aba, 66,152 versus 58,969. These are weighted oracle-call counts, not wall-clock timings.

Local Python microbenchmark for L=2,000,b=64, one run per method on the same deterministic row: predecessor full-grid DP used 2,000,744 transition cost evaluations, 7.75784 seconds, 3,083,156 bytes peak tracemalloc; slack–Monge used 6,438 evaluations, 0.027707 seconds, 176,388 bytes tracked peak. These measured times and bytes are environment-specific. The exact numeric bench JSON and full native Python program are preserved in the separately attached evidence bundle.

Novel contribution is the BRC-specific slack-coordinate reduction plus explicit Monge identity and tested optimizer, not a claim to have invented generic Monge DP. Classical method: CP-Algorithms, Divide and Conquer DP, https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html ; Aggarwal, Klawe, Moran, Shor & Wilber, Algorithmica 2 (1987), doi:10.1007/BF01840359.

## Next question

PREFIX-507: aggregate PREFIX-500's mod-12 support formula over an entire V interval to avoid all L individual support queries during W-row index construction; cross-check exact interval sums against complete V enumeration n<=9. The current PREFIX-506 improves the optimal-boundary planner while the overall explicit support acquisition of the current rank index remains O(n^6) across all quotient rows. Independent mathematical review and formal project acceptance remain open.
