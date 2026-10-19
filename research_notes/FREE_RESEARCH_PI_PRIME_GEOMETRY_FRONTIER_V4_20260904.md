# Free Research — Pi-to-Prime Geometry Frontier V4

Status: `FREE_RESEARCH_CURRENT_FRONTIER / SELBERG_COEFFICIENT_CLOSED / EXACT_MINUS_ONE_SUPPORT_MODE_EXCLUDED / LOG_SCALE_HARDY_LIMIT / PNT_ENERGY_TRANSFER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V3_20260904.md`

## 1. Current unified architecture

The pi-to-prime line now consists of four coupled layers.

### A. Completion magnitude

For the endogenous full-turn constant `tau` and the arithmetic prime-birth block `B_M` of the genuine Hamming/Krawtchouk integer spectrum,

\[
\tau^2
=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1}
\]

at the existing analytic-completion strength.

The coefficient `3!` is the cardinality of the ordered three-flip history fiber over a common shell-3 endpoint.

### B. Native three-sector chirality

For the native cycle matrix `P` and `J=P^2-P`,

\[
\chi_3(p)=\frac13\operatorname{Tr}(JP^p),
\]

so primes act on the native `120 degree` orientation channel as ramified, preserving, or reversing according to their residue modulo `3`.

### C. Saturated prime-winding determinant

The finite tower

\[
\mathcal W_M
=\bigoplus_{p\le M}pI_{\lfloor\log_pM\rfloor}
\]

satisfies

\[
\det\mathcal W_M=L_M=\operatorname{lcm}(1,\ldots,M),
\qquad
\psi(M)=\log\det\mathcal W_M.
\]

The jump of this determinant is exactly the von Mangoldt prime-power current.

### D. Harmonic recoalescence and return geometry

The ordered harmonic history volumes

\[
\mathcal H_r(N)
=\sum_{n_1\cdots n_r\le N}
\frac1{n_1\cdots n_r}
\]

obey the exact Möbius recoalescence law

\[
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H_r(\lfloor N/d\rfloor)
=\mathcal H_{r-1}(N).
\]

At degree two this forces Selberg's coefficient `2`, and the quotient generators `2` and `4` form an odd triangle that forbids a nonzero exact sign-reversing return mode.

---

## 2. First V3 gate is closed

Define

\[
M_j(N)
=\sum_{d\le N}\frac{\mu(d)}d
\log^j(N/d).
\]

The degree-one harmonic collapse gives

\[
M_0(N)=O(1),
\qquad
M_1(N)=O(1).
\]

The degree-two history volume has the logarithmic-simplex expansion

\[
\mathcal H_2(\lfloor y\rfloor)
=\frac12\log^2y+2\gamma\log y+C_2
+O((1+\log y)/\sqrt y).
\]

The exact collapse `H_2 -> H_1` therefore gives

\[
\boxed{M_2(N)=2\log N+O(1).}
\]

Consequently the positive primitive energy

\[
\Psi_2(N)
=
\sum_{n\le N}\Lambda(n)\log n
+
\sum_{ab\le N}\Lambda(a)\Lambda(b)
\]

satisfies

\[
\boxed{
\Psi_2(N)=2N\log N+O(N).
}
\]

The V3 forcing term is therefore

\[
\boxed{F(N)=O(N).}
\]

The coefficient `2` is geometrically the inverse of the area coefficient `1/2` of the ordered two-history logarithmic simplex.

---

## 3. Positive factorial provenance extends to every degree

For

\[
\Lambda_r:=\mu*\log^r,
\qquad
(Df)(n)=f(n)\log n,
\]

we have the exact recurrence

\[
\boxed{
\Lambda_{r+1}=D\Lambda_r+\Lambda*\Lambda_r.
}
\]

It follows inductively that every `Lambda_r` is nonnegative. Degree `r` decomposes into positive ordered collision channels involving at most `r` prime-winding histories.

At the top squarefree shell with exactly `r` distinct directions, commutative scalarization leaves coefficient `r!`. Thus the shell-3 factor `3!` and Selberg's degree-two energy are consecutive members of one positive provenance hierarchy.

---

## 4. Floor-free normalized return equation

For real `x>=2`, let

\[
r(x)=\frac{\psi(x)}x-1.
\]

The coefficient-two formula and the linear boundary transport imply

\[
\psi(x)\log x
+
\sum_{a\le x}\Lambda(a)\psi(x/a)
=2x\log x+O(x).
\]

The exact factorial mass plus `psi(x)=O(x)` gives

\[
\sum_{a\le x}\frac{\Lambda(a)}a
=\log x+O(1).
\]

Therefore

\[
\boxed{
r(x)
+
\frac1{\log x}
\sum_{a\le x}\frac{\Lambda(a)}a r(x/a)
=O(1/\log x).
}
\]

This is the current clean return equation.

---

## 5. Return mass is uniform in logarithmic scale

Define

\[
\nu_T
=\frac1T
\sum_{a\le e^T}\frac{\Lambda(a)}a
\delta_{\log a/T}.
\]

Then uniformly for `0<=u<=1`,

\[
\boxed{
\nu_T([0,u])=u+O(1/T).
}
\]

Hence `nu_T` converges to Lebesgue measure with discrepancy `O(1/T)` against fixed bounded-variation tests.

The limiting quotient-return operator is therefore

\[
(\mathcal Hf)(t)=\frac1t\int_0^t f(v)\,dv.
\]

Its bounded homogeneous equation

\[
f+\mathcal Hf=0
\]

has only the zero solution.

This removes every fixed smooth logarithmic-scale `-1` mode. The only possible surviving obstruction is concentration/roughness that is invisible to fixed smooth tests.

---

## 6. Exact finite support gap

Let

\[
q_2(n)=\lfloor n/2\rfloor,
\qquad
q_4(n)=\lfloor n/4\rfloor.
\]

Then

\[
q_2\circ q_2=q_4.
\]

For

\[
\delta_2f(n)=f(n)+f(q_2(n)),
\qquad
\delta_4f(n)=f(n)+f(q_4(n)),
\]

we have

\[
\boxed{
2f(n)=\delta_2f(n)+\delta_4f(n)-\delta_2f(q_2(n)).
}
\]

Thus exact sign reversal along all prime-power quotient edges forces `f=0`.

The quantitative form is

\[
\boxed{
\sum_{n=4}^{N}|f(n)|^2
\le
\frac94\sum_{n=2}^{N}|\delta_2f(n)|^2
+
\frac34\sum_{n=4}^{N}|\delta_4f(n)|^2.
}
\]

Accordingly, the V3 phrase “find a two-step spectral gap” is now refined:

- support-level gap: **closed**;
- smooth limiting gap: **closed**;
- arithmetic energy-to-edge-defect transfer: **open**.

---

## 7. Current exact theorem status

- prime birth as irreducible Krawtchouk mode: `EXACT FINITE`;
- prime powers as winding-layer births: `EXACT FINITE`;
- `det W_M=lcm(1,...,M)`: `EXACT FINITE`;
- quotient determinant RG and Möbius inverse: `EXACT FINITE`;
- factorial provenance hierarchy: `EXACT ALGEBRAIC`;
- `psi(M)=Theta(M)`: `PROVED`;
- exact centered return equation: `EXACT FINITE`;
- harmonic recoalescence hierarchy: `EXACT FINITE`;
- `Psi_2(M)=2M log M+O(M)`: `PROVED / ELEMENTARY ASYMPTOTIC`;
- logarithmic return-mass discrepancy: `PROVED`;
- exact nonzero `-1` support mode: `EXCLUDED`;
- uniform signless support Poincare inequality: `PROVED / EXACT FINITE`;
- energy-to-defect transfer for the actual error profile: `OPEN`;
- `psi(M)~M`: `OPEN`;
- `pi(M)~M/log M`: `OPEN`;
- Foundation or Working Truth promotion: `NO`.

---

## 8. Current artifacts

Primary new theorem packet:

- `research_notes/FREE_RESEARCH_PRIME_WINDING_HARMONIC_RECOALESCENCE_GAP_20260904.md`.

Exact checker:

- `scripts/check_free_research_prime_winding_harmonic_gap.py`.

Earlier V3 artifacts remain provenance and dependencies; V4 is the current research frontier.

---

## 9. Next mother question

The remaining bridge is now sharply typed:

> Can the degree-three positive provenance energy be polarized into a Gram form that controls the degree-two signless quotient-edge defects, at least on the `2-2-4` odd triangles carrying the finite support gap?

A sufficient estimate is

\[
\boxed{
\frac1{\log N}
\sum_{a\le N}\frac{\Lambda(a)}a
|r(N)+r(N/a)|^2\to0.
}
\]

Once this is obtained, the exact finite odd-triangle inequality or the Hardy limiting equation forces

\[
r(N)\to0,
\]

which is equivalent to the prime number theorem normalization.
