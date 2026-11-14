# PREFIX-771 / R6 — Exact diagonal Gamma second jet and a sharper stationary bracket

Date: 2026-11-14 (Asia/Shanghai). Scientific input: immutable `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_EXACT_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.
Scope: external 189-layer killed-Pascal BRC first-stop auxiliary and two independent Gamma clocks. This continues PREFIX-769/770, without claiming native X6 dynamics, a new 1/768 exclusion, or an accepted mathematical Result.

## Theorem 771.1 — diagonal second-jet identity

Let \(s(u)=(S_0(u),\ldots,S_{188}(u))\) be the exactly reconstructed survivor vector, \(d=s'\), \(e=s''\), \(f=s'''\), and let \(K_{ij}=\binom{i+j}{i}/2^{i+j+1}\), \(L_{ij}=(i+j+1)K_{ij}\) from PREFIX-760. For \(Y(p,z)=\max(C_p,C_z)\), let \(\mu=E[Y]\), \(W=\operatorname{Var}Y\), and \(A=-\partial_{pz}\mu\), \(D=-\partial_{pz}W\), \(Q=A/D\) where \(D>0\).

All quantities below are evaluated at \(p=z=u\), with primes denoting *diagonal* derivatives \(d/du\), not partial derivatives. Put

\[
m=2{\bf1}^Ts-s^TKs,\quad v={\bf1}^Td-d^TKs,\quad
w={\bf1}^Te-e^TKs,\quad A=d^TKd,\quad B=d^TLd.
\]
Then
\[
m'=2v,\quad m''=2(w-A),\quad
v'=w-A,\quad v''={\bf1}^Tf-f^TKs-3e^TKd,
\]
\[
A'=2e^TKd,\quad A''=2f^TKd+2e^TKe,
\quad B'=2e^TLd,\quad B''=2f^TLd+2e^TLe,
\]
\[
D=B+2v^2-2mA,\quad
D'=B'+4vv'-2m'A-2mA',
\]
\[
D''=B''+4(v')^2+4vv''-2m''A-4m'A'-2mA''.
\]
In particular,
\[
Q'=\frac{A'D-AD'}{D^2},\qquad
\boxed{Q''=\frac{(A''D-AD'')D-2(A'D-AD')D'}{D^3}}.
\]

**Proof.** PREFIX-760 gives \(\mu(p,z)=\sum_i(S_i(p)+S_i(z))-s(p)^TKs(z)\) and \(M_2\) with cross kernel \(L\). Thus \(\mu_{pz}=-d(p)^TKd(z)\), \(M_{2,pz}=-d(p)^TLd(z)\), and \(D=B+2\mu_p\mu_z-2\mu A\). At the diagonal \(\mu_p=\mu_z=v\). Differentiating these finite polynomial identities termwise along \(p=z=u\) gives every displayed first and second derivative. The quotient rule yields the expression for \(Q''\). All polynomial and kernel sums are finite. QED.

## Theorem 771.2 — exact pointwise curvature and a narrower stationary interval

For the frozen 189-layer width predicate with \(W=2^{18}\), let
\[
u_L=\frac{502971451}{10^{10}},\qquad
u_R=\frac{502971452}{10^{10}}.
\]
The attached standalone Python integer checker reconstructs all 189 survivor rows, confirms exactly 9,529 nonzero survivor positions and an empty terminal row, and evaluates the preceding identities using integers only. It proves:
\[
D(u_L)>0,\quad D(u_R)>0,\qquad
Q'(u_L)<0<Q'(u_R),
\]
\[
\boxed{4<Q''(u_L)<5,\qquad 4<Q''(u_R)<5}.
\]
Consequently by continuity and the intermediate value theorem,
\[
\boxed{\exists u_*\in(502971451/10^{10},502971452/10^{10}):Q'(u_*)=0}.
\]
This bracket has width \(10^{-10}\), 100 times smaller than PREFIX-769's \(10^{-8}\) bracket.

For the right endpoint, exact integer cross multiplication additionally proves
\[
\boxed{0<q_c\le Q(u_R)<
\frac{28518591162857609314}{10^{21}}
=0.028518591162857609314}.
\]
The bound improves the certified PREFIX-769 value \(q_c<0.028518591162858\). Pointwise negative mixed curvature for \(q>Q(u_R)\) supplies the upper inequality under PREFIX-763's definition of \(q_c\).

Rounded *displays only*, not sign tests:
- \(u_L\): \(Q=0.02851859116285760931560447086858859\), \(Q'=-2.6598727576074\times10^{-10}\), \(Q''=4.9538847682562\).
- \(u_R\): \(Q=0.02851859116285760931377516712891208\), \(Q'=+2.2940120091837\times10^{-10}\), \(Q''=4.9538847653261\).

## Exact arithmetic implementation and evidence

The executable `PREFIX771_R6_DIAGONAL_HESSIAN_CHECK.py` uses integer width tests, binomial recursion, positive K/L kernels scaled by \(T=2^{377}\), and four survivor jets \(S,S',S'',S'''\). At rational \(u=x/B\), all four jets are represented as integer vectors divided by common \(J=B^{191}\). With \(E=J^2T\), the checker builds integer-scaled \(A,A',A'',D,D',D''\) and tests the signs of the exact rational \(Q'\), \(Q''\) and upper-bound inequality using integer products, before displaying any decimal values. It was run locally and returned `ALL_CHECKS_PASS PREFIX771 DIAGONAL_JET`; the structured output is `PREFIX771_R6_DIAGONAL_SECOND_JET_RESULTS.json`.

The exact second-derivative check at two endpoints establishes local convexity **at those points**. Uniqueness of the stationary root over the whole bracket, positive curvature uniformly over the bracket, off-diagonal/global minimization and the native X6 relation remain open. An attractive next route is interval/Bernstein certification of \(Q''>0\) and transverse \(Q_2>0\) throughout the bracket, followed by examining the full two-parameter Hessian and an unsolved 1/768 cell.

No earlier source byte was modified, and no historical area/exclusion count is increased.
