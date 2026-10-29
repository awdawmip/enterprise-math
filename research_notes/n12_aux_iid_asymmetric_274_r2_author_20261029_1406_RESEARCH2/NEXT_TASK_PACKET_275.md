# Stage275 — Exact continuation beyond R274 M--Jnew

Date: 2026-10-29. Parent: Stage274 complete author proof at PROOF_STAGE274.md, REPRO_STAGE274.py and REPRO_STAGE274_EXECUTED_STDOUT.txt in existing Enterprise Math Draft PR #1571 (this branch's next commit). Scope remains **external** ternary-IID, horizon-12, four-observer full-ordered-history sequential decision. No native P000-X6 correspondence, formal Source CLAIM/Result, independent review or Driver acceptance is inherited.

## Fixed model and highest verified frontier

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), max observations N=12; errors eP,eQ, times tP,tQ. V12(a,b)=minimum max(tP,tQ) under eP<=a,eQ<=b.

Stage274 proved exactly:

~~~text
lambdaP = 445906494464/2706255861
lambdaQ = 76440567684/902085287
H = 1758667527952600918633/20945528728608964608
R274 = conv(K_e,J_e,Jnew_e,M_e)
area = 7179682704150390625/1104122877824872835186688
only Bellman ties: T=(0,0,5) P/C, S3=(1,2,6) Q/C
full ordered-history equality family:
  Obs(r,k)=K+r*(J-K)+(k/80)*(M-K)
  0<=r<=1, 0<=k<=80+3*r
~~~

Every (r,k) in this nested-history trapezoid is attainable, and R274 exactly characterizes all real caps saturating the Stage274 dual bound. The boundary M--Jnew has S3 continuing. Do not replace the 80+3r exposure rule with independent always-active coins. Stage274 is author-checked and not Source-admitted.

## Exact new exterior feasible point: upper bound only

Let S4=(1,2,7), whose unique Stage274-optimal action is Q. Starting from M (T:P,S3:C), replace only S4:Q by S4:C, defining deterministic M2. Independently executed unmerged ordered P/Q DFS: 10,573 nodes; 7,049 terminal words; both total source masses exactly 1.

~~~text
M2=(545662756283/7925422620672,9188342405/11609505792,
    13885256030731/2972033482752,64511064545/11609505792)
old Stage274 dual slack(M2)=1798033664453125/654547772769030144>0
~~~

The legal convex mixture (49/100)M+(49/100)Jnew+(1/50)M2 produces:

~~~text
a275 = 1175053055941/15850845241344
b275 = 867218405255/1114512556032
tP275 = 1079662613531/220150628352
tQ275 = 539955234235/92876046336 > tP275
~~~

Thus the currently proved claim is only V12(a275,b275)<=539955234235/92876046336. Exterior orientation: orient(M,Jnew,(a275,b275))=-39140485205078125/276030719456218208796672<0, and orient(M,Jnew,K)>0.

## One executable scientific operation

First derive the candidate exact positive Bellman multipliers from equality at T=(0,0,5) and S4=(1,2,7), while checking whether S3 becomes unique C. Solve the two affine equations exactly, then evaluate **all** 455 count states and 1,274 legal action costs with Fraction, reporting complete exact tie set and minimum positive gap. A different active-tie set is evidence to report, not a reason to force the hypothesized geometry.

For the true equality set, independently propagate complete ordered prefix paths to compute S4 reached-history count for T stopped/continued and the exact ancestry through S3; preserve conditional survival weights, multiplicities, separately labelled P/Q masses and any required cross-history correlation. Prove the entire four-observer zero-dual-gap family (not just four sample policies), its real error-cap projection, strict convexity/intersection along M--Jnew if applicable, and time objective dominance. Match an exact positive rational mixture saturating a275,b275 against the global dual to prove V12(a275,b275), or deliver a precisely checked obstruction. Recompute P/Q masses with a full-word DFS independent of the count recursion.

Persist complete proof, actually executed checker source/stdout, verification scope, unresolved parts and the smallest Stage276 question to the current authorized research PR with a head-CAS / no-force update and scoped readback. Leave status PORTABLE_AUTHOR_EXACT/UNREVIEWED/NOT_ADMITTED until legitimate Source identity/claim and independent review. The native three-dimensional X6 Cell bridge remains a separate problem; this external IID auxiliary model cannot be renamed a P000 or BRC-native dynamics theorem.
