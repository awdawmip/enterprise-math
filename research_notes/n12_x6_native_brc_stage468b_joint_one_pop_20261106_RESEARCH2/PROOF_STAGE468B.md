# Stage468-B — exact joint P-POP/Q-POP/Q-APPEND classes over full ternary X6 fibers

Date: 2026-11-06. Status: AUTHOR_SIDE_PROOF, FINITE_EXHAUSTIVE_CHECKED, UNREVIEWED.
Predecessor: Stage467-B, source commit 397434d3ed8260064c3cda10645c10d47df59c70.
Frozen scientific source pins carried unchanged: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Behavioral rules are read at their current canonical snapshots, separately.

## 1. Model and observer

Take the native six-axis signed-step alphabet D={+E_i,-E_i:1<=i<=6}; original historical words P,Q are over the ternary subset Sigma={A=+E1,B=+E2,C=+E3}, with 2<=m=|P|<n=|Q| and P_1=Q_1=A. Distinct source histories retain their order, branch identity and unit positive BRC weight.

The complete initial/future observer Phi consists of both path lengths, both native signed six-component displacements, both directed 12-by-12 adjacent-step count matrices, and K(P,Q)=sum_{i<=min(|P|,|Q|)}[P_i=Q_i].

Allowed actions are P-POP at most once, Q-POP at most h times (0<=h<=n), Q-APPEND at most once with a chosen label u in all twelve D, in arbitrary legal order. A POP of an appended direction consumes a Q-POP budget. One compares the entire labeled tree of intermediate Phi observations, not only the final state.

Set t=max(1,n-h), and retain the Stage467-B Q-only repair word

Lambda_h(P,Q)=(Q_t, ((P_j,Q_j) for t<j<=m), (Q_j for max(t,m)<j<=n))

in increasing position order, with only Q_j for j>m. Define the extra POP repair

R_468(P,Q)=(Lambda_h(P,Q), P_{m-1}, e_m if t>m else empty),

where e_m=[P_m=Q_m]. Every quantity is a label of original ordered sources, not a quotient of their multiplicities.

## 2. Theorem — exact complete joint-future equivalence

For any fixed nonempty initial complete-observer fiber F, and any H,H' in F,

H ==_future H'  iff  R_468(H)=R_468(H').

### Necessity

1. The subtrees leaving P untouched are exactly the Q-POP/Q-APPEND futures of Stage467-B, so they distinguish Lambda_h.
2. The initial P first letter is fixed as A. From the directed-edge matrix, the imbalance out(x)-in(x)=[x=A]-[x=P_m] determines the original last direction P_m on the initial fiber. P-POP changes the directed-edge matrix by minus the single ordered edge (P_{m-1},P_m); hence the full future tree distinguishes P_{m-1} (also for m=2, where it equals fixed P_1).
3. If t>m, Q cannot POP as far back as original index m. Performing P-POP before any Q operation changes K by precisely -[P_m=Q_m]=-e_m, identifying this additional bit. If t<=m, Q_m occurs already in Lambda_h and P_m is initial-observer-determined; e_m is thus already determined.

### Sufficiency

Fix Phi and R_468. The initial P observer, known P_m and P_{m-1} reconstruct the observer after an optional P-POP, including displacement and the removed directed boundary edge. All reachable Q observers and the original matching-number corrections along Q-POP, before P-POP, are determined by (Phi,Lambda_h) by Stage467-B. An appended Q direction u and its subsequent removal have action-known displacement and directed boundary contributions.

For the K correction when P has POPped, there are exactly three cases for the current Q position m:

(i) original Q_m is still present: subtract [P_m=Q_m], given by Lambda_h and known P_m when t<=m, or by e_m when t>m;

(ii) Q has been trimmed to original length m-1 and then APPEND_Q(u) occupies index m: subtract [P_m=u], known from the initial observer and the chosen action;

(iii) Q has length <m: subtract zero.

All new matching terms from Q-APPEND at a position j<=m, before or after P-POP, depend on P_j with j>t, already recorded in Lambda_h, except the fixed initial P_1=A if Q was emptied. The shorter P after POP simply omits j=m. Thus the complete labeled observation tree is a deterministic function of (Phi,R_468). This covers every interleaving, Q empty-path boundaries when h=n and negative appended native directions.

### Necessity of both new coordinates on actual fibers

Write source words with A/B/C symbols. With h=0, (m,n)=(4,5), Q=AAAAA and P_1=AABA versus P_2=ABAA share the same initial Phi and Lambda, but P_{m-1} is B versus A. POP_P separates the directed-edge observations.

With h=0, (m,n)=(3,4), P=AAA, Q_1=AABA versus Q_2=ABAA have equal initial Phi, Lambda=Q_4=A and P_{m-1}=A, yet [P_3=Q_3] is 0 versus 1. POP_P separates K. These witnesses certify the role of the additional boundary letter and match bit, each within the required exact observation fiber. Some individual coordinates may be determined automatically in particular fibers.

## 3. Positive BRC population and rank

Use the Stage467-B exact 25-counter additive state (P/Q ternary letter counts, two directed 3x3 edge matrices, K). Branch weight is the positive integer number of source-distinct ordered history pairs; class mass is M(lambda,z,b)=sum of hidden-path weights producing the complete Phi and repair R_468. No source branch is discarded when deriving Boolean support.

Extend the hidden-prefix transfer by a constant ternary tag for P_{m-1}, and, only when t>m, a single bit e_m computed at the original overlap column m. P_m is determined by the complete initial observer, so no independent key coordinate for P_m is needed. The visible-emission word is still scanned deterministically as in Stage467-B, while terminal support and population evaluate the additional tags. The number of possible tags is at most 3x2=6, independent of m,n,h. The predecessor bound O(n(n+1)^25) exact integer operations therefore remains polynomial for this fixed ternary input alphabet, up to a constant state multiplier and boundary handling. Lexicographic rank/unrank uses suffix support counts for the ordered pair (visible emissions, tags), and mass queries use the positive transfer count. This is a mathematical algorithm extension, not a claim that a large-case optimized implementation was executed in this run.

For every fiber, sum_R M(R)=|F|, by disjoint grouping of original ordered histories; q_F=sum_R [M(R)>0].

## 4. Executed verification and closed forms

The companion exact Python program enumerates every original history and every full initial-observer fiber for (m,n)=(2,3),(2,4),(3,4),(3,5),(4,5),(4,6); for each h=0..n it compares every distinct pair in each fiber through the entire legal action tree, using all twelve signed Q-APPEND labels and all legal POP interleavings. 33 configurations, 53,473 fiber-configuration count checks, 1,538 same-repair pairs and 12,789 different-repair pairs passed all assertions. An independent small-instance checker was not used: the future-tree comparisons and repair-key assertions are in one transparent script; the analytic proof above provides the independent logical basis. The full local executed JSON is reproducible from STAGE468B.py; a concise true subset is saved as STAGE468B_EXECUTED_SUMMARY.json.

Two exact unbounded-parameter subfamilies provide large integer checks without history enumeration:

(a) P=A X_1 A X_2 ... A X_k A, X_i in {B,C}, exactly b of the k variables B; Q=A^n with n>2k+1 and h=0. The fixed initial fiber consists of all binomial(k,b) choices, with just two repair classes for 0<b<k according to X_k; their masses are binomial(k-1,b-1) and binomial(k-1,b). For k=50,b=23,n=110, the masses are 49,699,896,548,176 and 58,343,356,817,424, totaling 108,043,253,365,600.

(b) P=A^m, Q=A^(j-1) B A^(n-j), j=2..m, 3<=m<n, and h<n-m. The complete initial observer is fixed across j: one AB and one BA edge, one mismatched overlap position. Lambda and P_{m-1} are fixed, while e_m distinguishes j=m from the m-2 choices j<m. This gives exactly 2 classes of masses 1 and m-2. For (m,n,h)=(64,80,15), those masses are 1 and 62.

These closed forms and the 33 finite configurations are separate checks of different parts of the exact theorem. Full code and summary counts are retained as source; subsequent independent Driver review and any Source Result are separate operations.

## 5. Next question

Stage469-B: allow one native P-APPEND, with P-POP<=1, Q-POP<=h and Q-APPEND<=1. Determine which Q-original boundary letters become visible to the P probe and how an appended P letter changes the P-POP boundary observer. Derive a precise distinguishing repair key and adapt the positive-integer transfer, then compare complete short-fiber trees over all twelve signed APPEND choices on both sources.
