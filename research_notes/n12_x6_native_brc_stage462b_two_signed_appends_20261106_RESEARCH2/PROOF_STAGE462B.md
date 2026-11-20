# Stage462-B — two P APPENDs and two POPs per source (native signed X6)
Date: 2026-11-06. Status: author-side mathematical proof, exact-integer computation, finite full-future verification; formal Source Result and independent review pending.

## Scientific scope and frozen sources
Continue Stage461-B at commit `6ee92b23fb303d0ab1e600ebf4ceeab9cd4edd87`. Frozen sources: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 original blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules are read separately from current canonical main.

Take 2<=m<n, two **source-distinct** original ordered X6 words P,Q of lengths m,n over binary native signed directions A=+E1, B=-E1. Both begin/end A; interior B defects are isolated (never adjacent). Fix the full initial observation: lengths, six signed endpoint components, complete directed 12x12 adjacency matrices for each source, and positional match count K. In this binary isolated-defect fiber the defect counts kP,kQ and mismatch count d determine the initial observer. Each original pair is one weight-one positive BRC branch; populations are natural numbers. This is a typed ordered-word model embedded in full native X6, not a primitive lower-dimensional geometry.

Future labeled operations: up to two POPs on each source (only if nonempty), up to two P APPENDs, and either zero or one Q APPEND. Each APPEND selects any of twelve native signed X6 directions; POP may follow APPEND; all legal operation orders occur. Observations are taken after every action and the resulting labeled future trees are compared exactly.

## Theorem 462.1 — exact future equivalence and Q APPEND independence
Let one-based index sets be
`IP = {m-2,m-1} ∩ {2,...,m-1}`,
`IQ = {m-1,m,m+1,m+2,n-2,n-1} ∩ {2,...,n-1}`.
Deduplicate indices; original endpoints A are implicit. Define the repair key
`R462=((P_i)_{i in IP},(Q_j)_{j in IQ})`.
For either Q APPEND budget rQ=0 or rQ=1, two histories in the same complete initial-observation fiber have identical complete *labeled* future observation trees **if and only if** their R462 keys agree. The key has at most eight binary coordinates, so qF<=256. Allowing the first Q APPEND does not split the partition in this model.

**Sufficiency.** At any step the current history consists of a surviving original prefix plus a suffix of action-known appended directions. The at-most-two POP budget can delete at most two original steps from each history, including under interleaving with APPEND. Hence deleted original directions and original directed-edge predecessors are given by the P last-three directions (P_{m-2},P_{m-1},P_m=A) or Q last-three (Q_{n-2},Q_{n-1},Q_n=A). All added steps and edges are action-known. This determines lengths, six signed endpoints and directed adjacency statistics.

For K, original/original matches at positions <=m-2 are preserved except when an original tail is removed; their initial aggregate is reconstructed by subtracting the finitely many tail comparisons, whose letters lie in the repair key or fixed original endpoints. A P APPEND can compare against original Q no farther than index m+2; after POP its reachable original Q positions are contained in {m-1,m,m+1,m+2}, all retained when variable. A Q APPEND after at most two Q POPs first occupies index >=n-1>=m, and can therefore compare with an original P direction only at the known P tail (P_{m-1},P_m=A) or with an action-known appended P direction. For n=m+1 the lower boundary is exactly P_m. Appended/appended matches are action-known. When appended steps are later POPped the same decomposition applies. Therefore initial observation, R462, and the labeled actions determine observations at each node, and legal children are fixed by budgets and current lengths. Induction proves full future equality.

**Necessity.** The all-POP subtree is available for both rQ budgets; Stage460-B's exact two-POP grid recovery distinguishes all variable coordinates in the six-bit old repair key P_{m-2},P_{m-1},Q_{m-1},Q_m,Q_{n-2},Q_{n-1}. At the root the action APPEND_P(A) changes K by [Q_{m+1}=A] whenever an original Q_{m+1} exists. A second APPEND_P(A) changes K by [Q_{m+2}=A] when original Q_{m+2} exists. In the binary alphabet these bits recover the complete directions; fixed or out-of-range positions add no coordinate. Thus different new keys generate different labeled future observations. QED.

## Strict witness: extra Q_{m+2} is detectable
Let m=3,n=9, P=AAA, Q1=AAAABAAAA, Q2=AAAAABAAA. The Q histories each have one isolated B, matching directed adjacency counts and endpoints; initial positional K=3. The old Stage461 repair coordinates agree, but Q1_5=B whereas Q2_5=A. Under APPEND_P(A); APPEND_P(A), final K is 4 versus 5. Hence the additional original Q_{m+2} direction is genuinely necessary for some fibers.

## Theorem 462.2 — exact positive BRC support, population and rank
For every repair key w, a finite integer DP processes original slots 1..n with state (a,b,h,lastP,lastQ): defect count in each source, original positional mismatch count and previous directions for isolated-defect constraints. It enforces original fixed endpoints and repair-key bits, and sums nonnegative branch counts. Terminal count M(w) is exactly the number of original history pairs yielding w. Form a binary prefix-support tree with leaves (1,M(w)) when M(w)>0, otherwise (0,0), adding both children componentwise at each prefix. Its root is (qF,|F|). Lexicographic rank/unrank uses the left subtree's class count; there is no enumeration of original history pairs or supported-class roster.

There are <=256 candidate complete keys and <=511 cached support-tree nodes. With N=max(m,n), fixed budgets imply O(2^8 n(kP+1)(kQ+1)(d+1)) arbitrary-precision integer additions, O((m+n)) bits per count, and corresponding conservative O(2^8 n(kP+1)(kQ+1)(d+1)(m+n)) bit work with conventional addition. A rank/unrank call costs O(s) cached accesses after preprocessing, s<=8. No polynomial claim is inferred for growing append windows.

## Actual executable evidence
An independent local Python program enumerated 13 small configurations, including n=m+1 and n=m+2, all 12 signed directions and legal operation orders. It used complete six-axis integer endpoints, directed 12x12 edges, K, and interned *full labeled observation trees*, cross-checking exact future equivalence, each class population, support and rank/unrank: **130 nonempty initial fibers, 262 original history pairs, 252 supported-class checks, 276 within-fiber pair comparisons, 602252 memoized future states; all checks passed**.

Exact grouped integer DP gave (m,n,kP,kQ,d)=(8,10,2,2,1) -> qF=4, mass=20; (64,80,15,17,1) -> qF=49, mass=5061384194832966. The 64/80 initial population matches Stage461-B's 5061384194832966, while the new two-append quotient increases from 34 to 49 classes. Source `STAGE462B.py` is a same-mathematics adaptation of the Stage461-B reproducer; `STAGE462B_EXECUTED.json` summarizes the separately executed local validation and its exact counts. The local program attempted an additional 92/126 parameter but hit a runtime limit; the completed successful rerun omits it.

Proof strength: the exact iff is established by explicit reconstruction and distinguishing-action arguments; finite tests are separate evidence. Native Source Result and independent Driver acceptance are pending.
