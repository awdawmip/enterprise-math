# Arithmetic invariants of the primitive finite spectral algebra

Status: `FREE_RESEARCH / FINITE-ADELEBRA SYNTHESIS THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive spectral factor `Psi_d`;
- trace, norm, resultant and discriminant laws already derived.

## 1. Primitive spectral algebra and integral order

For `d>1`, define the finite rational algebra

\[
\boxed{
\mathscr A_d:=\mathbb Q[u]/(\Psi_d(u)).
}
\tag{ASA-1}

and its monogenic integral order

\[
\boxed{
\mathscr O_d:=\mathbb Z[u]/(\Psi_d(u)).
}
\tag{ASA-2}

The polynomial `Psi_d` has simple real roots, so `mathscr A_d` is finite etale over `Q`.  It need not be a field: for odd `d>1`, the reflection decomposition

\[
\Psi_d=\Psi_d^E\Psi_d^O
\]

splits the algebra into two orientation components.

Let `ubar` denote the class of `u`.

## 2. Rank is Euler totient

The primitive degree theorem gives

\[
\boxed{
\dim_{\mathbb Q}\mathscr A_d
=\operatorname{rank}_{\mathbb Z}\mathscr O_d
=\deg\Psi_d
=\varphi(d).
}
\tag{ASA-3}

Thus Euler totient is the primitive spectral algebra rank.

## 3. Endpoint norm is primitive prime-power mass

For a monic polynomial `f` of degree `r`, the norm of the root class is `(-1)^r f(0)`.  Therefore

\[
\boxed{
|N_{\mathscr A_d/\mathbb Q}(\bar u)|
=|\Psi_d(0)|
=P_d,
}
\tag{ASA-4}

where

\[
P_d=\begin{cases}p,&d=p^a,\\1,&\omega(d)\ge2.
\end{cases}
\]

The later logarithmic readout is

\[
\boxed{
\log|N(\bar u)|=\Lambda(d).
}
\tag{ASA-5}

Thus von Mangoldt is the log norm of the primitive endpoint spectral coordinate, not an independent carrier.

## 4. Decimation traces are Ramanujan traces

For the integer phase-multiplication polynomial `R_(2q)`, the primitive trace theorem is

\[
\boxed{
\operatorname{Tr}_{\mathscr A_d/\mathbb Q}
\left(R_{2q}(\bar u)\right)
=2(\varphi(d)-c_d(q)).
}
\tag{ASA-6}

Equivalently,

\[
\boxed{
 c_d(q)
=\dim\mathscr A_d
-\frac12\operatorname{Tr}(R_{2q}(\bar u)).
}
\tag{ASA-7}

Hence Ramanujan sums are phase-polynomial trace defects in the primitive finite spectral algebra.

For odd denominators, the E/O factors refine this trace into orientation-symmetric and orientation-antisymmetric components.

## 5. Reciprocal traces are Jordan combinations

No primitive root is zero, so `ubar` is invertible in the rational etale algebra.  For integer `s>=1`,

\[
\boxed{
\operatorname{Tr}_{\mathscr A_d/\mathbb Q}(\bar u^{-s})
=Z_s^{\rm prim}(d).
}
\tag{ASA-8

The primitive moment theorem gives

\[
\boxed{
\operatorname{Tr}(\bar u^{-s})
=\sum_{r=1}^{s}a_{s,r}J_{2r}(d).
}
\tag{ASA-9

Thus the even Jordan totients are the common pullback eigencoordinates in which reciprocal traces diagonalize.

The endpoint resolvent is

\[
-\frac{\Psi_d'(z)}{\Psi_d(z)}
=\operatorname{Tr}\left((\bar u-z)^{-1}\right)
\]

up to the conventional sign/variable orientation, and its Taylor coefficients are the reciprocal moments.

## 6. Resultants are relative norms

For another monic primitive factor `Psi_n`,

\[
\boxed{
N_{\mathscr A_m/\mathbb Q}
\left(\Psi_n(\bar u)\right)
=\pm\operatorname{Res}(\Psi_m,\Psi_n).
}
\tag{ASA-10

Hence the native prime-power resultant theorem is a relative norm law:

\[
\boxed{
\left|N(\Psi_n(\bar u))\right|
=\begin{cases}
p^{\varphi(m)},&n/m=p^a,\\1,&\text{otherwise}.
\end{cases}
}
\tag{ASA-11

The stronger integral-order theorem upgrades this norm statement to

\[
\Psi_{mp^a}(\bar u)=p\cdot\text{unit}
\]

inside `mathscr O_m`.

## 7. Discriminant is the trace-pairing determinant

The power basis

\[
1,\bar u,\ldots,\bar u^{\varphi(d)-1}
\]

has trace-pairing discriminant

\[
\boxed{
\det\left[
\operatorname{Tr}(\bar u^{i+j})
\right]_{0\le i,j<\varphi(d)}
=\operatorname{Disc}\Psi_d.
}
\tag{ASA-12

The native formula is

\[
\boxed{
|\operatorname{Disc}\Psi_d|
=\frac{
2^{\varphi(d)}d^{\varphi(d)}
}{
P_d\prod_{p\mid d}p^{\varphi(d)/(p-1)}
}.
}
\tag{ASA-13

So primitive self-separation is the determinant of the standard trace form on the same finite algebra whose rank, norm and traces already carry the other arithmetic functions.

## 8. Standard-invariant dictionary

The previous arithmetic dictionary can now be rewritten without introducing separate ad hoc observers:

\[
\boxed{
\begin{array}{c|c}
\text{arithmetic readout}&\text{invariant of }\mathscr A_d\\
\hline
\varphi(d)&\text{rank/dimension}\\
P_d&|N(\bar u)|\\
\Lambda(d)&\log|N(\bar u)|\\
c_d(q)&\dim-\frac12\operatorname{Tr}(R_{2q}(\bar u))\\
Z_s^{\rm prim}(d)&\operatorname{Tr}(\bar u^{-s})\\
J_{2r}(d)&\text{pullback eigencoordinates of reciprocal traces}\\
\operatorname{Res}(\Psi_d,\Psi_n)&\text{relative norm of }\Psi_n(\bar u)\\
\operatorname{Disc}\Psi_d&\text{trace-pairing discriminant}
\end{array}}
\tag{ASA-14

The observables remain distinct standard invariants; the point is that they belong to one finite algebraic carrier.

## 9. Orientation-resolved algebra

For odd `d>1`,

\[
\mathscr A_d
\cong
\mathscr A_d^E\times\mathscr A_d^O
\]

with

\[
\mathscr A_d^{E/O}=\mathbb Q[u]/(\Psi_d^{E/O}).
\]

The complement involution exchanges the two components.  Endpoint norms, odd-phase traces and same-orientation resultants refine componentwise, while full positive traces/norms may recoalesce them.

Thus the finite etale algebra naturally preserves the same orientation typing discovered at the spectral-factor level.

## 10. Pullback morphisms

Whenever `A|A(R_n)`, substitution

\[
\bar u\mapsto R_n(\bar u)
\]

defines an endomorphism or a map between the relevant finite spectral orders.  The primitive pullback semigroup therefore acts not only on denominator labels but on these finite algebras themselves.

Rank/Jordan eigencoordinates describe the induced action on traces; endpoint norm conservation and unit/prime quotient laws describe the induced action on multiplicative arithmetic invariants.

## 11. Interpretation

The #1159 research has moved from

```text
finite spectral formulas
```

to

```text
one finite primitive spectral algebra
    rank
    norm
    trace
    reciprocal trace
    relative norm
    discriminant
    phase-pullback endomorphisms
```

with familiar arithmetic functions appearing as different standard invariants of that one carrier.

This is stronger and cleaner than identifying those arithmetic functions with one another.

Freeze:

`PRIMITIVE_SPECTRAL_FACTOR -> FINITE ETALE ARITHMETIC ALGEBRA`.

`PHI / LAMBDA / RAMANUJAN / JORDAN / RESULTANT / DISCRIMINANT = DISTINCT STANDARD INVARIANTS OF ONE CARRIER`.
