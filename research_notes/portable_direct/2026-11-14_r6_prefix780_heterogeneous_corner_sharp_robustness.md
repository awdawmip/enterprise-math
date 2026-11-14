# PREFIX-780 / R6 — Exact heterogeneous-corner robustness criterion for reflected Gamma witnesses

Date: 2026-11-14 (Asia/Shanghai). Research continuation: R6 / PREFIX-779 -> PREFIX-780. Evidence status: **AUTHOR_EXACT_ALGEBRAIC_PROOF_WITH_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED**.

**Frozen scientific pin:** \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Predecessor: \`research_notes/portable_direct/2026-11-14_r6_prefix779_sharp_two_noise_reflection_tradeoff.md\` (commit \`9de2d43a6559507aabf062d0ae84d0e0b47dec8a\`). Inherited verified Gamma model inequalities are \`A1,A2>0\`, \`0<B1<B2\`, \`D=A2*B1-A1*B2>0\`. The model is the external 189-layer killed-Pascal first-stop / two independent unit-rate Gamma clocks. All this note's new arguments are exact algebra conditional on those inherited integer certificates.

## Model, geometry and heterogeneous observer budgets

Let \`R1=[38,39]^2/768\`, \`R2=[39,40]^2/768\`; let \`R1#\`, \`R2#\` be their reflections under \`(p,z)->(p,1-z)\`. Base cells share the vertex \`c=(39,39)/768\`, coefficient \`+1\` in each mixed increment. There are six private base vertices and seven reflected partners, 14 in total. Let \`L1,L2\` be their signed four-corner difference functionals. For \`V_q=q² Var(Y)-q E[Y]\`, \`Delta_Ri V_q=q xi(q)\` with \`xi(q)=Ai-q Bi\`; by exact reflection, \`Delta_Ri# V_q=-q xi(q)\`.

At fixed \`q>0\` let normalized errors at the seven base vertices and their partners be
\`e_v=(Vhat_q(v)-V_q(v))/q\`, \`f_v=(Vhat_q(v#)-V_q(v#))/q\`.
Allow an individually measured amplitude budget \`epsilon_v>=0\` for *each reflected pair*:
\`|e_v|,|f_v|<=epsilon_v\`.
Allow *arbitrary* pairwise reflection-defect budgets \`delta_v>=0\`:
\`|e_v-f_v|<=delta_v\`.
Only the common pair's defect bound \`delta_c\` enters the sharp robustness threshold. Put
\`S1=sum_(v in R1\{c}) epsilon_v\`, \`S2=sum_(v in R2\{c}) epsilon_v\`, \`c0=epsilon_c\`,
\`d=min(delta_c,2*c0)\`, and
\`H=B2*S1+B1*S2+(B2-B1)*c0+B1*d\`.

## Theorem 780.1 — sharp if-and-only-if guarantee for the 14-vertex observer class

For every real \`q>0\` and every scalar readout obeying the above pairwise budgets, the four cells have **at least one strictly positive and at least one strictly negative mixed difference** if and only if

\`\`\`
 H < D.
\`\`\`

In fact, when \`H<D\`, for *every* such readout and every \`q>0\`:
\`\`\`
 max_{R in {R1,R2,R1#,R2#}} Delta_R Vhat_q >= q*(D-H)/(B1+B2) > 0,
 min_{R in {R1,R2,R1#,R2#}} Delta_R Vhat_q <= -q*(D-H)/(B1+B2) < 0.
\`\`\`
If \`H>=D\`, an admissible readout and a positive \`q\` exist for which the four increments are all nonnegative, defeating the universal strict-two-sign assertion. At the constructed threshold witness the normalized increments in order \`(R1,R1#,R2,R2#)\` are exactly \`(0,d_t,d_t,0)\` for some \`d_t>=0\`.

**Quantifier scope:** \`H<D\` is the exact condition for the *guarantee under all errors and all q* for this declared 14-vertex scalar observer family. It is not a statement about a particular unmeasured native X6 comparator.

## Proof: exact support and sign separation

Define normalized mixed increments
\`y_i=xi+Li e\` and \`z_i=-xi-Li f\`.
The exact q-elimination identities are
\`B2*x1-B1*x2=-D\`,
\`B2*y1+B1*z2=-D+B2*L1 e-B1*L2 f\`,
\`B2*z1+B1*y2=D-B2*L1 f+B1*L2 e\`.

The six private vertices are independent: the support of the private contributions in either weighted combination is \`B2*S1+B1*S2\`. At common vertex c, the two-variable support problem is
\`max (B2*e_c-B1*f_c)\` under \`|e_c|,|f_c|<=c0\`, \`|e_c-f_c|<=delta_c\`.
Since \`B2>B1>0\`, this maximum is exactly
\`(B2-B1)*c0+B1*min(delta_c,2*c0)\`, attained at \`e_c=c0, f_c=c0-d\`. Exchanging \`e,f\` gives the same maximum for \`B2*f_c-B1*e_c\`.
Consequently \`B2*y1+B1*z2<=-(D-H)\` and \`B2*z1+B1*y2>=D-H\`. Positive weighted averages lie between their entries, proving both displayed bounds whenever \`H<D\`.

For sharpness, suppose \`H>=D\`. Define
\`W=B2*S1+B1*S2+(B2-B1)*c0\` and the continuous strictly increasing function \`F(t)=t*W+B1*min(delta_c,2*t*c0)\` on \`[0,1]\`. Then \`F(0)=0\`, \`F(1)=H>=D>0\`, so some \`t in (0,1]\` satisfies \`F(t)=D\`. Put \`d_t=min(delta_c,2*t*c0)\` and
\`q=(A1+t*(S1+c0))/B1>0\`.
At common vertex choose \`e_c=t*c0\`, \`f_c=t*c0-d_t\`. At R1's three private vertices, choose \`e_v=f_v=t*epsilon_v*sgn(L1[v])\`, giving \`L1 e=t(S1+c0)\`, \`L1 f=t(S1+c0)-d_t\`. At R2's private vertices choose \`e_v=f_v=-t*epsilon_v*sgn(L2[v])\`, giving \`L2 e=-t*S2+t*c0\`, \`L2 f=-t*S2+t*c0-d_t\`.
All amplitude budgets are respected; all private reflection defects are zero; the shared defect is \`d_t<=delta_c\`. Because \`F(t)=D\`,
\`x1=-t(S1+c0)\` and \`x2=t(S2-c0)+d_t\`.
Hence \`(y1,z1,y2,z2)=(0,d_t,d_t,0)\`. This is an admissible counterexample to a *universal strict* two-sign guarantee whenever \`H>=D\`. QED.

## Corollaries, measurement design and comparison with PREFIX-779

1. **Uniform reduction.** If all seven pair budgets equal \`epsilon\` and \`delta_c=delta\`, then \`S1=S2=3*epsilon\`, \`c0=epsilon\` and \`H=(2*B1+4*B2)*epsilon+B1*min(delta,2*epsilon)\`. Thus Theorem 780.1 specializes exactly to PREFIX-779, including its sharp phase boundary.
2. **Localized reflection precision.** Only the shared vertex's reflection defect enters the exact criterion. The private pairs may have any \`delta_v\`, including unbounded defects, subject to their own finite amplitude budgets. The extremal construction has **zero private-pair reflection defect**. When \`c0=0\`, the criterion becomes \`B2*S1+B1*S2<D\`, independent of all reflection-defect bounds.
3. **Precision allocation.** A unit increase in a private R1 amplitude budget costs \`B2\` of certificate margin, versus \`B1\` for a private R2 budget. A common-corner amplitude increase has piecewise cost \`B2+B1\` while \`delta_c>=2*c0\`, and \`B2-B1\` while \`delta_c<2*c0\` (with fixed \`delta_c\`). The kink is exactly \`delta_c=2*c0\`. This identifies concrete observation coordinates whose measurement precision most affects robust sign certification.

## Validation, boundaries and next question

Companion: \`research_notes/portable_direct/PREFIX780_R6_HETEROGENEOUS_CORNER_BUDGET_CHECK.py\`. Exact Python \`fractions.Fraction\` regression enumerates rational corner-support polygon vertices and checks both bounds and explicit sharpness witnesses for **512** distinct exact scenarios (69 strictly certified; 443 sharpness constructions). It returned \`ALL_CHECKS_PASS PREFIX780 HETEROGENEOUS_SHARP_CORNER_BUDGET\`. This finite regression supports implementation correctness; the universal statement follows from the preceding algebraic proof. Inherited model-specific \`Ai,Bi\` inequalities are sourced from immutable PREFIX-778 code/certificate, not recomputed in this subunit.

No original-comparator grid exclusions were added. A native transfer needs a typed observation map that retains Cell/Link/Port, branch, signed source, and time/provenance; use it to measure heterogeneous \`epsilon_v\` and especially \`delta_c\`. The discriminating next scientific step is to attempt an actual native map or obtain a nontransfer counterexample from original typed observations. The 14-corner scalar budgets are representation-level errors, not evidence that native source/port histories can be identified or collapsed.