# Stage484-B — Arbitrary fixed nonconstant common X6 prefix: exact future key and Euler–BRC boundary law

Date: 2026-11-06. Research2 author-side mathematical argument and exact integer verifier; UNREVIEWED / NOT_ADMITTED.

## Sources, immutable scientific inputs and semantic scope

Parent: Stage483-B, PR #1736 at commit `d268ce509401af5940dd2faa10b7c3b2fd5d7976`. Preserve task-frozen scientific inputs GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current conduct and proof policies were read separately using GLOBAL main `74eac3180409934ec6e71119615f661aec3b93a0` and EM main `95fa835c4aafab4c3dc773caa4ae9b15fbba2d01`.

The ambient spatial substrate remains native X6: a chart-relative affine torsor over Z^6 with primitive signed steps `D={+E1,...,+E6,-E1,...,-E6}`; there are six axes and twelve directions, and no native two-dimensional plane. P000 and the observer-preservation contract remain unchanged. Fix an arbitrary **known nonempty** word T in D^m with m=2k+2, k>=1; T may be nonconstant and need not end in A=+E1. Let W in D^k and H in D^u, u>=1, and define

```
P=T
Q=T W A H A
```

An action is P_POP (when length>1), P_APPEND(d), Q_POP (when length>1), or Q_APPEND(d), with arbitrary d in all twelve signed native directions. Total budgets: P at most k POP and k APPEND, Q at most h POP and one APPEND, with arbitrary interleaving. The full observation at every step is (lengths, both signed six-coordinate displacements, both complete 144-type directed adjacency multisets, positional equality count K). The initial observer is fixed to one exact fiber; both histories have the same fixed T.

## Theorem 484.1 — Exact key for every fixed T

For any integers h>=0 and r=min(h,u), two histories in the same complete initial-observation fiber are equivalent under **all common legal future action words** if and only if

```
(W1, suffix_r(H1)) = (W2, suffix_r(H2)).
```

This includes all nonconstant T and all legal interleavings, including APPEND then POP. No new key coordinate is introduced by T's internal transitions or its terminal boundary.

**Sufficiency.** Both P paths start at identical T and undergo identical P operations, so their subsequent words agree and have length <=m+k. If h<=u, the Q side can POP at most h times, retaining the entire original prefix T W. Any prefix of Q of length <=m+k, thus every positional comparison with P, is determined by T, W and subsequent known Q actions. The full original Q directed-edge multiset and six-displacement agree by hypothesis. Every Q POP deletes the terminal signed letter and its incident predecessor→terminal edge, which are determined by the last A and the known suffix_h(H); any Q APPEND adds known direction and edge, and subsequent POP of that APPEND is also known. Hence all observed Q lengths, displacements, edge counts and K agree after every legal action. If h>u, the key contains all H; together with T and W this determines the complete original Q, so the same conclusion holds even for POP into the fixed separator or T.

**Necessity.** If W1!=W2, append all k directions of W1 to P, taking no Q actions. The P continuation equals T W1. Its new k positions agree entirely with Q1 but disagree in at least one position with Q2, giving a different K. If W agrees but the retained suffixes differ, choose the differing H letter nearest the right end, at distance j<=r, with all later H letters equal. Q_POP repeated j times first removes the known final A and the j-1 later H letters. The j-th deletion removes x→z in one history and y→z in the other with x!=y and the same right neighbor z. Previous deleted edges are equal, while the initial 144-edge multisets agree; therefore the resulting full directed-edge multisets differ. All j operations are legal because Q retains a long fixed prefix. Thus every different key has a separating legal future.

## Theorem 484.2 — Exact nonconstant-boundary Euler–positive-BRC populations

Write E(V) for the directed edge multiset of a word V and Θ=E(Q) for the fixed initial fiber. Since the first Q letter T_1 is known, Θ determines Q symbol counts by `count(v)=indeg_Θ(v)+[v=T_1]`; therefore the six-coordinate signed endpoint is already fixed within this edge fiber, although it remains explicitly observed. Initial K=m, because P=T and Q begins with T.

For W of length k let a=T_m, b=W_1, c=W_k and

```
B_T(W) = E(T) + [a→b] + E(W) + [c→A].
R_W    = Θ - B_T(W) = E(A H A).
```

This is the required new boundary repair: Stage483 used a constant T ending in A; here the single edge `a→b` must be retained. Negative residual entries make W inadmissible. For any directed-edge vector e, let N(ell,s,t,e) denote the number of length-ell vertex words beginning s, ending t, and using each edge exactly e times; N is an exact nonnegative integer computable by the directed Euler/BEST/matrix-tree formula of Stage483, or equivalently by prefix recurrence

```
N(1,s,t,e) = [s=t and e=0]
N(ell,s,t,e) = sum_{v:e(s,v)>0} N(ell-1,v,t,e-1_{s→v}).
```

For r=0, `M_R(empty)=N(u+2,A,A,R)`. For 1<=r<=u, let S be a length-r candidate suffix of H and set `R'=R-E(S A)`. Then

```
M_R(S) = N(u-r+2, A, S_1, R') if R' nonnegative, else 0.
q_R(r) = sum_{S in D^r} [M_R(S)>0].
```

The equality is bijective: a path `A V S_1` with `|V|=u-r` and remaining edges R' has a unique completion by the prescribed S suffix and final A. These populations count original source histories; support uses Boolean positivity. For the full Θ fiber:

```
q_Θ(r)    = sum_{W in D^k: R_W>=0} q_{R_W}(r)
|F_Θ|     = sum_{W in D^k: R_W>=0} N(u+2,A,A,R_W).
```

For efficient sparse counting, group W by its first/last letters and E(W), and multiply each grouped contribution by exact N(k,b,c,E(W)); the BRC reverse-residual automaton from Stage483 supplies q_R without expanding all 12^r suffixes. Lexicographic class rank/unrank follows prefix support counts. All numeric arithmetic is nonnegative integer; this is a positive multiplicity carrier, not signed-amplitude cancellation.

## Finite executed verification

The committed Python reproducer exhaustively enumerates W,H over {A=+E1,B=+E2,G=-E1} for four distinct fixed nonconstant T (ABGA, ABGB, GABA, BGAB), with k=1,u=2 and Q POP budget h=0,1,2,3. Its observer uses the full 12-direction, 144-edge, signed-six-component representation. For **every pair in the same full initial-observation fiber**, it synchronously explores all legal action sequences with 12-way APPEND branches, comparing the full observer after every operation. A second exact Euler prefix DP checks each class's raw population against direct enumeration.

Executed with Python standard library, 16 parameter configurations, 288 full-observer fibers (18 per configuration), 2,536 history-pair equivalence checks traversing 115,582 paired future states, and 408 class-population and sorted-key-index consistency checks. All assertions passed. The maximum initial fiber size is four and 24 compared pairs have distinct raw histories yet the same complete future key. For T=ABGA the four h budgets yield respectively 21,27,27,27 supported classes across the 18 fibers; for T=ABGB likewise 21,27,27,27. This finite execution independently checks examples; the all-k,u,T,h claim is supported by the written mathematical argument above.

Sample exact distinguishing witness in one initial fiber: T=ABGA, W1=A,H1=AB,Q1=ABGAAAABA and W2=B,H2=AA,Q2=ABGABAAAA; P_APPEND(A) separates K. Another same-W initial fiber has (W=A,H=AB) versus (W=A,H=BA); one Q_POP separates their last-H edge contribution. When T ends B, the boundary term is B→W_1, so substituting the Stage483 A→W_1 term would miscount classes.

## Research status and next question

Author-side proof and executed finite certificate, pending independent Driver review. The original mother objective is faithful compact state for native ordered X6 histories and future observers. Next Stage485-B: allow both Q_POP and **two Q_APPEND** (instead of one), with full legal interleaving. Decide by proof or shortest exact witness whether the same key survives, and characterize the smallest new boundary data for a variable (not fixed) common prefix or unequal P initial prefixes. Also test sparse support s=3..10 and exact cost including Euler type enumeration, big-integer lengths and rank recovery.

EM-Source-status at author time: no confirmed native claim; session request FAILED/OSError and tasks WAITING_RESOURCE/EVENT_COLLECTION_IO. Formal Source Result and Driver acceptance remain pending.
