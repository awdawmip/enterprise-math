# R284GP addendum: relaxation boundaries and count correction (2026-11-24)
Frozen reference: R284GP proof note commit 4b5d6d5a9a0fc6d775273ad557b66cd06fb10567; SMT query 46993baa50424690e4bba39b3a625f9ebdd09455. Same auxiliary four-phase binary tag model; independent review pending.

## Exact aggregate correction
Re-summed the actual 32 C++ critical-width output rows (u=5,q=6..16; u=6,q=7..20; u=7,q=8..14). The checked count is 9,635,990,195, correcting the transcription in the frozen GP note. Opposite pass 8,798,877,387; GE+opposite pass 687,153; first edge failure 351,336; second edge failure 335,817; later edge failures 0; survivors 0. No proof implication changes.

## One crossing condition is insufficient for the relaxation
Delete only the second cross assertion from the frozen SMT query and request a model. Z3 returned SAT: q=7,u=4, (x1,...,x7)=(1,0,3,0,31,23,1). Width 59 < F=60. Direct exact arithmetic check: GE values (25,41,24,40), threshold 24; both opposite maxima 9, threshold 9. For each crossing, list (max(K0,C0,J0),lo,hi,m,q-P+2r): first (9,0,2,42,24), true; second (0,0,22,12,25), false. Here m is the four-term maximum in GP. Thus the first crossing alone does not exclude all subcritical candidates of the GP relaxation.

## Rational relaxation and the integer gap
Replace Int by Real and QF_LIA by QF_LRA in the frozen query, retain strict inequalities, request a model. Z3 returned SAT at q=21/10,u=1, x=(0,0,69/10,0,22/5,69/10,1/10), width 183/10 < F=92/5. Direct rational check: GE values (36/5,71/10,71/10,71/10), threshold 71/10; opposite maxima 27/5,11/2, threshold 3; crossing tuples (27/10,5/2,59/10,81/10,81/10) and (27/10,12/5,59/10,81/10,81/10), both true. This is a witness only for the algebraic real relaxation, not a fractional protocol.

Strengthen the real query by replacing q>u with q>=u+1 and both n<F bounds with n<=F-1 in their respective branches. Z3 returned UNSAT. These replacements retain all integer candidates. Therefore an independent rational linear certificate is a promising next route. No independent Farkas certificate has yet been completed. Further strengthening the crossing strict inequality lo>hi to lo-hi>=1 is also valid on integers and provides a finite affine disjunction route; it need not preserve every real feasible point. The original integer GP result is unchanged.

Next: independently certify the tightened rational system, then classify equality at n=F. Do not redo finite scans.
