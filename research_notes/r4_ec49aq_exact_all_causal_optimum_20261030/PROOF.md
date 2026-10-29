# EC49AQ — exact global causal optimum by a truncated-polytope certificate

Date: 2026-10-30 (Asia/Shanghai). Author-side portable continuation of EC49AP PR #1724 at immutable predecessor commit 5a4067ce27d95685f21087aebe0b468660eeb891. Status: AUTHOR_ANALYTIC_PROOF / TWO_EXACT_FRACTION_CHECKS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Theorem: full real causal optimization (auxiliary positive BRC only)

Let the hidden source state be \(w\in\{0,1,2\}\), the later disclosed observation \(u\in\{0,1\}\), and the optional purchased observation \(z\in\{0,1,2\}\). Fix \(\eta=1/25\) and the normalized strictly positive 18+18-leaf source populations

\[
t(w,u)=\frac12+(2u-1)(1-w)\eta,\qquad
P(w,u,z)=\frac{t(w,u)}{12}\bigl(1+\mathbf1_{\{z=w\}}\bigr),\qquad
Q(w,u,z)=\frac{t(w,u)}9.
\]

**Causal order:** At \(w\), select \(c\in\{A0,A1,B0,B1,STOP\}\) with conditional probabilities \(x[w,c]\), action costs \((1,1,2,2,0)\), row sums one and first expected cost \(C_1=43/48\), i.e. \(\sum_{w,c}\operatorname{cost}(c)x[w,c]=43/16\). Then **erase \(w\)** and disclose only \((c,u)\). Based on this observable pair, a fresh independent behavioral purchase coin of probability \(r(c,u)\in[0,1]\) may reveal \(z\). The exact expected sensor-purchase cost is \(C_2=13/16\). Terminal acceptance depends only on realized observations and independent behavioral coins.

Writing \(\alpha=P(\mathrm{accept})\), \(\beta=Q(\mathrm{accept})\) and \(H=\alpha-\frac{177}{172}\beta\), the **exact full-real optimum** is

\[
\boxed{\max_{\text{all lawful real causal policies}}H=\frac{77}{688}.}
\]

## Proof I — BRC fiber support and an all-policy upper envelope

For every paid action \(c<4\) and observation \(u\), define

\[
q_z(c,u)=\frac{x[z,c]t(z,u)}3,\quad
T(c,u)=\sum_{z=0}^2q_z(c,u),\quad
V(c,u)=\frac1{172}\sum_{z=0}^2[43q_z(c,u)-16T(c,u)]_+.
\]

The purchased observation \((c,u,z)\) has \(P=(T+q_z)/4\) and \(Q=T/3\), hence positive-part support score \([43q_z-16T]_+/172\). Unpurchased observation \((c,u,\mathrm{no\ sensor})\) has equal P and Q masses (as does STOP), and its contribution is optimally zero by rejecting it.

Let

\[
c(x)=\sum_{c<4,u}T(c,u)=\frac13\sum_{w,c<4}x[w,c],
\qquad F(x)=\sum_{c<4,u}V(c,u).
\]

The function \(F\) is convex in the first-stage array \(x\): every \(V\) is a sum of positive parts of linear forms. For any lawful terminal decision and any purchase fractions satisfying the exact resource budget,

\[
H\le\sum_{c<4,u}r(c,u)V(c,u)\le F(x),\qquad
\frac{13}{16}=\sum_{c<4,u}r(c,u)T(c,u)\le c(x).
\]

Thus \(H\) is bounded by the maximum of convex \(F\) on the **truncated first-cost polytope**

\[
\mathcal P=\left\{x\ge0:\ \sum_cx[w,c]=1\ (w=0,1,2),\
\sum_{w,c}\operatorname{cost}(c)x[w,c]=\frac{43}{16},\
\sum_{w,c<4}x[w,c]\ge\frac{39}{16}\right\}.
\]

This reduction keeps all eight observable purchase fibers and their causal coin restrictions; it never accesses erased \(w\) during a later decision. Positive mass is not interpreted as signed or phase cancellation.

## Proof II — exact enumeration of every vertex of the truncated polytope

A convex function on a compact polytope attains its maximum at a vertex. Without the final purchase inequality, the three row sums and first cost give four independent linear equalities. An original vertex has at most four positive \(x[w,c]\) entries. Exactly three is impossible because one deterministic action per row has an integer aggregate action cost, whereas \(43/16\) is noninteger. Exhaustive rational solution of all \(\binom{15}{4}=1365\) possible four-entry supports gives **168 distinct original vertices**; **24** lie strictly above the purchase threshold \(c(x)=13/16\), all with \(c(x)=43/48\). None is exactly on the threshold.

A new cut vertex lies on the paid-cost equality \(\sum_{w,c<4}x[w,c]=39/16\), a fifth independent equality; it has at most five positive entries. All supports of size below five are already exhausted, and none is on this boundary. Enumerating all \(\binom{15}{5}=3003\) five-entry supports, exact Gaussian elimination over rational numbers, and strict positivity checks yields **144** new boundary vertices. Thus \(\mathcal P\) has exactly \(24+144=168\) vertices.

Direct evaluation of the original purchased P/Q leaf masses at these vertices, without relying on a fractional-purchase optimizer, proves the two exact finite maxima:

\[
\max_{\text{24 high-cost original vertices}}F=\frac{12177}{137600}
<\frac{77}{688},\qquad
\max_{\text{144 boundary vertices}}F=\frac{77}{688}.
\]

Exactly 24 boundary vertices attain the latter maximum. This is a **complete finite proof certificate** for the all-real upper bound, because every real \(x\in\mathcal P\) is a convex combination of its checked vertices and \(F\) is convex. The certificate executes using Python standard-library Fraction (no floats, tolerance, sampling, or grid interpolation).

## Explicit equality witness

Take first-stage rows

\[
x[0]=(0,3/16,1/4,0,9/16),\quad
x[1]=(1,0,0,0,0),\quad
x[2]=(0,1,0,0,0).
\]

Buy the sensor whenever a paid \((c,u)\) branch has positive mass; on purchase accept precisely when \((c,z)\) is \((A0,1)\), \((A1,2)\), or \((B0,0)\), irrespective of \(u\). All decisions depend solely on allowed observations. Direct sum over the 18 positive leaves of each source yields

\[
C_1=\frac{43}{48},\quad C_2=\frac{13}{16},\quad
\alpha=\frac{25}{64},\quad \beta=\frac{13}{48},\quad
H=\frac{77}{688}.
\]

The upper and lower bounds coincide, proving the theorem.

## Executed checkers, scope and next problem

VERIFY.py is the independently structured support-matrix enumerator: it solves all 4- and 5-coordinate systems and computes \(F\) from original P/Q leaves. VERIFY_EDGE.py reconstructs the original 168 vertices and all 924 original edges, finds the 144 threshold-crossing edges, checks the same maximum using BRC \(q_z,T\) and validates the explicit witness. They produced EXACT_REPORT.json and EDGE_REPORT.json via actual execution on 2026-10-30. Both are author-side exact rational crosschecks, **not** an independent reviewer verdict, a formal proof assistant result, or native Source Result admission.

The theorem is specifically for the **auxiliary positive probability BRC observer**, at its stated one-step causal horizon. The signed/phase BRC, native six-axis X6, three-dimensional native slice and heartbeat models require a separately proved typed state/observer/future-operation preservation map. P000 and the ACTIVE residual-fidelity worldview remain unchanged.

**Parameter continuation (EC49AR) completed:** PARAMETER_COROLLARY.md proves the same exact optimum for every real 0 <= eta <= 175/674, identifies the sharp plateau endpoint and constructs a lawful strict-improvement witness for every eta above it and below 1/2. VERIFY_PARAMETER.py and PARAMETER_REPORT.json contain the actual endpoint certificates. This continuation changes no base-model premises or protected state.

**Next problem EC49AS:** Determine the true all-real global envelope immediately above eta=175/674 with the same costs and causal erasure, rather than only the now-sharp end of the constant-value plateau. Preserve the typed positive-auxiliary BRC limitation and native-transfer obligation.
