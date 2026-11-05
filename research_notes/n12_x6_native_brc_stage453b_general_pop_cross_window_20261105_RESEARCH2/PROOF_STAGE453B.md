# Stage453-B — exact arbitrary-budget two-source X6 future-repair theorem

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / FINITE_EXACT_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Predecessor: Stage452-B proof, Git commit `1c5875e66a3167062cbd0bd77dd7dab260b08f1d`. Preserve its scientific frozen inputs: account science `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math science `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules were read separately from canonical main. P000 remains fixed.

## Domain, observer, and future

Fix lengths `2<=m<n`, original path words `P=(P_1,...,P_m)`, `Q=(Q_1,...,Q_n)` in `{A=+E1,B=-E1}`; both start and end in A, with B defects internal and nonadjacent. Fix both defect counts `kP,kQ` and the **entire** current observation
`O=(m,n,V(P),V(Q),J(P),J(Q),K(P,Q))`.
Here V is the ordered six-component signed native endpoint, J is the full directed 12-by-12 native adjacency histogram, and `K(P,Q)=sum_{i<=min(m,n)}[P_i=Q_i]`. The initial observation fiber F consists of source-distinct ordered history pairs; their multiplicity is retained.

A future is any common legal labeled sequence of P:POP, Q:POP, P:APPEND(z), Q:APPEND(z), where `z` is any of twelve signed native directions, with separate nonnegative budgets `(pP,pQ,rP,rQ)`. POP of an empty word is illegal; a POP of a previously appended letter still consumes the POP budget. At **every** operation prefix compare all components of O. Legal operation labels depend on lengths and budgets, not hidden original letters. Let `H ~ H'` mean equality of this complete labeled future observation tree.

Set `a=min(pP,m)`, `b=min(pQ,n)`, `c=min(m-a,n-b)`, `t=min(n,m+rP)`. Define the coalesced indexed repair key:

```
R453 =
  P[i] for max(1,m-a) <= i <= m-1                    (POP predecessor tail)
  Q[i] for max(1,n-b) <= i <= n-1                    (POP predecessor tail)
  P[i] for c+1 <= i <= min(m,n+rQ)                   (Q-side alignment)
  Q[i] for c+1 <= i <= min(n,m+rP)                   (P-side alignment)
```

Repeated coordinates occur once. Endpoints `P_m=Q_n=A` are fixed, so they need not be separately stored. Empty ranges contribute nothing.

## Theorem 453.1 — exact future quotient for all budgets

For **every** nonnegative tuple `(pP,pQ,rP,rQ)` and **every** pair of histories H,H' in a fixed observation fiber F of the stated A/B nonadjacent-defect model,

```
                         H ~ H'   iff   R453(H) = R453(H').
```

**Sufficiency.** A future label sequence determines which original prefixes remain and which appended directions remain, independently of hidden letters. Every original prefix of length c survives in both sources because at most a P-original letters and b Q-original letters can be removed. In the initial O, isolate the prefix contribution to K by subtracting the fully key-known initial matches at indices c+1,...,m (for m<n both source letters are in the exposure windows). Every later matched position outside this fixed prefix uses key-known original letters or explicit appended letters. Hence K at every future prefix is computable from O, R453 and that future's labels. Each deleted original P adjacency edge can touch only `P[max(1,m-a),...,m]`; its predecessor is in the P tail and the terminal A is fixed. Analogously for Q. Deleted endpoint contributions, appended direction contributions and new edges are therefore computable. Starting from V and J in O gives their full future values. Thus the complete observation tree factors through the key.

**Necessity: POP tails.** For j=1,...,min(a,m-1), compare J before and after the j-th consecutive P POP. The deleted edge is exactly `(P_{m-j},P_{m-j+1})`. With the terminal A known, induction backwards recovers every P tail predecessor in R453; the identical argument recovers the Q predecessor tail. Recovery uses one component of J, not endpoint-only data.

**Necessity: P cross-alignment.** For i in `[c+1,m]`, either `i>=m-a` (then `P_i` is already in the recovered P tail or equals fixed terminal A), or `c=n-b < m-a`. In the latter case `i>=n-b+1`. The opposite original letter `Q_i` is known from the Q predecessor tail (or fixed `Q_n=A`). Execute `n-i+1<=b` consecutive Q POPs with P unchanged. The increment in K between Q-length i and Q-length i-1 is precisely `[P_i=Q_i]`. Since P_i belongs to the two-element original alphabet, this recovers P_i. Because m<n, no larger P index can be reached by Q APPEND beyond m, so all P exposure coordinates are recovered.

**Necessity: Q cross-alignment.** For i in `[c+1,m]`, either Q_i is in the recovered Q tail, or `c=m-a<n-b` and P_i is in the recovered P tail (or fixed terminal A). Execute `m-i+1<=a` consecutive P POPs, read the K decrement at position i, and reconstruct the binary Q_i. For every `m<i<=t`, execute i-m P APPEND steps, choosing A on the last step; the increment of K on that step is `[A=Q_i]` and identifies binary Q_i. These traces recover all Q exposure coordinates. Thus future equivalence implies key equality.

The theorem makes no global irredundancy claim for each coordinate: a particular observation fiber may force some positions. It does establish that equality of the key is **exactly** the minimal observable equivalence partition.

## Theorem 453.2 — exact BRC population of an indexed key

For any proposed full key assignment w, let `M(w)` be the number of source-distinct initial histories in F with this key. The following exact nonnegative-integer transfer calculates M(w).

Scan original indices i=1,...,n. At each i<=m choose `(P_i,Q_i)` in `{A,B}^2`; at i>m choose Q_i only. Require A at positions P1,Pm,Q1,Qn, prohibit consecutive B within each word, and force every key-indexed letter. The DP state after index i is
`(number_B_P,number_B_Q,number_mismatches_in_1..min(i,m),last_P,last_Q)`.
Each admissible transition adds its incoming population, starting at integer weight one, and discard states exceeding `kP,kQ,d=m-K`. Sum terminal states with the exact three counters. This is M(w); zero means unsupported.

At most `4(kP+1)(kQ+1)(d+1)` states per index, at most four letter-pair choices per transition, so the per-key transfer uses `O(n(kP+1)(kQ+1)(d+1))` exact integer additions and polynomial storage. All populations are bounded above by `2^(m+n)`, giving O(m+n)-bit integers. This is an implemented exact population algorithm; emitting all M(w) individually incurs the number of emitted keys.

**Grouped support counting (constructive polynomial algorithm).** For m<n, all paired positions c+1,...,m are visible in the key; the only unobserved paired positions form one initial prefix 1,...,c, where the exposed side's boundary at c is fixed if applicable. All unobserved Q-only letters occur in at most one interval between the exposed window ending at `t>=m` and the terminal Q predecessor tail beginning at `u=max(1,n-b)`. If t>=u-1 this latter interval is empty. Thus there are at most two hidden runs: the initial paired prefix and a later Q-only gap.

Every indexed visible key has a fixed **aggregate summary** σ consisting of: the exposed original letters at c where present; counts of P-defects, Q-defects and P/Q mismatches in visible paired positions c+1,...,m; counts of Q-defects in each of the at most two visible Q-only runs; and the finitely many binary letters adjacent to the two hidden runs (including the first paired visible letter pair). First/last letters are enough for the nonadjacent-B constraints at a run boundary. The population of a visible key depends only on σ: hidden-prefix and hidden-gap transfers depend on σ's exact remaining counters and boundary letters, not on the order of the other visible symbols. Call this common integer M(σ).

Count distinct visible keys with a given σ by a left-to-right *visible-letter DP* C(σ): emit each source/index coordinate once, enforce the two nonadjacent-defect constraints wherever both successive letters are visible, and track σ's five integer counters and finite boundary letters. Its paths are the distinct key words, not hidden completions. The paired-prefix transfer T and Q-only gap transfer U supply M(σ); sum over their remaining defect/mismatch counters without enumerating original histories. Therefore

```
q_F = sum_sigma C(sigma) * [M(sigma)>0]
|F| = sum_sigma C(sigma) * M(sigma).
```

There are at most O(N^5) integer-counter summaries (N=max(m,n)), with a constant number of boundary bits, and each visible/hidden-run transfer has a constant number of letter states and polynomially many bounded counters. Computing the summary counts, prefix and gap transfers, and summing their bounded counter products is polynomial; O(N^12) exact integer arithmetic operations is a conservative loose bound obtained even by re-running the O(N^4) prefix transfer and O(N^2) gap transfer per summary and polynomially summing residual counters. No exponential subset-state determinization or listing of all q_F labels is needed for the aggregate count. The delivered checker tests **per-key** M and sampled aggregate-summary mass constancy; a separately optimized large-N grouped implementation and tighter complexity analysis remain Stage454-B work.

## A strict new P-window witness

Take `m=7,n=8,kP=kQ=1,d=2`, `(pP,pQ,rP,rQ)=(1,4,0,0)`:

```
P1 = AAAABAA      (B at position 5)
P2 = ABAAAAA      (B at position 2)
Q  = AABAAAAA     (B at position 3)
```

Both have identical V, full directed J, K=5 and predecessor-only terminal keys (P6=A and Q4..Q7=AAAA). Since c=min(6,4)=4, the extra P5 direction is required. After 0,1,2,3,4 consecutive Q POPs, the observed K lists are respectively `[5,5,4,3,3]` and `[5,5,4,3,2]`. The *fourth* Q POP gives a strict distinguishing trace; no earlier prefix of that trace separates the histories. This is a direct counterexample to a tail-only repair when the longer source can POP below the shorter's retained prefix.

## Executed finite checks

The attached standalone standard-library Python program `STAGE453B.py` and `STAGE453B_EXECUTED.json` were executed on 2026-11-05. Exact observer and complete future-tree comparison covered 228 parameter configurations; 460 fixed-O fibers with 1,664 histories, 4,648 unordered history pairs; 67,831 memoized future states; 41,401 distinct future signatures; all 12 future APPEND directions with budgets 0/1 in the finite configurations. The indexed-key partition matched every full future-tree partition. 1,180 class populations matched the integer DP exactly. A further 1,116 parameter/fiber checks grouped 3,165 visible keys into 3,073 aggregate-summary groups; masses were constant within each group. All counters are exact integers.

The universal theorems rest on the proofs above; these finite exhaustive experiments check the declared small domains, not unrestricted runtime performance.

## BRC interface and next unit

Carrier: labeled ordered original P/Q history pairs. Boolean support: `[M(w)>0]`. Positive population: exact nonnegative integer M(w). Observer: original full native X6 tuple and all future operation traces. Safe quotient: indexed R453; erased information: hidden initial paired prefix and hidden Q-only gap; repair: both exact integer transfer counts. No external graph/vector surrogate and no phase cancellation.

Stage454-B: implement the grouped C(σ),T,U counting algorithm for unrestricted POP/APPEND budgets, run beyond original-history enumerability, audit its polynomial bound and provide rank/unrank; then test whether the exact key theorem extends beyond the binary initial alphabet while retaining six-dimensional endpoint and native J. Formal CLAIM/Source Result and independent review require their own authorized runtime gates.
