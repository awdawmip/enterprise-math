# Stage195 — author-level exact optimal interval (N14 external ternary IID)

Date 2026-10-27. Status AUTHOR_EXACT / PORTABLE_RESEARCH / UNREVIEWED / NOT_ADMITTED.

Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 canonical main@f9f5620c6fa2b9cfff8b49551878080e158a98d9; Enterprise Math initial main@3d8ac3b6ea6782d8633c19efa1bfd15b7d29bc60; original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches global startup projection. P000, ACTIVE worldview, research protocol, BRC priority, joint observer safety and native X6/time typing were loaded. Immediate Stage194 author-predecessor: 24386bb9384ba04fce58f132a50cc7b382ca4bf8. This paper is an external finite IID auxiliary model, not a native P000 Cell transition theorem.

Set N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies randomize stopping/deciding P or Q based on entire ordered histories, stopping by N. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P[T], tQ=E_Q[T]. Define V14(alpha)=min max(tP,tQ) with both errors <=alpha.

## Theorem

alpha194=1849072830472476953/5258930030792146944;
V194=1153308642566039965/109561042308169728.

For **every real** delta, including irrational delta, such that 0<=delta<=13382075/676302730297344,

V14(alpha194+delta) = V194 -(165537648/535283)*delta.

In particular alpha195=1849072934531492153/5258930030792146944 and V195=1153307972138565565/109561042308169728. For every alpha>alpha195, the **fixed Stage195 Bellman supporting line** is strictly below V14(alpha). No formula for V14 beyond this endpoint is asserted.

## Universal Bellman inequality

At count state s=(n,a,b) (a,b are counts of symbols 0,1), ell(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Put K=L=82768824/535283>0 and H=1748561457410484827718287/14661540852461004128256. The finite exact backward recurrence is h(s)=min(K*ell(s), L, 1+sum_i P_i*h(child_i(s))), disallowing continuation at n=14. Fraction arithmetic over all 680 states yields h(root)=H, precisely 1238 strict positive alternative-action gaps, minimum 3412925531/88797026304, and exactly two ties: Y=(9,5,2) P/C and Z=(14,0,0) terminal P/Q.

At every *ordered* prefix the same count state has the same IID suffix law; Bellman conditional induction and convexity of random actions yield tP+K eQ+L eP>=H for any full-history randomized policy. Thus V14(alpha)>=H-(K+L)*alpha for every real alpha, with K+L=165537648/535283.

## Attaining full-real family

Choose the unique minimizing action outside Y,Z. At Y choose P with probability y, else continue; at Z choose P with probability z, else Q. Y has a=5 whereas Z has a=0, and symbol counts cannot decrease, hence Y cannot precede Z. Z at depth 14 cannot precede Y at depth 9. Consequently the two first-hit cones are disjoint, with **exact zero mixed term** in the four-observable vector O=(eP,eQ,tP,tQ).

Exact rational suffix DP gives O(y,z)=B+y DY+z DZ:

B=(309449721742548403/876488338465357824,56196512771291/160489808068608,1153308642566039965/109561042308169728,137455194880391/13374150672384).

DY=(-1753375/12524124635136,14825/82556485632,-9579725/1565515579392,-670775/185752092672).

DZ=(-6103515625/78364164096,6103515625/78364164096,0,0).

Independent unmerged **ordered-history** integer-mass DFS agrees at all 4 deterministic corners using P=(3,1,20)/24, Q=(2,2,20)/24 and 24^14 denominator. DFS nodes for y,z=00/01/10/11 are respectively 139054/139054/132142/132142 = 542392 total. Each corner has 144 first-hit Y ordered paths and 1 first-hit Z path, with zero ancestor intersections. This applies BRC positive-rational branch mass and ordered provenance; count compression is certified only for these finite-IID four observables and fixed horizon, not for native X6 dynamics or signed amplitude.

Solving eP=eQ gives

z(y)=1525099996562693/81920000000000000 - (1050385239/512000000000000)*y.

The left z(0) is exactly the Stage194 endpoint Z coin. For all real y in [0,1], 0<z(1)=1524931934924453/81920000000000000<z(0)<1, so both coins are legal. Substitution:

eP(y)=eQ(y)=alpha194+(13382075/676302730297344)*y;
tP(y)=V194-(9579725/1565515579392)*y;
tQ(y)=137455194880391/13374150672384-(670775/185752092672)*y.

The affine time gap is positive at y=0: 336736865504653/1352605460594688, and at y=1: 3030601257510677/12173449145352192; hence tP>tQ throughout. Common error strictly increases and tP strictly decreases. The slope ratio (9579725/1565515579392)/(13382075/676302730297344) = 165537648/535283=K+L. Every used action is Bellman minimizing and achieves tP+K eQ+L eP=H. For every real delta in range choose y=delta/Delta195, z=z(y), proving exact attainment of the universal bound.

## Right-side fixed-support strictness

A finite-horizon history-dependent behavioral policy space is a finite product of compact simplices; error/time functionals are continuous, so feasible minima are attained. Equality with the fixed line at alpha>alpha195 would require eP=eQ=alpha (K,L>0) and every reached action Bellman minimizing (strict other gaps, positive prefix masses). Thus only the Y,Z tie histories may randomize. The 144 Y first-hit ordered histories have identical P weights, Q/P ratios and IID continuation observables; averaging their conditional coins preserves the four outputs. Z is one terminal history. Since cones are disjoint, any equality policy reduces for this declared observer to O(y,z) with y,z in [0,1]. Error equality forces the displayed z(y), whose attainable common error is bounded by alpha195 since it is strictly increasing in legal y<=1. Contradiction; compact attainment yields strict inequality.

## New exact dual-only Stage196 frontier, evidence and admission

Along the saturated Y=P / terminal Z P-Q tie, decrease K,L in direction (-1,-1). Exact Stage195 Y-continue gap opens with rate 535283/71663616. The first strict gap closes at step 7980326496/928716005, U=(10,2,2), C/Q. Fresh exact Bellman: K196=L196=253368/1735; H196=168137908605541983707/1485065690661519360, only U Q/C and Z P/Q ties, 680 states, 1238 positive gaps, minimum 9719/249840. Stage196 primal remains to be proved.

Local executed pass markers: STAGE195_AUTHOR_EXACT_FULL_REAL_PASS, STAGE195_REFERENCE_FULL_REAL_PASS, STAGE196_DUAL_SCAN_PASS. Executed sources, full stdout, exact certificates, SHA256 manifest and full proof are in EM_STAGE195_AUTHOR_EXACT_PORTABLE_20261027.tar.xz, archive SHA256 f8503c46fc942955761caa2812865e4ad68ecfaa17b0aed5b30e13576714cd77. GitHub source readback does not imply remote execution.

Native service observation: research_authority_granted=false and em_control_tasks returned CONTROL_QUOTA. Current active Source owner/CLAIM could not be established. This is an author-level portable result by the actual Researcher-2 task conversation, no borrowed native identity, Source Result, Driver acceptance or X6 transition theorem. Formal activity registration is pending.
