# PREFIX-1004 — Native X6 single-Link first-interior exact scalarization and sharp asymptotic

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / EXACT_TYPED_Z2_BRC_CHECKED / NOT_REVIEWED. This is an independently saved portable scientific result, not an authenticated shared Task Result, CLAIM, or Review.

## Frozen scientific scope

P000 V5 is fixed at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. The setting is an affine X6 Cell torsor with a chosen, chart-relative anchor; six signed primitive spatial axes, twelve directed ports and a separately typed step counter. The local signed Stage46 BRC *candidate* has incoming-neighbour port h, outgoing direction d, coefficient C(h,d)=1/6−[h=d], and next incoming port −d. Initial incoming port: −e1. Close the undirected Link {0,e1} by absorbing branches in both directions without renormalizing.

Branch weights and phases belong to the positive-weight Z2 phase cover. The signed character is taken *per complete joint fibre* (terminal Cell, last incoming-neighbour port), before squaring and summing. This is model mathematics, not an admitted heartbeat-physics claim. The proof extends exact PREFIX-1003 at enterprise-math@d9c53f6af236cf7d128409c9eb07dd3e735f523c.

## Theorem 1004.1: exact all-length marked Laurent scalarization

All polynomials below are formal elements of the native chart displacement group ring, not new spatial axes. Set

\[
S(z)=\sum_{i=1}^{6}z_i,\qquad U(z)=\sum_{i=1}^{6}z_i^{-1}.
\]

The *integer numerator* of the free BRC packet at length n with last actual step +e_j (terminal incoming-neighbour −e_j) is, for n≥3,

\[
\boxed{F_{n,j}(z)=z_j S^{n-3}\Big((n-1)SU-36(n-3)-6S/z_1-6S/z_j\Big).}
\]

With last actual step −e_r (terminal incoming-neighbour +e_r), for n≥2 the numerator is

\[
\boxed{N_{n,r}(z)=z_r^{-1}S^{n-2}(S-6z_r).}
\]

The corresponding masked packets for the one-Link absorbing model, for every integer n≥5, are

\[
\boxed{\begin{aligned}
F^L_{n,j}&=F_{n,j}-z_1F_{n-1,j}+25z_1z_jS^{n-4},\\
N^L_{n,r}&=N_{n,r}-z_1N_{n-1,r}.
\end{aligned}}
\]

All these are amplitude *numerators*: divide each coefficient at step n by 6^n. Hence the complete first-interior joint-port mass is precisely

\[
\boxed{M^L_{n,1}=\frac{1}{36^n}\operatorname{CT}
\left(\sum_{j=1}^{6}F^L_{n,j}(z)F^L_{n,j}(z^{-1})
+\sum_{r=1}^{6}N^L_{n,r}(z)N^L_{n,r}(z^{-1})\right).}
\]

Here CT extracts the zero vector coefficient in all six Laurent variables. At each n≥5 every packet factors as S^(n−4) times a Laurent polynomial of bounded monomial support *independent of n* and with coefficients at most linear in n. Thus the scalar is a finite linear combination of shifted six-label collision sums

\[
H_m(\delta)=\sum_{\substack{a\in\mathbb N^6\\|a|=m}}
\binom{m}{a}\binom{m}{a+\delta},\qquad m=n-4,
\]

where the same finite shift set works for all n. A binomial with an invalid argument is zero. Unmarked H_m(0) is the already known A6(m); no unproved claim is made that *all* marked shifts reduce to A6 alone.

**Proof.** Locate the unique negative step −e_r in the first-interior sector. If the preceding positive prefix has length m≥1, its numerator before that step is S^(m−1)(S−6z_r); if m=0, its local numerator is 1−6[r=1]. A positive suffix of length q≥1, ending with +e_j, contributes z_j(1−6[r=j]) for q=1, or z_j(S−6z_r)S^(q−2) for q≥2. Multiply by z_r^(-1) for the negative displacement and sum over all negative positions. The n−3 interior positions yield identical contributions. The two polynomial summations simplify via

\[
\sum_r z_r^{-1}(S-6z_r)^2=S^2U-36S
\]

and

\[
\sum_rz_r^{-1}(S-6z_r)(2-6[r=1]-6[r=j])
=2SU-6S/z_1-6S/z_j.
\]

These yield F. Putting the negative step last gives N. For the mask reuse the separately proved complete joint-fibre identity of PREFIX-1003,

\[
\Psi^L_{n,1}=\Psi_{n,1}-\tfrac16\tau_{e_1}\Psi_{n-1,1}
+\tfrac{25}{216}\tau_{e_1}\Psi_{n-3,0}.
\]

Multiplication by 6^n gives the two masked identities, because the positive-only packet at length m≥1 has terminal +e_j-travel numerator z_jS^(m−1), while it has no negative-travel terminal component. Finally, in the Laurent group ring, multiplying each terminal-port packet by its reversed monomial packet and taking CT exactly sums squares of its signed coefficients. Different named ports are never coherently merged. QED.

An explicit combinatorial coefficient form uses T_m(a)=m!/∏a_i! when a_i≥0 and ∑a_i=m, and zero otherwise. For positive last travel +e_j, terminal displacement x,

\[
\begin{aligned}
a_{n,j}(x)={}&(n-1)\sum_rT_{n-2}(x-e_j+e_r)-36(n-3)T_{n-3}(x-e_j)\\
&-6T_{n-2}(x-e_j+e_1)-6T_{n-2}(x),
\end{aligned}
\]

and for last travel −e_r,

\[
b_{n,r}(x)=T_{n-1}(x+e_r)-6T_{n-2}(x).
\]

Then a^L_(n,j)(x)=a_(n,j)(x)−a_(n−1,j)(x−e1)+25T_(n−4)(x−e1−ej), and b^L_(n,r)(x)=b_(n,r)(x)−b_(n−1,r)(x−e1). Squaring these integers and dividing their sum by 36^n is a second exact scalar algorithm; the reduction is for this declared observer and does not justify erasing histories before other port-resolved future operations.

## Theorem 1004.2: sharp masked first-interior asymptotic

Write M_(n,1) for the unmasked first-interior mass, and M_n for the unmasked outer-grade mass. Then

\[
\boxed{\lim_{n\to\infty}\frac{M^L_{n,1}}{M_{n,1}}=\frac{7475}{11664}.}
\]

Consequently, independently re-deriving the PREFIX-998 first-interior/outer leading ratio 35/4 and using the PREFIX-996 outer asymptotic,

\[
\boxed{\lim_{n\to\infty}\frac{M^L_{n,1}}{M_n}=\frac{261625}{46656},}
\]

\[
\boxed{M^L_{n,1}\sim\frac{261625}{41472\pi^{5/2}}n^{-5/2}.}
\]

The single occupied Link changes the leading coefficient but not this power-law exponent, within this exact absorbing Stage46 candidate.

**Proof.** Apply analytic coefficient extraction only *after* the exact typed BRC group-ring calculation above. Parseval converts CT to a unit-torus scalar integral. For |S(z)|≤6 equality holds exactly along the common-phase diagonal; away from that diagonal all contributions are exponentially smaller despite the polynomial factors. In a neighbourhood of the diagonal set z_i=exp(i(φ+t_i/√n)), with ∑t_i=0 and V=∑t_i². Direct expansion of the already derived Laurent symbols yields

\[
SU=36-\frac{6V}{n}+O(n^{-3/2}),
\quad \frac{|S|^{2(n-3)}}{36^{n-3}}\longrightarrow e^{-V/6}.
\]

For each positive-terminal port j, after factoring out z_jS^(n−3),

\[
\frac{F_{n,j}}{z_jS^{n-3}}\longrightarrow -6V,
\quad
\frac{F^L_{n,j}}{z_jS^{n-3}}\longrightarrow -5V+25/6.
\]

All negative-terminal packets are smaller by O(n^(−1/2)) in this neighbourhood and vanish from the leading scalar mass. A standard Gaussian majorant near the diagonal and the strict exponential gap outside it justify dominated Laplace convergence for the polynomial prefactors. In the five-dimensional relative-coordinate Gaussian with radial density proportional to exp(−V/6), E[V]=15 and E[V²]=315. Thus

\[
\lim\frac{M^L_{n,1}}{M_{n,1}}
=\frac{\mathbb E[(-5V+25/6)^2]}{\mathbb E[(-6V)^2]}
=\frac{25(315)-(250/6)(15)+625/36}{36(315)}
=\frac{7475}{11664}.
\]

The corresponding free first-interior/outer mass ratio is E[36V²]/36²=315/36=35/4. The prior outer-grade formula M_n∼9/(8π^(5/2))n^(−5/2) then gives the other two results. QED.

The Gaussian integral and π here are *proof tools for asymptotic integer coefficient extraction*, not BRC-native update inputs or physical residual computations. No classical trigonometric dynamics, Taylor, Padé, Cayley or matrix-exponential fallback is used.

## Exact execution and scope

The accompanying independent script uses a positive integral N[Z2] phase-cover branch recurrence with full terminal Cell/port, plus the derived multinomial formulas. They agree on **every joint fibre** for all n=5,…,9. In particular the masked first-interior mass at n=8 is exactly 259181485/78364164096, matching PREFIX-1003. Exact scalar sums were checked at n=5,6,7,8,9,10,12,14,16,20. At n=20 the rational masked/free ratio has decimal display 0.660246413473, toward the analytically proved 7475/11664≈0.640860768176. This independent phase-cover checker is not claimed as an invocation of the historical canonical Stage46 core; all physical calibration, independent Review and formal Result admission remain pending.

## Continuation and authority

Next: determine the symmetry orbits of the finite marked collisions H_m(δ), compress their exact recurrence if possible, extend the finite-prefix mechanism to k=2 (five-step horizon) and compare an explicitly defined norm-preserving Link response with absorption.

Historical R6 provenance: EM-DIRECT-FBEA5D; Activity RA-3FB2D033BE6048D8712FF056; old Session MCP-45ad6d29cd534c1aad25595a72e3c532. They do not authenticate this turn or confer CLAIM/PROGRESS permission. The old owner-inventory request r6-20261122-1100-scoped-leased-owner-prefix1003-v1 has now returned SUCCEEDED with scoped LEASED=[] and execution_authorized=false at its original as-of snapshot; no live shared CLAIM is inferred. Mathematical mother objective B_fix,odd(32)∈{19,20} is open.