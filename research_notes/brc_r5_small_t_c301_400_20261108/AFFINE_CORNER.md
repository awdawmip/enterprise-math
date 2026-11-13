# R5 — explicit affine 11-edge transport through the endpoint t=0

Date: 2026-11-08. **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / PORTABLE_ONLY.** This is a separate second scientific increment on the same frozen seven-node P/Q-BRC *statistical* observer as RESEARCH.md. No native Heartbeat physical dynamics or BRC–Shor arithmetic are calculated here.

## Theorem

For all **real** \(0\le t\le 1/50\), fix \(p=0,\ q=1,\ \theta=1,\ \kappa=3/4,\ g=b=1,\ a=t\). The lawful FULL_HIST source is
\[
x(t)=(1,t,1,0,27/160+t/10,21/80+3t/40,t/10).
\]

Define the following **explicit lawful seedless** target flow:
\[
\boxed{y(t)=(1,0,1,23t/160,27/160+9t/16,21/80-t/32,0).}
\]
The coordinates have the standard order \(g,a,b,u,v,w,z\), so in particular \(a'=z'=0\) and therefore the seedless relation \(9b'z'=4a'(v'-z')\) holds identically. For \(0\le t\le1/50\), both physical capacities and nonnegative masses hold. The target can be viewed on a varying seedless chart with \(C(t)=3/4+5t/2\), since \(v'=9C(t)b'/40\), but the *target flow itself is affine in t*.

There is an explicit nonnegative \(7\times7\) Blackwell transfer \(Q(t)\) independent of terminal declaration, preserving each of the seven Q masses, all seven likelihood-ratio-weighted P masses and both stopping times:
\[
\boxed{(e_P,e_Q,T_P,T_Q)_{\text{FULL}}=(e_P,e_Q,T_P,T_Q)_{\text{seedless}}.}
\]
It applies to every randomized seven-node terminal declaration and the whole source/target convex interpolation.

## Exact 11-edge construction

Set \(t_1=1/50\), and write \(M(x(0))=(869/12000,1/80,1/2,1181/6000,0,0,873/4000)\).
Let \(Q_0=\operatorname{diag}M(x(0))\), and define \(Q_1\) by precisely these eleven **positive** entries; entries not shown equal zero. Edge code \(s=7i+j\), where row i is a target LR node and column j is a source LR node:

| s | \(Q_{1,ij}\) |
|---:|---:|
| 0 | 131317/1800000 |
| 1 | 20647/3600000 |
| 8 | 77/8000 |
| 15 | 5603/2300000 |
| 16 | 49/100 |
| 17 | 17397/2300000 |
| 24 | 339269/1800000 |
| 38 | 1/1600 |
| 43 | 99661/82800000 |
| 45 | 7261/4140000 |
| 48 | 395317/1800000 |

Then for each real \(t\in[0,1/50]\), define
\[
\boxed{Q(t)=(1-50t)Q_0+50tQ_1.}
\]
Both coefficients are nonnegative. All entries of \(Q(t)\) are nonnegative because \(Q_0,Q_1\) are, with at most eleven positive edges for interior t.

The checker \`VERIFY_AFFINE_CORNER.py\` performs exact Python \`fractions.Fraction\` verification at \(t=0\) and \(t=1/50\) of nonnegative masses, both Q/P normalizations, the seven row equations, seven Q column equations, seven likelihood-ratio P column equations, physical capacities, seedless identity, and \(T_P,T_Q\). In particular, \(M(x(t)),M(y(t)),T_P(x(t)),T_Q(x(t)),T_P(y(t)),T_Q(y(t))\) are all affine in t under the frozen observer formulas of \`VERIFY.py\`, and x(t),y(t) are affine themselves. Since all equalities are linear in the flows and Q, the two verified endpoints and convex interpolation prove every equality for **all real t in the closed interval**. All inequalities for the target and Q likewise follow from convexity. This is an analytic whole-interval proof, not an inference from the 101 regression points.

## Executed independent exact check

The standalone checker \`VERIFY_AFFINE_CORNER.py\` uses the exact seven-node mass, LR and stopping-time formulas from the adjacent \`VERIFY.py\`. Run from the same research directory with \`python3 VERIFY_AFFINE_CORNER.py\`. Actual local Python stdlib Fraction stdout:

\`\`\`text
PASS_EXACT_ENDPOINTS_AFFINE_11_EDGES_T_0_TO_1_50
PASS_EXACT_101_AFFINE_REGRESSIONS
PROVED_ALL_REAL_T_0_TO_1_50_P0_Q1_THETA1_KAPPA3_4_EXACT_SEEDLESS
\`\`\`

Thus the previously undecided \(t\downarrow0\) positive-residual corner \(p=0,q=1,\theta=1,\kappa=3/4\) now has an **explicit closed-interval exact solution**. Combining with prior PR #1808 (all capacities, \(t\ge1/100\)) yields this one corner for every \(0\le t\le1/5\), with overlap \(t\in[1/100,1/50]\). The complete mixed-capacity region for \(0<t<1/1000\) and varying \(\kappa\) remain the next targets. Every reported result here remains author-side, pending independent review and formal admission.

## Provenance and frozen scope

Source observer: \`research_notes/brc_r5_theta_positive_c45_20261108/VERIFY_SUPPORT.py\` at immutable \`1605721551f0151dabe00709cda45c994dd81ed9\`; the local compatible model functions are preserved in adjacent \`VERIFY.py\`. Frozen scientific input pins remain GK \`a01383f825ef9d43b4b754254303298c64041568\`, Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`, not replaced with current rules or main scientific content. Researcher-ID \`EM-DIRECT-D20310 / TASK_RESEARCH\` and current activity \`RA-6A29F796D3B96F8EDAB8C156\` are separately native-verified; no formal CLAIM, Result, Review or theorem admission is asserted.
