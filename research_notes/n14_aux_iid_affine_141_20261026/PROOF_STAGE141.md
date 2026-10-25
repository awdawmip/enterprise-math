# Stage141 — exact full-real optimum and right-sharp support (author)

**Research status:** Author computation-assisted proof in an external finite iid sequential-test model. It has not been independently reviewed by Research Driver or promoted to a native P000/X6 theorem, Task CLAIM or frozen Result.

## Model and inherited source

Under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), any test may use the full ordered ternary observation history, randomized stopping and randomized P/Q decision, but must stop by N=14. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), V14(alpha)=min max(tP,tQ) under eP,eQ<=alpha.

Inherited Stage140 author-level endpoint (source blob 5387c19c5c43d0579cd832ca668b9bcb0331e7ed at Enterprise Math input commit d27c9cb7cd8c225b3983393ef8bda98d4a75e549):

\[
\alpha_{140}=\frac{12238132303043365565}{35205614928358539264},\quad
V_{140}=\frac{72273280897285196803}{5867602488059756544}.
\]
At that endpoint F=(5,3,0) is P-stop saturated, B=(11,0,1) is an interior Q/continue mixture.

## Exact theorem — full real interval

For **all real** \(\delta\) satisfying

\[
0\leq\delta\leq \eta_{141}=\frac{1456203515}{1466900622014939136},
\]

\[
\boxed{V_{14}(\alpha_{140}+\delta)=V_{140}-\frac{20527795408}{22403131}\delta}.
\]

The new exact endpoint is

\[
\boxed{\alpha_{141}=\frac{12238132337992249925}{35205614928358539264}},\qquad
\boxed{V_{141}=\frac{72273275560058390723}{5867602488059756544}}.
\]

This dual supporting line is **strictly below** the true value function for every \(\alpha>\alpha_{141}\). That does not mean the testing problem becomes infeasible above alpha141.

## Exact dual direction and Bellman certificate

At count state s=(n,a,b), with counts of symbols 0 and 1, the iid likelihood ratio is \(r(s)=Q(s)/P(s)=2^{a+b}/3^a\). For all nonterminal states:

\[
H(s)=\min\{K r(s)\;[\mathrm{P}],\;L\;[\mathrm{Q}],\;
1+\sum_{j=0}^{2}P_j H(\mathrm{child}_j(s))\;[\mathrm{continue}]\}.
\]

Continuation is excluded at n=14. The exact 680 count states cover every possible literal history via suffix-law sufficiency, without assuming that a competitor is count-Markov. Therefore for **all** ordered-history randomized policies,

\[
H(\mathrm{root})\leq t_P+L e_P+K e_Q
\leq\max(t_P,t_Q)+(K+L)\alpha.
\]

From the Stage140 dual K0=335982923928/696000641, L0=46093407704/99428663, the B continue-minus-Q affine cost has coefficients \((239/192,7/288,-43/1536)\) in \((1,K,L)\). The direction \(dK=-43/1536,dL=-7/288\) keeps B tied and decreases K+L. The former F P/continue tie becomes strictly P-optimal, with continue-minus-P directional derivative \(199752183967/2282521714753536>0\).

For the frozen locally optimal policy, exhaustive exact comparison of all positive action gaps along that ray yields the first closure at \(\lambda=8951513294009032704/15592593536406971\), state Y=(9,6,2), P versus continue. The closing gap at Stage140 was \(40470889820281/876760359475392\), with derivative \(-22403131/278628139008\). All 836 positive-gap closure candidates occur at or after this point; thus the Bellman policy remains optimal through the first closure by backward induction.

The new dual values are

\[
K_{141}=\frac{10454693976}{22403131},\quad
L_{141}=\frac{10073101432}{22403131},\quad
K_{141}+L_{141}=\frac{20527795408}{22403131}.
\]

Exact Bellman root:
\(H_0=541362578363817699004362379/1636340255550979191078912\).

At this new dual point the full 680-state Bellman computation has **1238 strictly positive nonselected-action gaps, zero negative gaps**, and minimum positive gap \(11615145378420647/231190470314164224\). The **only** ties are B=(11,0,1) Q/continue and Y=(9,6,2) P/continue.

## Positive literal branches and four-observer affine law

Use a BRC-like typed positive branch carrier: ordered ternary word and depth, P numerator weights (3,1,20) over denominator 24^n; Q numerator weights (1,1,10) over 12^n. We compress only after proving that this particular iid experiment's four observers (eP,eQ,tP,tQ) and suffix laws depend on the declared count state.

Y at depth 9 has six first-symbol events; B at depth 11 has zero. Counts cannot decrease, hence Y cannot precede B; B cannot precede Y because its depth is larger. Thus the two first-hit cones are **disjoint**. An independent literal-prefix integer DFS (no reuse of the Fraction Bellman observer recursion) confirms B has 11 first-hit ordered histories with P mass 107421875/1451188224, Q mass 107421875/725594112; Y has 117 first-hit histories with P mass 65/100663296, Q mass 65/286654464.

Let w in [0,1] denote immediate Q-decision probability at B and z in [0,1] immediate P-decision probability at Y. Choose the unique Bellman action everywhere else. Then \(M=(eP,eQ,tP,tQ)\) is exactly affine:

\[
M(w,z)=M_{00}+w d_B+z d_Y.
\]

~~~text
M00=(
 2428854347846962769/7011906707722862592,
 447683877048541/1283918464548864,
 10843897619210051711/876488338465357824,
 1272910804099433/106993205379072)
dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128)
dY=(
 -1141985/400771988324352,
 154375/35664401793024,
 -12336545/16698832846848,
 -877435/2972033482752)
~~~

The independent integer-weight literal DFS agrees **exactly** with the Fraction observer calculation for all four deterministic corners (w,z)=(0,0),(1,0),(0,1),(1,1), visiting respectively 650290, 650158, 643270, 643138 literal prefix nodes. The cross-corner mixed four-vector defect equals (0,0,0,0).

## Primal attainment over all real parameters

Equalizing the two errors gives the exact compensation

\[
\boxed{w(z)=\frac{48289598022407437}{81438720000000000}
+\frac{1258288239}{678656000000000}z},\quad 0\leq z\leq1.
\]

The endpoints w(0)=48289598022407437/81438720000000000 and w(1)=48289749016996117/81438720000000000 are both strictly in (0,1). Every real z in [0,1] therefore gives a valid randomized policy with

\[
e_P=e_Q=\alpha_{140}+\eta_{141}z,\quad
t_P=V_{140}-(K_{141}+L_{141})\eta_{141}z,
\quad t_P+L_{141}e_P+K_{141}e_Q=H_0.
\]

At z=0 and z=1 respectively,

\(t_P-t_Q=82703190692937556807/158425267177613426688>0\) and
\(82703143791980924407/158425267177613426688>0\).
This difference is affine, so tP=max(tP,tQ) on the whole real interval. The constructed policies attain the global Bellman lower bound; this proves the theorem.

## Strict right sharpness

The finite-horizon behavioral strategy space is compact and feasible minima attain. Suppose an alpha>alpha141 attained the same supporting line. Equality throughout the Bellman chain with K,L>0 would force eP=eQ=alpha and Bellman-minimizing actions on every reached prefix. The 1238 positive gaps restrict mixed actions to B,Y. Any literal-history-specific tie randomization has the same four-observer effect as an effective pair (w,z) in [0,1] because all histories in a count state have the same prefix likelihood ratio, iid suffixes, and disjoint B/Y cones. Error equality forces the displayed compensation w(z); hence alpha=alpha140+eta141*z <=alpha141. Contradiction.

## Verification and governance boundary

Actually executed locally: exact Fraction Bellman/observer algorithm and a separate integer-weight literal-prefix DFS, four corners, result PASS_STAGE141. A separate exact locally executed ray scan established **only** a Stage142 dual candidate. The GitHub CHECKER_STAGE141.py is a portable source adaptation of the Stage140 checker, not byte-identical to the executed author program, and is **not claimed remotely executed**. The full local source, certificate and run logs are in the Stage141 attached archival bundle.

Fixed GLOBAL_KNOWLEDGE_V1 source read main@0183fd75aab2551ce64bd1ab0a6e60a4bff3d4a3; Enterprise Math research input main@d27c9cb7cd8c225b3983393ef8bda98d4a75e549; P000 original verified blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. No native X6, physical, or six-axis-space theorem is inferred. GitHub authenticated login was awdawmip, but native control returned CONTROL_QUOTA and native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The active native owner, formal Researcher session, CLAIM and Result remain unverified. Independent Research Driver review is pending.

Stage142 precise dual and primal question are in NEXT_TASK_PACKET_142.md.
