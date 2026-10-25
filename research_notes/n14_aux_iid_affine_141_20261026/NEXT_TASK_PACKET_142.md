# Stage142 — continuation from Stage141 exact author frontier

Scope: external ternary iid N=14 only. P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Complete ordered-history randomized tests, errors eP=P(decide Q), eQ=Q(decide P), minimizing max(tP,tQ). No native P000/X6 theorem claimed.

Verified Stage141 **author** result (independent Research Driver review still pending):

~~~text
alpha140=12238132303043365565/35205614928358539264
V140=72273280897285196803/5867602488059756544
eta141=1456203515/1466900622014939136
alpha141=12238132337992249925/35205614928358539264
V141=72273275560058390723/5867602488059756544
K141=10454693976/22403131
L141=10073101432/22403131
V14(alpha140+delta)=V140-(20527795408/22403131)*delta
for ALL REAL 0<=delta<=eta141, with right-support sharpness.
~~~

Stage141 ties B=(11,0,1) Q/continue, Y=(9,6,2) P/continue. At alpha141, Y has P-stop probability 1 while B has interior Q-stop probability 48289749016996117/81438720000000000.

**Stage142 exact dual-only discovery:** Follow B tie ray (dK,dL)=(-43/1536,-7/288), now with Y uniquely P-stop. The first positive Bellman gap closes at lambda=10742567341705980715008/19621237215327572363 for J=(4,3,0), P vs continue. Exact candidate:

~~~text
K142=395290882339224/875825669873
L142=54591710813272/125117952839
Hroot142=20527217718648439652667729706057/63970915514357897417453469696
680-state Bellman: only ties B Q/continue, J P/continue;
1238 strict positive other gaps; zero negative gaps;
min positive gap=145705394717149261/3309864318741169728.
~~~

B and J path cones are disjoint: J has depth 4, a=3; B depth 11, a=0. J cannot precede B by count monotonicity, B cannot precede J by depth.

**First remaining question:** compute exact B,J literal first-hit masses and four observer corner vectors (including a separately implemented ordered integer-weight DFS), solve eP=eQ for B coin as function of J coin, verify 0<=coins<=1 and tP>=tQ on a *nondegenerate* real alpha interval. Either prove Stage142 full-real optimality plus sharpness from complete dual gaps, or produce an exact feasibility obstruction. The prior Y P-stop remains fixed; do not double-randomize it.

Source inputs: Global main@0183fd75aab2551ce64bd1ab0a6e60a4bff3d4a3, Enterprise Math input main@d27c9cb7cd8c225b3983393ef8bda98d4a75e549. Native owner/session/CLAIM/Result unverified (CONTROL_QUOTA, STATIC_READONLY_SCOPE_DENIED); author source publication does not change native authority.
