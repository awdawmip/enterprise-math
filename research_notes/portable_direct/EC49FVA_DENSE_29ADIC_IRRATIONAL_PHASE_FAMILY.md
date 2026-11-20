# EC49FVA — A dense rational-width family of irrational lattice phases

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_MODULAR_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

Frozen science: BRC16943 @ \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Direct predecessor: EC49FUZ, PR #2866 @ \`2c07017fbeefd3e8f2bdcb26985cc1a3878e56e0\`. Original author / SID / Activity are historical provenance only; this independent note does not assert ownership, CLAIM, Result, Review, or a new authenticated Researcher-ID. The Bernoulli hit observer is a declared lossy readout of the P000 Heartbeat X6 system, not a complete native state.

## Exact model and statement

Let
\[
\beta=3/637,\quad E=31597745/1653649,\quad
u_0=\frac{21829245984}{45529434409},\quad
u_E=\frac{21829245984}{45529434409-456083905E}
=\frac{4822040484}{8132285009}.
\]
For \(0<x<1\), define
\[
T_0=(1-x)(1-\beta x),\qquad
T_E=(1-x)(1+\beta(E-1)x),
\]
\[
p_E=1-T_E,\quad a=p_0=1-T_0,\quad
b=q_E=1-u_ET_E,\quad q_0=1-u_0T_0.
\]
Set
\[
R(x)=\frac{1-a}{1-b}=\frac{T_0}{u_ET_E},
\quad S(x)=\frac{b(1-a)}{a(1-b)}=\frac b a R,
\quad t(x)=\frac{\log R(x)}{\log S(x)}.
\]

**Theorem 1 (exact congruence classification and density).** Take a rational width \(x=m/d\in(0,1)\) in reduced terms, \(29\nmid d\), and denote \(r=m d^{-1}\pmod {29}\). For every
\[
\boxed{r\in\mathbb F_{29}\setminus\{0,1,19,20,23\}},
\]
one has the exact 29-adic witnesses
\[
\boxed{v_{29}(R(x))=1,\qquad v_{29}(S(x))=0},
\]
and hence **\(t(x)\) is irrational**. There are exactly 24 eligible residue classes out of 29 for 29-integral rational widths. In every nonempty open real interval contained in \((0,1)\) there are infinitely many eligible rational widths. The five excluded classes are *not* classified as having rational \(t\); this is a sufficient witness family.

**Theorem 2 (phase nonconvergence across this family).** For each *fixed* rational width from Theorem 1, consider the cross-pair Bernoulli game on \(a=p_0,b=q_E\). Put
\[
A=\log S,\quad C=D(t\Vert a)=D(t\Vert b),\quad
r_a=\frac{a(1-t)}{t(1-a)},\quad
r_b=\frac{b(1-t)}{t(1-b)},
\]
\[
L=\frac{r_a(1-r_b^{-1})}{1-r_a},\quad
c=\frac{\log L}{A},\quad d_n=\lceil nt+c\rceil-nt.
\]
Then \(0<r_a<1<r_b\), \(A>0\), and its optimal equal-prior Bayes overlap \(G_n^*\) obeys
\[
G_n^*=\frac{e^{-nC}}{\sqrt n}\bigl(h(d_n)+O_x(n^{-1})\bigr),\qquad
h(d)=\frac{r_b^d}{2\sqrt{2\pi t(1-t)}(1+e^{Ad})}
\left(\frac1{r_b-1}+\frac1{1-r_a}\right).
\]
The continuous, glued phase function satisfies \(h(c)=h(c+1)>0\) and is strictly log-concave between those endpoints. Thus
\[
\operatorname{Acc}(\sqrt n e^{nC}G_n^*)
=[h(c),h(d_*)],\quad
d_*=\frac1A\log\frac{\log r_b}{-\log r_a}\in(c,c+1),
\]
where \(h(d_*)>h(c)\). Every fixed eligible width therefore has a **nonconvergent second-order normalized optimal risk**, with a full nondegenerate interval of limit points.

Conditional on the author-proved, still-unreviewed **endpoint-only reduction** of EC49FUQ/FUR for this frozen composite model, the same formula and accumulation interval hold for its actual composite minimax risk \(V_n(x)\), and the least-favorable endpoint weights have accumulation interval
\[
\boxed{\operatorname{Acc}(\lambda_n)=
[(1+e^{A(c+1)})^{-1},(1+e^{Ac})^{-1}].}
\]
The \(O_x(\cdot)\) constants depend on the fixed width: this is not a uniform joint \((n,x)\) theorem.

## Proof of Theorem 1

The rational constants are 29-integral where required, with
\[
\beta\equiv26,\quad E\equiv9,\quad \beta(E-1)\equiv5
\pmod {29},\qquad v_{29}(u_E)=-1.
\]
The last valuation is exact because the numerator \(4822040484\) is a 29-unit while its denominator \(8132285009\) is divisible by 29 but not by \(29^2\).

At a rational width \(x\) with 29-unit denominator, all three polynomials below can be reduced modulo 29:
\[
a=x(1+\beta-\beta x),\quad
T_0=(1-x)(1-\beta x),\quad
T_E=(1-x)(1+\beta(E-1)x).
\]
Their respective zero sets in \(\mathbb F_{29}\) are
\[
Z(a)=\{0,20\},\quad Z(T_0)=\{1,19\},\quad
Z(T_E)=\{1,23\}.
\]
Consequently for the stated 24 residue classes,
\(v_{29}(a)=v_{29}(T_0)=v_{29}(T_E)=0\).
As \(v_{29}(u_E)=-1\), the identities \(b=1-u_ET_E\)
and \(1-b=u_ET_E\) give
\[
v_{29}(b)=v_{29}(1-b)=-1.
\]
Therefore
\[
v_{29}(R)=v_{29}(T_0)-v_{29}(u_E)-v_{29}(T_E)=1,
\]
\[
v_{29}(S)=v_{29}(b)-v_{29}(a)+v_{29}(R)=0.
\]

For \(0<x<1\), the strict probability order \(0<p_E<a<b<q_0<1\)
follows from \(0<u_0<u_E<1\), \(0<\beta(E-1)<1\),
\(T_E>T_0\), and the exact rational bound
\[
u_E<\frac{1-\beta}{1+\beta(E-1)}
\le\frac{1-\beta x}{1+\beta(E-1)x}.
\]
In particular \(1<R<S\), so \(t\in(0,1)\).
If \(t=h/k\in\mathbb Q\) with \(k>0\), then
\(R^k=S^h\). Applying \(v_{29}\) yields \(k=0\),
a contradiction. This proves irrationality.

For density, fix a real open interval \(I=(\ell,u)\subset(0,1)\).
For arbitrarily large positive integers \(m\), let \(d=29m+1\).
Choose an integer \(k\) with \(k\equiv25\pmod {29}\) and
\(\ell d<k<u d\), possible when \((u-\ell)d>29\).
Then \(x=k/d\in I\) and \(x\equiv25\pmod {29}\).
Reduction of \(k/d\) preserves the fact that the denominator is
a 29-unit and preserves its residue class. Varying \(m\) produces
infinitely many distinct eligible rational widths, completing the proof.

## Proof of Theorem 2 and scope transfer

For the cross-pair, the mixture overlap is
\[
G_n(\lambda)=\frac12\sum_{k=0}^n
\min\{(1-\lambda)P_{n,a}(k),\lambda P_{n,b}(k)\},
\quad G_n^*=\max_{\lambda\in[0,1]}G_n(\lambda).
\]
The strict order \(a<b\) produces a log-likelihood crossing at
\(k=nt+O(1)\). Uniform Stirling expansion of the binomial masses at
\(k=\lfloor nt\rfloor+m\), together with geometric bounds on both
tails, gives the phase-uniform bilateral geometric overlap
\[
\sqrt n e^{nC}G_n(\lambda)=
\frac1{2\sqrt{2\pi t(1-t)}}
\sum_{m\in\mathbb Z}
\min\{(1-\lambda)r_a^{m-\{nt\}},
\lambda r_b^{m-\{nt\}}\}
+O_x(n^{-1}).
\]
The uniform bound applies to all \(\lambda\in[0,1]\): each summand
is Lipschitz in the masses, and the two geometric tails are summable.
Maximizing the piecewise-linear geometric sum gives a kink at
\(j=\lceil c+\{nt\}\rceil\) and
\(\lambda=(1+e^{A(j-\{nt\})})^{-1}\).
Summing the geometric tails then gives the displayed \(h(d_n)\).
At an exact switching phase there is a plateau of maximizers;
the optimal value remains the same by continuity.
The identity \(e^{Ac}=r_a(1-r_b^{-1})/(1-r_a)\)
implies \(h(c)=h(c+1)\).
Since
\[
\frac{d^2}{dd^2}\log h(d)=
-\frac{A^2e^{Ad}}{(1+e^{Ad})^2}<0,
\]
the circle-prefactor is nonconstant and has its unique maximum
at \(d_*\in(c,c+1)\). Theorem 1 makes \(\{nt\}\) dense;
its continuous phase image therefore attains the full interval
of limiting values.

For the full endpoint-mixture dual, define \(F_n(\lambda)\) as in
EC49FUZ using the two extra, strictly farther binomial laws
\(p_E<a<b<q_0\). Their Chernoff tails at the cross-pair boundary
are exponentially smaller: on any compact interior
\(\lambda\)-interval,
\(F_n(\lambda)-G_n(\lambda)=O_x(e^{-n(C+\eta_x)})\),
with \(\eta_x>0\).
The limiting geometric overlap increases uniformly near \(\lambda=0\)
and decreases uniformly near \(\lambda=1\), so all finite optimal
weights eventually remain in a common compact interior interval.
This extends the cross-pair formula to \(\max_\lambda F_n\)
and the limit-point argument for its optimizing weights. The
identification \(\max F_n=V_n(x)\) uses exactly the existing
EC49FUQ/FUR endpoint-reduction premise, not an additional
claim about the complete X6 native dynamics.

## Recalculation and next problem

The companion standard-library exact checker confirms:
* \(29\)-unit denominators, \(v_{29}(u_E)=-1\) and the three polynomial zero sets;
* 24 permitted classes, rational examples including \(x=7/20,1/2,3/4,100/301\);
* exact rational order and \(v_{29}(R)=1,v_{29}(S)=0\) for every tested eligible instance;
* explicit eligible witnesses in three separated real intervals.

The modular argument proves every eligible rational width; finite
execution checks arithmetic implementation and examples only.
Unresolved: classify the five omitted 29-adic classes by other
valuation primes; derive effective \(n\)-bounds uniform on controlled
width intervals; determine the distribution of \(t(x)\) and of phase
prefactors over increasing-denominator rational widths.
