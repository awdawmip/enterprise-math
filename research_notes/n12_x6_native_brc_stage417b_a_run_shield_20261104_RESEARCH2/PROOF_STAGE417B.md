# Stage417-B — A-run shielding and 29-state future-memory upper bound

2026-11-04; Enterprise Math / Research2; portable author-side proof candidate. Parent Stage416-B immutable commit f9dc57364001654b9f86cdd4c55fc7b59b80ea7f, Draft PR #1736. Frozen scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; native P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Classification: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact model

Let D={+E_j,-E_j : j=1,...,6} be the original native signed six-axis label set (twelve directions); A=+E1, B=-E1. The full observer on an ordered two-source history (P,Q) is O=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q)), where z is the six-component signed chart-relative endpoint, J is each source's COMPLETE directed adjacency histogram on D×D, and K is the number of equal labels at the same absolute positions through the shorter length. Enabledness of each attempted operation is observed.

Future actions: APP(a,b) with arbitrary (a,b) in D×D; up to p Q-only POP operations; up to c paired inverse CANCEL operations. CANCEL is executable iff each source's final two labels form an inverse pair; it removes both labels from each source. All operations edit at the right end. An unsuccessful action yields a DENIED observation.

## Theorem 417.1 — common terminal run shields arbitrary old history, at every finite horizon

Fix p,c ≥ 0 and m=p+c+1. Take any two initial equal-length pairs (P,Q),(P',Q') with identical full O. Suppose ALL FOUR words end in the same m-fold repetition A^m of one fixed signed primitive direction A. Then the two starting histories are future-equivalent for arbitrary common finite action traces over the FULL twelve-direction APP alphabet and the declared POP/CANCEL budgets.

Proof. After any common successful trace prefix, the current words each split into a surviving original prefix of lengths n-dP or n-dQ, followed by appended suffixes U,V. Since all edits occur at the right end, the appended suffixes and remaining budgets are identical in the two compared histories as long as enabledness agrees.

While any original A remains, Q-only POP deletes at most one original label, and each paired inverse CANCEL deletes at most one original label in each source: two terminal original A labels cannot form an inverse pair. Therefore 0≤dP≤c and 0≤dQ≤p+c, and m=p+c+1 ensures that a surviving original A remains in both words. Every removed original label is A.

At any such state, both six-component endpoints are determined by their respective initial z, the original deletion count times A, and the signed displacement of the common appended suffix. For source-directed adjacency J, deleting d original labels removes exactly d copies of directed A→A, while appending a nonempty suffix adds the original/appended junction A→first(U) or A→first(V) and the internal appended edges. The original J and the appended suffix are common, so all directed J values agree.

For absolute-position joint K, write d=max(dP,dQ)≤p+c. Originally aligned positions through n-d remain aligned original-to-original. The omitted original aligned positions n-d+1,...,n were all (A,A), contributing exactly d to original K. Every remaining comparison after position n-d involves a common appended label; if the other operand is an original label, it lies in the last d original positions and is A. Hence K is determined by the common initial K, dP,dQ,U,V. The complete observation agrees after each common successful prefix.

APP enabledness is unconditional. POP enabledness follows from the common Q length and remaining POP count. Before a further CANCEL, at most c-1 CANCELs have been used: dP≤c-1 and dQ≤p+c-1=m-2. Hence each surviving original A-run still contains at least TWO consecutive A labels. Any CANCEL terminal inverse test using two originals sees A,A on both sides and fails; using one original sees A and the identical neighboring appended label; using no originals sees identical appended labels. Thus CANCEL enabledness agrees. The induction closes for every finite trace. QED.

This exact compression preserves the full joint K and source-specific directed J. It is a statement about the declared future observer, not a claim of universal physical history deletion.

## Corollary 417.2 — uniform bound 16 ≤ q(F_n) ≤ 29

Consider the complete Stage411/415 defect fiber F_n of pairs

P_i = A^(i-1) B A^(n-i),    Q_(r,s) = A^(r-1) B A^(s-r-1) B A^(n-s),

where 2≤r, r+2≤s≤n-1 and i is either r or s. All have the same complete O: lengths (n,n), signed endpoints ((n-2)E1,(n-4)E1), P adjacency AA:n-3, AB:1, BA:1, Q adjacency AA:n-5, AB:2, BA:2, and K=n-1. There are (n-3)(n-4) original histories.

Define G_n as those with s≤n-5. Both P and Q then end in A^5, so Theorem417.1 with p=c=2 makes EVERY pair of histories in G_n future-equivalent. Its exact cardinality is

|G_n| = 2 sum_(s=4)^(n-5) (s-3) = (n-7)(n-8), for n≥9.

By Stage416-B, the (P last 6,Q last 7) raw suffix key is sufficient for full future equivalence, and precisely 32 raw keys occur in F_n for every n≥11. In G_n exactly four such keys occur, represented at n=11 by (r,s,i)=(2,4,2),(2,5,2),(2,6,2),(2,6,6). Their safe merger yields at most 32-4+1=29 actual future classes. Stage415-B proves 16 pairwise distinguishable representatives under exact legal traces. Thus for EVERY integer n≥11:

             16 ≤ q_(2POP,2CANCEL)(F_n) ≤ 29.

At n=16, G_n comprises 72 of the 156 histories, in one rigorously proved all-future equivalence class. The 16 lower and 32 raw-key upper inputs remain the cited author-side, unreviewed earlier theorems; the A-run shielding theorem is independently established above.

## Theorem 417.3 — exact 16-signature finite-test classes and populations

Take the Stage415-B three fixed tests:
V1: APP(B,B),CANCEL,POP,POP,APP(B,B),CANCEL.
V2: APP(B,B),CANCEL,APP(B,A),POP,POP,CANCEL.
V3: APP(B,B),CANCEL,CANCEL,POP,POP.
Each signature is the ordered triple of entire step-by-step full-O sequences, including DENIED if an action cannot execute.

For EVERY n≥11, this finite-test signature partitions all (n-3)(n-4) histories into EXACTLY 16 classes:

| Class | Exact parameter membership | Population |
|---|---|---|
| 0 | s≤n-5, either i | (n-7)(n-8) |
| 1 | s=n-4, either i | 2(n-7) |
| 2 | s=n-3, i=r | n-6 |
| 3 | s=n-3, i=s | n-6 |
| 4 | s=n-2, i=r, r≤n-5 | n-6 |
| 5 | s=n-2, i=s, r≤n-6 | n-7 |
| 6 | s=n-1, i=r, r≤n-5 | n-6 |
| 7 | s=n-1, i=s, r≤n-6 | n-7 |
| 8 | r=n-5,s=n-2,i=s | 1 |
| 9 | r=n-5,s=n-1,i=s | 1 |
| 10 | r=n-4,s=n-2,i=r | 1 |
| 11 | r=n-4,s=n-2,i=s | 1 |
| 12 | r=n-4,s=n-1,i=r | 1 |
| 13 | r=n-4,s=n-1,i=s | 1 |
| 14 | r=n-3,s=n-1,i=r | 1 |
| 15 | r=n-3,s=n-1,i=s | 1 |

Proof. Enumerate F11 exactly by increasing r,s,i: it has 56 triples and exactly 32 first-seen raw (last6(P),last7(Q)) keys. Deterministic exact integer evaluation of the three V traces on representatives produces these disjoint key-index groups (0-based first-seen order):

[0,1,2,3] / [4,5,12,13] / [6,14,20] / [7,15,21] / [8,16,22] / [9,17] / [10,18,24] / [11,19] / [23] / [25] / [26] / [27] / [28] / [29] / [30] / [31].

For n≥11, prepend A^(n-11) to both words of each F11 key representative. Every F_n key is realized by this padding: the F11 key set injects, and Stage416-B proves both sets have 32 members. Prefix padding adds the same length, signed endpoint, directed AA adjacency and aligned K contributions at every successful trace prefix; these right-end tests cannot touch the padded first A. Its equal/distinct trace-signature relations are therefore unchanged. Moreover any F_n history with the same raw key as a padded representative has the same initial full O; Stage416's all-future suffix theorem supplies equality under all V tests. The F11 signature grouping therefore transfers exactly to every n≥11.

Reading the B positions in each raw key yields the listed membership predicates. For each row, counting the permitted r values (and twice summing r<s-1 for class 0) yields the population formula. The sixteen populations sum exactly to (n-3)(n-4). This gives a finite exhaustive, integer-arithmetic certificate for the 32-key grouping, followed by an algebraic all-n extension. QED.

CAUTION ON CLASSIFICATION: these sixteen are classes of the specified finite-test suite, not yet proved classes of the full future language. Class 0 is individually proved to be one all-future class by Theorem417.1. The remaining fifteen may split under additional legal traces.

## Reproduction, status, continuation

The exact saved ECMAScript reproducer REPRO_STAGE417B.js was executed in the tool runtime. It checks the full F_n combinatorics and class formulas for 11≤n≤60, the 32-key / 16-test partition of all F11 histories, representative padding through n=15, all 144 native paired first-APP directions on G11, and four mixed traces involving ±E2, ±E3 and ±E4. The exact output is saved as REPRO_STAGE417B_EXECUTED.json; status marker STAGE417B_A_RUN_SHIELD_AND_SIXTEEN_TEST_CLASS_PASS. General future equivalence uses the symbolic proof, not extrapolation from the finite tests. Scientific pins are unchanged; no native CLAIM, Source Result or independent Driver admission is claimed.

Next Stage418-B: for one of the fifteen remaining finite-test groups (begin with class 1) prove a budget-aware full-future bisimulation with directed J and absolute K, or construct a shortest legal twelve-direction distinguishing trace; propagate to the remaining groups to decide q(F_n) exactly. Reuse the Stage412 Euler/K exact residual-edge DP for class sizes once all-future equivalence is established.

