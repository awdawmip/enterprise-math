# Native full and primitive spectral discriminant formulas

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- `R_M'(u)=M D_(M-1)(u)`;
- the two-critical-value identity;
- primitive divisor factorization;
- native prime-power resultant law.

## 1. Full finite spectral polynomial

Let

\[
Q_M(u):=(-1)^{M-1}D_{M-1}(u),
\]

so `Q_M` is monic of degree `M-1` with simple real roots

\[
u_{1,M},\ldots,u_{M-1,M}.
\]

The root product is

\[
\boxed{
\prod_{k=1}^{M-1}u_{k,M}=M.
}
\tag{SD-1}
\]

Complement symmetry permutes the root set, hence also

\[
\boxed{
\prod_{k=1}^{M-1}(4-u_{k,M})=M.
}
\tag{SD-2}
\]

---

## 2. Derivative at a critical spectral root

Write `R=R_M` and `D=D_(M-1)`.  The exact finite identities are

\[
R'(u)=M D(u),
\]

\[
R(u)(4-R(u))=u(4-u)D(u)^2.
\]

Let `alpha` be a root of `D`.  Then `R(alpha)` is either `0` or `4`.

Expand the second identity to second order at `alpha`.  Because the critical point is simple,

\[
\boxed{
|R''(\alpha)|
=\frac{2M^2}{\alpha(4-\alpha)}.
}
\tag{SD-3}
\]

Since

\[
D'(\alpha)=R''(\alpha)/M,
\]

and `Q_M'` differs only by the global sign,

\[
\boxed{
|Q_M'(\alpha)|
=\frac{2M}{\alpha(4-\alpha)}.
}
\tag{SD-4}
\]

---

## 3. Full discriminant

For a monic polynomial with simple real roots,

\[
\operatorname{Disc}(Q_M)
=\prod_{k=1}^{M-1}|Q_M'(u_{k,M})|.
\]

Insert (SD-4), (SD-1), and (SD-2):

\[
\begin{aligned}
\operatorname{Disc}(Q_M)
&=
\frac{(2M)^{M-1}}
{\left(\prod_k u_{k,M}\right)
 \left(\prod_k(4-u_{k,M})\right)}\\
&=\frac{(2M)^{M-1}}{M^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{Disc}(Q_M)
=2^{M-1}M^{M-3}.
}
\tag{SD-5}
\]

For `M=2`, the right side is interpreted literally as `2 * 2^(-1)=1`, agreeing with the linear polynomial discriminant.

Classification: `EXACT_FINITE_CRITICAL_GEOMETRY`.

---

## 4. Primitive factorization and resultant contribution

Let

\[
Q_M=\prod_{\substack{d\mid M\\d>1}}\Psi_d
\]

be the monic primitive denominator factorization.

For distinct primitive factors, the native resultant theorem gives

\[
\boxed{
|\operatorname{Res}(\Psi_d,\Psi_e)|
=
\begin{cases}
 p^{\varphi(d)},& e/d=p^a,\\
 p^{\varphi(e)},& d/e=p^a,\\
 1,&\text{otherwise}.
\end{cases}
}
\tag{SD-6}
\]

The discriminant of a product is

\[
\operatorname{Disc}\!\left(\prod f_i\right)
=
\left(\prod\operatorname{Disc}(f_i)\right)
\left(\prod_{i<j}\operatorname{Res}(f_i,f_j)^2\right).
\tag{SD-7}
\]

Thus (SD-5) and (SD-6) determine every primitive discriminant recursively.

---

## 5. Primitive spectral mass

Define

\[
P_d:=|\Psi_d(0)|.
\]

The primitive mass law is

\[
\boxed{
P_d=
\begin{cases}
 p,&d=p^a\text{ is a prime power},\\
 1,&d\text{ has at least two distinct prime divisors}.
\end{cases}
}
\tag{SD-8}
\]

---

## 6. Closed primitive discriminant formula

For every `d>2`, let

\[
\Delta_d:=\operatorname{Disc}(\Psi_d)>0.
\]

Then the exact closed formula is

\[
\boxed{
\Delta_d
=2^{\varphi(d)}
\frac{d^{\varphi(d)}}
{P_d\displaystyle\prod_{p\mid d}
 p^{\varphi(d)/(p-1)}}.
}
\tag{SD-9}
\]

This is obtained natively from (SD-5)-(SD-8), without using the classical cyclotomic discriminant theorem.

### Arithmetic verification of the divisor recursion

Fix a prime `p` and write

\[
d=p^a m,
\qquad p\nmid m.
\]

The `p`-valuation contributed by the candidate primitive discriminants over all divisors of `d` is built from three terms.

First,

\[
\sum_{i=1}^{a}\sum_{c\mid m}
 i\varphi(p^i)\varphi(c)
=
 m\left(
 a p^a-\frac{p^a-1}{p-1}
\right).
\]

Second, the denominator

\[
\prod_{p\mid e}p^{\varphi(e)/(p-1)}
\]

subtracts

\[
m\frac{p^a-1}{p-1}.
\]

Third, the primitive-mass factors `P_(p^i)=p` subtract exactly `a`.

The squared resultant contributions for all divisor pairs whose ratio is a positive power of `p` add

\[
2\left(
 m\frac{p^a-1}{p-1}-a
\right).
\]

The total is

\[
ma p^a-3a
=a(d-3),
\]

which is exactly the `p`-valuation of `d^(d-3)` in the full discriminant (SD-5).  The universal `2^(d-1)` part is supplied by

\[
\sum_{e\mid d,e>1}\varphi(e)=d-1.
\]

Thus the primitive formula reconstructs the full finite discriminant exactly.

---

## 7. Examples

The formula gives

```text
Disc Psi_5  = 2^4 * 5^2
Disc Psi_8  = 2^11
Disc Psi_9  = 2^6 * 3^8
Disc Psi_12 = 2^8 * 3^2
Disc Psi_15 = 2^8 * 3^4 * 5^6
Disc Psi_20 = 2^16 * 5^6
```

matching exact symbolic computation.

---

## 8. Projective primitive discriminant

For `d>2`, let

\[
\Psi_d(u)=(-1)^{h}\Omega_d(u(4-u)),
\qquad h=\varphi(d)/2.
\]

The two-sheet discriminant lift gives

\[
\operatorname{Disc}(\Psi_d)
=4^h\Omega_d(4)\operatorname{Disc}(\Omega_d)^2.
\]

Therefore

\[
\boxed{
\operatorname{Disc}(\Omega_d)^2
=
\frac{d^{\varphi(d)}}
{P_d\,|\Omega_d(4)|
 \displaystyle\prod_{p\mid d}p^{\varphi(d)/(p-1)}}.
}
\tag{SD-10}
\]

The midpoint mass is

\[
|\Omega_d(4)|=
\begin{cases}
1,&d\text{ odd},\\
P_{d/2},&d\text{ even and }d>2.
\end{cases}
\]

So the projective discriminant is also determined entirely by finite spectral arithmetic.

---

## 9. Structural consequence

The discriminant arithmetic now closes internally:

```text
finite critical map R_M
  -> normalized Jacobian Q_M
  -> full discriminant 2^(M-1) M^(M-3)
  -> primitive divisor factorization
  -> prime-power resultant law
  -> primitive mass P_d
  -> exact primitive discriminant formula
  -> projective degree-halved discriminant formula
```

Freeze:

`FULL_SPECTRAL_DISCRIMINANT = CRITICAL_JACOBIAN_PRODUCT`.

`PRIMITIVE_SPECTRAL_DISCRIMINANT = NATIVE_DIVISOR_RESULTANT_ARITHMETIC`.

The later equality of the arithmetic factor in (SD-9) with a classical cyclotomic discriminant expression is a compatibility theorem, not a proof input.
