# R749SSS — Optimal fifth-order cross-phase jet alias for the five-labeled-source observer

Date: 2026-11-17. Status: **AUTHOR_EXACT_NOT_REVIEWED** (independent review pending). Research mode: independent portable N2 scalar observer; no shared TASK CLAIM or native X6/BRC time-dynamics result is claimed.

Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R749SSR, PR #2585 @ fe048d48fe9d3e21391f2f132e66ec52f6a06366. The five source labels and the specially marked first weight-one source remain distinct; no information-reducing source collapse is made.

## Definitions and exact statement

Let the five distinct source weights be \(w=(1,1,2,3,6)\). Define for integers \(q\ge6\):

\[
\Omega_q=\{(k_1,\ldots,k_5)\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad C_q=|\Omega_q|,\quad T_q=\sum_{\Omega_q}k_1.
\]

Write \(S(x)=18x^4+54x^3-345x^2+2070x-16315\) and

\[
Y_q(e,d)=q^3\,\frac{T_q+e}{C_q+d}-\frac{S(q)}{108}.
\]

All error parameters are real and lie in \([-2,2]\); they are fixed across ordered six-step observations of their *own* candidate cutoff. Different candidate cutoffs may choose independent parameters.

**Theorem (fifth-order cross-phase alias and its fixed-parameter optimality).** Define the following exact rational errors:

\[
(e_2,d_2)=\left(\frac{69402481}{101966688},-\frac{656227}{472068}\right),\qquad
(e_4,d_4)=\left(\frac{194725627}{101966688},-\frac{755303}{472068}\right).
\]

All four numbers belong strictly to \((-2,2)\). For every integer \(q\ge8\) with \(q\equiv2\pmod6\),

\[
\Delta(q):=Y_q(e_2,d_2)-Y_{q+2}(e_4,d_4)>0,\qquad
\lim_{\substack{q\to\infty\\q\equiv2(6)}}q^5\Delta(q)=\frac{55842420440}{39339}>0.
\]

Thus \(\Delta(q)=\Theta(q^{-5})\). These four rational parameters are the **unique real, q-independent calibration quadruple** whose Laurent difference cancels all coefficients through \(q^{-4}\). In particular no fixed calibration quadruple, admissible or otherwise, gives \(o(q^{-5})\) for this residue-2 versus residue-4 candidate family.

For infinite ordered six-step observations,

\[
\mathcal O_q^{(\infty)}(e,d)=(Y_{q+6j}(e,d))_{j\ge0},
\]

there exists a finite constant \(K>0\), independent of \(q\), such that

\[
0<\|\mathcal O_q^{(\infty)}(e_2,d_2)-\mathcal O_{q+2}^{(\infty)}(e_4,d_4)\|_\infty\le \frac{K}{q^5}
\quad(q\ge8,\ q\equiv2\bmod6).
\]

The gap is \(\Theta(q^{-5})\) because its initial coordinate is \(\Delta(q)\). Hence even allowing an unbounded or growing number of these six-step reads cannot create a cutoff-independent positive *absolute* error tolerance. The statement concerns robust identification, not a claimed exact infinite-sequence collision.

## Proof and exact coefficient certificate

The labeled-source generating functions are

\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Multiply by \((1-z^6)^6\) and \((1-z^6)^7\), respectively. The resulting numerators are \(z(1+\cdots+z^5)^3(1+z^2+z^4)(1+z^3)\) of degree 23 and \(z^2(1+\cdots+z^5)^4(1+z^2+z^4)(1+z^3)\) of degree 29. Coefficient extraction on each residue class yields exact polynomials \(C_r(q)\) of degree five and \(T_r(q)\) of degree six. Terms in their binomial extensions vanish at the early indices, so interpolation at six/seven valid values per residue proves identities for **every** relevant integer, not a finite-fit extrapolation.

Use these exact polynomials to expand

\[
Y_q(e,d)-Y_{q+2}(E,D)=\sum_{j=1}^5 c_j(e,d,E,D)q^{-j}+O(q^{-6}),
\quad q\equiv2\pmod6.
\]

The constant coefficient vanishes because both phases 2 and 4 have limit \(-25/36\). Rational polynomial division gives the following five complete coefficients:

\[
\begin{aligned}
c_1&=-\tfrac{80}{9}(-81D+81d-17),\\
c_2&=\tfrac{10}{9}(-18792D-3888E+17496d+3888e-967),\\
c_3&=-\tfrac{40}{81}(-854631D-297432E+691335d+262440e-16988),\\
c_4&=\tfrac{40}{27}(-4916862D-2260872E+3372840d+1701000e-18479),\\
c_5&=-\tfrac{80}{243}(-349991442D-194188104E+201756582d+123084360e+3235021).
\end{aligned}
\]

The linear system \(c_1=c_2=c_3=c_4=0\) has exactly one real solution:

\[
d=-656227/472068,\quad e=69402481/101966688,\quad
D=-755303/472068,\quad E=194725627/101966688.
\]

At that solution \(c_5=55842420440/39339\ne0\). The uniqueness and nonzero fifth coefficient show the stated optimal rate among q-independent fixed calibrations. They also preclude an exact identity of the two rational functions at these calibrated values.

For the global positivity claim, exact simplification yields

\[
\Delta(q)=\frac{40P(q)}{9A(q)B(q)},
\]

where

\[
\begin{aligned}
P(q)={}&6102180493581q^5+134080545748875q^4\\
&+1233225094191450q^3+3431784881667150q^2\\
&-3622263392910916q-3120788668960440,\\
A(q)={}&4371q^5+131130q^4+1384150q^3+6031980q^2+9371424q-25782840,\\
B(q)={}&4371q^5+174840q^4+2608030q^3+17833680q^2+54654984q+29699720.
\end{aligned}
\]

The denominator is positive for all \(q\ge8\), as it is a positive multiple of \((C_q+d_2)(C_{q+2}+d_4)\), and \(C_8=98,\ C_{10}=203\), with \(C_q\) increasing. Writing \(t=q-8\ge0\), the coefficients of \(P(t+8)\), descending in degree, are

\[
(6102180493581,\ 378167765492115,\ 9429198074047290,\
115759280836964670,\ 687635127000756764,\ 1568096750641526440);
\]

every coefficient is strictly positive. Hence \(P(q)>0\), proving \(\Delta(q)>0\) for every claimed integer (indeed every real \(q\ge8\) under these polynomial extensions). Its rational leading coefficient gives the stated fifth-order limit.

For the full future horizon, \(\Delta(x)>0\) for all \(x=q+6j\ge q\) in phase 2. Since \(x^5\Delta(x)\) is continuous on \([8,\infty)\) and converges to the finite positive value \(55842420440/39339\), its supremum \(K\) is finite. Therefore \(\sup_{j\ge0}\Delta(q+6j)\le Kq^{-5}\), while the \(j=0\) coordinate is asymptotic to a strictly positive constant times \(q^{-5}\).

## Reproducibility and precise scope

The accompanying standalone Python 3/SymPy script performs integer recurrence and independent direct-label enumeration checks for 24 small cutoffs, verifies the quasipolynomial generating-function degrees, exactly reconstructs the two phases, derives the Laurent coefficients, solves the complete coefficient system over the rationals, checks all error intervals and the nonzero fifth coefficient, and proves the shifted numerator's six strict positivity coefficients. Local execution on 2026-11-17 returned **PASS**. The accompanying JSON preserves the exact parameters, certificate coefficient list, and representative finite diagnostics.

The result is an *N2 scalar observation theorem* over retained source labels. There is no new native X6 spatial/time, BRC Cell/Link/Port, or physical measurement claim. An eventual BRC interpretation requires a typed observer carrier, preservation of source provenance and joint error relations, and a future-operation fibre certificate. These have not been supplied here. A local exact certificate is not an independent mathematical review.

The optimality is only over **q-independent fixed** calibration quadruples for the phase-2/phase-4 family \(q,q+2\). q-dependent calibrations, minimax distances over independently optimized errors, exact multi-read collisions across arbitrary cutoffs, native dynamics and formal Result/review admission remain open.

## Next research direction

Determine the minimax infinite-horizon distance for the same phase-2/phase-4 family when errors may depend on the unknown cutoff. Separately, study if any pair of distinct cutoffs has a four-read exact collision, rather than inferring global injectivity from previously certified small pairs.