# RB Enterprise Degree-6 CM(-24) Blind Replication — Phase A Reduction

Status: `BLIND_INCOMPLETE_EXACT_REDUCTION / PHASE_A_FIREWALL_PRESERVED / NOT_UNBLINDED`

Task-ID: `RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION`  
Publication-ID: `TP2-9F1A3C0DEFAED8B6E247`  
Researcher-ID: `EM-RBV2REP-6D9A31`  
Claim-ID: `chatgpt-rbv2rep-20260908-1012-sol6d9a31`  
Execution-Record-ID: `ER-RBV2REP6D9A31`

## Primary verdict

`BLIND_INCOMPLETE_EXACT_REDUCTION`

This Phase A execution did **not** reconstruct a full degree-6 map and did **not** prove nonexistence. It preserved the blind firewall and froze a strict exact reduction of the reconstruction target. No originating explicit formula, common base point, target twist constant, symbolic replay, prior result history, or originating period-scaling value was inspected before this freeze.

## Task-local inputs used

Only the task-local blind data were used:

\[
D:\quad w^4=(R+2)^2R(R^2-3),
\qquad
t=\frac{w^2}{R+2},\quad t^2=R^3-3R,
\]

\[
\phi=\frac{dR}{w}\left(1+\frac{k}{t}\right),
\qquad
k=-i\,3^{1/4}(\sqrt6-2),
\]

\[
\lambda_*=35+24\sqrt2-20\sqrt3-14\sqrt6.
\]

The coefficient-field working envelope remained within
\[
\mathbf Q(i,3^{1/4},\sqrt2).
\]

## Exact Phase A reductions

Let
\[
C:\quad t^2=R^3-3R,\qquad h=(R+2)t.
\]
Then
\[
K(D)=K(C)(w),\qquad w^2=h.
\]

The principal differential rewrites as
\[
\phi=\frac{t+k}{wt}\,dR=\frac{t+k}{w}\frac{dR}{t}.
\]
Since \(dR/t\) is the invariant differential on \(C\), the zero divisor of \(\phi\) is the pullback of \(t=-k\).

The task-local constant satisfies
\[
k^2=12\sqrt2-10\sqrt3.
\]
The cubic
\[
R^3-3R-k^2=0
\]
has discriminant
\[
108-27k^4=216(-73+30\sqrt6)\neq0,
\]
so the divisor \(t=-k\) consists of three reduced points on \(C\), and \(\phi\) has six reduced zeros on \(D\).

The target modulus has the exact factorization
\[
\lambda_*=((2-\sqrt3)(\sqrt3-\sqrt2))^2
\]
and the Legendre \(j\)-invariant
\[
j(\lambda_*)=256\frac{(1-\lambda_*+\lambda_*^2)^3}
{\lambda_*^2(1-\lambda_*)^2}
\]
satisfies
\[
j^2-4834944j+14670139392=0.
\]

## Descended certificate

The deck involution \(\iota:w\mapsto-w\) sends \(\phi\mapsto-\phi\). Therefore any morphism
\[
f:D\to E
\]
with \(f^*\omega_E\) proportional to \(\phi\) must, after fixing a target origin, descend through the quotient \(E/(P\mapsto T-P)\cong\mathbf P^1\).

Thus the blind reconstruction is reduced to the following exact problem on \(C\):

> Find a degree-6 function \(x\in K(C)\) and a square witness \(s\in K(C)\) such that the four fibers over \(0,1,\lambda_*,\infty\) have branch square-class
> \[
> x(x-1)(x-\lambda_*)\equiv h=(R+2)t\pmod{K(C)^{*2}},
> \]
> and the differential equation
> \[
> \left(\frac{dx}{dR/t}\right)^2
> =
> \mu^2(t+k)^2\frac{x(x-1)(x-\lambda_*)}{(R+2)t}
> \]
> holds for some constant \(\mu\).

Equivalently, solve the degree-6 Hurwitz / square-class system on \(C\) with six marked odd points
\[
O,\ (0,0),\ (\sqrt3,0),\ (-\sqrt3,0),\ (-2,i\sqrt2),\ (-2,-i\sqrt2),
\]
and with the remaining simple ramification over the three reduced points \(t=-k\).

## Tested routes

### Route U0: zero-divisor trial

Set
\[
U_0=\left(\frac{t+k}{w}\right)^2
=\frac{(t+k)^2}{(R+2)t}.
\]

This has zero divisor \(2(t=-k)\) on \(C\) and pole divisor at the six branch points of \(D\to C\), so it is a natural degree-6 quotient candidate. However the exact monic square test only gives the degenerate family
\[
F(U_0)=U_0(U_0-A)^2.
\]
This records a useful boundary but does not produce a nondegenerate Legendre target with three distinct finite branch values.

Status: `ROUTE_REDUCED_NOT_CLOSED`.

### Route q: conjugate-ratio normalization

Set
\[
q=\frac{t+k}{t-k},\qquad X=q^2.
\]

For this normalization, the square-class condition would force
\[
\frac{L}{R+2}\in K(C)^{*2},
\]
where
\[
L=(1-\lambda_*)(R^3-3R+k^2)+2k(1+\lambda_*)t.
\]

At the two points over \(R=-2\), namely \(t=\pm i\sqrt2\), the residues of \(L\) are nonzero. Hence this normalization cannot supply the required square divisor at the \(R=-2\) branch points.

Status: `EXACT_ROUTE_NO_GO_FOR_THIS_NORMALIZATION`.

## BRC / observer discipline

BRC was used only as a firewall-compatible observer and provenance discipline, not as an external formula source. The population was the row/fiber-level branch-squareclass data of a possible degree-6 cover. The reduction deliberately retained:

- the six marked odd branch points;
- the three reduced \(t=-k\) ramification points;
- the distinction between square-class support and exact multiplicity;
- the quotient-map coordinate \(x:C\to\mathbf P^1\);
- the future operations needed for Driver review or successor continuation.

No compression to a single yes/no novelty bit or a numerical-fit artifact was used.

## Frozen smaller unresolved unit

`DEGREE6_QUOTIENT_MAP_ON_C_WITH_CM24_BRANCH_CROSS_RATIO`

Precise next action:

Solve the descended degree-6 Hurwitz / square-class system on
\[
C:t^2=R^3-3R
\]
over \(\mathbf Q(i,3^{1/4},\sqrt2)\), with cross-ratio \(\lambda_*\), branch square-class \(h=(R+2)t\), and differential zeros at \(t=-k\).

The most constrained next subcase is the three-pair allocation of the six branch points of \(h\) among three of the four target 2-torsion fibers, with the fourth fiber carrying only double points. This preserves the Riemann-Hurwitz count: nine double points in the special fibers plus three simple \(t=-k\) ramification points.

## Non-claims

This return does not claim:

- a reconstructed degree-6 map;
- an equivalent map under target/source automorphisms;
- a proof of nonexistence;
- the target twist constant;
- the period-scaling value \((B_1/\Omega_P)^2\);
- any post-freeze comparison with the withheld formula.

No unblinding was performed in this Phase A reduction.

## Artifacts

- Raw reduction artifact: `research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/blind_phase_a_reduction_20260908.json`
- Deterministic checker: `scripts/check_rb_enterprise_degree6_cm24_blind_replication.py`

Next action: continue Phase A from the descended Hurwitz / square-class system, or Driver may accept this as a strict incomplete reduction and dispatch a successor run without exposing the withheld formula.
