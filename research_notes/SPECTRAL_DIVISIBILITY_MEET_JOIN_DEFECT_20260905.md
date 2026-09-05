# Spectral divisibility embedding and the mixed join-defect polynomial

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- monic spectral length polynomials `Q_M=(-1)^(M-1) D_(M-1)`;
- primitive divisor factorization `Q_M=prod_(d|M,d>1) Psi_d`;
- primitive endpoint mass law and reciprocal-moment polynomial laws.

## 1. Divisibility order embeds into spectral-polynomial divisibility

Because

\[
Q_M(u)=\prod_{\substack{d\mid M\\d>1}}\Psi_d(u)
\]

with pairwise disjoint primitive root sets, for positive integers `m,n>=2`,

\[
\boxed{m\mid n\iff Q_m\mid Q_n.}
\tag{SJD-1}
\]

Moreover the monic polynomial gcd is

\[
\boxed{\gcd_{\rm monic}(Q_m,Q_n)=Q_{(m,n)}.}
\tag{SJD-2}
\]

Thus `M -> Q_M` is an injective order embedding of the integer divisibility poset into monic polynomial divisibility and preserves the meet operation exactly.

Evaluation at zero recovers the integer meet:

\[
\boxed{(m,n)=|Q_{(m,n)}(0)|=|\gcd(Q_m,Q_n)(0)|.}
\tag{SJD-3}
\]

Similarly, if `Lpoly` is the monic polynomial lcm of `Q_m,Q_n`, then

\[
|Lpoly(0)|=[m,n].
\]

## 2. The map does not preserve joins

Let

\[
g=(m,n),\qquad \ell=[m,n].
\]

Define the monic join-defect polynomial

\[
\boxed{
\mathcal J_{m,n}(u)
:=\frac{Q_\ell(u)Q_g(u)}{Q_m(u)Q_n(u)}.
}
\tag{SJD-4}
\]

Primitive-factor exponents reduce to indicator arithmetic:

\[
\boxed{
\mathcal J_{m,n}
=
\prod_{\substack{d\mid\ell\\d\nmid m\\d\nmid n}}\Psi_d.
}
\tag{SJD-5}
\]

Thus the join defect contains exactly the primitive denominators created by the lcm which were present in neither input spectrum.

The ordinary polynomial lcm is

\[
\operatorname{lcm}_{\rm monic}(Q_m,Q_n)=\frac{Q_mQ_n}{Q_g},
\]

so

\[
Q_\ell
=\operatorname{lcm}_{\rm monic}(Q_m,Q_n)\,\mathcal J_{m,n}.
\]

Hence `M -> Q_M` is a meet-semilattice embedding but not, in general, a join-semilattice homomorphism.

## 3. Exact mixed-mode count

Write

\[
m=ga,\qquad n=gb,\qquad(a,b)=1.
\]

Then `ell=gab`, and degree arithmetic gives

\[
\boxed{
\deg \mathcal J_{m,n}
=\ell+g-m-n
=g(a-1)(b-1).
}
\tag{SJD-6}
\]

Because coprime `a,b` make `(a-1)(b-1)` even, this degree is even.

Consequently

\[
\boxed{
\mathcal J_{m,n}=1
\iff
m\mid n\text{ or }n\mid m.
}
\tag{SJD-7}
\]

For incomparable integers, `J_(m,n)` contains a strictly positive number of genuine mixed finite modes.

## 4. Endpoint mass is blind to the mixed modes

Every primitive denominator `d` occurring in (SJD-5) has at least two distinct prime factors.  Indeed, if `d=p^r` were a prime power dividing `ell`, then its full `p`-power would already divide whichever of `m,n` supplies the maximal `p` exponent, contradicting `d` dividing neither input.

Therefore the primitive endpoint-mass law gives

\[
\Psi_d(0)=1
\]

for every mixed factor.  Hence

\[
\boxed{\mathcal J_{m,n}(0)=1.}
\tag{SJD-8}
\]

Complement symmetry of the finite Dirichlet spectrum gives the same value at the other endpoint:

\[
\boxed{\mathcal J_{m,n}(4)=1.}
\tag{SJD-9}
\]

Thus positive endpoint mass completely recoalesces the mixed sector even though its spectral support is nontrivial.

This is an exact finite example of the global type principle

`POSITIVE_MASS_EQUALITY != SUPPORT_OR_INTERNAL_STRUCTURE_EQUALITY`.

## 5. First reciprocal mixed moment

Let

\[
Z_1(M)=\sum_{k=1}^{M-1}u_{k,M}^{-1}=\frac{M^2-1}{6}.
\]

Additivity of logarithmic derivatives under the quotient (SJD-4) gives

\[
\sum_{\mathcal J_{m,n}(\alpha)=0}\alpha^{-1}
=Z_1(\ell)+Z_1(g)-Z_1(m)-Z_1(n).
\]

Substituting `m=ga,n=gb,ell=gab` yields

\[
\boxed{
\sum_{\mathcal J_{m,n}(\alpha)=0}\frac1\alpha
=
\frac{g^2(a^2-1)(b^2-1)}6.
}
\tag{SJD-10}
\]

This is strictly positive exactly in the incomparable case.

Therefore the mixed sector can have endpoint mass one while carrying a quantitatively nonzero reciprocal spectral moment.

## 6. All reciprocal mixed moments

For fixed `s>=1`, write the already derived full moment polynomial as

\[
Z_s(M)=P_s(M^2)
=a_{s,0}+\sum_{r=1}^{s}a_{s,r}M^{2r}.
\]

Then the `s`-th reciprocal moment of the join defect is

\[
\boxed{
Z_s^{\rm join}(m,n)
=P_s(\ell^2)+P_s(g^2)-P_s(m^2)-P_s(n^2)
}
\tag{SJD-11}
\]

and therefore

\[
\boxed{
Z_s^{\rm join}(m,n)
=
\sum_{r=1}^{s}
 a_{s,r}
 g^{2r}(a^{2r}-1)(b^{2r}-1).
}
\tag{SJD-12}
\]

For example

\[
Z_2^{\rm join}(m,n)
=
\frac{
2g^4(a^4-1)(b^4-1)
+5g^2(a^2-1)(b^2-1)
}{180}.
\]

The positivity of the left side is intrinsic because it is a sum over positive finite roots; no endpoint mass is needed to witness it.

## 7. Interpretation

The exact structure is

```text
integer divisibility meet
    -> polynomial gcd exactly
integer lcm join
    -> polynomial lcm
       times a new mixed spectral factor J_(m,n)
J_(m,n)(0)=J_(m,n)(4)=1
but
J_(m,n) has positive degree and positive reciprocal moments when m,n incomparable
```

So the join operation creates internal finite spectral structure that a single positive endpoint-mass observer cannot see.

Freeze:

`INTEGER_DIVISIBILITY -> SPECTRAL_POLYNOMIAL_MEET_EMBEDDING`.

`JOIN_FAILURE -> MIXED_PRIMITIVE_SPECTRUM`.

`MIXED_ENDPOINT_MASS = 1 != MIXED_STRUCTURE_TRIVIAL`.
