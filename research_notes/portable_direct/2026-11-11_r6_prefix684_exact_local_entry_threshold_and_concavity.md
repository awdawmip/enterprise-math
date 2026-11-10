# PREFIX-684-R6 — Exact local entry threshold and full-branch concavity for the BRC variance crossover

Date: 2026-11-11 (Asia/Shanghai). Mode: independent author-side TASK_RESEARCH. Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Model, scope and pinned sources

Reuse the frozen 189-level BRC first-stop observer model from PREFIX-682, immutable Enterprise Math commit d437f76a2d52b617e938130c9cb9e8e61257c5a9, and PREFIX-683 at 2d8d843fcf28c6e6eed8d2cdd985f79734b0104d. For Y(p,z), the maximum of two independent Poissonized first-stop clocks, define

\[
A(z)=\mathrm{Var}(Y(z,z))-\mathrm{Var}(Y(0,z)),\quad
B(z)=\mathbb E Y(z,z)-\mathbb E Y(0,z),
\]
\[
F_q(z)=qA(z)-B(z),\quad D_q(z)=qF_q(z)=V_q(z,z)-V_q(0,z),
\quad V_q=q^2\mathrm{Var}(Y)-q\mathbb E Y.
\]

These are scalar observer and slot parameters; preserve frozen source and branch provenance. No native physical inference is asserted.

Put \(L=2663/50000=0.0532600\), \(R=53261/1000000=0.0532610\), \(I=[L,R]\), and let \(z_A\) be the unique zero of A in I. PREFIX-682 certifies throughout I:

\[
-1800<A'<-1600,\quad 100<B'<150,\quad 793/100<B<794/100,
\]
with \(A(L)>0>A(R)\) and \(z_A\in(0.05326047313,0.05326047314)\). PREFIX-683 yields \(|A''|<110000000\) and \(|B''|<36000\) throughout I.

## New theorem: exact local entry and full-branch concavity

Define the rational entry threshold

\[
\boxed{q_c=\frac{B(L)}{A(L)},\qquad 9816<q_c<9929.}
\]

For **every real \(q\ge0\)**, the equation \(F_q(z)=0\) has exactly one solution in the closed interval I if \(q\ge q_c\), and no solution there if \(0\le q<q_c\). When \(q=q_c\) the unique solution is L. For every \(q>q_c\), the unique solution \(z(q)\) lies in \((L,z_A)\), and \(D_q\) changes sign from positive to negative at it.

The branch \(z:(q_c,\infty)\to(L,z_A)\) is smooth, strictly increasing and strictly concave, with

\[
\lim_{q\downarrow q_c}z(q)=L,\qquad \lim_{q\to\infty}z(q)=z_A.
\]

For all real \(q>q_c\), the derivative and curvature inequalities are

\[
\frac{793}{100q(1800q+150)}<z'(q)<
\frac{794}{100q(1600q+100)}
\]
and
\[
\boxed{z''(q)<-\frac{3144\cdot793}{100q(1800q+150)^2}<0.}
\]

For \(q\ge9929\), the stronger 3145 curvature coefficient of PREFIX-683 still applies. In particular, its previous large-slot \(q\ge10000\) theorem is extended to **all real q above the intrinsic local entry threshold**. The theorem is restricted to I, not a uniqueness assertion on the larger interval [0.052,0.054].

## Proof and exact rational validation

**1. Threshold bracket.** PREFIX-682 certifies the exact integer floors of \(10^8\) times the center jets at \(c=106521/2000000\):

| jet | order 0 | order 1 | order 2 |
|---|---:|---:|---:|
| A | -4562 | -169792160954 | -6657264578649 |
| B | 793095029 | 12820091523 | -99474141353 |

An integer floor k encloses the exact jet in \([k/10^8,(k+1)/10^8)\). With \(h=1/2000000\) and \(L=c-h\), apply quadratic Taylor expansion and the frozen uniform third-derivative bounds \(M_{A,3}=218571424275456\), \(M_{B,3}=69527880576\). The remainders are bounded by \(M_{X,3}h^3/6\). Exact outward rational arithmetic gives

\[
\frac{639023129476163751}{800000000000000000000}
<A(L)<\frac{80789605452834869}{100000000000000000000},
\]
\[
\frac{6344708950375631849047}{800000000000000000000}
<B(L)<\frac{793088620086653983531}{100000000000000000000}.
\]

The Fraction program establishes strict cross-products \(B_{\rm low}>9816 A_{\rm high}\) and \(9929 A_{\rm low}>B_{\rm high}\). Since A(L)>0, this proves \(9816<q_c<9929\). The ratio is rational because the pinned 189-level finite survivor recurrence and L have rational coefficients/inputs.

**2. Existence and uniqueness.** For every \(q\ge0\), \(F'_q=qA'-B'<0\) throughout I. Also \(F_q(R)<0\), since A(R)<0 and B(R)>0, whereas \(F_q(L)=A(L)(q-q_c)\). Continuity and strict decrease give the complete iff classification on I. Since \(F_q(z_A)=-B(z_A)<0\), roots for q>q_c are in (L,z_A). Because q>0 on this branch, \(D_q=qF_q\) has the asserted orientation.

**3. Smooth monotone branch.** Let \(T=q(-A'(z(q)))+B'(z(q))\). Then \(1600q+100<T<1800q+150\); implicit differentiation gives
\[
z'(q)=\frac{A(z(q))}{T}=\frac{B(z(q))}{qT}>0.
\]
This gives the derivative envelope. Continuity of the unique root gives the q_c endpoint. As q grows, \(A(z(q))=B(z(q))/q\to0\); uniqueness of the A-zero on I yields \(z(q)\to z_A\).

**4. Strict concavity for the whole branch.** Two differentiations yield
\[
Tz''=2A'z'+(qA''-B'')(z')^2.
\]
For \(q>q_c>9816\),
\[
|(qA''-B'')z'|<
\gamma(q):=\frac{794}{100}\frac{110000000+36000/q}{1600q+100}.
\]
The positive function \(\gamma(q)\) decreases for q>0, and exact Fraction checks prove \(\gamma(9816)<56\) and \(\gamma(9929)<55\). Thus \(Tz''<(-3200+56)z'=-3144z'\) for all q>q_c. Dividing by T>0 and applying the lower bound on z' and upper bound on T proves the stated curvature inequality. For q>=9929 use 55 and 3145.

## Evidence, scope, next problem

The accompanying Python 3 standard-library Fraction program locally returned ALL_CHECKS_PASS PREFIX684-R6; its JSON records all exact interval endpoints and gamma values. This proves new implications conditional on the pinned PREFIX-682 exact jet certificate; the 189-level recurrence was not rerun here. BRC reuse: REUSE_APPLIED (frozen survivor observer, exact moment jets and inherited implicit-function method). Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

Next: directly evaluate the exact rational A(L), B(L) from the 189-level recurrence to refine q_c; use signed Bernstein patches on [0.052,0.054] to count additional crossover roots. In parallel continue the ordered two-dimensional variance bound search with the PREFIX-675 complete edge maximum.
