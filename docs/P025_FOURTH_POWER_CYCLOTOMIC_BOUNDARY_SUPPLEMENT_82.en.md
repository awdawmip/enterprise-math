# P025 Supplement 82 — Fourth-Power Counter-Pressure and the Cyclotomic-Depth Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 72, 79–81  
Hard block: `NONE`

## 1. The next pressure test is exponent four

Stage 79 proves a strong theorem for odd prime exponents: threshold-one activation forces repetition in the unique nonlinear cyclotomic factor.

It would be tempting to promote this to a statement about all exponents. Exponent four disproves that extension.

The failure is not merely an odd/even parity issue. The decisive object is the **cyclotomic factorization depth for the chosen sign**.

## 2. Equal fourth-power projective atoms

Let

\[
3\le q<p
\]

be distinct odd primes. With complements

\[
p^4,\ q^4,
\]

the exact equal-exponent projective denominator is

\[
4(p+q).
\]

Thus

\[
\boxed{
\rho_{4,+}
=\frac{m(p^4+q^4)}{4(p+q)},
\qquad
\rho_{4,-}
=\frac{m(p^4-q^4)}{4(p+q)}.
}
\]

Introduce centered coordinates

\[
A=\frac{p-q}{2},
\qquad
B=\frac{p+q}{2}.
\]

Then

\[
\gcd(A,B)=1,
\]

and `A,B` have opposite parity.

## 3. The two signs have different cyclotomic depth

The sum is

\[
\boxed{p^4+q^4=\Phi_8(p,q).}
\]

There is only one cyclotomic layer for this sign.

The difference is

\[
\boxed{
p^4-q^4
=\Phi_1(p,q)\Phi_2(p,q)\Phi_4(p,q)
=(p-q)(p+q)(p^2+q^2).
}
\]

So the difference branch has **three** layers: two linear layers and one top quadratic layer.

This is the first exact place where the Stage-79 top-factor forcing mechanism can fail.

## 4. P025-T169 — exact centered difference formula

Set

\[
Q=A^2+B^2.
\]

Then

\[
p^2+q^2=2Q
\]

and

\[
p^4-q^4
=8ABQ.
\]

Because `A,B` are coprime and have opposite parity,

\[
Q\text{ is odd},
\]

and

\[
\gcd(A,Q)=\gcd(B,Q)=1.
\]

Therefore

\[
\boxed{
m(p^4-q^4)=8m(A)m(B)m(Q).}
\]

Since

\[
4(p+q)=8B,
\]

we obtain the exact atom

\[
\boxed{
\rho_{4,-}
=
\frac{m(A)m(Q)}{\operatorname{rad}(B)}.
}
\]

The top homogeneous cyclotomic factor is

\[
\Phi_4(p,q)=p^2+q^2=2Q.
\]

Its multiplicity residual is exactly `m(Q)`.

Hence, if `Phi_4` is squarefree,

\[
\boxed{
\rho_{4,-}
=
\frac{m(A)}{\operatorname{rad}(B)},
}
\]

which is precisely the same centered carrier already seen in the prime-square difference shell.

So exponent four can inherit lower-layer pressure from the centered radius without any repeated top cyclotomic prime.

## 5. P025-C24 — top repetition is not necessary for fourth-power difference activation

Take

\[
(q,p)=(23,41).
\]

Then

\[
A=9,
\qquad
B=32,
\qquad
Q=9^2+32^2=1105=5\cdot13\cdot17.
\]

Thus

\[
\Phi_4(41,23)
=41^2+23^2
=2210
=2\cdot5\cdot13\cdot17
\]

is completely squarefree.

Nevertheless

\[
m(A)=3,
\qquad
m(Q)=1,
\qquad
\operatorname{rad}(B)=2,
\]

so

\[
\boxed{
\rho_{4,-}
=\frac32>1.
}
\]

Therefore the natural extension

\[
\text{activation}
\Longrightarrow
\text{repetition in the top nonlinear cyclotomic factor}
\]

is false for exponent four.

This is a hard negative boundary, not a missing proof.

## 6. P025-T170 — the fourth-power sum still has top forcing

The sum branch behaves differently. In centered coordinates,

\[
p^4+q^4
=2H,
\]

where

\[
\boxed{
H=B^4+6A^2B^2+A^4.
}
\]

Because `A,B` have opposite parity, `H` is odd. Hence

\[
m(p^4+q^4)=m(H)
\]

and

\[
\boxed{
\rho_{4,+}=\frac{m(H)}{8B}.
}
\]

If `H` is squarefree, then `m(H)=1`, so

\[
\rho_{4,+}<1.
\]

Thus

\[
\boxed{
\rho_{4,+}\ge1
\Longrightarrow
H\text{ is nonsquarefree}.
}
\]

Equivalently, fourth-power **sum** activation still forces repetition in the unique top factor `Phi_8`.

## 7. P025-T171 — repeated fourth-power sum primes are `1 mod 8`

Let an odd prime `r` repeat in `H`, equivalently

\[
r^2\mid p^4+q^4.
\]

Since `r` is coprime to `pq`, the ratio

\[
x=pq^{-1}\pmod r
\]

satisfies

\[
x^4\equiv-1\pmod r.
\]

Therefore `x` has exact order eight, so

\[
8\mid r-1.
\]

Hence

\[
\boxed{r\equiv1\pmod8.}
\]

The factor two occurs only once in `p^4+q^4` for odd `p,q`, so it never contributes residual.

An exact activated example is

\[
(q,p)=(839,1277),
\]

for which

\[
p^4+q^4
=2\cdot17401\cdot9521^2,
\]

and

\[
\boxed{
\rho_{4,+}=\frac{9521}{8464}>1.
}
\]

The repeated prime satisfies

\[
9521\equiv1\pmod8.
\]

## 8. The real boundary is cyclotomic factorization depth

The standard homogeneous factorizations are

\[
p^n-q^n
=\prod_{d\mid n}\Phi_d(p,q),
\]

and

\[
p^n+q^n
=\prod_{\substack{d\mid2n\\d\nmid n}}\Phi_d(p,q).
\]

For an odd prime exponent `ell`:

- difference indices are only `{1,ell}`;
- sum indices are only `{2,2ell}`.

So there is one linear layer plus one nonlinear layer, and Stage 79 proves the linear layer cannot activate by itself.

For exponent four:

- sum indices are only `{8}`;
- difference indices are `{1,2,4}`.

The sum therefore retains top forcing, while the difference gains enough lower layers to carry pressure without top repetition.

Hence the correct organizing principle is

\[
\boxed{
\text{sign-specific cyclotomic divisor depth},
}
\]

not parity alone.

## 9. Architectural consequence

Stage 72 showed that exponent-only precision saturates. Stage 79 then showed that for prime exponents one may switch to one top cyclotomic congruence coordinate.

Stage 82 proves that this is still too coarse for composite exponents. The next state object must be able to answer:

> Which cyclotomic layer, or which combination of layers, actually carries the projective multiplicity pressure?

That suggests a **cyclotomic divisor-lattice carrier state** rather than a single top-factor state.

For exponent four difference, the carrier may lie entirely in the lower `Phi_1/Phi_2` geometry even when `Phi_4` is squarefree.

## 10. Prior-art / novelty discipline

Cyclotomic factorizations, centered fourth-power identities, multiplicative orders, and the congruence `r=1 mod 8` for primitive eighth-order support are classical mathematics.

P025 claims none of those ingredients individually.

The project-side result is the exact projective counterexample to top-factor forcing, the sign-dependent contrast at the same exponent, and the resulting precision-routing boundary. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_fourth_power_cyclotomic_boundary.py`;
- `tests/test_abc_fourth_power_cyclotomic_boundary.py`.

The executable layer verifies:

- centered factorization and pairwise gcd structure;
- exact difference formula `rho_4,-=m(A)m(A^2+B^2)/rad(B)`;
- the explicit squarefree-top activated counterexample `(23,41)`;
- sum-side top forcing;
- repeated sum support of exact order eight.

## 12. Next frontier

No hard block exists. Continue with:

1. define the sign-specific cyclotomic index set for arbitrary exponent `n`;
2. build a divisor-lattice carrier state that records residual pressure by cyclotomic layer without pretending those layer values are always coprime;
3. formulate an exact criterion for when a chosen upper set of layers is forced to carry repetition;
4. test exponent nine (`Phi_1 Phi_3 Phi_9`) as the first odd composite counter-pressure;
5. only after the divisor-lattice semantics survives those tests, relay the abstraction to A2/P023.
