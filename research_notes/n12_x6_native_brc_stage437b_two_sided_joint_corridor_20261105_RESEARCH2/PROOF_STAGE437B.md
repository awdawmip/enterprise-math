# Stage437-B: two-sided X6 bounded joint corridor theorem

Date 2026-11-05. AUTHOR_SIDE_PROOF / EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED.

## Scientific pins, domain, and positive BRC interface

Parent Stage436-B, immutable proof commit e75835e9cf0918ed75ec08aa47536f22811faaa8 in Draft PR #1736. Frozen scientific input remains GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative overlay verified separately at GLOBAL main@74b16ebf12a1897da88c35563f0d500bd90b97e7 and EM main@3670f593de5850b22bab708a5352edebce481f6d.

Let D={+E_i,-E_i:1<=i<=6}, twelve signed step directions of the six native spatial axes. Ordered finite words P,Q in D* carry provenance by their exact direction/index pairs. The complete readout at each state is O=(length_P,length_Q,V_P,V_Q,J_P,J_Q,K), where V is a six-component signed endpoint displacement, J(a,b) is the complete directed-adjacency multiplicity table, and K=sum_{i<=min(length_P,length_Q)}[P_i=Q_i]. A matching position contributes one positive unit-weight BRC branch; its exact positive CWM summary is (C,W,M)=(K,K,1) for K>0 and (0,0,0) for K=0. This is the positive-unit specialization of the published BRC cwm_edge/cwm_recoalesce interface; signed X6 endpoint displacement is a different typed observer, not a positive mass or complex phase. Time/heartbeat dynamics and full three-dimensional slice semantics are not invoked.

Both sources may independently execute POP or APPEND(d) for arbitrary d in D. Legal words can interleave operations, can pop earlier appends, and have separate total budgets p_P,r_P,p_Q,r_Q (POP/APPEND respectively). Assume m=|P|>=p_P+1 and n=|Q|>=p_Q+1, with all budgets nonnegative.

## Theorem 437.1 (sufficient joint state, every legal future)

Set c=min(m-p_P,n-p_Q). Define original-index corridors
   I_P=[c+1,min(m,n+r_Q)]
   I_Q=[c+1,min(n,m+r_P)]
with empty intervals when the upper bound is below the lower.

Retain the original P_i on I_P, Q_i on I_Q, the last p_P+1 and p_Q+1 original directions of P and Q, initial complete O, plus the known budgets. After each operation, retain the current original-prefix lengths, live append stacks, updated O and remaining budgets. Then this record determines *every component of O and every legal-action decision after every legal finite joint operation word*. Two original pairs with identical records have identical complete future traces for the declared budget language.

**Proof.** (i) A source POP budget can delete at most p_s original directions, regardless of how many appended directions are subsequently popped. Therefore both words permanently retain their original first c directions at positions 1,...,c. Their K contribution K_fixed=sum_{i=1}^c[P_i=Q_i] is invariant. It is determined from the cached initial K by subtracting all original-overlap matches with c<i<=min(m,n); those two compared original directions lie in I_P and I_Q.

(ii) All remaining cross-source equality comparisons are available: if some original P_i with i>c ever meets a Q position, then i<=m and i<=length_Q<=n+r_Q, hence i in I_P. Similarly every compared original Q_i lies in I_Q. Any nonoriginal letter was appended after startup and remains explicitly on that source's append stack while live. Thus every changed K comparison is determined. On APPEND to a source of old length L, K increases by [other_length>=L+1][d=other_(L+1)]; on POP from old length L it decreases by [other_length>=L][old_last=other_L]. These indices exceed c because the original prefix lengths cannot fall below their respective survival bounds.

(iii) For each source APPEND(d) changes V by +vec(d), adds only the ordered J edge (old_last,d), and updates the append stack. POP changes V by -vec(old_last), removes only J(old_penultimate,old_last), and removes the last appended or last original direction. Every needed original source boundary direction is among the final p_s+1 original letters; after all appended symbols have been popped, no more than p_s original POP operations can occur. Hence V,J and operation feasibility are determined from the record. By induction over arbitrary legal action words, all observed traces are identical.

(iv) If c=m-p_P<=n-p_Q, then |I_P|<=p_P and |I_Q|<=p_P+r_P. Otherwise |I_Q|<=p_Q and |I_P|<=p_Q+r_Q. So corridor slots plus both suffixes are bounded by
   |I_P|+|I_Q|+(p_P+1)+(p_Q+1) <= 3(p_P+p_Q)+r_P+r_Q+2.
The bound is independent of m,n and |m-n|; duplicate stored letters may be merged. QED.

This is **sufficiency**, not a proof of minimum joint equivalence-state size. It does not rely on the Stage435/436 restricted defect-family classification.

## Proposition 437.2 (strict naive-summary counterexample)

Write A=+E_1, B=-E_1, C=+E_2. Take
   P=AAABAAA,  P'=ABAAAAA,  Q=CC
and budgets (p_P,r_P,p_Q,r_Q)=(1,1,0,2).

Both P words have six A, one B, J(AA)=4,J(AB)=J(BA)=1, identical six-dimensional endpoints, and identical final two letters AA. With common Q=CC they have identical present complete readout O (K=0), and the same POP-sufficient original suffixes. Thus current endpoint/J/lengths/K together with independently stored POP suffixes cannot distinguish them. After two legal Q-APPEND(A) operations, Q=CCAA. The final K values are 1 for P and 2 for P': position 4 exposes B versus A. The joint corridor I_P=[3,4] retains AB versus AA and repairs exactly this loss. This refutes the *specified naive summary*, not a properly cross-observer-conditioned one-sided Stage436 quotient.

## Exact cost and verification boundary

Input conversion requires a full O(m+n) word scan to construct V,J,K and select the indexed original slots. Let B=p_P+r_P+p_Q+r_Q. Initial extra label storage is O(B) signed direction symbols, and future append stacks use O(r_P+r_Q); with fixed six axes, the current 144-entry J, six-dimensional endpoints and lengths consume O(log(m+n+B)) total bits, plus O(B) finite direction symbols. Each POP/APPEND needs O(1) direction comparisons and O(1) bounded-integer updates (O(log(m+n+B)) bit time); total initial scan and B-step incremental trace is O(m+n+B) word operations. Serializing B full observations costs O(B) additional records. Recovery of all dropped original prefix details is a separate problem, not promised by this observer quotient.

The independent source REPRO_STAGE437B.js executes exact safe-integer finite tests on all twelve original signed direction labels (all tested counts < 2^53). It uses the positive-unit (C,W,M) BRC recoalescence law from src/enterprise_math/brc_weighted.py, current EM source blob 3f205696709e847909958a153f8fe10d3f6b70f0, and compares the reconstructed observer with full paths after each checked legal step. Exact finite coverage and counterexample are recorded in REPRO_STAGE437B_EXECUTED.json. This is **not** a run of the deployed native BRC physics/runtime or a phase-cancellation/heartbeat residual certificate. The infinite-parameter theorem rests on the symbolic proof here, not the finite tests.

## Next scientific frontier

Find the minimum observer-conditioned *joint* quotient on a fixed present-observation fiber; rank/unrank a smaller coupled code if possible, or prove lower bounds with exact separating futures. Calculate the full positive BRC class populations, input conversion/representation/rank/recovery costs; retain joint provenance and do not infer arbitrary-coupling safety from a product of separately optimal one-sided codes. Native CLAIM/Result/Driver independent acceptance remain separate authority questions.
