# Stage427-B — Bounded two-sided alignment corridor for full X6 J/K observers

Date: 2026-11-04. Parent Stage426-B: `6a5edb132234af324697a4470ed9a82624f2a615`; Draft PR #1736.
Scientific inputs remain frozen: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. All present behavioral rules were read separately at global main `8af13ca22c76796fb2b39b73b091714c778f301c`, EM main `83a08de960769517241eb947e7523ef216914811`. Status: author-side theorem and executed checker; UNREVIEWED / NOT_ADMITTED.

## Exact model

Let D={+E1,-E1,...,+E6,-E6}, the 12 **typed** primitive signed directions in the chart-relative native X6 lattice. Let P,Q be source words of respective initial lengths m_P,m_Q. Their observation comprises both current lengths, both six-component signed displacement endpoints, each full directed adjacency inventory J_s(a,b), and the diagonal absolute-index matching number K(P,Q)=sum_(k=1)^min(|P|,|Q|) [P_k=Q_k].

The future operation alphabet permits independent or paired one-letter APPEND (any typed direction), independent or paired one-letter POP (remove the last letter), and an optional paired CANCEL that removes an inverse pair of final directions from each word. CANCEL is one atomic operation deleting two letters per source; it requires the pair to be inverse and sufficient deletion budget. Assume **per-source cumulative** budgets a_s appended letters and p_s removed letters; a paired operation charges each affected source, and CANCEL charges two deletions per source. Each intermediate operation's executability is part of the observer. Empty words are used only as auxiliary path stacks.

## Theorem 427.1 — Exact bounded-horizon alignment carrier

Set
 c_s=max(0,m_s-p_s), c=min(c_P,c_Q), H=min(m_P+a_P,m_Q+a_Q), W=H-c.
Retain (1) initial/current length, endpoint and J for each source, the four remaining resource budgets, and current lengths; (2) each original last m_s-c_s typed letters as a mutable stack, plus the original letter at index c_s if c_s>0 as a boundary predecessor; (3) each source's original letters at **absolute indices** c<k<=min(c_s,H) as an immutable indexed map; and (4) scalar
 B=K(P,Q)-sum_(k=c+1)^min(m_P,m_Q) [P_k=Q_k].
All letters in the subtracted sum are accessible from the retained mutable stacks or indexed maps at initialization. No earlier prefix letters need be stored.

This carrier is **fully future sufficient**: two original word pairs with the same carrier admit exactly the same legal finite operation sequences within the declared budgets, and after every such sequence they have identical lengths, endpoints, J and K.

Moreover
 ```
 0 <= W <= max(a_P+p_P, a_Q+p_Q).
 ```
Thus the number of original alignment indices needed is bounded by operation budgets, **independently of the initial difference |m_P-m_Q|**. In addition to initial observers/counters, at most 2W immutable indexed labels, sum_s min(m_s,p_s) original mutable labels, two predecessor labels, and sum_s a_s future appended labels are retained. This is a sufficient bounded-resource carrier, with no assertion of global state minimality.

### Proof

For source s, at most p_s original letters can be removed, so every original position k<=c_s stays fixed at the same absolute index through all permitted operations. The full current source word factors uniquely as its unmodified prefix of length c_s and a mutable stack containing the surviving original suffix and appended letters. A legal suffix deletion can be performed from the mutable stack: if c_s>0, its initial stack has p_s letters, so an empty stack implies exhaustion of at least p_s deletions (appends would require additional deletions); if c_s=0 the anchor is empty and the stack is the whole current word. A predecessor at c_s suffices for adjacent-edge updates. Endpoint changes are exactly the native typed direction increments. A two-letter inverse CANCEL is a pair of deletions after the pre-deletion legality test.

At every time t the current overlap h_t=min(|P_t|,|Q_t|) lies in [c,H], since |s_t| >= c_s and |s_t|<=m_s+a_s. For k<=c both initial letters remain unchanged, and their matching contribution is the stored B. For c<k<=h_t, if k<=c_s the original letter is in the indexed map; otherwise the letter is in the current mutable stack at offset k-c_s. Thus
 K(P_t,Q_t)=B+sum_(k=c+1)^h_t [letter_P(t,k)=letter_Q(t,k)].
The right side is determined entirely by the carrier. Every primitive operation transforms its stacks, endpoint, J, counters and K using only those stored fields. Legalities are determined by budgets, stack lengths and (for CANCEL) the two current tail directions. The carrier therefore defines a deterministic, observer-preserving quotient of the full-word transition system for this operation language; induction over the finite operation sequence proves future sufficiency.

For the width, let x_s=c_s and y_s=m_s+a_s. Since y_s-x_s<=a_s+p_s, taking minima gives min_s(y_s)-min_s(x_s)<=max_s(y_s-x_s)<=max_s(a_s+p_s), proving W's bound. QED.

### Conversion, update and resource costs

Constructing initial J, endpoints, K and the carrier from explicit full words costs O(m_P+m_Q) typed steps plus bookkeeping; this input-read cost must be included when claiming a speedup. The observer holds two 12×12 edge-count tables and 12 signed endpoint coordinates, whose bit lengths grow logarithmically with initial lengths and budgets. An implementation keeping the stated indexed maps and stacks requires O(288 + W + p_P+p_Q + a_P+a_Q) word/counter slots (plus bit sizes). One one-letter update changes at most one J edge and one signed endpoint coordinate; CANCEL changes at most two edges per source. Recomputing K from the bounded alignment corridor costs O(W) comparisons, or it may be incrementally maintained using Stage425's boundary-pair law. Source-to-Cell address conversion and time-labelled dynamics are separate typed operations, not assumed here.

## Proposition 427.2 — POP then APPEND reveals a hidden absolute-index residual

For **every integer L>=1**, take A=+E1, B=-E1, C=+E2, and
 P=AAABA A^L, P'=ABAAA A^L, Q=AC.
The pairs (P,Q) and (P',Q) have the same current lengths, both six-dimensional endpoints, both full J inventories, identical first letters, the same last L available labels in P/P' and the identical Q, and K=1. Independently POP Q's final C (new Q=A, K=1), then independently APPEND A to Q (new Q=AA). The future K values are respectively **2 and 1**. The endpoints and J of P/P' remain equal throughout; operation sequence is legal for a_Q=p_Q=1. This is a parameterized strict witness to information lost by a fixed terminal-only carrier in the unequal-length asynchronous model. It complements Stage425's one-step witness by displaying the POP–APPEND composition.

## Executed exact validation

`REPRO_STAGE427B.js` was actually executed in a JavaScript V8 isolate before publication. It exhausts 338 initial pairs of three-symbol native-direction words (each length 0..2) for the two explicit budget profiles [1,1,1,1] and [2,1,1,2]. For each reachable state it compares the compressed carrier's full observer to independent direct word recomputation, checks all possible operation legalities against an independent raw-stack predicate, and compares all legal successor observers. It also checks all 144 full twelve-direction independent append pairs from a fixed sample state, and four values L=1,2,7,32 of the unbounded witness. Counts and exact scope appear in `REPRO_STAGE427B_EXECUTED.json`.

The result gives a resource-bounded native-X6 path-operator theorem, not a physical heartbeat dynamics claim. Frozen source semantics and P000 are unchanged. No formal native CLAIM/Result or independent Driver mathematical acceptance was obtained.

## Next

Stage428-B: (i) prove or refute minimality of each component of the indexed corridor under the full (J,K,endpoint,legalities) observer, using a tailored family of strict distinguishing futures; (ii) optimize K updates and the Euler-DP so cached states record only the needed corridor, measuring preprocessing, memoization, and output recovery; (iii) analyze Stage424's observed 68n-463 memo-state and 85n-628 transition formulas against the original code's exact pruning, without promoting finite observation to a theorem.
