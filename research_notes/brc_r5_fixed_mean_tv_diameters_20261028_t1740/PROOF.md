# R5 — Exact simultaneous two-measure TV diameter at a fixed likelihood-ratio mean

Author-side portable research, 2026-10-28. Role label LOCAL_EM_R5_20261028_1740_FIXED_MEAN_TV / TASK_RESEARCH (not a native session). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen inputs: global knowledge main@4e6b4b7e39335bb344269a4ca6db242ba6ad5f3e; Enterprise Math main@62dde0f7f44a19deb06d4ccac4bd2e3249a59c10. P000, ACTIVE worldview, native observer-preservation, current research operation and portable research protocols read. Native owner lookup returned CONTROL_QUOTA; no formal CLAIM, Result or review is inferred. This is a portable nonadmitted research note.

Predecessor: research_notes/brc_r5_npoint_middle_tv_20261028_t1640/RESEARCH.md proved the sharp *ratio* bound (s2/r)d_Q <= d_P <= (s[n-1]/r)d_Q. Here we compute sharp absolute diameters at a specified parent ratio r.

## Theorem

Fix n >= 3, 0 < s1 < ... < sn, s1 < r < sn. Two hidden histories with common parent likelihood ratio r have Q-conditionals q^a,q^b with sum_i q_i = 1 and sum_i s_i q_i = r. The corresponding P-conditionals are p_i = (s_i/r) q_i. Write d_Q = TV(q^a,q^b) and d_P = TV(p^a,p^b), with TV(u,v) = (1/2) sum_i |u_i-v_i|.

Define

    R_Q = min(1, (r-s1)/(s2-s1), (sn-r)/(sn-s[n-1]))
    R_P = min(1, s2*(r-s1)/(r*(s2-s1)),
                s[n-1]*(sn-r)/(r*(sn-s[n-1]))).

For all real conditional kernels, 0 <= d_Q <= R_Q and 0 <= d_P <= R_P.

**Simultaneous sharpness:** one pair of possibly sparse conditional kernels attains *both* bounds. If every Q/P conditional entry must be strictly positive, a single family of pairs approaches both bounds simultaneously, with exact values (1-epsilon)R_Q and (1-epsilon)R_P for every epsilon in (0,1). Rational s,r and rational epsilon admit rational positive witnesses. The extremum is a supremum, rather than generally a maximum, on the strict-positive class. For n <= 2, same normalization and first moment force the two kernels to coincide, so d_Q=d_P=0; a strictly positive n>=3 law requires s1<r<sn.

Equivalently: if r<s2, the diameter pair is ((r-s1)/(s2-s1), s2*(r-s1)/(r*(s2-s1))). If s2<=r<=s[n-1], it is (1,1). If r>s[n-1], it is ((sn-r)/(sn-s[n-1]), s[n-1]*(sn-r)/(r*(sn-s[n-1]))). For n=3 the middle interval is the single point r=s2.

## Complete algebraic proof

For two probability laws u,v, TV(u,v)=1-sum_i min(u_i,v_i).

When r<s2, every admissible Q law obeys r=sum_i s_i q_i >= s1*q1+s2*(1-q1), hence q1 >= (s2-r)/(s2-s1). Any two such laws have at least this much overlap at index 1, giving d_Q <= (r-s1)/(s2-s1). When r>s[n-1], every Q law obeys q_n >= (r-s[n-1])/(sn-s[n-1]), so d_Q <= (sn-r)/(sn-s[n-1]). In the middle interval, d_Q<=1.

For P, normalization gives sum_i p_i=1 and the reciprocal-moment condition sum_i p_i/s_i=1/r. If r<s2, then 1/r <= p1/s1+(1-p1)/s2 and therefore p1 >= s1*(s2-r)/(r*(s2-s1)). The resulting common overlap gives d_P <= s2*(r-s1)/(r*(s2-s1)). If r>s[n-1], then 1/r >= p_n/sn+(1-p_n)/s[n-1], so p_n >= sn*(r-s[n-1])/(r*(sn-s[n-1])); hence d_P <= s[n-1]*(sn-r)/(r*(sn-s[n-1])). In the middle interval, d_P<=1.

To achieve both bounds, let b^(i,j) denote the two-point Q law on signatures i<j bracketing r, with b_i=(s_j-r)/(s_j-s_i) and b_j=(r-s_i)/(s_j-s_i).

- If r<s2, compare b^(1,2) with b^(1,n). Their only overlapping index is 1. Its minimum Q and P masses exactly match the preceding mandatory-overlap bounds.
- If r>s[n-1], compare b^(n-1,n) with b^(1,n). Their only overlapping index is n; both bounds are attained.
- If s2<=r<=s[n-1] and n>=4, compare b^(1,n-1) with b^(2,n). Their supports are disjoint, so both TVs are 1, including degenerate endpoint weights.
- If n=3 and r=s2, compare b^(1,3) with the point mass at index 2. Again both TVs are 1.

These four cases cover the entire admissible range. For strict positivity, take any common strictly positive Q baseline q^0 with sum 1 and mean r (such a law exists since s1<r<sn); replace both extreme laws q^c by (1-epsilon)q^c+epsilon*q^0. Every Q entry, and therefore every P entry, becomes strictly positive; difference vectors scale exactly by (1-epsilon). Rational baseline and rational epsilon give rational witnesses. This proves simultaneous sharpness over all real kernels. QED.

## Exact witnesses and numerical meaning

For s=(1/2,1,2,3) the sharp (R_Q,R_P) pairs are: r=3/4 -> (1/2,2/3); r=3/2 -> (1,1); r=5/2 -> (1/2,2/5). A shared rational baseline with epsilon=1/100 gives strictly positive pairs with exact TVs (99/200,33/50), (99/100,99/100), and (99/200,99/250), respectively. For n=3 at r=s2, both suprema equal 1.

VERIFY.py was run with Python fractions.Fraction, validating the constructive boundary and positive witnesses, exact P and Q normalization, and 3278 pairs drawn from explicitly finite strictly positive rational grids for n=3,4,5,6. EXACT_OUTPUT.txt records the output. These finite calculations validate their declared examples only; the all-real assertion follows from the proof above.

## BRC reuse and predictive-budget corollary

BRC REUSE_APPLIED: positive rational branch masses, hidden-source provenance, exact P/Q likelihood-ratio transport, signed zero-mass/moment residual, and TV observer. Keep the source-tagged laws; the TV observer loses sign and source information. Let F be a hidden-source fiber with common parent ratio r_F and a common ordered union s(F) of possible successor likelihood ratios. Taking maxima over pairs gives delta_F^Q <= R_Q(r_F;s(F)) and delta_F^P <= R_P(r_F;s(F)), regardless of source count. For an occupation-weighted budget epsilon_t^mu = sum_F C_F^mu*delta_F^mu with C_F^P = r_F*C_F^Q:

    epsilon_t^Q <= sum_F C_F^Q * R_Q(r_F;s(F))
    epsilon_t^P <= sum_F r_F*C_F^Q * R_P(r_F;s(F)).

These are a priori algebraic caps on the existing TV budget, independent of a new global sequential-coupling proof. They do not imply equality of the four-dimensional full-history and seedless-LR behavioral images.

External prior-art context: Charalambous, Tzortzis, Loyka & Charalambous (2013), "Extremum Problems with Total Variation Distance and their Applications," https://arxiv.org/abs/1301.4763, studies TV extrema with linear functional constraints in broad settings. This note makes no claim of historical priority or a completed novelty audit.

Scope: external finite two-measure statistics; embedding into Heartbeat World's six-dimensional native discrete spatial Cell state and separately typed time, preserving future-observer and joint-relation semantics under P000, remains a separate problem. Probabilistic signature indices are not native spatial axes.

**Next:** classify the exact feasible *joint* region of (d_Q,d_P), rather than intersecting the ratio wedge with independent diameter caps, and use its certificates to screen interacting two-nonterminal-collision rational trees before full signed-support equality testing.