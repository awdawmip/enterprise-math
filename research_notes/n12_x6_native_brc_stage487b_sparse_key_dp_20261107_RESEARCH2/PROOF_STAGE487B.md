# Stage487-B — Sparse Euler–BRC key automaton: exact support and rank/unrank

Date: 2026-11-07 Asia/Shanghai. **AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Parent: Stage486-B, research2 PR #1736, last source commit 86cd5b8ef20d96b37bbc6194d70f184301f28928.

Frozen science (unchanged): GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules separately read from latest main. The world remains native signed six-axis X6 with 12 directions, not a 12-dimensional spatial model.

## Domain, input, and observer

Let D={+E1,...,+E6,-E1,...,-E6} and A=+E1. For k,u>=1, m=2k+2, consider ordered native words P=T, Q=T W A H A, with |T|=m, |W|=k, |H|=u. Fix the **complete initial observer fiber** (lengths, 6-component signed displacements of both words, 144 directed adjacency counts for both words, positional-equality K=m). Its first T direction s is uniquely determined by
  v(s)=DeltaP - sum_{x,y} ThetaP[x,y] v(y);
the 12 signed unit vectors v(.) are distinct. Thus the fiber is determined by the pair of adjacency vectors and this first direction within this structural word family.

Allow P_POP<=k, P_APPEND<=k, Q_POP<=h, Q_APPEND<=a for any finite a, and all 12 native direction labels on APPEND. POP requires current length>1. Stage486-B's author-side future-equivalence theorem supplies the key
  R_h=(sigma,W,S)=(suffix_L(T),W,suffix_r(H)),
  L=max(k+1,h-k-u-1), r=min(h,u), 0<=h<=|Q|-1.
This stage proves a new exact counting and ranking result **for the key partition**. Equating that partition with all-future equivalence uses the Stage486-B theorem, which remains independently unreviewed.

## Theorem 487.1 — nonenumerative exact support, mass, rank

Fix source alphabet Sigma subset D, containing A, |Sigma|=d. Let ThetaP=E(T) and ThetaQ=E(Q) be directed edge-count vectors in the fixed initial fiber, and let sP be the number of active positive edge types in ThetaP, sQ those in ThetaQ-ThetaP, s=max(sP,sQ). Then a deterministic labeled residual-edge DAG of depth L+k+r computes:

1. q_h = number of distinct supported keys (sigma,W,S);
2. exact original ordered-word population, retaining all Euler path multiplicities;
3. zero-based lexicographic rank and inverse rank on supported keys without listing that key set.

A conservative arithmetic-operation bound, including Euler memoization and key readout, is O((L+k+r)d^3(n+1)^s), where n=|Q|; every counter is a nonnegative integer using O(n log d) bits at fixed d. The present executable uses dense length-d² edge tuples; its tuple updates cost O(d²), while a sparse active-edge implementation can cost O(s). The exponent is large if many edge types are active; the improvement applies especially to small s. An Euler recursion can store O(d²(n+1)^s) endpoint/edge-vector states, with at most d transitions per state.

**Automaton and weights.** Begin P_rem=ThetaP, Q_rem=ThetaQ-ThetaP. Read key letters in the order sigma,W,S, each with one labeled transition per candidate source letter. In the sigma block, subtract each consecutive edge (sigma_i,sigma_{i+1}) from P_rem, rejecting negative counts. On its final character evaluate
  N_T=N(s,sigma_first,P_rem).
Here N(a,b,e) counts ordered directed paths from a to b with edge multiset e; base N(a,b,0)=[a=b], and N(a,b,e)=sum_{c:e[a,c]>0} N(c,b,e-[a,c]). The remaining edge count forces the intended path length m-L+1. Reject if N_T=0, multiply raw mass by N_T if positive, and discard both P_rem and sigma_first.

In the W block subtract boundary sigma_last->W_first, all W internal edges and the final W_last->A edge from Q_rem. In S subtract internal S edges and final S_last->A. If r>0, terminal hidden-completion number is N_H=N(A,S_first,Q_rem). If r=0, it is N_H=N(A,A,Q_rem). The residual count forces length u-r+2 or u+2. The terminal contributes one class per labeled key path iff N_H>0 and N_T>0; original population is multiplied by N_H. Thus one key of length L+k+r is counted once even if many original T/H completions exist.

**Why exact?** For T=U overlapped with sigma, E(T)=E(U)+E(sigma). Independently, E(Q)-E(T)=E(sigma_last W A)+E(A H A). When r>0, write H=Hprefix S: E(A H A)=E(A Hprefix S_first)+E(S A). These are disjoint edge-multiset contributions in the overlapping path convention. Each Euler-positive completion is an actual ordered native word, and all completions of U and Hprefix can be combined independently. Hence class population is N_T*N_H. Every key has exactly one sequence of labeled transitions, so addition of prefix **path counts** at merged states counts unique keys, while addition of mass-weighted paths retains provenance multiplicity. No Boolean OR may replace integer path addition for class counting. A backward memoized accepting-suffix count gives lexicographic rank/unrank by summing sizes of smaller transitions and then choosing the unique target branch.

**State bound.** During sigma, Q_rem is fixed and only P_rem varies; afterwards P_rem is discarded and only Q_rem varies. Together with at most three live endpoint letters and the position this gives O((L+k+r)d^3(n+1)^s) possible transition candidates rather than (n+1)^(sP+sQ) paired residual combinations. The program uses exactly counted integer operations. Arbitrary integers' bit operations and dense tuple copying are separate from the arithmetic-operation bound.

## Independent audit of Stage486-B positional K

With k=3,u=2, T1=AABAAAAA, T2=AAABAAAA, W=ABG, H=AB, where A=+E1, B=+E2, G=-E1, the initial full observations and h=8 repair keys coincide. An independently written direct-string simulator enumerated **6084 paired states** with all 12 native APPEND labels (at most one APPEND per participant, P_POP<=3, Q_POP<=8), and separately **6084 paired states** with the native 3-letter source subset but two APPENDs per participant. It asserted equal positional match count at each state. At Q_POP=11 the original Q directed adjacency counts differ, consistent with the larger retained T suffix.

The general K argument is also direct: P's APPEND can occupy only positions >=m-k+1 and P never reaches H indices (maximum length m+k). Thus any Q original symbol facing a P APPEND lies in known suffix_(k+1)(T), W or separator A. Q APPEND starts at indices >=n-h+1; when it faces a retained original P symbol inside T, that index is inside suffix_L(T), because L>=h-k-u-1. Two retained original symbols agree within each history by the shared T prefix; two APPEND symbols are prescribed by the common action trace. This holds for POP/APPEND interleavings. It is an independent scoped audit, not a formal independent Driver acceptance.

## Actual execution and verification scope

The complete executed local Python checker uses standard-library exact integers and an independent finite-fiber oracle that enumerates matching original T and W/H tails from the full edge bags and known first signed direction, not using the key automaton. It verifies the class populations and all rank/unrank pairs in the two small fibers, and compares large fiber population with an independent structured-tail DP.

- ABG, k=2,u=2: 4 T choices × 4 tails = 16 histories; h=0,1,2,8,9,11 gives 6,12,12,12,16,16 classes.
- ABG, k=3,u=2: 6 T choices × 7 tails = 42 histories; h=0,1,8,11 gives 20,28,28,35 classes.
- AB, k=8,u=6: 364 T choices × 314 tails = **114296** histories; h=0,1,3,6,20,25,26,28,32 gives respectively **2300,4600,9150,15700,15700,22922,32342,58718,114296** classes. At h=32 there are 114296 classes computed with **242 cumulative layer states and 326 automaton transitions** (not by listing 114296 keys). For each large budget, three rank/unrank roundtrips were executed. All assertions passed.

The attached independently executed standalone portable reproduction checks the same exact class totals, raw mass, rank/unrank samples and measured layer state counts; its complete stdout is persisted. The larger local checker also contains the direct-string K audit and full finite-key oracle. Its local SHA256 is 79d75e2f5aaa07617d1d9e0634ed374edfe930e33b55169a6d5a9fce48b4b21c; the full local JSON evidence SHA256 is 55dff1a79ffe4d60470de5d5b565a86c9c2c4695d03b24a801216719a95144d6. Full local artifacts remain separately available as conversation files. These checks establish the declared finite inputs; the general algorithm follows the proof in this record.

## Next exact unit

Stage488-B: implement sparse active-edge IDs (instead of d² dense tuples) in the signed native X6 path counter, expand original-letter tests to 4–6 active signed directions, and compare support/rank/mass and real costs under the same observed fibers. Separately test interior Q read/edit operations as a changed future-operation language; find a typed repair witness or scoped preservation proof. Preserve frozen science pins and existing owner/Driver boundaries.
