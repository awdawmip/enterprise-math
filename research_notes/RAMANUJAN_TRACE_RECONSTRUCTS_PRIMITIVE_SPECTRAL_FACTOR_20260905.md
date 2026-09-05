# Ramanujan trace coordinates reconstruct the primitive spectral factor

Status: `FREE_RESEARCH / EXACT FINITE-RECONSTRUCTION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive spectral factor `Psi_d`;
- complement involution `u -> 4-u`;
- primitive trace identity `T_d(q)=2(phi(d)-c_d(q))`;
- integer Dickson/Chebyshev phase-multiplication polynomials.

## 1. Centered primitive factor

For `d>2`, Euler's totient `phi(d)` is even.  Write

\[
h=\frac{\varphi(d)}2.
\]

Complement symmetry permutes the primitive roots and gives

\[
\Psi_d(4-u)=\Psi_d(u).
\]

Set `u=2-x`.  Then

\[
\widehat\Psi_d(x):=\Psi_d(2-x)
\]

is an even monic polynomial of degree `2h`.  Hence there is a unique monic

\[
B_d(y)\in\mathbb Z[y],\qquad \deg B_d=h,
\]

such that

\[
\boxed{
\Psi_d(2-x)=B_d(x^2).
}
\tag{RTR-1}
\]

The roots of `B_d` are the squared centered primitive mode coordinates.

## 2. Phase-multiplication polynomials

Let `C_n(X)` be the rescaled Chebyshev/Dickson recurrence

\[
C_0=2,\qquad C_1=X,\qquad C_{n+1}=XC_n-C_{n-1}.
\]

The finite phase-decimation polynomial is

\[
R_n(u)=2-C_n(2-u).
\]

For even index `2q`, `C_(2q)(x)` is an even monic polynomial of degree `2q`.  Therefore there is a unique monic degree-`q` polynomial `E_q(y)` with

\[
\boxed{C_{2q}(x)=E_q(x^2).}
\tag{RTR-2}
\]

Equivalently, by the composition law,

\[
E_q(y)=C_q(y-2).
\]

Examples:

\[
E_1(y)=y-2,
\]

\[
E_2(y)=y^2-4y+2,
\]

\[
E_3(y)=y^3-6y^2+9y-2.
\]

## 3. Ramanujan sums as algebra traces

The primitive decimation trace theorem says

\[
\sum_{\Psi_d(\alpha)=0}R_{2q}(\alpha)
=2(\varphi(d)-c_d(q)).
\]

Since `R_(2q)=2-C_(2q)(2-u)`, this is equivalent to

\[
\boxed{
\sum_{\Psi_d(\alpha)=0}
C_{2q}(2-\alpha)
=2c_d(q).
}
\tag{RTR-3}
\]

In finite-algebra language, if `ubar` is the class of `u` in the finite etale algebra `Q[u]/(Psi_d)`,

\[
\boxed{
\frac12\operatorname{Tr}
\left(C_{2q}(2-\bar u)\right)
=c_d(q).
}
\tag{RTR-4}
\]

Thus Ramanujan sums are exact algebra traces of integer phase-multiplication polynomials on the primitive finite spectral algebra.

## 4. Pass to squared centered roots

Let

\[
y_1,\ldots,y_h
\]

be the roots of `B_d`, and define ordinary power sums

\[
p_j:=\sum_{i=1}^{h}y_i^j.
\]

Each `y_i` corresponds to a complement pair `x,-x` of centered primitive roots.  Using (RTR-2) in (RTR-3) gives

\[
\boxed{
 c_d(q)=\sum_{i=1}^{h}E_q(y_i).
}
\tag{RTR-5}
\]

Write

\[
E_q(y)=y^q+\sum_{j=0}^{q-1}e_{q,j}y^j.
\]

Then

\[
\boxed{
 p_q
=c_d(q)-h e_{q,0}
-\sum_{j=1}^{q-1}e_{q,j}p_j.
}
\tag{RTR-6}
\]

Therefore `c_d(1),...,c_d(q)` recursively determine `p_1,...,p_q`.

## 5. Finite reconstruction theorem

Take `q=1,...,h`.  Formula (RTR-6) determines the first `h` power sums of the roots of `B_d`.  Newton identities then uniquely determine every coefficient of the monic degree-`h` polynomial `B_d`.

Consequently

\[
\boxed{
\left(
\varphi(d),
 c_d(1),\ldots,c_d(\varphi(d)/2)
\right)
\Longrightarrow
B_d
\Longrightarrow
\Psi_d.
}
\tag{RTR-7}
\]

Conversely, `Psi_d` determines all traces (RTR-4), hence all Ramanujan sums `c_d(q)`.  Thus at fixed `d` the primitive finite spectral polynomial and the finite initial Ramanujan trace coordinates contain mutually recoverable information.

## 6. Examples

### d=5

Here `phi(5)=4`, `h=2`, and

\[
c_5(1)=c_5(2)=-1.
\]

From `E_1(y)=y-2`,

\[
p_1=c_5(1)+2h=3.
\]

From `E_2(y)=y^2-4y+2`,

\[
p_2=c_5(2)+4p_1-2h=7.
\]

Newton gives

\[
B_5(y)=y^2-3y+1.
\]

Hence

\[
\boxed{
\Psi_5(u)=u^4-8u^3+21u^2-20u+5.
}
\]

### d=6

Here `phi(6)=2`, `h=1`, `c_6(1)=1`.  Therefore

\[
p_1=1+2=3,
\]

so

\[
B_6(y)=y-3,
\]

and

\[
\Psi_6(u)=u^2-4u+1.
\]

## 7. Interpretation

The direction discovered earlier was

```text
primitive spectral factor Psi_d
 -> phase-decimation traces
 -> Ramanujan sums c_d(q).
```

The present theorem supplies the converse finite reconstruction:

```text
finite Ramanujan trace coordinates
 -> centered squared-root power sums
 -> Newton reconstruction
 -> primitive spectral factor Psi_d.
```

Thus Ramanujan sums are not merely compatible external harmonic coefficients; they are finite trace coordinates sufficient to reconstruct the primitive rotation-spectrum algebra itself.

Freeze:

`RAMANUJAN_SUM = PRIMITIVE_PHASE_POLYNOMIAL_TRACE`.

`FINITE_INITIAL_RAMANUJAN_TRACES -> RECONSTRUCT_PSI_d`.

`PSI_d <-> FINITE_RAMANUJAN_TRACE_COORDINATES`.
