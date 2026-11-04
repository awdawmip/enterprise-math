# Stage420-B — Exact 16-state future quotient for the native-X6 double-budget defect fiber

Date: 2026-11-04. Author-side mathematical proof, independent review and native admission pending. Parent: Stage419-B at immutable commit eca3dc004a617173c13d4c87c66c3a45dda43235, Draft PR #1736.

Frozen science unchanged: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative context is read separately. This is a statement about a specific ordered-path observer embedded in P000 native six-axis space, not a global statement about all Heartbeat World processes.

## Model and exact result

D={+E_j,-E_j | 1<=j<=6}; A=+E_1, B=-E_1. For all integers n>=11, let F_n consist of pairs:
P_i=A^(i-1) B A^(n-i), Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
2<=r, r+2<=s<=n-1, i in {r,s}.

Each pair has the same initial full observation O=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q)), where z is the respective signed six-coordinate displacement, J the respective full directed adjacent-direction histograms, and K the number of equal directions at absolute aligned positions up to the shorter length. Attempted-operation enabledness and each successful intermediate O are observable. Futures permit unrestricted paired APP(a,b) for all (a,b) in D squared, up to two Q-only POP operations, and up to two paired CANCEL operations. A CANCEL is enabled iff each source ends in a two-letter inverse pair; it deletes both pairs simultaneously. Equivalence means agreement under *every finite attempted trace* including failure.

THEOREM 420.1. The exact number of all-future observational equivalence classes for every n>=11 is

q(F_n) = 16, while |F_n| = (n-3)(n-4).

The 16 class sizes in the fixed three-test signature order are
((n-7)(n-8), 2(n-7), n-6, n-6, n-6, n-7, n-6, n-7, 1,1,1,1,1,1,1,1).
For n=16 this partitions 156 histories into
(72,18,10,10,10,9,10,9,1,1,1,1,1,1,1,1).
A 4-bit fixed-width class identifier suffices in this finite quotient; general algorithmic complexity is not claimed.

## New original-tail deletion lemma

Write each current word as a surviving ORIGINAL prefix followed by its still-surviving APPENDED suffix. Let dP,dQ count original labels deleted from the right. Consider the four non-singleton Stage417 test signatures:

signature 4: s=n-2, i=r, 2<=r<=n-5;
signature 5: s=n-2, i=s, 2<=r<=n-6;
signature 6: s=n-1, i=r, 2<=r<=n-5;
signature 7: s=n-1, i=s, 2<=r<=n-6.

LEMMA 420.2. In signatures 4/6, every successful future obeys dP<=2 and dQ<=4; if a CANCEL remains, dQ<=3. In signatures 5/7, every successful future obeys dP<=3 and dQ<=5; if a CANCEL remains, dQ<=4. All bounds cover the entire twelve-direction alphabet.

PROOF. Every CANCEL deletes at most two original directions in a source; Q POP deletes at most one original Q direction. For i=r, P has at least five trailing original A directions. No original AA terminal pair can be cancelled, so each of the two CANCELs deletes at most one original P A and dP<=2. For i=s, P has one original B. A CANCEL deleting two original P labels must include that B; this happens at most once. The other CANCEL deletes at most one original label, so dP<=3.

APPEND-COUNT INVARIANT: if no Q POP has deleted an APPENDED Q label, the numbers of surviving appended labels in P and Q always agree. APP increases both counts. A Q POP removing an ORIGINAL occurs only with zero appended Q labels, so both appended counts are zero. Under a paired CANCEL with equal appended counts k, both sources delete respectively 0, 1 or 2 appended labels for k=0,1 or k>=2. Thus equality persists by induction. Consequently a CANCEL that removes two original Q labels without any prior Q POP of an appended label must also delete two original P labels; both original terminal pairs must then be inverse.

For i=r, suppose dQ>=5. If both Q POPs delete originals, at least one of two CANCELs must delete two original Q labels. By the append-count invariant it would simultaneously cancel an original P inverse pair; no such pair is reachable inside P's all-A terminal run. If at least one POP deletes an appended Q label, at most one POP deletes an original Q label. To delete five original Q labels, both CANCELs would then have to delete two originals. Each such cancellation must contain an original B, since the other original labels are A. But among Q's five rightmost original labels only the B at fixed s occurs: the other B is at r<=n-5, outside those five positions. Thus at most one such double-original Q CANCEL is possible. This proves dQ<=4. With <=1 CANCEL used, identical counting gives dQ<=3.

For i=s, to have dQ>=6, both POPs must delete original Q labels and both CANCELs must delete two original Q labels. The append-count invariant then forces *two* different double-original inverse P CANCELs, impossible because original P has only one B. Thus dQ<=5. With <=1 CANCEL used, dQ<=2+2=4. QED.

## New all-future equivalences within signatures 4–7

THEOREM 420.3. For a fixed n>=11, all histories within any *one* of signatures 4, 5, 6 or 7 are equivalent under every finite signed-X6 APP/POP/CANCEL trace with budgets (2,2).

PROOF. Couple two histories with different allowed r in the same signature. Maintain equal original deletion counts dP,dQ, equal surviving appended direction words U,V, equal budgets and equal current full O. These hold initially.

For signatures 4/6, the only variable original B is the COMMON early P/Q B at r<=n-5; neither source can reach/delete it by Lemma420.2. All original directions at indices >=n-4 are identical between the histories, including the fixed second Q B at s. For signatures 5/7, the only variable original B is Q's early first B at r<=n-6; it survives, and all original directions at indices >=n-5 are identical, including the fixed B at s of both P and Q.

Current endpoints and lengths agree because the initial endpoints agree, deleted original suffixes are identical and appended U,V are identical. For each full directed J, subtract from initial J the edges incident to the removed original suffix (requires original directions at indices >=n-dP or >=n-dQ), and add the common boundary junction and internal appended edges; the required original labels all lie in common terminal tails. Hence full directed J agrees.

For K, let t=n-max(dP,dQ), the length of the remaining aligned original-original prefix. In signatures 4/6, t>=n-4 and the unique original mismatch is at fixed s, so this prefix contributes t-[t>=s], independent of r. In signatures 5/7, t>=n-5 and the mismatch lies at r<=n-6, so the prefix contributes t-1, independent of r. All remaining comparisons touch appended and/or original directions at indices >t, where the original directions are common; therefore entire absolute-position K agrees.

APP is always enabled; POP enabledness depends on budgets and lengths. If a CANCEL remains, Lemma420.2 strengthens the Q bound to dQ<=3 (4/6) or dQ<=4 (5/7), so the two terminal directions needed for inverse-pair tests lie in common original tails or are common appended labels. P terminal directions are likewise in common tails. CANCEL enabledness agrees. Each successful action deletes the same number/type of original/appended labels, giving equal updated counters/U/V; by the preceding paragraphs full O remains equal. Failed actions fail on both. Induction on arbitrary finite traces proves the theorem. QED.

## Completion of the minimum and class sizes

Stage416-B established that the last P:6 and Q:7 original labels are a sufficient full-future state key. Stage417-B enumerated 32 such keys for all n>=11 and gave three exact finite test traces partitioning them into sixteen *pairwise distinguishable* signatures, with raw-key index groups

[0,1,2,3] [4,5,12,13] [6,14,20] [7,15,21]
[8,16,22] [9,17] [10,18,24] [11,19]
[23] [25] [26] [27] [28] [29] [30] [31].

Stages417–419 proved complete full-future equivalence within the first four multi-key signature groups. Theorem420.3 establishes the four remaining multi-key merges. Eight singleton groups are automatically sufficient by the Stage416 suffix-key theorem. This proves q<=16.

The attached checker independently reconstructs all sixteen distinct observed three-test signatures at n=11, so q>=16 there. For n>11, prepend A^(n-11) to both words of each n=11 representative. The distinguishing short trace remains terminal and never touches this prefix; every endpoint and directed J receives the same additional contribution and K receives the same prefix matching count (n-11). Hence all sixteen observed test signatures remain pairwise different for every n>=11, and q>=16. This completes Theorem420.1.

Grouping raw keys by the fixed three tests yields counts
((n-7)(n-8),2(n-7),n-6,n-6,n-6,n-7,n-6,n-7,1,1,1,1,1,1,1,1);
they sum to (n-3)(n-4), and the attached program independently checks every n=11..40.

## Actual computation and next scientific question

REPRO_STAGE420B.py (Python standard library) computed the initial complete fiber, signed native endpoints, both full directed J and absolute K, reconstructed the 32 raw keys and the sixteen trace signatures, checked 16,760 original histories across n=11..40, tested all 144 APP direction pairs for eight distinct-key pairs in groups 4–7 (1,152 checks), and performed exhaustive reachable-pair BFS with all destructive budgets and up to 3 APP operations from ±E1, ±E2. The actual executed stdout JSON carries marker STAGE420B_PARAMETRIC_EXACT_SIXTEEN_CLASS_PASS and exact per-pair BFS counts. Finite computation cross-checks the theorem; the all-horizon assertion follows from Lemma420.2 and Theorem420.3.

BRC reuse: original provenance, ordered paths and joint K were preserved until proving full future equality; class-ID is a lossless quotient for the explicitly declared operation language. This is a local model-internal minimal-memory result, not a generic asymptotic algorithm claim.

Stage421-B: compute the quotient directly from remaining-Euler-edge/J/K data without enumerating historical pairs, accounting for input/output costs; separately change only the Q POP budget from 2 to 3 and seek a shortest exact splitting witness (or a valid preservation theorem). Retain independent native CLAIM/Result/Driver admission, frozen scientific pins and current role rules.
