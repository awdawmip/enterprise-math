# R5 — Exact low-excess nonadaptive spectrum through 425

**2026-11-20; independent portable R5 author result; NOT_REVIEWED.** This is a theorem about frozen scalar nonadaptive physical-query **labels used as unit prices** (integer budgets 214..314), not an X6/BRC dynamical or native-heartbeat theorem. All queries are fixed before observation; query order is irrelevant. The original 256-hypothesis model allows up to \(f\) unflagged adversarial wrong readings and \(e\) identified erasures.

## Immutable inputs and predecessor

Keep original science pin \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551\`, exact integer-center source \`EXACT_R5_ALL_101_BUDGETS.json\`, SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`, and \(\tau=58182461585441404127941754879\). The previously published 32,640-pair/53-support-mask certificate gives these five minimal separating price-label sets:
\[
S_1=\{214,\dots,218\},\quad
S_2=\{214,216,\dots,221\},\quad
S_3=\{215,216,\dots,221\},\quad
S_4=\{223,\dots,290\},\quad S_5=\{296,\dots,312\}.
\]
Any unordered multiset has the required mixed-fault unique-decoding property **iff** each \(S_i\) occurs at least \(m=2f+e+1\) times, with multiplicities counted. The established unique optimum has cost \(735m\), consisting of \(m\) copies each of 216,223,296. The prior 2026-11-20 theorem classified all designs with excess \(0\le D\le212\) via three Gaussian polynomials. This note does not change the frozen scientific input or the finite witness certificate.

## New theorem — closed coefficient formula through 425

For integer \(m\ge1\), define
\[
G_{n,r}(q)=\left[\begin{smallmatrix}n+r\\r\end{smallmatrix}\right]_q,\quad n\ge0;\qquad G_{n,r}=0\ (n<0),
\]
where \(G_{n,r}\) generates size-\(n\) unordered multisets from \(\{0,\dots,r\}\) by sum. Put
\[
B_m=G_{m,2}G_{m,67}G_{m,16},
\quad O=q^{222}+q^{291}+q^{292}+q^{293}+q^{294}+q^{295}+q^{313}+q^{314},
\]
\[
P=q^{214}+q^{215}+q^{219}+q^{220}+q^{221},\quad
T=q^{213}+q^{217}+2q^{218}+2q^{219}+q^{220},\quad
U=q^{216}+q^{217}+q^{218},
\]
and
\[
A_m=P G_{m,2}+q^{216}G_{m+1,2}+T G_{m-1,2}+U G_{m-2,2}.
\]
Then for every \(f,e\ge0\), \(m=2f+e+1\), and every integer \(0\le D\le425\), the **exact number of feasible unordered nonadaptive query multisets** of cost \(735m+D\) is the coefficient \([q^D]F_m(q)\), where
\[
\boxed{\begin{aligned}
F_m(q)\equiv{}& B_m + A_m G_{m,67}G_{m,16}+O B_m\\
&+q^{223}G_{m,2}G_{m+1,67}G_{m,16}\\
&+q^{296}G_{m,2}G_{m,67}G_{m+1,16}
\pmod{q^{426}}.
\end{aligned}}
\]
The Gaussian factors are untruncated polynomials; congruence means equality of coefficients at degrees \(0,\dots,425\). This explicitly classifies 426 consecutive integer cost levels, including 213 new levels beyond the earlier result. **First correction:** \([q^{213}](F_m-B_m)=1\) for every \(m\ge1\). The simple one-excursion formula has a sharp uniform boundary: at excess \(D=426\) and \(m\ge2\), replacing two 216 queries by two 214 and two 215 queries yields an additional valid multiset not covered by these correction terms.

## Proof

Write \(c\) for the total number of central queries \(\{216,217,218\}\), \(a\) for 214 occurrences, \(b\) for 215 occurrences, and \(d\) for the total number of \(\{219,220,221\}\) occurrences. The three early constraints become
\[
a+b+c\ge m,\qquad a+d+c\ge m,\qquad b+d+c\ge m.
\]
Let \(n_M,n_L\) count queries in \(M=\{223,\dots,290\}\) and \(L=\{296,\dots,312\}\). Necessarily \(n_M,n_L\ge m\). All other available prices are exactly \(\{222,291,292,293,294,295,313,314\}\) and support none of the five minimal witness constraints.

The cheapest schedule for each independent block costs \(216m\), \(223m\), and \(296m\). All price increments within a fixed block are nonnegative. If \(c=m\) and \(a=b=d=0\), exactly \(m\) central queries generate \(G_{m,2}\). Adding one early partial-support query gives \(P G_{m,2}\) with excess at least 214; adding two gives excess at least 428. If \(c=m+1\), with no partial query the excess is 216 and the generator is \(q^{216}G_{m+1,2}\); one partial query adds at least 214 and brings the excess to at least 430. If \(c\ge m+2\), excess is at least 432.

For \(c=m-r<m\), the early constraints require \(a+b,a+d,b+d\ge r\). At \(r=1\), exactly two partial-support queries can be (214,215), (214,219/220/221), or (215,219/220/221); this gives the polynomial \(T\) with \(c=m-1\). Using at least three partial queries costs at least 427 in excess (the cheapest feasible triple is two 214 and one 215). At \(r=2\), exactly three partial queries must have \(a=b=d=1\), with \(d\)'s price 219/220/221, giving \(U\) with \(c=m-2\). Four or more partial queries cost at least 426 excess (the cheapest feasible quadruple is two 214 and two 215). For \(r=3,4\), direct minimization under the same three inequalities gives minimum early excess respectively 429 (multiplicities \(a,b,d=(2,2,1)\)) and 432 (\((2,2,2)\)). For \(r\ge5\), the inequalities imply \(a+b+d\ge\lceil3r/2\rceil\), so the excess is at least \(214\lceil3r/2\rceil-216r\ge632>425\). Thus these four cases enumerate **all** early deviations of excess at most 425 and yield \(A_m\). For \(m=1\) the negative-index Gaussian terms vanish.

Independently, the middle block can contain one extra query (cheapest excess 223), contributing \(q^{223}G_{m+1,67}\), and the late block can contain one (cheapest 296), contributing \(q^{296}G_{m+1,16}\). Two middle extras cost at least 446 and two late extras at least 592. One outside query contributes \(O\), while two outside queries cost at least 444. Finally, the minimum excess of any two distinct excursions is \(213+214=427\) if they both occur inside the early group, and at least \(213+222=435\) across independent groups. Hence **at most one** such excursion can occur at \(D\le425\), and every listed correction is disjoint. Multiplication by the unmodified Gaussian factors generates all internal price upgrades, yielding the displayed formula. The 426 counterexample proves the sharp uniform truncation boundary. QED.

## Reproducibility and evidence scope

Author-side script \`VERIFY_R5_LOW_EXCESS_425.py\` uses the SHA-matched archived frozen integer input and exact five witness sets. It computes the theorem's coefficient polynomial through degree 425 and separately enumerates bounded partial-price multiplicity vectors and the cover inequalities. For \(m=1,2,3,4,8,17\), **all 426 coefficients** agree between implementations, using Python arbitrary-precision integers. The predecessor's original verifier was also re-run on the same frozen bytes, returning PASS for 32,640 named pairs, 53 separation patterns and the five minimal sets. These checks are author-side, not independent project Review.

Scientific observer scope: the five-set reduction is exact only for the fixed scalar readout and fixed multiset query game. It retains the joint witness separation incidence and does not reduce native X6 path/branch identities or assert BRC equivalence.

## Frontier and research tasks

Extend the exact spectrum to \(D\ge426\) by adding the first multi-partial corrections and overlapping excursions, or derive a uniform rational/diagonal generating function for arbitrary excess. Separately, the original full adaptive eight-error question remains at previously reported \(8335\le C_8^*\le8343\); a verified decision-tree strategy or a new finite lower-bound certificate would be needed to change it. Retain existing provenance \`EM-DIRECT-4C3E47\` as historical research-source attribution; this portable note grants no current CLAIM, RUN or Review authority.
