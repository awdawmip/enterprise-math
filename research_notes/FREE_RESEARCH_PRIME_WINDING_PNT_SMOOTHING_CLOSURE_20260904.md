# Free Research — Prime-Winding PNT Smoothing Closure

Status: `FREE_RESEARCH_FRONTIER / PNT_NORMALIZATION_CLOSED_AT_REAL_SMOOTHING_STRENGTH / NATIVE_FINITE_RG_GAP_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_NOT_CLAIMED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_HARMONIC_RECOALESCENCE_GAP_20260904.md`

## 1. Result

Let

\[
\psi(x):=\sum_{n\le x}\Lambda(n),
\qquad
R(x):=\psi(x)-x,
\qquad
V(u):=e^{-u}R(e^u).
\]

Starting from the finite prime-winding determinant carrier, the exact harmonic recoalescence hierarchy, and the positive degree-two provenance energy, the previous checkpoint proved

\[
\Psi_2(x)
:=\sum_{n\le x}
\bigl(\Lambda(n)\log n+(\Lambda*\Lambda)(n)\bigr)
=2x\log x+O(x).
\]

This checkpoint completes the standard real-variable smoothing step and obtains

\[
\boxed{R(x)=o(x)},
\qquad
\boxed{\psi(x)\sim x},
\qquad
\boxed{\pi(x)\sim\frac{x}{\log x}}.
\]

No complex analysis, zeta zero-free region, numerical PNT assumption, or primitive numerical value of `pi` is used.

This is not claimed as a new proof of the classical prime number theorem. The project-specific content is the carrier and interpretation of the Selberg input: prime-power winding births, Hamming/Mobius history recoalescence, and positive provenance energy. The final smoothing mechanism is classical real-variable mathematics in the Selberg--Erdos--Wright--Levinson lineage.

---

## 2. The positive primitive energy gives the second Selberg return inequality

The exact centered return equation is

\[
R(x)\log x
+
\sum_{n\le x}\Lambda(n)R(x/n)
=O(x).
\tag{2.1}
\]

Multiply by `log x` and split

\[
\log x=\log n+\log(x/n).
\]

Apply (2.1) again at the quotient scale `x/n` to the part carrying `log(x/n)`. After finite reindexing,

\[
R(x)\log^2x
=
\sum_{k\le x}
\bigl((\Lambda*\Lambda)(k)-\Lambda(k)\log k\bigr)
R(x/k)
+O(x\log x).
\]

Because

\[
\Lambda_2(k)
:=\Lambda(k)\log k+(\Lambda*\Lambda)(k)\ge0,
\]

we obtain

\[
\boxed{
|R(x)|\log^2x
\le
\sum_{k\le x}\Lambda_2(k)|R(x/k)|
+O(x\log x).
}
\tag{2.2}
\]

The cumulative weight satisfies

\[
\sum_{k\le t}\Lambda_2(k)
=2t\log t+O(t).
\]

Finite Abel summation, together with `R(y)=O(y)`, converts (2.2) into

\[
\boxed{
|R(x)|\log^2x
\le
2\int_1^x\log t\,|R(x/t)|\,dt
+O(x\log x).
}
\tag{2.3}
\]

The coefficient `2` in this smoothing kernel is exactly the coefficient already forced by the two-history logarithmic simplex in the preceding checkpoint.

---

## 3. Logarithmic triangular averaging

Put `x=e^T` and substitute `t=e^{T-u}` in (2.3). Since

\[
R(e^u)=e^uV(u),
\]

we get

\[
\boxed{
T^2|V(T)|
\le
2\int_0^T(T-u)|V(u)|\,du
+O(T).
}
\tag{3.1}
\]

Equivalently,

\[
T^2|V(T)|
\le
2\int_0^T\left(\int_0^v|V(u)|\,du\right)dv
+O(T).
\]

Define

\[
\alpha:=\limsup_{T\to\infty}|V(T)|,
\qquad
\beta:=\limsup_{T\to\infty}
\frac1T\int_0^T|V(u)|\,du.
\]

The already proved Chebyshev-scale bounds make both finite. Dividing (3.1) by `T^2` and taking the upper limit gives

\[
\boxed{\alpha\le\beta.}
\tag{3.2}
\]

The rest of the proof shows that `alpha>0` would force the strict reverse inequality `beta<alpha`.

---

## 4. Bounded signed transport

The first prime-winding mass satisfies

\[
A(x):=\sum_{n\le x}\frac{\Lambda(n)}n
=\log x+O(1).
\]

Partial summation gives

\[
A(x)
=
\frac{\psi(x)}x
+
\int_1^x\frac{\psi(t)}{t^2}\,dt.
\]

Therefore

\[
\int_0^T V(u)\,du
=
\int_1^{e^T}\frac{R(t)}{t^2}\,dt
=A(e^T)-T-\frac{\psi(e^T)}{e^T}
=O(1).
\]

Hence there is a constant `C>0` such that every interval obeys

\[
\boxed{
\left|\int_a^bV(u)\,du\right|\le C
\qquad(0\le a\le b).
}
\tag{4.1}
\]

This is the finite-current cancellation input used below. It controls absolute mass on any interval on which `V` has one sign.

---

## 5. One-sided local dynamics after a zero

Let

\[
D(x):=\sum_{ab\le x}\Lambda(a)\Lambda(b).
\]

The degree-two energy formula and elementary partial summation imply

\[
\boxed{
R(x)\log x+D(x)=x\log x+O(x).
}
\tag{5.1}
\]

The function `D` is nondecreasing because every coefficient is nonnegative.

Suppose `V(t)=0`, equivalently `R(e^t)=0`. Fix `h>=0` in a bounded interval and compare (5.1) at `e^t` and `e^{t+h}`. Monotonicity of `D` gives

\[
V(t+h)
\le
1-e^{-h}\frac{t}{t+h}+O(1/t)
=1-e^{-h}+O(1/t).
\]

On the other hand, monotonicity of `psi` gives

\[
V(t+h)
=\frac{\psi(e^{t+h})}{e^{t+h}}-1
\ge e^{-h}-1.
\]

Thus, uniformly for `h` in every fixed bounded interval,

\[
\boxed{
|V(t+h)|
\le1-e^{-h}+O(1/t).
}
\tag{5.2}
\]

Integrating and using

\[
h+e^{-h}-1\le\frac{h^2}{2}
\qquad(h\ge0)
\]

gives, for every fixed `v>0`,

\[
\boxed{
\int_t^{t+v}|V(u)|\,du
\le\frac{v^2}{2}+o_{t\to\infty}(1).
}
\tag{5.3}
\]

A zero therefore creates a definite triangular deficit relative to a persistent height `v`.

---

## 6. Sign geometry between zeros

Between consecutive jump points of `psi(e^u)`, the numerator `psi(e^u)` is constant and

\[
V(u)+1=ce^{-u},
\]

so `V` is strictly decreasing. At a prime-power jump, `V` jumps upward.

Consequently, on an interval containing no zero of `V`, the sign can change at most once: the only zero-free sign change is a negative-to-positive upward jump. A later positive-to-negative change would occur continuously and would create a zero.

Combining this with (4.1), on every zero-free interval `I`,

\[
\boxed{
\int_I|V(u)|\,du\le2C.
}
\tag{6.1}
\]

Indeed, split at the possible single sign-changing jump; each sign-constant part has absolute integral bounded by `C`.

---

## 7. Uniform block deficit

Assume for contradiction that `alpha>0`.

Fix a block length

\[
\boxed{
\delta>\frac{2C}{\alpha}+2\alpha.
}
\tag{7.1}
\]

For every sufficiently large `a`, consider the block `[a,a+delta]`. Since `alpha` is a limsup, for every small `epsilon>0` we have eventually

\[
|V(u)|\le\alpha+\epsilon.
\tag{7.2}
\]

There are two cases.

### Case A: an early zero exists

If a zero `t` lies in `[a,a+delta-alpha]`, then `[t,t+alpha]` is contained in the block. By (5.3),

\[
\int_t^{t+\alpha}|V|
\le\frac{\alpha^2}{2}+o(1).
\]

On the rest of the block use (7.2). Hence

\[
\int_a^{a+\delta}|V|
\le
(\delta-\alpha)(\alpha+\epsilon)
+\frac{\alpha^2}{2}+o(1).
\]

For sufficiently small fixed `epsilon` and sufficiently large `a`, this is at most

\[
\delta\alpha-c_1
\]

for some `c_1>0` independent of `a`.

### Case B: no early zero exists

If `[a,a+delta-alpha]` contains no zero, (6.1) controls the long part, while (7.2) controls the final segment:

\[
\int_a^{a+\delta}|V|
\le
2C+\alpha(\alpha+\epsilon)+o(1).
\]

By (7.1), for sufficiently small `epsilon` and large `a` this is at most

\[
\delta\alpha-c_2
\]

for some `c_2>0` independent of `a`.

Taking `c=min(c_1,c_2)`, every sufficiently late block satisfies

\[
\boxed{
\int_a^{a+\delta}|V(u)|\,du
\le\delta\alpha-c.
}
\tag{7.3}
\]

Partition `[A,T]` into blocks of length `delta`. The initial prefix and final remainder contribute `o(T)` after division by `T`. Therefore

\[
\boxed{
\beta\le\alpha-\frac{c}{\delta}<\alpha.
}
\tag{7.4}
\]

This contradicts (3.2). Hence

\[
\boxed{\alpha=0.}
\]

Therefore

\[
V(T)\to0,
\qquad
\frac{\psi(x)}x\to1.
\]

---

## 8. From `psi` to the prime counting function

The contribution of proper prime powers is negligible:

\[
0\le\psi(x)-\vartheta(x)
\le O(\sqrt x\log x),
\]

so

\[
\vartheta(x)\sim x.
\]

Partial summation then gives

\[
\pi(x)
=
\frac{\vartheta(x)}{\log x}
+
\int_2^x\frac{\vartheta(t)}{t\log^2t}\,dt
\sim\frac{x}{\log x}.
\]

Thus the prime-number-theorem normalization is recovered.

---

## 9. Enterprise interpretation

The completed chain is

\[
\boxed{
\begin{aligned}
\text{prime-birth Krawtchouk modes}
&\to\text{saturated winding determinant }L_x,\\
\log L_x
&=\psi(x),\\
\text{two-history harmonic simplex}
&\to\Psi_2(x)=2x\log x+O(x),\\
\text{positive return kernel}
&\to\alpha\le\beta,\\
\text{bounded signed transport + one-way jumps}
&\to\alpha>0\Rightarrow\beta<\alpha,\\
&\to\psi(x)\sim x,\\
&\to\pi(x)\sim x/\log x.
\end{aligned}}
\]

Geometrically:

> The macroscopic density `1` is selected because a nonzero persistent relative winding defect would simultaneously have to equal or lie below its own triangular past average and have a uniform deficit from that average. The positive degree-two provenance energy supplies the averaging law; finite recoalescence and one-way birth jumps supply the deficit.

---

## 10. What is and is not closed

### Closed at research-note theorem strength

- `psi(x)~x` from the prime-winding determinant plus real Selberg smoothing;
- `pi(x)~x/log x` by standard prime-power removal and partial summation;
- the coefficient `1` is no longer an unexplained imported normalization.

### Not closed

- the real-variable smoothing chain is not yet formalized in Lean in this repository;
- the PNT has not been derived solely from a primitive P000/G0 finite rotation operator with a proved spectral gap;
- the exact relation between the odd-triangle signless Poincare gap and the Selberg block-deficit proof remains interpretive rather than an equality of quadratic forms;
- no error term stronger than `o(x)` is obtained;
- no zeta-zero or Riemann-hypothesis statement follows;
- no external novelty claim is made for the classical PNT proof.

---

## 11. Next frontier

The local-to-global distribution problem is now solved at first-order density. The next genuinely new question is no longer PNT itself but the fluctuation geometry:

> Can the finite prime-winding/Hamming carrier produce a canonical centered quadratic form whose spectrum controls the size and sign oscillation of `psi(x)-x`, rather than only proving it is `o(x)`?

The first discriminating target is a finite variance identity for the centered winding current and a comparison with the existing `2-2-4` signless quotient gap. A successful result would provide an Enterprise-native remainder theory; a Riemann-hypothesis-scale bound is not assumed or claimed.
