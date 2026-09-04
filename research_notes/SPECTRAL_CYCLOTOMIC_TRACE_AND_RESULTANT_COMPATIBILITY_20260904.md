# Classical trace transform and resultant law for spectral cyclotomic factors

Status: `FREE_RESEARCH / CLASSICAL COMPATIBILITY THEOREM + EXACT SYMBOLIC CHECKS / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Native precursor: `DIRICHLET_SPECTRAL_CYCLOTOMIC_DIVISIBILITY_LATTICE_20260904.md`.

Boundary: this note is explicitly a downstream classical compatibility layer. It does not supply the native finite Dirichlet carrier or its internal phase quantization.

## 1. Reciprocal cyclotomic trace polynomial

For `N>2`, the cyclotomic polynomial `Phi_N(z)` is reciprocal of even degree `phi(N)`. Therefore there is a unique monic polynomial `C_N^tr(x)` of degree `phi(N)/2` such that

\[
\boxed{
\Phi_N(z)
=z^{\varphi(N)/2}
\,C_N^{\rm tr}(z+z^{-1}).
}
\tag{CTR-1}
\]

Call `C_N^tr` the real trace transform of the cyclotomic polynomial.

## 2. Spectral variable

Under classical compatibility, let

\[
z=e^{i\theta},
\qquad
x=z+z^{-1}=2\cos\theta,
\]

and

\[
\boxed{u=2-x=2-z-z^{-1}.}
\tag{CTR-2}
\]

The finite Dirichlet root indexed by `r/d` is exactly the image of

\[
z=e^{i\pi r/d}
\]

under (CTR-2).

The native spectral theory reached the same roots internally as `2-2C(r tau/d)` before this classical naming.

## 3. Even denominator

Let `d` be even. Every primitive residue `r mod d` is odd, hence

\[
z=e^{i\pi r/d}
\]

is a primitive `2d`-th root of unity.

Modulo the inversion pair `z<->z^-1`, the primitive `2d` roots map bijectively to the roots of the spectral primitive polynomial `Psi_d`.

Therefore

\[
\boxed{
\Psi_d(u)
=(-1)^{\varphi(d)}
C_{2d}^{\rm tr}(2-u).
}
\tag{CTR-3}
\]

For `d>2`, `phi(d)` is even, so the sign is positive. For `d=2`, the sign gives `Psi_2(u)=u-2` correctly.

## 4. Odd denominator

Let `d>1` be odd. Primitive residues split by parity:

- even `r`: `z` is a primitive `d`-th root;
- odd `r`: `z` is a primitive `2d`-th root.

Each parity class contributes one inversion-reduced trace factor. Therefore

\[
\boxed{
\Psi_d(u)
=
C_d^{\rm tr}(2-u)
\,C_{2d}^{\rm tr}(2-u).
}
\tag{CTR-4}
\]

The total degree is

\[
\frac{\varphi(d)}2+rac{\varphi(2d)}2
=\varphi(d),
\]

as required.

Examples:

\[
\Psi_3(u)=(u-1)(u-3),
\]

coming from the trace factors of `Phi_6` and `Phi_3` respectively.

## 5. Primitive mass from cyclotomic evaluation

Set `u=0`, so `z=1` and `x=2`.

For even `d`, (CTR-3) gives the primitive root mass from `Phi_(2d)(1)`; for odd `d`, (CTR-4) gives the product `Phi_d(1) Phi_(2d)(1)`.

The standard cyclotomic value law therefore reproduces

\[
\prod\operatorname{Roots}(\Psi_d)
=\begin{cases}
p,&d=p^a,\\1,&\omega(d)\ge2,\end{cases}
\]

exactly matching the independently derived spectral Möbius theorem.

Thus the agreement `P_d=Phi_d(1)` is the constant-term shadow of the full trace-transform compatibility.

## 6. Resultant law

Let `2<=m<n`. Exact symbolic computation of the native spectral primitive polynomials gives the pattern

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
\begin{cases}
p^{\varphi(m)},& n/m=p^a\text{ for a prime }p,\\[1mm]
1,&\text{otherwise}.
\end{cases}
}
\tag{CTR-5}
\]

This is exactly the prime-power dichotomy of the classical cyclotomic resultant law.

## 7. Why the exponent is phi(m)

The trace map identifies each spectral root with an inversion pair of roots of unity.  Consequently, the square of the spectral resultant is the appropriate product of classical cyclotomic resultants before inversion pairing.

### Both denominators even

`Psi_m` and `Psi_n` come from `Phi_(2m)` and `Phi_(2n)`. If `n/m=p^a`, the cyclotomic resultant has magnitude

\[
p^{\varphi(2m)}=p^{2\varphi(m)}.
\]

Taking one representative from each inverse pair gives the spectral magnitude

\[
p^{\varphi(m)}.
\]

### Both denominators odd

Each spectral factor corresponds to the product of the `d` and `2d` cyclotomic trace sectors. For `n/m=p^a` with odd `p`, the two nontrivial classical resultants are

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|
=p^{\varphi(m)},
\]

and

\[
|\operatorname{Res}(\Phi_{2m},\Phi_{2n})|
=p^{\varphi(m)}.
\]

Their product is `p^(2 phi(m))`; inversion pairing again takes the square root.

### Odd m and even n

The only prime-power ratio changing parity is `p=2`. If `n/m=2^a`, the relevant classical factors `Phi_m`, `Phi_(2m)` against `Phi_(2n)` each contribute `2^(phi(m))` before inversion pairing, again yielding spectral magnitude `2^(phi(m))`.

If `n/m` is not a prime power, all corresponding cyclotomic resultants have unit magnitude, so the spectral resultant is also a unit.

This proves (CTR-5) in the classical compatibility layer.

## 8. Exact symbolic checks

Direct exact polynomial construction from the finite Dirichlet family gives, among many checks:

```text
|Res(Psi_2,Psi_4)|   = 2
|Res(Psi_2,Psi_6)|   = 3
|Res(Psi_3,Psi_6)|   = 4   = 2^phi(3)
|Res(Psi_3,Psi_9)|   = 9   = 3^phi(3)
|Res(Psi_3,Psi_15)|  = 25  = 5^phi(3)
|Res(Psi_5,Psi_10)|  = 16  = 2^phi(5)
|Res(Psi_5,Psi_15)|  = 81  = 3^phi(5)
|Res(Psi_7,Psi_14)|  = 64  = 2^phi(7)
|Res(Psi_8,Psi_24)|  = 81  = 3^phi(8)
```

Pairs whose quotient is not a prime power give resultant magnitude one in the tested range.

## 9. Research consequence

The spectral primitive factors reproduce three levels of cyclotomic arithmetic:

1. divisor factorization and gcd lattice — proved natively from finite spectra;
2. prime-power constant-term law — proved natively by spectral Möbius inversion;
3. prime-power resultant law — proved here through the later classical trace compatibility and verified by exact finite symbolic computation.

Freeze the typing boundary:

`SPECTRAL_CYCLOTOMIC_DIVISIBILITY = NATIVE_FINITE`.

`SPECTRAL_CYCLOTOMIC_RESULTANT_COMPATIBILITY = CLASSICAL_TRACE_READOUT`.

Do not use the classical root-of-unity representation as input to the native finite spectral construction.
