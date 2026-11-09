# R680｜原子事件时间下的最小整数优先级与顺序记忆

Date: 2026-11-10 Asia/Shanghai. Author-side finite exact research. Task lineage: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW / TP2-47D65B35A7D48082EFBB. Frozen scientific pin: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Predecessor: R679@fab76ba01a87745b098ab57a0219d958707bdbb9.

## 1. Declared model

One shared Cell o is embedded in native six-axis X6. Four internal field/port labels are not native spatial axes. The 20 active triads S are the 3-subsets of {0,...,5}, encoded by the four V23 perfect-matchings into distinct c(S) in {-1,0,1}^4 as specified by R679. Allowed successors T share exactly two axes with S. On the V29 nonnegative-count ledger, set A=PASS(o;0→1), B=PASS(o;1→2), C=PASS(o;2→0). At every primitive event time update u=(M−Mᵀ)1+Rin−Rout, Ω=M−Mᵀ and score Φ(S,T)=u·c(T)+c(S)ᵀΩc(T).

Fix each of R679's six L1=19 baseline biases, and perform all 6 permutations of A,B,C. This gives 36 positive unit-weight, label-distinguished BRC event histories, each with four prefix states. Baseline V27 successor maps and completed-batch maps are strict, whereas each middle prefix contains tied maximizers.

## 2. Theorem A: exact minimum contextual covector

Let P be the union, across all 36 histories, four prefixes and twenty source triads, of unordered pairs {T,T'} tied at maximal primary score. Exact enumeration gives |P|=30; the largest winner set has size 3. A fixed integral priority covector w∈Z^4 resolves all these ties precisely when w·(c(T)−c(T'))≠0 for every pair in P.

Complete integer L1 shell enumeration yields counts (shell size / number of admissible covectors):
0: 1/0; 1: 8/0; 2: 32/0; 3: 88/0; 4: 192/0; 5: 360/12.
Thus min ||w||_1=5, with exactly 12 minimizers enumerated in the evidence. For example w=(-1,1,-2,-1) works. Three co-maximizer differences are (-1,0,1,0), (-1,1,0,0), (0,1,-1,0), requiring w_0,w_1,w_2 to be pairwise distinct. The full finite search establishes all remaining low-norm cases. Across 36 histories, the total number of source triads with a tie is 108 at prefix 1, 108 at prefix 2 and zero at prefixes 0 and 3.

The L1 optimization quantifies an integral contextual covector in this specified normalization; it is not a physical count of transfers or an unconditional minimal information state.

## 3. Theorem B: everywhere strict primitive-time selector

Choose w=(-1,1,-2,-1). Across all 20 V23 codes its readout r(T)=w·c(T) lies in [-3,3]. Define the integer update score Ψ(S,T)=7Φ(S,T)+r(T). If Φ(S,T)>Φ(S,T'), the integer primary gap is at least 1; the secondary difference has magnitude at most 6, hence Ψ(S,T)>Ψ(S,T'). Within a primary co-maximizer set, all secondary readings differ by the 30-pair certificate. Therefore every prefix of every declared history has exactly one Ψ-maximizing neighbor at every source triad, and whenever Φ was strict, its winner is unchanged.

For this w, multiplier 7 is sharp for preserving every strict pairwise primary preference across the declared prefix/neighbor domain: K=6 fails for bias (-4,-3,-2,10), history ABC, prefix 2, source 023. Candidate 012 has primary score 1 above 025 but secondary score 6 below; multiplying Φ by 6 creates equality. An exact checker verifies K=7 against every scored pair.

## 4. Theorem C: final ledger does not determine time-resolved future

Fix one baseline u, starting triad S and the chosen w. For each of six PASS orders, update the V29 ledger after each event, then send the current triad along the unique Ψ winner, preserving primitive event time. This is a deterministic triad-update rule *conditional on the supplied PASS order*. The final V29 M,u,Ω are equal for all six event orders, because their additive event multiset is identical.

Exact computation of 6 biases × 20 initial triads × 6 event orders = 720 trajectories gives the histogram, over 120 (bias,starting-triad) cases, for the number of distinct final triads across six orders:
1 distinct: 59; 2: 29; 3: 27; 4: 5.

Witness: bias (-4,-3,-2,10), starting triad 012. Final outputs ABC→034, ACB→123, BAC→025, BCA→123, CAB→123, CBA→123. Thus equal completed V29 ledgers can have different event-time futures after consistent deterministic updates. The observer-safe BRC carrier retains the labeled PASS history or a certified sufficient residual together with the active triad/frame.

## 5. Typed covariance, validation and next question

Under an allowed typed field relabeling with c'(gT)=P c(T), u'=Pu, Ω'=PΩPᵀ and contextual priority w'=Pw, the exact identity Ψ'(gS,gT)=Ψ(S,T) holds. The covector must transform together with the field types. This is a conditional theorem about the transformed model, not a claim that the fixed oriented event grammar ABC is invariant under every rotation.

R680_VERIFY.py uses independent integer and set enumeration of V23 encodings, V27 scores and V29 primitive increments; it enumerates all 30 tied pairs, all 681 covectors of L1≤5, and 720 time-resolved paths. The output R680_EVIDENCE.json is a finite exact certificate. The project mother objective remains open: derive an event scheduler from source-backed local X6 relations, and combine the slot frame h, V39 loop current j, ledger and typed priority into a minimal future-sufficient autonomous state. Frozen scientific inputs and independent Driver review remain distinct from this author-side proof.

Sources: R679 exact proof and checker at immutable fab76ba01a87745b098ab57a0219d958707bdbb9; X6 V27 and V29 original notes at current project control snapshot; locked P000 and current BRC observer-preservation policy.
