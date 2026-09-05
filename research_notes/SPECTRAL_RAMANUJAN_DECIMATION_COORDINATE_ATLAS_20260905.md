# Ramanujan arithmetic coordinates from primitive spectral decimation traces

Status: `FREE_RESEARCH / EXACT FINITE HARMONIC-ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive even-decimation trace theorem
  `T_d(q)=2(phi(d)-c_d(q))`;
- finite divisor formula for Ramanujan sums;
- no continuous Fourier/Sturm--Liouville spectrum.

## 1. Centered primitive decimation trace

For `d>1`, define

\[
\mathcal T_d(q)
:=\sum_{\Psi_d(\alpha)=0}R_{2q}(\alpha).
\]

The previous spectral-arithmetic dictionary proves

\[
\mathcal T_d(q)=2(\varphi(d)-c_d(q)).
\]

Define the centered trace

\[
\boxed{
X_d(q):=\mathcal T_d(q)-2\varphi(d).
}
\]

Then exactly

\[
\boxed{X_d(q)=-2c_d(q).}
\tag{RDA-1}
\]

Thus primitive even-decimation traces are Ramanujan sums up to an affine normalization.

## 2. Exact finite orthogonality

Let `L` be any common multiple of `m,n`.  The finite Ramanujan orthogonality identity is

\[
\sum_{q=1}^{L}c_m(q)c_n(q)
=L\,\varphi(m)\,\delta_{mn}.
\]

Therefore

\[
\boxed{
\sum_{q=1}^{L}X_m(q)X_n(q)
=4L\,\varphi(m)\,\delta_{mn}.
}
\tag{RDA-2}
\]

No continuous Fourier basis is used.  A purely finite proof reduces multiplicatively to prime powers.  For `m=p^a`,

\[
c_{p^a}(q)=
\begin{cases}
\varphi(p^a),&p^a\mid q,\\
-p^{a-1},&p^{a-1}\mid q\text{ but }p^a\nmid q,\\
0,&p^{a-1}\nmid q,
\end{cases}
\]

from which the same-prime-power orthogonality is immediate; CRT then gives the general result.

## 3. Mean and variance of one primitive trace channel

For `d>1`, Ramanujan sums have zero mean over one period, hence

\[
\boxed{
\frac1d\sum_{q=1}^{d}\mathcal T_d(q)
=2\varphi(d).
}
\tag{RDA-3}
\]

The centered variance is

\[
\boxed{
\frac1d\sum_{q=1}^{d}
(\mathcal T_d(q)-2\varphi(d))^2
=4\varphi(d).
}
\tag{RDA-4}
\]

So one primitive denominator channel has the exact finite relation

\[
\operatorname{Var}(\mathcal T_d)=2\,\operatorname{Mean}(\mathcal T_d).
\]

This is an arithmetic identity, not a probabilistic limit assertion.

## 4. Finite gcd-class function space

Fix `N>=1`.  Let

\[
V_N
:=\{f:\mathbb Z/N\mathbb Z\to\mathbb C:
 f(q)\text{ depends only on }(q,N)\}.
\]

There is one gcd class for every divisor of `N`, so

\[
\dim V_N=\tau(N),
\]

the divisor-count function.

The classical finite Ramanujan theorem states that

\[
\{c_d(\cdot):d\mid N\}
\]

is an orthogonal basis of `V_N`.  Using (RDA-1), this becomes the #1159 spectral statement

\[
\boxed{
\{1\}
\cup
\{X_d(\cdot):d\mid N,\ d>1\}
\text{ is an orthogonal basis of }V_N.
}
\tag{RDA-5}
\]

Thus all finite arithmetic observables which see only gcd fibers admit coordinates in primitive rotation-spectrum decimation traces.

## 5. Exact coordinate formula

For `f in V_N`, write

\[
f(q)=\sum_{d\mid N}\widehat f(d)c_d(q).
\]

Orthogonality gives

\[
\boxed{
\widehat f(d)
=\frac1{N\varphi(d)}
\sum_{q=1}^{N}f(q)c_d(q).
}
\tag{RDA-6}
\]

For `d>1`, substitute `c_d=-X_d/2`:

\[
\boxed{
f(q)
=\widehat f(1)
-\frac12
\sum_{\substack{d\mid N\\d>1}}
\widehat f(d)X_d(q).
}
\tag{RDA-7}
\]

Equivalently in the uncentered trace observer,

\[
f(q)
=\widehat f(1)
+\sum_{d\mid N,d>1}
\widehat f(d)
\left(\varphi(d)-\frac12\mathcal T_d(q)\right).
\]

This is a finite arithmetic coordinate atlas derived from primitive spectral phase-decimation channels.

## 6. Divisibility and Mobius as special coordinate observations

The primitive trace vanishes exactly on divisibility hits:

\[
\boxed{d\mid q\iff \mathcal T_d(q)=0.}
\]

At `q=1`,

\[
\boxed{\mu(d)=\varphi(d)-\frac12\mathcal T_d(1).}
\]

So the same decimation-trace coordinate family simultaneously encodes divisor incidence, Ramanujan harmonic coordinates, and the Mobius function.

## 7. Interpretation and typing

The finite construction is

```text
primitive denominator spectrum Psi_d
    -> integer phase-multiplication polynomial R_(2q)
    -> algebraic trace T_d(q)
    -> centered trace X_d(q)
    -> exact orthogonal arithmetic coordinate channel
```

The primitive factor, its endpoint mass, its reciprocal moments and its decimation trace remain different readouts.  Orthogonality of the trace channels does not identify them with positive mass or support.

Freeze:

`RAMANUJAN_SUM = PRIMITIVE_EVEN_DECIMATION_TRACE_DEFECT`.

`GCD_CLASS_ARITHMETIC = FINITE_PRIMITIVE_TRACE_COORDINATE_SPACE`.

`NO_CONTINUOUS_FOURIER_INPUT_REQUIRED`.
