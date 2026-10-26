# Stage175 — exact primal continuation, currently DUAL ONLY

Mother problem: finite external ternary IID N14 full ordered-history sequential minimax test, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), tP/tQ and both errors constrained as in Stage174.

Frozen Stage174 author result:
alpha174=10295869835213079092569/29500515812940089131008;
V174=677877812657492293580503/59001031625880178262016;
K174=L174=16044588/70019;
at Stage174 endpoint terminal Z=(14,0,0) has Q decision probability z=1, and T=(8,2,0) has P decision probability t=3537410849994591/7720251392000000.

An exact dual-ray scan along dK=dL=-1 shows first positive gap closure at
epsilon=4258982656225980/1535633560488809.
Candidate:
K175=L175=4964732675352/21931669411,
H175=12727571546676169210383728225/75089267507105089342930944.
The new Bellman ties are B=(6,3,3): Q/continue and Z=(14,0,0): P/Q; T becomes uniquely P. The other 1238 gaps are strictly positive; minimum 39435024594685/2728650581438976. **This is only a candidate dual certificate, not a Stage175 primal theorem.**

First independent unit: use exact Fraction suffix DP and unmerged integer-numerator DFS to calculate (eP,eQ,tP,tQ) at all four deterministic B/Z corners, test first-hit cone disjointness and exact mixed-zero; derive balanced z(b), its maximal legal probabilities (not assumed [0,1]), Stage174 endpoint continuity, tP>=tQ, monotone alpha and dual tightness. If feasible, prove the next full-real interval and strict right support; if not, preserve a precise rational obstruction. Keep original P000/active worldview unchanged, treat auxiliary IID as external and report native CLAIM/Driver status truthfully.