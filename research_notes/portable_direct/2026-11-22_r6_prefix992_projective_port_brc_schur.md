# PREFIX-992 — Exact projective-history compression for positive BRC port feedback

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.
Research: independent portable continuation of PREFIX-991, without shared Task CLAIM.
Scope: finite named-edge graphs with positive rational historical weights and BRC histogram readouts. An explicit Schur-complement recurrent-port module is coupled to the frozen auxiliary signed-source bit-flip observer. This is not an identification with native X6 Cell/Link/Port dynamics.
Frozen P000 scientific premise: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (V5).
Sources: PREFIX-989, PREFIX-990, PREFIX-991, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md (WBRC-T30/T31); definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md (WBRC-T36/T37); definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json.

## Exact problem

Let S be a finite state set and E an alphabet of **named** legal edges a:s→t with a positive source factor v_a. Each edge exposes an output port j(a) in a finite set J, and eligibility and target depend on s and a, not on the preceding port. Let g(h,a)>0 be the rational weight of traversing a after incoming port h; the new port becomes j(a). The desired observer is the full exact positive-rational weight histogram, indexed by source and endpoint states, starting history h and terminal port j, for every fixed path length. Under WBRC-T36 this is the semiring H=N[Q_{>0}^×], with multiplicity-preserving addition and weight-multiplying convolution.

PREFIX-991 handled the rank-one history law g(h,a)=u_h v_a. Here the dependence on h can be **nonseparable globally**, but its rows can occupy a small number of *positive projective classes*.

## Theorem 992.1 — projective-history boundary transfer

Assume there exist a map κ:J→C, positive rational scalars ρ_h, and positive rational templates f_{c,a}, such that for every relevant pair

    g(h,a)=ρ_h f_{κ(h),a}.                                  (992.1)

Define an H-weighted transfer matrix M on S×C:

    M[(s,c),(t,c')] =
      Σ_{a:s→t, κ(j(a))=c'} [ρ_{j(a)} f_{c,a}].           (992.2)

Let M_j retain only terms in (992.2) whose named source a has j(a)=j. For n≥1, the exact endpoint/terminal-port histogram satisfies

    K_n^{h,j}(s,t) =
      [ρ_h/ρ_j] (M^{n-1} M_j)[(s,κ(h)),(t,κ(j))].        (992.3)

For n=0 set K_0^{h,j}(s,t)=δ_{st}δ_{hj}[1]. Any two segments glue exactly through the **actual** terminal port:

    K_{n+m}^{h,k}(s,t) =
       Σ_{y∈S,j∈J} K_n^{h,j}(s,y) K_m^{j,k}(y,t).         (992.4)

These formulae preserve fixed-length counts, exact weight histograms, nonnegative masses, every integer moment, dominant weight with multiplicity, and endpoint-port composition within this declared observer. Intermediate history requires only |C| projective classes rather than |J| ports. The external terminal-port interface is still retained.

**Proof.** Let a_1...a_n be a valid named path with ports j_1,...,j_n and put j_0=h. Its original chronological weight is

    Π_{r=1}^n ρ_{j_{r-1}} f_{κ(j_{r-1}),a_r}
      = (ρ_h/ρ_{j_n})
        Π_{r=1}^n ρ_{j_r} f_{κ(j_{r-1}),a_r}.             (992.5)

The rightmost product is precisely the path contribution in M^{n-1}M_{j_n}; the prefactor is endpoint-only. Every named path is counted once; equality holds in H (not merely after taking first moments). A unique split at the original boundary state and actual port proves (992.4). The empty path identity is explicit. QED.

## Theorem 992.2 — canonical class count within row-scaling transfer factorizations

Suppose g(h,a) is specified for every h in J and a in one common nonempty named-edge alphabet A. Two histories h,k may belong to the same template class in (992.1) if and only if their positive rational rows are proportional:

    g(h,a)g(k,b)=g(h,b)g(k,a) for all a,b∈A.             (992.6)

Consequently, the number of distinct positive projective row classes is the least |C| among factorizations (992.1) over the complete common alphabet. Choose one representative per class and use ratios of any nonzero entry to obtain ρ_h; all entries here are strictly positive. This statement concerns the specified factorization family, not an unrestricted minimal weighted automaton or a claim that every actual state exposes all letters.

**Proof.** A shared template immediately implies (992.6). Conversely (992.6) makes every coordinate ratio g(h,a)/g(k,a) independent of a; choose the class representative as f and that positive ratio as ρ. Histories with nonproportional rows cannot share a template. QED.

## Typed recurrent BRC example (not a synthetic arbitrary weight table)

Use six visible ports J={0,1,2,3,4,5}, two hidden states, B=0,
A=diag(1/2,1/2), and X=(1/100) times the two rows

    (1,2,1,3,2,4)
    (2,1,3,1,4,2).

Set the six rows Y_h=(ρ_h/100)e_{κ(h)} with

    κ=(0,0,1,1,0,1),    ρ=(1,2,1,2,3,3).

The hidden block is stable. The WBRC-T30 Schur kernel is exactly

    W_eff=B+Y(I-A)^{-1}X,
    W_eff(h,j)=ρ_h Xnumerator[κ(h),j]/5000.             (992.7)

Take the chronological historical feedback law

    g(h,a)=W_eff(h,j(a)) v_a,
    v_a=2 for sign(a)=+1, v_a=3 for sign(a)=-1.          (992.8)

The two template rows are nonproportional: at ports 1 and 2 their cross-products are 2·3=6 and 1·1=1. Exactly TWO projective classes are required in (992.1), versus SIX raw preceding ports. Here f_{c,a}=Xnumerator[c,j(a)]v_a/5000. The model genuinely composes a canonical positive rational recurrent BRC module with an auxiliary named-source observer; it is not a claim that native X6 has precisely these feedback coefficients.

The obstruction is directly visible in the first auxiliary source word at state (phase=0,x=5): sources (0,1,2,-1) and (0,3,1,+1) are both eligible. For histories 0 and 2, the kernels at output ports (2,1) are respectively (1/5000,2/5000) and (3/5000,1/5000). Their row ratios differ. Thus treating both projective classes as one history template would change the two-source relative weights.

## Exact certificate and coverage

Signed-source inputs are the same frozen auxiliary construction as PREFIX-991: sources a=(q,i,j,sign), with c_q=2^i−sign·2^j, odd input x, legal when bit_j(x)=(1−sign)/2 and flip x↦x XOR 2^j. A standalone Python checker reconstructs the graph, constructs the rational Schur kernel, computes direct history-augmented histograms and projective-class delayed histograms, and compares every coefficient (endpoint state, last port, exact path weight, multiplicity).

Tested source words: (6,24,6,−3) at width 6 and (6,24,8,40) at width 7. For each word, all active-bit initial phase-zero states, all six initial-history ports, every length 0 through 12, and gluing splits (1,1),(2,3),(3,4) were checked with Python Fraction and integer Counter.

- First word: 16 initial states, 64 reachable old states. At length 8: 96 paths, total mass 122229/61035156250000000000000000, 23 exact weights. At length 12: 240 paths, 38 exact weights.
- Second word: 32 initial states, 120 reachable old states. At length 8: 84 paths, total mass 3483891/762939453125000000000000000, 15 exact weights. At length 12: 48 paths, 7 exact weights.

Theorem 992.1 is analytic for arbitrary finite graphs satisfying (992.1); these runs check two declared graph families and one explicit stable recurrent-port module. File PREFIX992_R6_BRC_PROJECTIVE_ROWS_CHECK.py is the complete executable checker, and PREFIX992_R6_EXACT_RESULTS.json records exact numerical outputs. Mathematical independent review remains NOT_REVIEWED.

## Information-preservation scope and next problem

The compressed transfer conserves the exact positive histogram with endpoint and last-port observations and concatenation. It does not itself identify named internal source words or signed/amplitude cancellation; the original named edge graph remains the provenance source. Full X6 Cell/Link/Port state, triadic native relations, six spatial axes and separately typed time are not replaced by the auxiliary bit-flip graph.

Next: extract an actual native X6/BRC typed feedback observation and its allowed history/source pairs, and test whether its nonzero weight rows have a small projective partition. If no positive row factorization applies, seek the smallest exact future-observer state extension, with a counterexample for each unsafe collapse. The mother problem B_fix,odd(32)∈{19,20} remains open.
