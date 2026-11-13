# Stage447-B — Polynomial exact output-word quotient and positive BRC class populations

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Parent Stage446-B: `31d442684cab3565af2056b2aaa7710a79689704`.
Frozen scientific input: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.
Current normative context was separately resolved from canonical main (2026-11-05).

## Domain and observer

The full native X6 signed direction domain is D={±E1,...,±E6}. Restrict **initial source histories only** to two distinct native directions A=+E1, B=-E1. Let 3≤m<n. P in {A,B}^m and Q in {A,B}^n, with A at both ends of each full original history and no adjacent B. Fix defect numbers kP,kQ and overlap disagreement d=m-K. Therefore the complete present observer O=(m,n,V_P,V_Q,J_P,J_Q,K) is constant within the declared fiber F: V_X=(length-2k_X)E1, J_AA=length-1-2k_X, J_AB=J_BA=k_X, J_BB=0. Here J is the complete ordered native adjacency histogram (all other entries zero).

Future controls: Q is immutable; P may perform 0 to r≥1 labelled APPEND operations, any selected direction z in all 12 original native directions, with the full observer recorded after every prefix. No POP in this theorem. Let ℓ=min(r,n-m), t=n-m-ℓ and W(Q)=Q_(m+1)...Q_(m+ℓ).

## Theorem 447.1 — Exact minimal future equivalence

For any H=(P,Q), H'=(P',Q') in F,

    H ≡_r H'  iff  W(Q)=W(Q').

In particular q_F is exactly the number of feasible length-ℓ binary output words. The minimal fixed-width category label has ceil(log2 q_F) bits (q_F>0). This holds also for r>n-m: observable matching saturates after the shorter Q ends.

**Proof.** Every P history in F ends in A. Given a labelled future appended sequence (z1,...,zs), the evolved P endpoint and its directed J arise from O, A and the labelled appended sequence. Q stays fixed. At step s its positional match statistic is exactly

    K_s = K_0 + Σ_(i=1)^(min(s,n-m)) [z_i=Q_(m+i)].

Equal W gives equal K after every step for every labelled action word; all other observer fields also agree. Conversely take two differing W and their first difference j≤ℓ. Choose arbitrary valid actions through j−1 and choose z_j=Q_(m+j). At step j the increment in K differs (the previous j−1 increments are equal), so the full trace distinguishes the histories. This is a typed finite-horizon future-observer factorization certificate. QED.

## Theorem 447.2 — Polynomial positive-mass support without enumerating classes

Define integer T(b,v) = number of length-m paired prefixes satisfying P's A endpoints, Q_1=A, neither source has adjacent B, P has exactly kP defects, overlap disagreements exactly d, and Q prefix contains b defects with last indicator v=[Q_m=B]. Each paired prefix has unit positive BRC branch population; each unique path contributes exactly one. Compute T by the integer transfer states (i,a,b,h,u,v), where a,b count Bs in the two prefixes, h the disagreements and u,v their previous-B bits. At position i choose s,t∈{0,1}, reject forbidden endpoints/consecutive B and increment the unique successor (a+s,b+t,h+[s≠t],s,t).

For a fixed output word w of length ℓ with s(w) Bs, first bit f and last bit v, let U_t(v,R) be the number of legal Q tails of length t, ending in A at full position n, containing R Bs and disallowing BB against previous v (for t=0: U_0(v,R)=[v=0][R=0]). Then the exact raw-history **population of the future class w** is

    M(w)= Σ_(b,q) T(b,q) · [not(q=f=1)] · U_t(v,kQ-b-s(w)).

All factors are nonnegative integers. Importantly M(w) depends only on the triple (s(w),f,v), not on the placement of the interior Bs. This is a population identity, not a quotient of branch provenance.

Count all binary w of length ℓ with no adjacent Bs by a deterministic weighted automaton with state (j,s,f,v), transition A or allowed B and integer path count W_(j,s,f,v). Each word follows exactly one path. At j=ℓ, keep the state iff M(s,f,v)>0. Then

    q_F=Σ_(s,f,v) W_(ℓ,s,f,v) [M(s,f,v)>0],
    |F|=Σ_(s,f,v) W_(ℓ,s,f,v) M(s,f,v).

Thus distinct word support is counted without enumerating exponentially many original histories or output classes. Reverse suffix support counts provide lexicographic rank and unrank of any supported w. T, the U tails and W determine each class population on demand. Given a specified w, an integer prefix-and-suffix DP with forced Q window enables within-class original-history ranking, unranking and full reconstruction, retaining source order and provenance.

**Complexity.** Let H=4(kP+1)(kQ+1)(d+1), N=n. T costs O(mH) integer additions, U costs O(t(kQ+1)), the output support automaton and suffix support cache cost O(ℓ(kQ+1)), and terminal class-mass support for all summaries costs O((kQ+1)^2) integer multiply-adds. Consequently O(mH+n(kQ+1)+(kQ+1)^2) exact integer operations and O(H+n(kQ+1)) integers suffice for counting and implicit rank/unrank preprocessing. Per-class population query costs O(kQ+1) after preprocessing or O(1) with terminal-mass caching; lex rank/unrank each takes O(ℓ) big-integer comparisons/additions. Since |F|≤2^(m+n), all populations and support counts have O(N) bits; multiplying two O(N)-bit integers must be included in bit complexity, so an O(N^2) elementary bit-cost upper bound per multiplication is safe. Initial input/schema parsing is O(N), and full history recovery requires Θ(m+n) output symbols plus its O(nH) completion preprocessing. A fixed-width class code uses ceil(log2 q_F) bits; the class rank does not reconstruct the raw history without a within-class rank.

## Strict Stage446-B key extension witness

P=AABAA (m=5,kP=1); Q1=AAAAAABABAA and Q2=AAAAAAABABA (n=11,kQ=2).
Both have d=1, K0=4, identical V and complete directed J, and Q1_6=Q2_6=A. Thus Stage446-B's one-letter key cannot distinguish these histories. But Q1_7=B versus Q2_7=A. A labelled P:APPEND(A), P:APPEND(B) trace yields K2=6 for Q1 and K2=5 for Q2. Hence the two-letter window is genuinely necessary when r=2.

## Executed evidence and scope

`REPRO_STAGE447B.js` uses JavaScript BigInt only. Run `node REPRO_STAGE447B.js` for the complete reproducible JSON result. The exact checker exhausts 1,728 small parameter/budget cases, 550 nonempty fibers, 2,150 original-history instances, 670 class mass checks and 670 lex rank roundtrips; r>n−m saturation occurs in 576 cases. Four independent full-future scenarios enumerate all 12 signed APPEND directions and every labelled action prefix, producing 10,210 full-observer prefix checks across 10 history trees. All tests passed. A larger implicit computation at (m,n,kP,kQ,d,r)=(64,80,15,17,1,12) gives q_F=188 and |F|=5061384194832966, with exact category population histogram in the JSON. General claims follow from the stated bijections/recurrences; finite tests exercise implementation and observer matching.

This is a static X6 ordered-history BRC positive-integer branch observer, not a physical heartbeat evolution, time calibration, phase-cancellation inference, or authorization of a formal Source Result.

## Next

Stage448-B: allow one asymmetric P POP before APPEND. Seek an exact key containing the newly exposed P suffix and a Q alignment window, with a shortest full-observer trace to test attempts to merge states. Derive an implicit class support DP and assess any boundary-state explosion; preserve source-specific integer populations and the frozen pins.
