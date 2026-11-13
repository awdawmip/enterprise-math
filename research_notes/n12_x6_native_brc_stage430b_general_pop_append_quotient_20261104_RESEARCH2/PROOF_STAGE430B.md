# Stage430-B — Exact p-POP / one-APPEND future quotient and a linear information lower bound

2026-11-04 | Research2 | AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific parent: Stage429-B at 05948084044a72e34bf4073c0bb8171240a35d3e.
Frozen scientific inputs: global main bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules have been separately read at 2026-11-04 main heads. The native X6 chart has six axes, twelve signed directions; this is a typed static path-observer problem with no new time axis or final Cell-address semantics.

## Model

D={+E1,-E1,...,+E6,-E6}; P and Q are ordered D-words of lengths m,n. Fix any integers p>=0, n>=p+1, m>=n+1. The complete observer is
O(P,Q)=(m,n,endpoint_X6(P),endpoint_X6(Q),J_P,J_Q,K(P,Q)),
where endpoints are signed six-component sums, J_s(u,v) counts each directed adjacent pair, and K=sum_{i=1}^{min(m,n)} [P_i=Q_i] at absolute 1-based indices. Include full observer traces and legality in future equivalence. P is frozen. Q may POP up to p times and APPEND(x) at most once, for arbitrary x in all twelve directions; arbitrary interleavings and partial words are permitted. No CANCEL or P edits.

## Theorem 430.1 (exact all-future quotient for every p)

Define
T_p(P,Q)=(Q_{n-p},...,Q_n ; P_{n-p+1},...,P_{n+1}).
For any two starting pairs with the same complete initial observer O, their complete future observer traces agree for every legal continuation if and only if T_p agrees. Thus each initial O fiber is partitioned exactly by its attained T_p values. In particular for p=2 the exact tuple is (Q_{n-2},Q_{n-1},Q_n;P_{n-1},P_n,P_{n+1}), and the proof applies even at m=n+1.

Proof — Sufficiency: At most p ORIGINAL Q symbols can be popped (possibly fewer if the single newly appended symbol is itself popped). A deleted original is among Q_{n-p+1}...Q_n; every deleted last edge has its predecessor among Q_{n-p}...Q_n. Thus the retained suffix and optional appended x determine all changes to Q endpoint and directed J. Only positions n-p+1 through n+1 can change their K contribution; the original P symbols at precisely those positions are retained. Q's symbol at each affected position is determined by the suffix plus x. All source lengths and POP legality are known. Each operation therefore yields the same complete next observer from the same current observer and retained tuple, and induction covers every legal word.

Necessity, p>=1: Observe POP^j for each j=1,...,p. Differences in Q six-vector endpoints identify, successively, Q_n,...,Q_{n-p+1}, since the twelve signed native directions are injectively encoded as six-component unit changes. At the p-th POP the unique edge removed from J_Q is (Q_{n-p},Q_{n-p+1}); its second entry has just been identified, so the first identifies Q_{n-p}. For each j=0,...,p and each x in D, observe POP^j followed by APPEND(x). The resulting K increment relative to the preceding POP^j state is [P_{n-j+1}=x]. All twelve singleton direction indicators uniquely identify P_{n-j+1}. This recovers every component of T_p. For p=0, APPEND(x) increments J_Q at (Q_n,x) and K by [P_{n+1}=x], recovering Q_n and P_{n+1}. QED.

This proves observer-safe future factorization within the exact operation language, including directed J, X6 endpoints, K, stepwise legality and source history multiplicity.

## Theorem 430.2 (attained 2^(p+1) lower-bound fiber)

For every p>=0 put L=p+1, n=L+2, m=5L+9, M=3L+3, R=L+1. Choose A=+E1, B=-E1, C=+E2. For each w in {A,B}^L let b(w) count Bs and r(w) count maximal consecutive B-runs. Set h=R-r(w)>=1 and z=M-b(w)>=h; define
V(w)=B^(z-h+1) (A B)^(h-1), t(w)=2+b(w)+r(w),
P(w)=A^3 w A V(w) A^t(w), Q=C^n.

Every P(w) has length m, M occurrences of B and R B-runs, starts and ends in A; consequently all share endpoint (m-2M)E1 and J_BB=M-R, J_AB=J_BA=R, J_AA=m-1-M-R (all other entries zero). All Qs coincide and K(P(w),Q)=0, hence all 2^L pairs lie in ONE full-O fiber.

For j=0,...,p, execute POP^j then APPEND(A). Original Q symbols all remain C, so the resulting K is [P(w)_{n-j+1}=A]. These positions sweep precisely 4 through L+3, the letters of w. The L legal probes recover the L bits of w. Thus all 2^L starting histories are future-distinguishable, establishing >=2^(p+1) states and >=p+1 binary bits for a fixed binary encoding on this fiber. For p=2 this supplies eight distinct histories and a three-bit lower bound. This is an order-sharp information-growth lower bound in p; T_p's 2(p+1) raw labels are a sufficient coordinate, not an asserted optimal per-fiber bit encoding.

## Exact executed verification

REPRO_STAGE430B.js directly constructs full signed X6 endpoints, 144-slot directed-J maps and positional K, enumerates every finite tested initial word pair and groups by identical full O. Each COLLIDING fiber pair is compared against every continuation, with APPEND ranging over all twelve native directions. For p=2 there are 75 possible continuations (including empty word), and for p=1 there are 38.

Test domains: p=2,n=3,m=4, input letters {A,B,C}: 2,187 histories; p=2,n=3,m=7: 59,049 histories and 37,206 colliding-fiber pairs (4,374 same-T pairs and 32,832 different-T pairs, all classified correctly); p=2,n=4,m=8, alphabet {A,B}: 4,096 histories; p=1,n=3,m=6, {A,B,C}: 19,683 histories. The program separately constructs the lower-bound family for p=0,...,7 and verifies 2 through 256 distinct future signatures within a common O fiber. Every arithmetic comparison is exact integer/word arithmetic. The finite checks are independent cross-checks; the general quantifiers are supported by the explicit proofs.

## Continuation

Stage431-B: allow TWO Q-APPENDs in any order with up to p POPs; test the candidate Q_{n-p..n} and P_{n-p+1..n+2} exact quotient, including appended-symbol POP interactions and arbitrary twelve-direction choices. In parallel, integrate indexed K updates into actual unequal-length Euler/J transfer and account for encoding, memo and output costs. This Stage430 author-side result is awaiting Source CLAIM/Result and independent Driver review.
