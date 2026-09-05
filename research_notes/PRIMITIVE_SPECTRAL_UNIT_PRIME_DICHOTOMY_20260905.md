# Primitive spectral unit/prime dichotomy in the integral quotient algebra

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive pullback semigroup;
- native primitive resultant law;
- integer phase polynomials `R_p`.

## 1. Primitive spectral order

For `m>=2`, define the free integral order

\[
\boxed{
A_m:=\mathbb Z[u]/(\Psi_m(u)).
}
\tag{UPD-1}

It is a free abelian group of rank

\[
\operatorname{rank}_{\mathbb Z}A_m=\deg\Psi_m=\varphi(m).
\]

Let `ubar` denote the class of `u`.

For any polynomial `f`, multiplication by `f(ubar)` is an integral endomorphism of this lattice, and its determinant is, up to sign,

\[
\operatorname{Res}(\Psi_m,f).
\]

## 2. Frobenius congruence for the phase polynomial

For a prime `p`, the integer phase-multiplication polynomial satisfies

\[
\boxed{R_p(u)\equiv u^p\pmod p.}
\tag{UPD-2}

This follows from the Dickson/Chebyshev recurrence or directly from the prime-local phase polynomial coefficients.  Composition gives

\[
R_{p^a}(u)\equiv u^{p^a}\pmod p.
\]

## 3. Primitive-factor congruence when p is new

Assume `p\nmid m`.  The prime pullback law is

\[
\operatorname{Monic}(\Psi_m(R_p))=\Psi_m\Psi_{mp}.
\]

Modulo `p`, Frobenius gives

\[
\Psi_m(R_p(u))
\equiv\Psi_m(u^p)
\equiv\Psi_m(u)^p.
\]

Cancel the nonzero polynomial `Psi_m` in `F_p[u]`:

\[
\boxed{
\Psi_{mp}(u)
\equiv\Psi_m(u)^{p-1}\pmod p.
}
\tag{UPD-3}

After the first step, `p` divides the denominator, so repeated pullback yields by induction

\[
\boxed{
\Psi_{mp^a}(u)
\equiv
\Psi_m(u)^{p^{a-1}(p-1)}\pmod p,
\qquad a\ge1,
}
\tag{UPD-4}

up to the harmless monic sign in the `p=2` convention, which is invisible modulo two.

## 4. Primitive-factor congruence when p is already present

If `p|m`, the pullback law is

\[
\operatorname{Monic}(\Psi_m(R_p))=\Psi_{mp}.
\]

Therefore modulo `p`,

\[
\Psi_{mp}(u)
\equiv \pm\Psi_m(u)^p.
\]

Iterating,

\[
\boxed{
\Psi_{mp^a}(u)
\equiv \pm\Psi_m(u)^{p^a}\pmod p.
}
\tag{UPD-5}

Again only divisibility by `Psi_m` modulo `p` matters for the quotient-algebra conclusion.

## 5. Prime divisibility inside A_m

Both (UPD-4) and (UPD-5) imply

\[
\Psi_{mp^a}(u)=\Psi_m(u)H(u)+pG(u)
\]

for integral polynomials `G,H`.  Passing to `A_m`,

\[
\boxed{
\Psi_{mp^a}(\bar u)=p\varepsilon
}
\tag{UPD-6}

for some `epsilon in A_m`.

## 6. Native resultant forces epsilon to be a unit

The prime-power resultant law gives

\[
\left|
\operatorname{Res}(\Psi_m,\Psi_{mp^a})
\right|
=p^{\varphi(m)}.
\]

This is the determinant of multiplication by `Psi_(mp^a)(ubar)`.  Using (UPD-6),

\[
|\det(p\,m_\varepsilon)|
=p^{\varphi(m)}|\det(m_\varepsilon)|.
\]

Therefore

\[
|\det(m_\varepsilon)|=1.
\]

An integral lattice endomorphism with determinant `+/-1` is unimodular.  Its inverse sends `1` to an integral element `eta` with

\[
\varepsilon\eta=1.
\]

Hence

\[
\boxed{\varepsilon\in A_m^\times.}
\tag{UPD-7}

Thus

\[
\boxed{
\Psi_{mp^a}(\bar u)\sim p
\quad\text{in }A_m,
}
\tag{UPD-8}

where `~` means association by an integral unit.

## 7. Non-prime-power ratios give units directly

Let `n>m` and suppose `n/m` is not an integer prime power.  The native resultant theorem gives

\[
|\operatorname{Res}(\Psi_m,\Psi_n)|=1.
\]

Therefore multiplication by `Psi_n(ubar)` is unimodular, hence

\[
\boxed{
\Psi_n(\bar u)\in A_m^\times.
}
\tag{UPD-9}

Combining with (UPD-8):

\[
\boxed{
\Psi_n(\bar u)
\sim
\begin{cases}
p,&n/m=p^a,\ a\ge1,\\1,&\text{otherwise},
\end{cases}
\qquad n>m.
}
\tag{UPD-10}

This is strictly stronger than the determinant/resultant magnitude law.

## 8. Exact quotient-lattice structure

If `n/m` is not a prime power, (UPD-9) gives

\[
A_m/\Psi_n(\bar u)A_m=0.
\]

If `n=mp^a`, multiplication by the unit `epsilon` is an automorphism and

\[
\Psi_n(\bar u)A_m=pA_m.
\]

Therefore

\[
\boxed{
A_m/\Psi_{mp^a}(\bar u)A_m
\cong A_m/pA_m
\cong(\mathbb Z/p\mathbb Z)^{\varphi(m)}.
}
\tag{UPD-11}

So the Smith normal form of multiplication by `Psi_(mp^a)(ubar)` has every invariant factor equal to `p`.

The depth `a` does not change this quotient module.

## 9. Why resultant mass is depth-blind

The quotient-lattice theorem gives the structural reason for

\[
|\operatorname{Res}(\Psi_m,\Psi_{mp^a})|
=p^{\varphi(m)}
\]

being independent of `a`: every prime-power jump, regardless of depth, creates exactly one flat layer of `p`-torsion in each of the `phi(m)` integral primitive spectral coordinates.

Thus

\[
\boxed{
\text{RESULTANT PRIME MASS}
=\text{ONE }p\text{-TORSION LAYER},
}
\]

while the exponent `a` remains separate scale-depth provenance.

## 10. Spectral norm formulation

The quotient algebra norm satisfies

\[
N_{A_m/\mathbb Z}(\Psi_n(\bar u))
=\pm\operatorname{Res}(\Psi_m,\Psi_n).
\]

Therefore (UPD-10) can be read as a finite algebraic norm law:

```text
prime-power denominator extension:
    Psi_n(ubar) = p * unit

all other distinct extensions:
    Psi_n(ubar) = unit
```

The low-dimensional rational probes are special cases:

- `m=2`, `A_2=Z`, `ubar=2`, giving the midpoint mass law;
- `m=3`, the two orientation-linear factors correspond to the rational probes `u=1` and `u=3`.

Freeze:

`PRIME_POWER_RESULTANT -> ELEMENT_IS_p_TIMES_UNIT`.

`NON_PRIME_POWER_RESULTANT_UNIT -> ELEMENT_IS_UNIT`.

`PRIME_POWER_QUOTIENT_LATTICE = (Z/pZ)^PHI(m)`.

`P_ADIC_JUMP_DEPTH != TORSION_LAYER_COUNT`.
