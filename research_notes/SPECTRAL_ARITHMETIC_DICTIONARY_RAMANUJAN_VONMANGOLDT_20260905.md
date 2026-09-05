# Spectral arithmetic dictionary from primitive Dirichlet rotation factors

Status: `FREE_RESEARCH / EXACT FINITE-ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive spectral factorization `Q_M = prod_(d|M,d>1) Psi_d`;
- internal phase quantization of finite Dirichlet roots;
- polynomial phase-multiplication/decimation semigroup `R_n`;
- primitive endpoint-mass and resultant laws already derived on the #1159 free-research branch.

## 1. Primitive finite spectral factor

Let

\[
Q_M(u)=(-1)^{M-1}D_{M-1}(u)
\]

be the monic finite Dirichlet spectral polynomial.  Its divisor factorization is

\[
\boxed{Q_M(u)=\prod_{\substack{d\mid M\\d>1}}\Psi_d(u).}
\]

`Psi_d` is monic integral, has degree `phi(d)`, and its roots are the finite modes whose phase fraction has reduced denominator exactly `d`.

Thus already

\[
\boxed{\deg \Psi_d=\varphi(d).}
\tag{SAD-1}
\]

This is the first entry of the arithmetic dictionary: Euler's totient is primitive spectral multiplicity.

## 2. Endpoint mass = von Mangoldt support

The primitive root product satisfies

\[
P_d:=|\Psi_d(0)|
=\begin{cases}
p,&d=p^a,\\1,&d\text{ has at least two distinct prime factors}.
\end{cases}
\]

(with the harmless sign of `Psi_2(0)` removed by absolute value).  Equivalently, as a later logarithmic readout,

\[
\boxed{\log P_d=\Lambda(d).}
\tag{SAD-2}
\]

The native integer statement is the prime/one dichotomy above; logarithm is not primitive state.

The full constant term identity

\[
|Q_M(0)|=M
\]

becomes

\[
M=\prod_{d\mid M,d>1}P_d,
\]

and taking the derived log readout recovers

\[
\boxed{\sum_{d\mid M}\Lambda(d)=\log M.}
\]

## 3. Even phase-decimation trace

Let `R_n(u)` be the integer phase-multiplication polynomial characterized internally by

\[
R_n(2-2C(\theta))=2-2C(n\theta),
\qquad
R_{mn}=R_m\circ R_n.
\]

In particular `R_2(u)=u(4-u)`.

For `q>=1` define the primitive even-decimation trace

\[
\boxed{
\mathcal T_d(q)
:=\sum_{\Psi_d(\alpha)=0}R_{2q}(\alpha),
}
\tag{SAD-3}
\]

counting the simple primitive roots once each.

### Full-length trace

For the complete length-`M` spectrum, internal phase quantization gives

\[
R_{2q}(u_{k,M})
=2-2C\left(\frac{2qk\tau}{M}\right).
\]

The finite rotation-state sum gives

\[
\sum_{k=0}^{M-1}C\left(\frac{2qk\tau}{M}\right)
=\begin{cases}
M,&M\mid q,\\
0,&M\nmid q.
\end{cases}
\]

Hence

\[
\boxed{
\sum_{k=1}^{M-1}R_{2q}(u_{k,M})
=\begin{cases}
0,&M\mid q,\\
2M,&M\nmid q.
\end{cases}}
\tag{SAD-4}
\]

This is a finite phase-sum theorem; no continuous Fourier spectrum is an input.

### Primitive Möbius inversion

The complete length-`M` spectrum is the disjoint union of primitive denominator-`d` spectra over `d|M`, `d>1`.  Therefore divisor Möbius inversion yields

\[
\mathcal T_d(q)
=2\sum_{\substack{e\mid d\\e\nmid q}}e\,\mu(d/e).
\]

Using

\[
\varphi(d)=\sum_{e\mid d}e\mu(d/e)
\]

and the divisor formula for the Ramanujan sum

\[
c_d(q)=\sum_{e\mid(d,q)}e\mu(d/e),
\]

we obtain the exact finite spectral trace law

\[
\boxed{
\mathcal T_d(q)=2\bigl(\varphi(d)-c_d(q)\bigr).
}
\tag{SAD-5}
\]

Equivalently,

\[
\boxed{
c_d(q)=\varphi(d)-\frac12\mathcal T_d(q).}
\tag{SAD-6}
\]

Thus Ramanujan sums are primitive even-decimation trace defects.

For `q=1`, `c_d(1)=mu(d)`, hence

\[
\boxed{
\mu(d)=\varphi(d)-\frac12\sum_{\Psi_d(\alpha)=0}R_2(\alpha).
}
\tag{SAD-7}
\]

So the Möbius function is the defect between primitive mode count and one half of the exact two-step decimation trace.

A direct consequence is the divisibility test

\[
\boxed{d\mid q\iff \mathcal T_d(q)=0,}
\tag{SAD-8}
\]

because `c_d(q)=phi(d)` exactly when `d|q`.

Summing (SAD-5) over `d|M` recovers the classical divisor identity internally:

\[
\boxed{
\sum_{d\mid M}c_d(q)
=\begin{cases}M,&M\mid q,\\0,&M\nmid q.\end{cases}}
\tag{SAD-9}
\]

## 4. Reciprocal moments = Jordan-totient combinations

Let

\[
Z_s(M):=\sum_{k=1}^{M-1}u_{k,M}^{-s}.
\]

The normalized finite spectral product is

\[
H_M(u)=\frac{D_{M-1}(u)}M
=\prod_{k=1}^{M-1}\left(1-\frac{u}{u_{k,M}}\right).
\]

Its elementary reciprocal-root coefficients are exactly

\[
E_j(M^2)
:=e_j(u_{1,M}^{-1},\ldots,u_{M-1,M}^{-1})
=\frac{\prod_{r=1}^{j}(M^2-r^2)}{(2j+1)!}.
\tag{SAD-10}
\]

Newton identities therefore imply that for every fixed `s>=1`

\[
\boxed{Z_s(M)=P_s(M^2),}
\tag{SAD-11}
\]

where `P_s` is a universal rational polynomial of degree `s`, determined recursively by

\[
P_s
=\sum_{j=1}^{s-1}(-1)^{j-1}E_jP_{s-j}
+(-1)^{s-1}sE_s.
\tag{SAD-12}
\]

Write

\[
P_s(X)=a_{s,0}+\sum_{r=1}^{s}a_{s,r}X^r.
\]

The primitive reciprocal moment

\[
Z_s^{\rm prim}(d)
:=\sum_{\Psi_d(\alpha)=0}\alpha^{-s}
\]

is the divisor Möbius transform of `Z_s(d)`.  For `d>1` the constant coefficient drops out, giving

\[
\boxed{
Z_s^{\rm prim}(d)
=\sum_{r=1}^{s}a_{s,r}J_{2r}(d).
}
\tag{SAD-13}
\]

The first cases are

\[
\boxed{Z_1^{\rm prim}(d)=\frac{J_2(d)}6,}
\]

\[
\boxed{Z_2^{\rm prim}(d)=\frac{2J_4(d)+5J_2(d)}{180},}
\]

\[
\boxed{Z_3^{\rm prim}(d)=\frac{8J_6(d)+21J_4(d)+42J_2(d)}{7560}.}
\]

Thus Jordan totients are the natural arithmetic coordinates of primitive reciprocal spectral moments.

Equivalently, near the endpoint `u=0`,

\[
-\frac{\Psi_d'(u)}{\Psi_d(u)}
=\sum_{s\ge1}Z_s^{\rm prim}(d)u^{s-1},
\]

so the entire Jordan hierarchy is encoded in the endpoint resolvent of the primitive finite spectral algebra.

## 5. Resultants = dilated von Mangoldt kernel

For `2<=m<n`, the native spectral resultant theorem gives

\[
|\operatorname{Res}(\Psi_m,\Psi_n)|
=\begin{cases}
p^{\varphi(m)},&n/m=p^a,\\1,&\text{otherwise}.
\end{cases}
\]

Therefore the derived logarithmic readout is exactly

\[
\boxed{
\frac1{\varphi(m)}
\log|\operatorname{Res}(\Psi_m,\Psi_n)|
=\mathbf 1_{m\mid n}\,\Lambda(n/m).
}
\tag{SAD-14}
\]

A log-free prime-specific form is

\[
\boxed{
\frac1{\varphi(m)}v_p\!\left(
|\operatorname{Res}(\Psi_m,\Psi_n)|
\right)
=\mathbf 1_{\{n/m=p^a,\ a\ge1\}}.
}
\tag{SAD-15}
\]

Thus pairwise primitive spectral resultants are the prime-power incidence kernel on the divisibility poset.

For fixed `m`, in the half-plane of absolute convergence `Re(s)>1`,

\[
\boxed{
\frac1{\varphi(m)}
\sum_{n>m}
\frac{\log|\operatorname{Res}(\Psi_m,\Psi_n)|}{n^s}
=-m^{-s}\frac{\zeta'(s)}{\zeta(s)}.
}
\tag{SAD-16}
\]

This is a clean interface to analytic prime theory; it does not by itself prove any new zero-free region or RH statement.

## 6. Spectral reconstruction of prime factorization

The endpoint factor supplies the virtual `m=1` von-Mangoldt contribution.  Combining it with all proper-divisor resultants gives

\[
\boxed{
 n
=|\Psi_n(0)|
\prod_{\substack{m\mid n\\2\le m<n}}
|\operatorname{Res}(\Psi_m,\Psi_n)|^{1/\varphi(m)}.
}
\tag{SAD-17}
\]

Equivalently, prime by prime,

\[
\boxed{
 v_p(n)
=\mathbf 1_{\{n=p^a\}}
+\sum_{\substack{m\mid n\\2\le m<n}}
\frac1{\varphi(m)}
 v_p|\operatorname{Res}(\Psi_m,\Psi_n)|.
}
\tag{SAD-18}
\]

Every summand on the right is `0` or `1`.  The finite spectral resultant neighborhood of `Psi_n`, together with its endpoint mass, reconstructs the ordinary prime factorization of `n`.

## 7. Dirichlet-series form of primitive moments

For `Re(w)>2s+1`, (SAD-13) and the standard Dirichlet series for Jordan totients give

\[
\boxed{
\sum_{d\ge2}\frac{Z_s^{\rm prim}(d)}{d^w}
=\sum_{r=1}^{s}a_{s,r}
\left(\frac{\zeta(w-2r)}{\zeta(w)}-1\right).
}
\tag{SAD-19}
\]

Hence reciprocal primitive spectral moments naturally produce finite linear combinations of shifted zeta ratios.  This is an interface theorem, not a claimed solution of the zeta-zero problem.

## 8. Arithmetic dictionary

For one and the same finite primitive spectral factor `Psi_d`:

```text
primitive degree                  -> phi(d)
endpoint root mass |Psi_d(0)|    -> exp(Lambda(d))  [log is derived]
even decimation trace R_(2q)     -> Ramanujan sum c_d(q)
q=1 decimation trace             -> Mobius mu(d)
reciprocal spectral moments      -> Jordan totients J_2,...,J_(2s)
pairwise primitive resultants    -> von-Mangoldt prime-power incidence
```

These observables are not identified with one another.  The distinction is structurally important: primitive support/multiplicity, positive endpoint mass, decimation trace, reciprocal moment data, and pairwise resultant coupling are different finite carriers/readouts.

This is compatible with the project-wide branch-typing rule that Boolean support, positive mass, provenance/orientation, and amplitude-like data must not be silently collapsed.

## 9. Scope

No historical novelty is claimed for Euler/Jordan totients, Mobius, von Mangoldt, Ramanujan sums, their classical divisor identities, or classical cyclotomic analogues.  The theorem-candidate strength here is the common finite Dirichlet-rotation spectral realization and its internal divisor/decimation derivation.

Freeze:

`PRIMITIVE_ROTATION_SPECTRUM -> ARITHMETIC_FUNCTION_DICTIONARY`.

`EVEN_DECIMATION_TRACE_DEFECT = RAMANUJAN_SUM`.

`SPECTRAL_RESULTANT_KERNEL = VON_MANGOLDT_DIVISIBILITY_KERNEL`.
