# Stage416-B — sharp asymmetric native-X6 BRC memory window (2 POP, 2 CANCEL)

2026-11-04; Research2 author-side continuation of Stage415-B at immutable PR #1736 commit c9be77fdb06f4471de33d121295c6f17ac35381b. Status: proof candidate with exact executable counterexamples; UNREVIEWED / NOT_ADMITTED. Frozen scientific pins: GLOBAL_KNOWLEDGE bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral policy was read independently from GK canonical main ff372b67724de0d53d33702f8e5678c064a57f44 and Enterprise Math main 41e74ef42a2bc07ff5ffd59d5cfae11395e97135.

## Definition and mother objective

Let D={+E_j,-E_j | 1<=j<=6} be the twelve native-X6 direction labels. Each ordered source history (P,Q) consists of equal-length words initially. The full observer is O(P,Q)=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q)), where z denotes native six-component displacement, J the complete directed adjacent-letter histogram, and K the number of equal labels at aligned absolute positions up to the shorter word's length. Action enabledness is part of the observation language. Legal future actions are arbitrary paired APP(a,b), up to p independent Q POP actions, and up to c paired CANCEL actions, where CANCEL simultaneously deletes two terminal mutually inverse letters from each source and is permitted exactly when both independent inverse tests hold.

This is the Stage415-B BRC source-labeled observer and action semantics, with no change to original scientific inputs. A and B below are the genuine labels +E1 and -E1, embedded in the full twelve-direction alphabet; other axes remain available for future APP operations. Only typed direction paths and joint K are used, rather than a total-only BRC projection.

## Theorem 416.1 — general asymmetric all-horizon sufficient window

Let p,c be arbitrary nonnegative integers. Put L_P=max(2c+1,p+2c), L_Q=p+2c+1. Two initially equal-length source pairs with the same full O and the same respective last L_P and last L_Q original labels (entire word if shorter) have identical complete O and action enabledness under every common finite legal future trace with budgets (p,c) and arbitrary APP labels in D².

Proof. After any shared enabled trace, each source has the form P0[1:n-dP] followed by a surviving appended word U, and Q0[1:n-dQ] followed by a surviving appended word V. Each appended suffix is identical in the compared histories. The number of erased original labels satisfies 0<=dP<=2c and 0<=dQ<=p+2c; it is enough to track dP,dQ, surviving appended words and remaining budgets in a coupled induction.

Original endpoint contributions are recovered from the initial equal endpoints by removing precisely the original suffixes of lengths dP,dQ and adding U,V. Original directed adjacency counts are recovered from initial J by removing all original edges incident to each erased tail: at most dP+1 or dQ+1 terminal labels determine the removed edges and the surviving-original/appended junction. These requirements are met by L_P>=2c+1 and L_Q>=p+2c+1. Internal appended edges are common.

For K, the still-aligned original-original coordinates are exactly indices 1 through n-max(dP,dQ); subtract their omitted suffix-alignment contributions from the initial K. At most p+2c terminal original positions of *both* sources are required, met by L_P>=p+2c and L_Q>=p+2c. Original/appended mixed comparisons lie in these terminal positions; appended/appended comparisons are common. Hence current full O is equal for each successful common trace.

APP is enabled always. Q POP enabledness depends on the current length and remaining budget, already equal. Before an additional CANCEL is attempted, at most c-1 cancellations have been used, so dP<=2(c-1), dQ<=p+2(c-1). Thus all terminal labels needed for the two inverse tests lie in the original last 2c labels of P or last p+2c labels of Q, or in the common surviving appended words. The same enabledness decision follows. After an enabled action update the coupled invariant and repeat. When c=0 the CANCEL case is vacuous. A word shorter than the declared window is known in its entirety, covering boundary cases. Induction over arbitrary finite traces proves the claim.

For p=2 and c=2 this yields L_P=6, L_Q=7. This improves the Stage415-B (7,7) safe suffix to (6,7), without weakening the observer or restricting any future APP direction.

## Theorem 416.2 — componentwise sharpness at two POP and two CANCEL

The (6,7) raw original-suffix window is componentwise optimal among windows that store the last fixed number of labels of each source separately and compare identical initial full O.

Witness against P=5, with n=8:
H=(P,Q)=(AABAABAB, AAABABAA);
H'=(P',Q')=(ABAAABAB, AAABABAA).
Both have P-last-five=AABAB; Q is identical (hence in particular Q-last-seven equal), full O initially matches (including K=5). Both admit the exact trace POP_Q, POP_Q, CANCEL, CANCEL. At its end, H has (AABA,AA), whereas H' has (ABAA,AA): endpoints and directed J remain equal, but K is respectively 2 and 1. Thus five P labels are insufficient even when Q is fully known.

Witness against Q=6, with n=9:
H=(AAAAAABAB,AABABABAA);
H'=(AAAAAABAB,ABAABABAA).
P is identical; Q-last-six=ABABAA, and initial complete O matches (including K=6). Under the same four-operation trace, both produce P=AAAAA, but their Q endpoints are AAB and ABA. The directed adjacency histograms of these resulting Q words differ (AA,AB versus AB,BA). Thus six Q labels are insufficient even when P is fully known.

Both witnesses use valid P000 native signed direction labels; the full twelve-direction APP alphabet includes these traces. The sufficiency theorem and the two independent strict component lower bounds prove the exact (6,7) minimum in this uniform raw-suffix representation class. They do not assert the minimum number of quotient classes.

## Theorem 416.3 — revised stable upper bound for the Stage411-B defect fiber

Keep the complete Stage415-B observation fiber F_n:
P_i=A^(i-1) B A^(n-i);
Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
2<=r, r+2<=s<=n-1, i=r or s.

The exact number of distinct (P-last-six,Q-last-seven) keys is 32 for EVERY integer n>=11. Consequently, under two POP and two CANCEL, q_2(F_n)<=32 for all n>=11. Combining the Stage415-B proven sixteen-representative future-distinguishability construction yields
16 <= q_2(F_n) <= 32 for every n>=11.

Proof of key count. For n>=11, the seven-letter Q tail covers absolute positions n-6,...,n; the six-letter P tail covers n-5,...,n. Partition on which Q-defect positions are in this Q tail.

(i) Both r,s earlier than n-6: the Q suffix is all A and the chosen P defect is earlier than n-5, giving 1 key, realizable by (r,s)=(2,4).
(ii) Exactly s lies in the Q tail: if s=n-6, both possible i lie outside the P tail, giving 1 key. For each of the five values s=n-5,...,n-1, i=r gives the all-A P tail and i=s gives a distinct marked P tail, yielding 2 each: 11 keys total.
(iii) Both r,s lie in the Q tail: they lie among positions n-6,...,n-1 (six positions) with spacing at least two. There are C(6,2)-5=10 valid ordered pairs; for each the two choices i=r or i=s produce distinct P tails, including when r=n-6. Therefore 20 keys.

The three cases have distinct Q tail signatures, and within each case the counted pairs give distinct keys. Sum 1+11+20=32. The construction works uniformly for all n>=11. Sufficiency Theorem416.1 identifies every same-key group as all-future equivalent, proving the upper bound. The existing sixteen-history lower bound is precisely from Stage415-B Theorem415.3 and is an independent earlier author-side proof.

## Exact reproducibility and remaining question

REPRO_STAGE416B.js executes finite exact native-X6 endpoint, directed-J, absolute-K and enabledness logic. It checks both entire initial observation equalities and both four-action divergence certificates, all 144 possible one-step APP direction pairs for each initial witness, and the full (n-3)(n-4) defect family plus (6,7)/(7,7) suffix-key counts for n=5..25. It returns STAGE416B_SHARP_6_7_EXACT_PASS and agrees with independent local Python exact arithmetic on both explicit witnesses. This finite check supports the counterexamples and formula cross-check; the general all-horizon assertion is justified by the symbolic induction above.

Next scientific unit: establish the exact all-future quotient q_2(F_n) for n>=8, starting with equivalence or distinguishing tests inside the 16 Stage415-B trace-signature groups at n=9. Use the new (6,7) rather than (7,7) finite-state interface and preserve joint K in every transformation. Frozen scientific pins and original owner/claim authority remain unchanged.
