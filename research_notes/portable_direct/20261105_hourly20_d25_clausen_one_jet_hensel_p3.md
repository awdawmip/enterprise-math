# D25 — Clausen one-jet Hensel curvature reduction

Date: 2026-11-05 (+08). Role: TASK_RESEARCH; author-side portable proof and exact check. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Status: AUTHOR-PROVED / 94 EXACT PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## Theorem (two universal one-jet curvature constants)

Let \(p=6n+1\ge7\) be prime and define the terminating polynomial over \(\mathbb Z_{(p)}\)

\[
G(z)={}_2F_1(-n,-2n;1-p/2;z),\qquad
L(z)=G(z)+12zG'(z),\qquad
\Psi(z)=G(z)L(z).
\]

At \(x=1/2\), set \(g=G(x)\), \(v=G'(x)\), \(f=g(g+6v)\). The following first identity holds exactly in \(\mathbb Z_{(p)}\), with no first-digit assumption:

\[
\boxed{\Psi'(x)=A=6v^2+(8+6p)gv+\frac43(p-1)^2g^2.}
\]

In addition,

\[
\boxed{\frac12\Psi''(x)\equiv B_0=\frac49(5g^2+24gv+9v^2)\pmod p.}
\]

Suppose the frozen first-digit premise \(f=\Psi(x)\equiv0\pmod p\) holds. The previously proved simple-root theorem for this polynomial shows that \(A\) is a unit, with exactly one of \(g\equiv0\) or \(g+6v\equiv0\pmod p\). The curvature ratio becomes

\[
\boxed{
\frac{\Psi''(x)/2}{\Psi'(x)}\equiv
\begin{cases}
2/3&g\equiv0\pmod p,\\
10/3&g+6v\equiv0\pmod p
\end{cases}\pmod p.
}
\]

With \(d=f/A\in p\mathbb Z_{(p)}\), the unique Hensel root of \(\Psi\) lifting \(x\bmod p\) satisfies

\[
\boxed{x_p\equiv\frac12-d-cd^2\pmod{p^3},
\quad c=\frac23\text{ for the G branch},\quad
c=\frac{10}3\text{ for the L branch}.}
\]

**The root can be reconstructed from the first jet \((p,g,v,\text{branch})\) modulo \(p^3\)**. No numerical \(G''\), \(G'''\), or separate second derivative of \(\Psi\) is needed. The frozen premise applies to the target classes \(p\equiv13,19\pmod{24}\). For any other \(p\equiv1\pmod6\), the theorem is conditional on that explicitly stated premise.

## Proof

The exact Gauss differential equation is

\[
z(1-z)G''+[1-p/2-(1-3n)z]G'-2n^2G=0.
\]

Since \(6n=p-1\), at \(x=1/2\),

\[
G''(x)=(p-1)v+\frac29(p-1)^2g.
\]

Using \(L(x)=g+6v\), \(L'(x)=13v+6G''(x)\) and the product rule,

\[
\Psi'(x)=v(g+6v)+g[13v+6G''(x)]
=6v^2+(8+6p)gv+\frac43(p-1)^2g^2.
\]

Differentiate the same Gauss equation once and reduce at \(x\) modulo \(p\):

\[
G''(x)\equiv-v+\frac29g,\qquad
G'''(x)\equiv\frac{65}{9}v-\frac29g\pmod p.
\]

Since \(L''(x)=25G''(x)+6G'''(x)\),

\[
\Psi''=G''L+2G'L'+GL''
\quad\Longrightarrow\quad
\frac12\Psi''(x)\equiv\frac49(5g^2+24gv+9v^2)\pmod p.
\]

In the \(g=0\) branch, \(A\equiv6v^2\), \(B_0\equiv4v^2\), so \(B_0/A\equiv2/3\). In the \(g+6v=0\) branch, \(v=-g/6\), \(A\equiv g^2/6\), \(B_0\equiv5g^2/9\), so \(B_0/A\equiv10/3\). Unit denominators follow from the prior simple-root theorem.

For \(x_p=x-\delta\), Taylor expansion gives \(0=f-A\delta+B\delta^2+O(\delta^3)\), where \(B=\Psi''(x)/2\). With \(d=f/A\in p\mathbb Z_p\), solving to order \(p^3\) yields \(\delta\equiv d+(B/A)d^2\pmod{p^3}\). Only \(B/A\bmod p\) is required, yielding the two constants and the one-jet root formula. QED.

## Exact validation

The companion program d25_clausen_one_jet_hensel_20261105.py was executed locally with exact modular integer arithmetic for all 94 primes \(7\le p\le1200\), \(p\equiv1\pmod6\). It independently forms \(G,G',G'',G'''\) from coefficient moments, checks exact \(A\) and the curvature ratio, and independently recomputes \(G(z),G'(z)\) at the predicted root to confirm \(\Psi(x_p)\equiv0\pmod{p^3}\). Result: **94/94 PASS**; finite testing is not the all-prime proof of the first-digit premise.

Examples \((p,\mathrm{branch},A\bmod p,c\bmod p,x_p\bmod p^3)\):
\((7,L,3,1,165)\), \((13,G,6,5,1918)\), \((19,G,5,7,675)\), \((31,L,27,24,28970)\), \((373,G,211,125,31342631)\).

## Information conservation / continuation

This is a specific certified BRC compression for the local Clausen-root operator: \((p,g,v,\mathrm{branch},\mathrm{precision})\) retains the data needed for its derivative and Hensel lift. Forgetting the branch leaves two inequivalent curvature values. It does not compress the full signed six-port, the original-class crystalline H0/B0 carrier, or the six-dimensional native world.

Next scientific action: combine the branch-local one-jet root with the prior signed six-port/harmonic expression for \(W_p-p\bmod p^3\); evaluate the resulting source residuals at \(p=13,19,373\) and seek a uniform finite cancellation certificate for frozen \(\Delta_p-R_p\). Original native p373 H0/B0, \([X]U\bmod139129\), rank, Frobenius direction, \(\eta,\kappa\) and independent review remain open.

Author-side portable evidence only. Native checkpoint and historical contributor/source pins are untouched. This is neither native task execution, mathematical admission nor native H0/B0 computation.
