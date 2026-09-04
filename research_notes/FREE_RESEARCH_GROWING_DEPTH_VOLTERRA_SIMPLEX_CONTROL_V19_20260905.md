# Free Research — Growing-Depth Volterra Simplex Control

Status: `FREE_RESEARCH_FRONTIER / UNIFORM GROWING-DEPTH FACTORIAL LAW / COMMUTATOR MASS BALANCE / VARIABLE-DEPTH ROUTE ENABLED / ROOT COERCIVITY STILL OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: V18 delayed-recanonicalization / discrete-Volterra-commutator frontier
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Executive advance

The fixed-order history-mass law can be made uniform while the provenance depth grows with the parent scale.

Let `mu` be a positive locally finite measure on the logarithmic action half-line, with cumulative mass

\[
F(t):=\mu([0,t])
\]

satisfying

\[
\boxed{|F(t)-t|\le C}\tag{1.1}
\]

for all `0 <= t <= T`.  Let

\[
H_k(T):=\mu^{*k}\{x_1+\cdots+x_k\le T\}.
\]

Then, whenever `T>kC`,

\[
\boxed{
\frac{(T-kC)^k}{k!}
\le H_k(T)
\le \frac{T^k}{k!}\exp\!\left(\frac{Ck^2}{T}\right).
}\tag{1.2}
\]

If additionally `kC/T <= 1/2`,

\[
\boxed{
\exp\!\left(-\frac{2Ck^2}{T}\right)
\le \frac{k!H_k(T)}{T^k}
\le \exp\!\left(\frac{Ck^2}{T}\right).
}\tag{1.3}
\]

Consequently

\[
\boxed{
k=o(\sqrt T)
\Longrightarrow
H_k(T)=\frac{T^k}{k!}(1+o(1))
}
\tag{1.4}
\]

uniformly along that growing-depth regime.

For the prime-winding measure

\[
d\mu=\sum_q\frac{\Lambda(q)}q\,\delta_{\log q},
\qquad T=\log N,
\]

the established first-mass law gives (1.1).  Thus depths

\[
k\asymp \log\log N
\]

are safely inside the uniform factorial regime, since

\[
(\log\log N)^2/\log N\to0.
\]

This removes the previous fixed-`k` limitation from the Volterra-defect program.

---

## 2. One-sided Stieltjes comparison

Let `phi` be nonnegative and nonincreasing on `[0,T]`.  Integration by parts and (1.1) give

\[
\int\phi\,d\mu
\le \int_0^T\phi(t)\,dt+C\phi(0).
\tag{2.1}
\]

The right side is integration against

\[
\nu_+:=dt+C\delta_0.
\]

Similarly, since

\[
F(t)\ge (t-C)_+,
\]

`mu` dominates, for nonincreasing tests, the shifted Lebesgue measure

\[
\nu_-:=\mathbf1_{[C,\infty)}(t)\,dt,
\]

whose cumulative mass is `(t-C)_+`.

The simplex indicator is downward closed.  Recursive integration therefore preserves the two stochastic orders and gives

\[
H_k^{\nu_-}(T)\le H_k^\mu(T)\le H_k^{\nu_+}(T).
\tag{2.2}
\]

---

## 3. Exact comparison-model masses

For the lower model, every coordinate is translated by `C`, hence

\[
H_k^{\nu_-}(T)=\frac{(T-kC)_+^k}{k!}.
\tag{3.1}
\]

For the upper model, choose `j` of the `k` factors from Lebesgue measure and the remaining `k-j` factors from the atom at zero.  Therefore

\[
\boxed{
H_k^{\nu_+}(T)
=\sum_{j=0}^k\binom kj C^{k-j}\frac{T^j}{j!}.
}\tag{3.2}
\]

Writing `ell=k-j`, the ratio of the `ell`th term in (3.2) to `T^k/k!` is

\[
\frac{(k^{\underline\ell})^2}{\ell!}
\left(\frac CT\right)^\ell
\le \frac1{\ell!}
\left(\frac{Ck^2}{T}\right)^\ell.
\]

Summation proves the upper bound in (1.2).  The elementary inequality

\[
(1-x)^k\ge e^{-2kx}
\qquad(0\le x\le1/2)
\]

with `x=kC/T` gives the lower exponential bound in (1.3).

---

## 4. Prime-winding history volumes

Let

\[
\mathcal C_k(N)
:=\sum_{q_1\cdots q_k\le N}
\prod_{i=1}^k\frac{\Lambda(q_i)}{q_i}.
\tag{4.1}
\]

The logarithmic change of variables identifies `C_k(N)` with `H_k(log N)`.  Hence, uniformly for

\[
k=o(\sqrt{\log N}),
\]

\[
\boxed{
\mathcal C_k(N)
=\frac{(\log N)^k}{k!}
\exp\!\left(O\!\left(\frac{k^2}{\log N}\right)\right).
}\tag{4.2}
\]

The same statement remains valid with `A(N)` replacing `log N`, since

\[
A(N)=\log N+O(1).
\]

This gives a uniform finite provenance interpretation of the Gamma history law through depths much larger than any fixed degree.

---

## 5. Uniform stopped/valid commutator balance

Let `L` be the unnormalized prime-winding quotient operator and `M_A` multiplication by `A(N)`.  Define

\[
\Delta_k:=[M_A,L^k]-kL^{k+1}.
\tag{5.1}
\]

The first positive term is the measure of a valid `k`-history followed by a stopped next action.  Its mass is

\[
S_k(N)=A(N)\mathcal C_k(N)-\mathcal C_{k+1}(N).
\tag{5.2}
\]

The second positive term has mass

\[
V_k(N)=k\mathcal C_{k+1}(N).
\tag{5.3}
\]

From (4.2), uniformly for `k=o(sqrt(log N))`,

\[
\boxed{
S_k(N),V_k(N)
=\frac{k}{(k+1)!}(\log N)^{k+1}
\exp\!\left(O\!\left(\frac{k^2}{\log N}\right)\right).
}\tag{5.4}
\]

Moreover

\[
\boxed{
\frac{S_k(N)}{V_k(N)}
=1+O\!\left(\frac{k^2+1}{\log N}\right)
}
\tag{5.5}
\]

uniformly, after enlarging the implied constant according to the discrepancy constant `C`.

Thus the two sides of the discrete Volterra commutator remain mass-balanced even at the natural variable depth `k asymp log log N`.

---

## 6. Equal-mass variance readout

Let `sigma_k` and `pi_k` be the two positive measures in (5.1), with masses `S_k` and `V_k`.  Put

\[
m_k:=\min(S_k,V_k)
\]

and rescale their common parts to positive measures `sigma_k^0,pi_k^0` of mass `m_k`.  For every bounded real readout `f`, let

\[
\eta_k:=\frac{\sigma_k^0+\pi_k^0}{2m_k}.
\]

Then the centered signed-density argument gives

\[
\boxed{
\left|\int f\,d(\sigma_k^0-\pi_k^0)\right|
\le 2m_k\sqrt{\operatorname{Var}_{\eta_k}(f)}.
}\tag{6.1}
\]

The unmatched mass contributes at most

\[
|S_k-V_k|\,\|f\|_\infty.
\]

After division by `A(N)^(k+1)`, (5.4)--(5.5) give

\[
\boxed{
\frac{|\Delta_k f(N)|}{A(N)^{k+1}}
\le
\frac{2k}{(k+1)!}
\exp\!\left(O\!\left(\frac{k^2}{\log N}\right)\right)
\sqrt{\operatorname{Var}_{\eta_k}(f)}
+
O\!\left(
\frac{k(k^2+1)}{(k+1)!\log N}
\right)\|f\|_\infty.
}\tag{6.2}
\]

This is the growing-depth version of the fixed-order defect readout.

Since

\[
\sum_{k\ge K}\frac{k}{(k+1)!}=\frac1{K!},
\tag{6.3}
\]

all polynomially weighted commutator tails are factorially summable for `K asymp log log N`.

---

## 7. Exact derivation identity

The entire defect hierarchy is generated by the first defect:

\[
\boxed{
\Delta_k
=\sum_{j=0}^{k-1}L^j\Delta_1L^{k-1-j}.
}\tag{7.1}
\]

Indeed

\[
[M_A,L^k]
=\sum_{j=0}^{k-1}L^j[M_A,L]L^{k-1-j},
\]

and the `k` copies of `L^(k+1)` remove the ideal Volterra part from every placement.

The mass identity is

\[
\boxed{
\Delta_k1
=A\mathcal C_k-(k+1)\mathcal C_{k+1}.
}\tag{7.2}
\]

Equations (7.1)--(7.2) identify `Delta_k` as a two-sided history smoothing of the first parity-fold defect.

---

## 8. Important no-go: factorial tails do not invert the first defect

Uniform factorial smallness of high-order defects does not, by itself, control `Delta_1`.

Take a finite carrier with a nonzero nilpotent operator `L` satisfying `L^2=0`, and a diagonal multiplication operator `M` not commuting with `L`.  Then

\[
\Delta_1=[M,L]\ne0,
\]

while

\[
\Delta_k=0\qquad(k\ge2).
\]

Therefore no inequality of the form

\[
\|\Delta_1f\|
\le C\sup_{k\ge K}\|\Delta_kf\|
\]

can hold on arbitrary finite relation states.

This shows exactly what the growing-depth mass law does and does not solve:

- it removes the mass/distribution obstruction to variable depth;
- it does not furnish a reverse frame inequality from smoothed commutators back to the first defect.

---

## 9. Updated unique gate

A successful native closure now needs one additional, sharply typed statement.  Valid alternatives are:

1. a **history-placement frame bound** controlling the first parity-fold defect by the family of two-sided transports in (7.1);
2. a **regularity theorem for the actual prime-error field** excluding the nilpotent/localized counterexample;
3. a positive **scale-averaged commutator square function** with a reverse inequality on the arithmetic quotient state.

The desired schematic form is

\[
\boxed{
\|\Delta_1 r\|_{\rm scalar}^2
\le
C\sum_{k\le K(T)}w_k
\mathscr V_{\eta_k}(r)
+o(1),
\qquad K(T)\asymp\log T,
}
\tag{9.1}
\]

with weights for which (6.3) makes the upper history tail summable.

This is narrower than the former global positive-recurrence problem.  The variable-depth simplex and mass normalization are no longer open; only reverse coercivity on the actual arithmetic state remains.

No quantitative prime remainder, Working Truth, Foundation status, or RH-scale statement is claimed here.
