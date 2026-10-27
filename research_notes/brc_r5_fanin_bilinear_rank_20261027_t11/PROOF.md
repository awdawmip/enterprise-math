# R5 — Exact fan-in bilinear rank and nonconvex LR observer slice

Date: 2026-10-27 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Local authorship label: EM-R5-FANIN-T11-2243; not a native session, CLAIM, Result or independent review.

## Immutable inputs, scope and source classification

Frozen GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@45b3f5d2d0e9bf1f242f192d929ad7b275a5aa10 (both entry files, ACTIVE worldview, mathematical/code/BRC and activity routes). Frozen project: awdawmip/enterprise-math@ee9a41c27e48d0e952678928c6c950deb252dd46 (AGENTS, P000 V5, native X6/time, joint observer preservation, portable/autonomous protocols). Predecessors: research_notes/brc_r5_two_level_critical_price_gate_20261027_t11/PROOF.md and research_notes/brc_lr_affine_circuit_duality_20261027_r5/PROOF.md. Native task list returned CONTROL_QUOTA; session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active Source owner and formal research authority were NOT verified.

A finite external dual-measure P/Q sequential observation tree is studied. The observer reports O=(P[declare Q],Q[declare P],E_P[tau],E_Q[tau]); a seedless LR policy shares its independent local action probability between histories with equal (time, P/Q-likelihood ratio), with no persistent common random seed. BRC is ACTUALLY USED for exact positive P/Q branch transport and ordered-history accounting; signed differences, determinants and exposing functionals are observer algebra, NOT positive BRC mass. This is not a native heartbeat dynamics or physics attribution theorem.

## Theorem A: universal two-control bilinear image gate

Fix all policy parameters except x,y in [0,1] at two distinct time-indexed LR signatures. Each observation path visits each time-indexed signature at most once. Therefore every terminal-path weight contains at most one of x or (1-x), and at most one of y or (1-y), proving the exact four-vector identity

F(x,y)=A+B*x+C*y+D*x*y,  A,B,C,D in R^4.                                      (A1)

Denote F(0,0)=v00=A, F(1,0)=v10=A+B, F(0,1)=v01=A+C, F(1,1)=v11=A+B+C+D. The Bernstein identity

F(x,y)=(1-x)(1-y)v00+x(1-y)v10+(1-x)y v01+xy v11                (A2)

shows conv(F([0,1]^2))=conv{v00,v10,v01,v11}; all coefficients are nonnegative and sum to one, and every corner is attained.

**Rank-three obstruction.** If rank(B,C,D)=3, the image is strictly nonconvex: the genuine convex combination

T=(v00+v10+v01)/3=A+(B+C)/3                                    (A3)

cannot equal F(x,y), because independent coefficients would require simultaneously x=1/3, y=1/3, xy=0, contradicting xy=1/9. This proves nonattainability for ALL REAL local randomizations, not a finite-grid claim.

**Convex degenerate cases.** D=0 makes F an affine image of the square. C=0 makes F=A+B*x+D*z for z=xy, with exact feasible triangle 0<=z<=x<=1; B=0 is symmetric. If the later control is reachable only through the earlier control's enabling action, no terminal path has an isolated y-factor, so C=0. All are scoped to the stated fixed-other-controls slice and do NOT assert convexity when other policy controls are freed.

## Theorem B: arbitrary nested-chain seedless convexification

Suppose the ONLY free seedless controls x1,...,xk occur at successive nested gates: every path that uses xj also passes every preceding gate and takes its enabling action. Other actions are fixed. Write u_j=prod(i=1..j)x_i. Each stopped or completed path has weight proportional to one of 1-u1, u1-u2,...,u(k-1)-u_k,u_k. Every expectation thus has form O=A+sum_j B_j*u_j. The exact attainable domain is the simplex 1>=u1>=u2>=...>=uk>=0.

For any convex mixture of deterministic threshold vertices with coefficients theta_0,...,theta_k>=0, sum theta=1, set u_j=sum_(l=j..k)theta_l. Reconstruct x1=u1 and x_j=u_j/u_(j-1) when denominator>0 (otherwise x_j=0). These are seedless local probabilities and reproduce the mixture EXACTLY, rationally when theta is rational. Thus the entire nested-only policy image is convex. Consequently, if ALL free LR controls of a model satisfy this nested-gate assumption, conv(O_LR)=O_full implies O_LR=O_full; the desired equal-hull/unequal-image witness is impossible in that class. The result does not require strong hidden-kernel lumpability.

## New 8-leaf positive rational intermediate-merge example

At t=1, Q(A)=Q(B)=1/2 with P/Q ratios R_A=1/2 and R_B=3/2. At t=2:
  A: Q(U|A)=1/3, Q(V|A)=2/3; P/Q conditional multipliers U=2,V=1/2;
  B: Q(U|B)=1/2, Q(V|B)=1/2; multipliers U=2/3,V=4/3.
Therefore R_AU=R_BU=1 (a genuine LR signature merge), R_AV=1/4 and R_BV=2. The conditional multipliers have Q-mean one. At t=3, each t=2 history has two equiprobable Q children with conditional P/Q multipliers:
  AU: (1/4,7/4); AV,BU,BV: (1/2,3/2).
Again each pair has mean one. The eight terminal P,Q masses are strictly positive and globally normalized.

Restrict to a **specified fixed-decision subfamily**. At t=1, A stops/declares P with probability 1-x, otherwise continues; B always continues. At t=2, AV stops/declares Q, BV stops/declares P. AU and BU stop/declare P unless they continue with probabilities y_A,y_B respectively. At t=3 after AU/BU, declare Q at the lower terminal LR multiplier and P at the higher. Full-history strategies have independent x,y_A,y_B; seedless LR at shared (t=2,R=1) requires y_A=y_B=y. Direct positive-mass summation yields

O_full(x,y_A,y_B)=A+B*x+C*y_B+D*x*y_A;                       (E1)
O_LR_slice(x,y)=A+B*x+C*y+D*x*y;                             (E2)

A=(0,1,7/4,3/2)
B=(1/12,-1/3,1/4,1/2)
C=(1/16,-1/8,1/4,1/4)
D=(1/48,-1/12,1/6,1/6).

The 3x3 minor det([B,C,D]_(coordinates 1,2,3))=5/4608 !=0. The two-control LR image is nonconvex by Theorem A. Full-history subfamily gives the affine image of the triangular prism (x,y_B,z) with 0<=x<=1,0<=y_B<=1,0<=z<=x, z=x*y_A; the seedless LR restriction cuts out the nonlinear graph z=x*y.

The three-corner barycenter is
T=(7/144,61/72,23/12,7/4).                                  (E3)
It is actually realized by full policy (x,y_A,y_B)=(1/3,0,1/3). For any four-vector O set dp=O1-A1, dq=O2-A2, dt=O3-A3. The inverse of the displayed minor extracts
 X=-24*dq/5-12*dt/5;
 Y=32*dp+8*dq;
 Z=-48*dp-24*dq/5+48*dt/5.                                 (E4)
Every seedless LR policy IN THIS SLICE has Z=X*Y, whereas T has (X,Y,Z)=(1/3,1/3,0), violating Z=1/9. This is an exact real-polynomial infeasibility certificate, not a parameter grid. The fourth coordinate satisfies dT+6*dq/5-2*dt/5=0, where dT=O4-A4.

The signed slice direction lambda=(-80,-8,12,0) has lambda*A=13 and lambda*B=lambda*C=-1, lambda*D=1. Thus every seedless LR policy in the fixed subfamily obeys lambda*O=13-x-y+xy=12+(1-x)(1-y)>=12, while full policy (x,y_A,y_B)=(1,0,1) attains 11. The fixed subproblem has a STRICT SUPPORT GAP 1 and is excluded from the mother-question candidates in that scope.

**Hard boundary:** T nonmembership and gap 1 have NOT been established for the UNRESTRICTED seedless LR policy set, where t=1 B, t=2 AV/BV and terminal declarations may vary. No unrestricted full-vs-LR hull equality or inequality has been certified. In particular, these statements must not be promoted to a global counterexample or a P000 physical finding.

## X6 observation bridge and exact evidence

Choose a chart-relative native Cell o in the six-axis Z^6 torsor. Label A/B by first +E1/+E2 steps, U/V by second +E3/+E4 steps, lower/higher terminal outcomes by third +E5/+E6 steps; record ordered path identity, P/Q positive branch masses and separately typed times. Every primitive step is one native axis; eight ordered paths and final cells are distinct. The LR signature is a declared lossy observer; the full X6 states and hidden AU/BU provenance are retained for future actions. This neither creates a native two-dimensional plane nor deduces P/Q dynamics from P000.

AUTHOR_VERIFY.py explicitly reconstructs the eight P/Q leaves with Fraction, checks positive normalization, the conditional LR means and collision, recomputes O from stop/declare path weights, confirms the coefficients, minor, inverse and T, and crosschecks 216 full and 36 LR rational parameter settings. Its literal executed stdout appears in AUTHOR_EXACT_OUTPUT.txt. Universal (A1)-(A3), (E4) all-real nonattainability and the k-chain theorem follow the written algebraic proofs, NOT the finite probes. The author verifier is locally executed; no Lean or independent formal/source review.

## Next discrimination

On this exact eight-leaf tree first release ALL decisions, enumerate unrestricted full and seedless LR deterministic four-vectors and give a rational supporting-direction separation or rational convex-combination certificates. If an unrestricted hull gap exists, exclude this candidate. For a new intermediate-fan-in tree only attempt seedless real-semialgebraic infeasibility after a complete unrestricted hull-equality certificate. Do not reuse the fixed-slice polynomial equation as an unrestricted certificate. Preserve Source owner/independent-review rules.