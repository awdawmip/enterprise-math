# CBRC F7 Driver r460 — exact rational B=8 finite-box minimax certificate

Date: 2026-11-22 (+08:00). Original scientific author: \`EM-CBRCF7-83A1D4\`. This extension and exact checker: Driver line \`EM-DVR-DEBB5E\` (shared, nonblind context). The original frozen \`RR-AA38973D56330E59D315\` remains unchanged; no Native Review, Result acceptance or Task completion is claimed.

## Exact statement and quantifier scope

Preserve the *original* F7 matrix and scalar assumptions:

\[
A=I+uv^T,\quad u=(1,1,-1,-1)^T,\quad v=(1,-2,-1,2)^T,
\]

\[
q:\mathbb Z^2\to[0,\infty),\quad q(0,0)=0,\quad q(-x,y)=q(x,y),\quad
q(s,0)=1\ (s\ne0),\quad
q(x,y)\ge\tfrac12\ \ ((x,y)\ne(0,0)),
\]

with exact fixed-scale marks \(q(2,1)=q(-1,-1)=1/2\). Define

\[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4).
\]

For a nonnegative integer B, let

\[
E_B^*=\inf_{\text{all globally scalar-admissible }q}
\max_{z\in\{-B,\ldots,B\}^4}|D_q(z)|.
\]

**Theorem (exact finite-input optimum).** For every integer \(1\le B\le8\),

\[
\boxed{E_B^*=\tfrac12.}
\]

The quantifiers only restrict **the error input box**; the candidate \(q_*\) is defined on the whole of \(\mathbb Z^2\) and satisfies every original scalar condition. The theorem neither proves \(E_\infty=1/2\) nor changes the inherited global interval \(1/2\le E_\infty\le4/7\).

## Lower bound for every B≥1

For \(z=(-2,1,0,0)\), \(v^Tz=-4\), \(Az=(-6,-3,4,4)\). First-coordinate evenness, the fixed mark and nonzero positivity yield

\[
D_q(z)=q(6,-3)+q(4,4)-\frac12\ge\frac12.
\]

This z belongs to each box with \(B\ge2\). For \(B=1\), use \(z=(1,-1,0,0)\): \(v^Tz=3\), \(Az=(4,2,-3,-3)\) and

\[
D_q(z)=q(4,2)+q(3,-3)-\frac12\ge\frac12.
\]

Thus the lower bound is elementary and uniform in the original scalar admissible class.

## Upper bound: explicit exact rational full-box certificate

The accompanying standalone Python checker defines a *global* function \(q_*\) as follows:

- \(q_*(0,0)=0\), \(q_*(s,0)=1\) for \(s\ne0\), \(q_*(2,1)=q_*(1,-1)=1/2\);
- \(q_*(-x,y)=q_*(x,y)\);
- on **524** specified canonical non-axis pairs \((|x|,y)\), \(q_*(x,y)=n_{|x|,y}/40\), where each table numerator belongs to \(\{21,\ldots,40\}\);
- on all remaining non-axis nonzero pairs \(q_*(x,y)=1/2\).

These definitions satisfy the complete original scalar assumptions globally and exactly.

The verifier uses \(k=a-2b-c+2d\) and \(Az=(a+k,b+k,c-k,d-k)\) for each \(z=(a,b,c,d)\). It enumerates **all** \(17^4=83{,}521\) ordered inputs \(z\in[-8,8]^4\), computes \(40D_{q_*}(z)\) using integers only and asserts \(-20\le40D_{q_*}(z)\le20\) on each input. The computed exact maximum magnitude is 20, with **3,176** saturating inputs and zero violations. The enumerated finite domain is complete, so this constitutes a finite exhaustive proof, not a floating-point extrapolation. The candidate was discovered via sparse LP exploration, but verification requires only Python's standard library.

Checker source: [CBRC_F7_R460_BOX8_EXACT_RATIONAL_CERT_20261122.py](https://github.com/awdawmip/enterprise-math/blob/e9b3cabec1ce5b46d4a9c23dfe0bd8ce52e8a951/research_checks/CBRC_F7_R460_BOX8_EXACT_RATIONAL_CERT_20261122.py). Its 524 override entries and 83,521 constraints were also evaluated separately using integer arithmetic, with identical maximal error and saturation count.

## Scientific significance and limits

The preceding r454–r459 papers improve *quadratic energy* lower bounds by incorporating original F7 mixed witnesses. Those results remain valid, but the present exact finite-box minimax certificate shows that their gains do not already force \(E_B^*>1/2\) for \(B\le8\). An exact larger-box certificate (or a rigorously certified finite-box obstruction) is the next discriminating route. No finite B alone establishes the global equality.

Research status: an exact finite-domain theorem, under unchanged scalar assumptions, with complete integer certificate and exact lower-bound witnesses; shared-context Driver scientific extension. Original F7 contribution, frozen Result, unreviewed/native acceptance state, Activity linkage debt, other owners and protected foundations remain unchanged.
