# Stage415-B — two-cancellation native-X6 BRC future-memory bounds

Date: 2026-11-04. Research2 author-side continuation from Stage414-B, PR #1736, source commit c7f99ce8c724634053787e5a0e65c90ba72cfe78. Immutable scientific inputs remain GK bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419 and P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules were separately read from GK main 62faf1e88ed6fcea716b91dab800642c50e70801 and EM main ecc64a8ea7be01d5b26b04433d5019b673fc65e9. Status: AUTHOR-SIDE PROOF + EXACT FINITE CHECK, UNREVIEWED / NOT_ADMITTED.

## Model and parent problem

Take native direction labels D={+E_j,-E_j: j=1,...,6}; set A=+E_1, B=-E_1, and regard signed displacement as six native coordinates relative to a chosen Cell (not a final Cell address). The full observer of an ordered source pair (P,Q) is

O(P,Q)=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q)),

where J counts every directed adjacent direction-label pair and K counts equality at absolute aligned positions through min(|P|,|Q|). Attempted-action enabledness is observable. The operation language has arbitrary paired APP(a,b) over all D², up to TWO independent Q-only POPs, and up to TWO paired CANCELs, each enabled only when the two terminal letters of P form an inverse pair and those of Q separately form an inverse pair. A successful CANCEL deletes the last two letters of both sources.

Study the complete shared-O history fiber F_n:

P_i=A^(i-1) B A^(n-i),
Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
2<=r, r+2<=s<=n-1, i=r or i=s.

Counting the two choices i for each valid (r,s) gives |F_n|=(n-3)(n-4). All members share directed J, endpoints and K=n-1. Stage414-B (unreviewed) gave the corresponding ONE-CANCEL exact quotient q_1(F_7)=8, q_1(F_n)=9 for n>=8. This note changes only the CANCEL budget.

## Theorem 415.1 — all-horizon seven-label suffix safety

For any two initially equal-length pairs with identical complete O and matching last seven original labels of P and Q respectively (whole words when shorter), every legal finite two-POP/two-CANCEL future has identical complete O and action enabledness, for arbitrary appended labels in the full twelve-direction D.

Proof. At each stage every current word has the form original prefix followed by surviving appended suffix, e.g. P=P0[1:n-dP]U, Q=Q0[1:n-dQ]V. Right-end edits never remove an interior original letter. Because there are at most two paired cancels, dP<=4; because there are at most two Q-only pops plus two cancels, dQ<=6. Inductively the two compared histories retain the same dP,dQ,U,V and remaining budgets while enabledness agrees.

Their endpoints are reconstructed from original endpoints by subtracting the known last d original labels and adding common U,V. Each directed-adjacency histogram is reconstructed from initial J by subtracting edges inside the deleted original tail and its preceding boundary edge, using at most d+1<=7 original labels, then adding surviving original/append junctions and appended edges. Their absolute-alignment count K is reconstructed from initial K by subtracting indicators in the last max(dP,dQ)<=6 original positions; mixed original/appended comparisons can occur only in those last six positions, and append/append comparisons are known. Thus complete observations agree after equal enabled edits. Before a *further* paired cancellation at most one was spent, so dP<=2 and dQ<=4, and the terminal two labels potentially tested are still visible within the seven known original labels or common appended suffixes. Q POP enabledness depends on length and remaining budget; APP is always enabled. Hence enabledness and transitions agree inductively for any finite trace. QED. This is a sufficient certificate, not a sharp-minimality assertion.

## Theorem 415.2 — exact F7 quotient is twelve

The complete fiber F7 has exactly 12 members, and all 12 are pairwise future-distinguishable with the following three tests, using only A/B APP labels and at most two POPs and two CANCELs:

U1: APP(B,A), POP, POP, CANCEL, APP(B,B), CANCEL.
U2: APP(A,A), APP(B,B), CANCEL, POP, CANCEL, POP.
U3: APP(B,B), CANCEL, APP(B,A), POP, POP, CANCEL.

Record initial complete O and full O after each successful step; if an attempted operation is disabled, report DENIED and stop that trace. For each Ui separately, sort all exact resulting observation-sequence tuples of the 12 histories lexicographically by their Python repr and assign distinct zero-based ordinal ranks. The triple of ordinal ranks is an injective equality-preserving certificate, reproduced exactly by REPRO_STAGE415B.py:

| r,s,i | U1,U2,U3 |
|---|---|
| 2,4,2 | 0,0,1 |
| 2,4,4 | 0,0,0 |
| 2,5,2 | 3,0,2 |
| 2,5,5 | 1,0,4 |
| 2,6,2 | 5,1,6 |
| 2,6,6 | 8,2,8 |
| 3,5,3 | 4,0,3 |
| 3,5,5 | 2,0,5 |
| 3,6,3 | 6,1,6 |
| 3,6,6 | 8,3,8 |
| 4,6,4 | 7,1,7 |
| 4,6,6 | 9,4,8 |

The finite domain is exactly the twelve parameter triples shown (no missing histories); each of the 66 unordered pairs has at least one distinct test outcome. Consequently 12<=q_2(F7)<=|F7|=12, so q_2(F7)=12. In particular the old Stage414 merged pair (r,s,i)=(2,4,2) and (2,4,4), which had common original safe key and complete O, is separated by U3 through final K=3 versus K=2. This is a strict witness that the second cancellation exposes a previously hidden joint alignment residual.

## Theorem 415.3 — for every n>=9, q_2(F_n)>=16

Use three fixed tests on F9:

V1: APP(B,B), CANCEL, POP, POP, APP(B,B), CANCEL.
V2: APP(B,B), CANCEL, APP(B,A), POP, POP, CANCEL.
V3: APP(B,B), CANCEL, CANCEL, POP, POP.

The following sixteen representatives of F9 have pairwise distinct exact observer-sequence rank triples, with ordinal ranks defined separately for V1,V2,V3 over the complete 30-member F9, exactly as for Theorem415.2:

| r,s,i | V1,V2,V3 |
|---|---|
| 2,4,2 | 0,0,0 |
| 2,5,2 | 1,0,0 |
| 2,6,2 | 2,2,0 |
| 2,6,6 | 2,1,0 |
| 2,7,2 | 5,3,0 |
| 2,7,7 | 3,5,1 |
| 2,8,2 | 7,7,4 |
| 2,8,8 | 10,9,5 |
| 4,7,7 | 3,5,2 |
| 4,8,8 | 10,9,6 |
| 5,7,5 | 6,4,0 |
| 5,7,7 | 4,6,3 |
| 5,8,5 | 8,7,4 |
| 5,8,8 | 10,9,7 |
| 6,8,6 | 9,8,4 |
| 6,8,8 | 11,9,8 |

Proof of uniform extension. For h=n-9>=0, prepend A^h to *both* words of every one of these sixteen representatives; the triple becomes (r+h,s+h,i+h) and remains admissible in F_n. In any V test, all original edits occur within the last six Q and last four P labels (the proven deletion-depth bounds). Thus no test can reach the first three letters of either original nine-step word. These original words all start with A. Prepending A^h to both sources leaves each action's enabledness unchanged; at every successful prefix it uniformly adds h to each word length, +h E1 to each endpoint, +h to each J(AA), and +h to aligned K, leaving all other counts and all differences between test outputs unchanged. The distinct 16 triples of exact V-sequence outputs remain distinct under this common uniform transformation. Therefore sixteen pairwise separable histories exist for every n>=9, proving q_2(F_n)>=16 without extrapolating a finite range. QED.

## Theorem 415.4 — uniform upper bound q_2(F_n)<=33 for n>=11

By Theorem415.1, two histories with identical (last7(P),last7(Q)) are future-equivalent. The count of these paired suffix keys is 33 for every n>=11. To show stabilization, normalize any n>=11 marked-B pattern to n=11 by retaining the exact locations of Bs inside the last seven positions, and mapping all earlier Bs to legal internal positions: if both Q defects are outside the window, choose (r,s)=(2,4); if only r is earlier, choose r=2 and retain the distance of s from the right; if both are in the window, retain their right-index offsets. Choose i=r or s to preserve P's marked position. Every normalized instance satisfies 2<=r,r+2<=s<=10. Conversely prepend A^(n-11) to any F11 history to realize its same final-seven key in F_n. Complete enumeration of F11's 56 permitted triples gives exactly 33 different final-seven keys, as checked by the executable. Therefore 16<=q_2(F_n)<=33 for all n>=11. For n=9 the suffix count is 30, for n=10 it is 32, and for n=8 the V-suite separates 15 of 20 history signatures: respectively 16..30, 16..32 and 15..20 bounds.

The one-CANCEL q_1(F_n)=9 claim for n>=8 was an earlier author-side, unreviewed result; this note independently establishes the two-CANCEL lower and upper theorems, without claiming q_2(F_n)=16 or q_2(F_n)=33.

## Exact computation, provenance, and remaining problem

REPRO_STAGE415B.py is a standalone Python-standard-library exact-integer reproducer. It constructs every original F_n triple, computes complete native-X6 endpoint vectors, directed adjacency counts, absolute aligned K, and attempted-action results. It exhaustively checks all 12 F7 histories against U1/U2/U3, all 30 F9 histories against V1/V2/V3, all F_n for n=5..22 for fiber size and suffix/signature counts, the Stage414-key split, and prefix-padding h=0..12. Two independent local executions produced byte-identical JSON stdout, marker STAGE415B_TWO_CANCEL_EXACT_CERT_PASS. The complete generated stdout may be regenerated by python3 REPRO_STAGE415B.py; REPRO_STAGE415B_EXECUTED_SUMMARY.json records the key executed outputs. The finite executable uses only +E1/-E1 APPs; the full-twelve-direction all-horizon seven-tail statement is the symbolic Theorem415.1. No float computation, formal proof assistant certification, native role CLAIM, Result, Driver approval or P000 change is claimed.

Next: Stage416-B must decide exact minimal quotient for n>=8 in the two-CANCEL language, distinguishing any histories not separated by V1/V2/V3 or constructing a sound budget-sensitive bisimulation that closes the gap 16..33. Reuse Stage412 Euler/K residual-edge DP to count symbolic classes without enumerating all history words, while preserving full joint K and directed J.
