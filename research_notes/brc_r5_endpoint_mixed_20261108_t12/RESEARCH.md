# R5: endpoint-inclusive four-parameter mixed-capacity Blackwell prism

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source, precise model and immutable scientific inputs

This is new directed, author-side mathematical work in the seven-likelihood-ratio P/Q-BRC terminal statistical observer. It continues PR #1811, immutable commit \`0c9ea943b58cb11774e0619a889c91f8253b2d94\`, and its \`RESEARCH.md\`, \`AFFINE_CORNER.md\`, \`VERIFY.py\`. The predecessor established a complete prism on \`t>=1/1000\` and a single positive-residual \`t=0\` corner. The present exact theorem has a four-parameter box touching \`t=0\`, both signs of history residual and independently variable physical side capacities. The frozen scientific provenance is global \`a01383f825ef9d43b4b754254303298c64041568\`, EM \`86149263e38c22292c9def1e0f69092efa1be77e\`. Current norms/P000/ACTIVE worldview are separate current reads; no rebase of the frozen scientific model, P000 alteration or native Heartbeat physical claim is made.

All quantities refer to the seven-node model with ordered likelihood ratios
\`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\`. The only preserved observer here is \`(e_P,e_Q,T_P,T_Q)\` for **every randomized seven-node terminal declaration**.

## All-real theorem

For **all real** parameters
\[
0\le t\le1/50,\qquad 0\le p\le77/152,\qquad
17/2112\le q\le1,\qquad 0\le\theta\le1,\qquad \kappa=3/4,
\]
define legal FULL_HIST flow \`x=(g,a,b,u,v,w,z)\`:
\[
x=\left(1,t,1,(13t/40+1/80)p,\ 27/160+t\theta/10,\
(3t/40+21/80)q,\ t\theta/10\right).
\]
Define an **explicit seedless target** (where unprimed \`u,v,w\` come from x):
\[
\boxed{y=(1,0,1,\ u+23t/160,\ v+37t/80,\ w-17t/160,\ 0).}
\]
For each such \`x\` there is a nonnegative, declaration-independent \`7 x 7\` Blackwell transport matrix from \`y\` to \`x\` that matches all Q-node masses and all likelihood-ratio-weighted P-node masses, and satisfies
\[
\boxed{(e_P,e_Q,T_P,T_Q)_x=(e_P,e_Q,T_P,T_Q)_y.}
\]
The same equivalence holds for each source/target interpolant \`(1-h)x+hy\` for \`0<=h<=1\` using \`(1-h)Q+h diag(M(y))\`. The source historical residual is \`R=(9t/10)(theta-3/4)\`, so this box contains strictly negative and strictly positive historical residuals with both physical side branches active.

## Exact mass and stopping-time laws

For any \`f=(g,a,b,u,v,w,z)\`, Q-mass vector is:
\`\`\`
M0=509*u/900+47*z/180+67*(v-z)/162+w/100
M1=13*a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9*b/40-v+191*(u+w)/450+43*z/90+14*(v-z)/81
M4=(g-b)/2
M5=3*a/40+21*b/80-w
M6=u/100+47*z/180+67*(v-z)/162+509*w/900
T_P=1+g+3*a/8+5*b/8+u/2+v+3*w/2
T_Q=1+g+(a+b)/2+u+v+w
\`\`\`
For nonnegative \`Q_{ij}\` with target row i and source column j, required equations:
\[
\sum_jQ_{ij}=M_i(y),\quad
\sum_iQ_{ij}=M_j(x),\quad
\sum_i r_iQ_{ij}=r_j M_j(x),\quad T_P(y)=T_P(x),\ T_Q(y)=T_Q(x).
\]
They preserve *each* terminal-decision probability under both P and Q.

## Proof — legal seedless target and sharp target capacity

\`a'=z'=0\` implies \`9b'z'=4a'(v'-z')=0\` identically. At \`t=0\`, \`x=y\`. Throughout the parameter box, the target satisfies
\[
0\le u'=(13t/40+1/80)p+23t/160\le1/80,
\]
\[
0\le w'=(3t/40+21/80)q-17t/160\le21/80,
\]
\[
0\le v'=27/160+t(\theta/10+37/80)\le9/50<9/40.
\]
The bound for \`u'\` is saturated at \`t=1/50,p=77/152\`; the lower bound for \`w'\` is saturated at \`t=1/50,q=17/2112\`. These are **sharp physical-capacity faces of this explicitly chosen target**, not global nonrealizability limits. The source is lawful by parameterization. For the two stopping times, exact algebra gives
\[
T_Q(y)-T_Q(x)=t(-1/2+23/160+37/80-17/160)=0,
\]
\[
T_P(y)-T_P(x)=t(-3/8+23/320+37/80-51/320)=0.
\]

## Proof — eight exact transfers, sixteen vertices, convex interpolation

At \`t=1/50\` the 8 vertices \`p∈{0,77/152}\`, \`q∈{17/2112,1}\`, \`theta∈{0,1}\` have **eight exact rational, strictly-positive** Blackwell matrices with a total of **96 positive edges**. Their complete sparse supports appear in \`VERIFY_R5_ENDPOINT_MIXED.py\`; the program reconstructs a **unique Fraction solution** to all 7 row-mass, 7 column Q-mass and 7 column P-mass equations by exact rational Gaussian elimination. It checks positivity, normalizations under P,Q, source and target lawful capacities and both times. There are no floating-point optimizers, estimated coefficients or unverifiable free parameters. At \`t=0\`, all 8 remaining vertices use exact identity transports \`diag(M(x(0)))\` since \`x(0)=y(0)\`.

For any real point let \`lambda=50t\`, \`beta=152p/77\`, \`gamma=(q-17/2112)/(1-17/2112)\`, \`epsilon=theta\`. The 16 product vertex weights
\[
W_{ijkl}=\lambda^i(1-\lambda)^{1-i}\beta^j(1-\beta)^{1-j}
\gamma^k(1-\gamma)^{1-k}\epsilon^l(1-\epsilon)^{1-l}
\]
are nonnegative, sum to one, and exactly interpolate \`x\` and \`y\` (both **separately affine** in each parameter). The matrix \`Q=sum W_{ijkl} Q_{ijkl}\` satisfies every linear mass/moment equation, physical inequality, normalization and stopping-time equality; every target stays in the common affine seedless face \`a'=z'=0\`. Hence the claimed conclusion holds for **every real parameter** including irrational values and the endpoint \`t=0\`.

## Actual local verification and audit scope

The executed Python standard-library \`Fraction\` checker returned:
\`\`\`
EXACT_8_NONTRIVIAL_ENDPOINT_CERTIFICATES_PASS 96
EXACT_8_SEEDLESS_ZERO_ENDPOINT_IDENTITIES_PASS
EXACT_151_INTERIOR_AND_BOUNDARY_INTERPOLATION_CHECKS_PASS
AUTHOR_PROVED_ALL_REAL_T_0_TO_1_50_P_0_TO_77_152_Q_17_2112_TO_1_THETA_0_TO_1_KAPPA_3_4
\`\`\`
The *all-real proof* is the complete exact 16-vertex certificate plus the multi-affine interpolation argument; 151 rational regression cases are implementation checks. The predecessor's immutable \`VERIFY.py\` is the reference for all seven mass and stopping-time formulas. The present new checker independently solves each vertex from sparse support only and rechecks the laws. Author-side, directed/nonblind, unreviewed; independent proof review and formal project admission remain future actions.

## Next mathematical unit

The present explicit \`a'=z'=0\` construction touches both physical sharp faces. Extend \`q<17/2112\` by changing the affine \`u,w,v\` correction (choose a different coefficient \`alpha\` that keeps \`w'≥0\`), and extend \`p>77/152\` by exploring positive \`a'\` and a moving seedless chart or an alternate representation. Then allow \`kappa\` to vary, preserving actual source flow and history residual. Distinguish a particular target's saturation from an obstruction to the mother FULL_HIST-to-seedless equivalence conjecture.

Control provenance: GitHub identity \`awdawmip\`; new service-issued Researcher-ID \`EM-DIRECT-7D1657 / TASK_RESEARCH\`, native activity \`RA-7F2C252BC38C71BCE022DB13\` registered canonical main at \`c41bf1a899efc198d7c01d25bc645da37a57c51f\`. No formal Task CLAIM or Result/Review authority is claimed, and no private session capability is included.
