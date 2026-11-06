# S23 tagged AV n=1000: optimized six-state full-ML lower bound

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor all-type exact ML partition theorem: commit 17329071ce4ab4e91c9346b77e9dbac5e131da0d.

For a,c in [1/2,7/8] set P_(a,c)=(a,(1-a)c,(1-a)(1-c)) on tags (stop1,stop3,stop4), and B_(a,c)=((1-a)c,1-(1-a)c). For n=1000 IID tagged observations with shared hidden (a,c), let delta_1000=inf_K sup_(a,c) TV(P_(a,c)^tensor1000,B_(a,c)^tensor1000 K) over parameter-independent stochastic kernels K.

Fix six rational q_j=Pr(stop4):
(1/28,65126/1000000,102302/1000000,146248/1000000,195886/1000000,1/4).
Each a_j=3/4-q_j and c_j=1/(1+4q_j) is legal and gives the identical compressed probability z=(1-a_j)c_j=1/4. Thus any K has a common output Q under all six hypotheses.

Use common integer denominator D=3500000; let Z=D/4=875000, A_j=D*(3/4-q_j), B_j=D*q_j. For all u,s>=0,u+s<=1000 define H_j(u,s)=B_j^u A_j^(1000-u-s). Let
M = sum_{u,s} C(1000,u)C(1000-u,s) Z^s max_j H_j(u,s).
The new exact rational six-hypothesis lower certificate is R_opt=(M-D^1000)/(6D^1000). Theorem:

**delta_1000 >= R_opt > 808199/1000000 = 0.808199.**

Decimal display (computed only after exact inequality): R_opt=0.808199574601456413140793752932214425667873944....

Proof: a complete word with u stop4 and s stop3 has probability D^(-1000) B_j^u Z^s A_j^(1000-u-s) under j. Its ML classifier therefore chooses the largest H_j. For i<j, B_j>B_i and A_j<A_i, so H_j(u,s)/H_i(u,s) is increasing in s. Smallest-index tie breaking yields a nondecreasing winning j for each u, and exact integer binary search finds its contiguous segments; those segments partition *every* (u,s) type.

If E_j denotes the disjoint exhaustive ML classes of complete words, then for a common output Q,
6 max_j TV(P_j^tensor1000,Q) >= sum_j(P_j(E_j)-Q(E_j)) = M/D^1000-1.
Infimizing over K proves the inequality. VERIFY.py computes each type-class mass with integer multinomial recurrence, checks exact divisibility and cross-multiplies the final threshold. All 501501 integer count types are covered by 1861 disjoint winning intervals; 296 u values have multiple winning classes. Type counts by j are [33241,22309,27184,31359,34761,352647]. Exact numerator and denominator have bit length 21742.

The four interior q values were discovered with noncertifying floating-point numerical exploration, then fixed to rational inputs. All asserted probabilities, classifier decisions and final inequality are calculated with exact standard-library integers/Fraction. The result improves the predecessor fixed-six ML lower R=0.808109549737987955... and sixty-strip lower R_60=0.808102201302498981....

Scope: exact author-side theorem for the *conditional tagged AV auxiliary model*. Transfer to the original ten-label S23 R_beh(k,10) still needs a lawful observer/encoder/decoder bridge; independent mathematical review and native formal Result admission remain pending.
