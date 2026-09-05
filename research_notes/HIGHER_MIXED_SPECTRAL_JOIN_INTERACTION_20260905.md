# Higher mixed spectral join interactions on the divisibility lattice

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- divisor embedding `n -> Q_n`;
- primitive factorization `Q_n=prod_(d|n,d>1) Psi_d`;
- primitive endpoint-mass and reciprocal-moment laws.

## 1. Multi-input spectral join defect

Let

\[
\mathbf n=(n_1,\ldots,n_r),\qquad r\ge2,
\]

and let

\[
L=\operatorname{lcm}(n_1,\ldots,n_r).
\]

Define the monic polynomial lcm of the input spectral polynomials and the higher join defect

\[
\boxed{
\mathcal J_{\mathbf n}(u)
:=
\frac{Q_L(u)}
{\operatorname{lcm}_{\rm monic}(Q_{n_1},\ldots,Q_{n_r})}.
}
\tag{HMJ-1}

Because primitive factors occur with exponent one, polynomial lcm corresponds exactly to union of divisor ideals.

## 2. Primitive mixed-factor support

The denominator `d` occurs in `Q_L` iff `d|L`, while it occurs in the polynomial lcm of the inputs iff `d|n_i` for at least one `i`.  Therefore

\[
\boxed{
\mathcal J_{\mathbf n}
=
\prod_{\substack{d\mid L\\d>1\\d\nmid n_i\ \forall i}}
\Psi_d.
}
\tag{HMJ-2}

Thus `J_n` contains precisely the primitive denominator modes which exist only after the input directions are jointly closed under lcm.

## 3. Inclusion-exclusion formula for the polynomial lcm

For each nonempty subset `S subseteq {1,...,r}`, put

\[
g_S:=\gcd(n_i:i\in S).
\]

Indicator inclusion-exclusion on primitive divisor support gives

\[
\boxed{
\operatorname{lcm}_{\rm monic}(Q_{n_1},\ldots,Q_{n_r})
=
\prod_{\varnothing\ne S\subseteq[r]}
Q_{g_S}^{(-1)^{|S|+1}}.
}
\tag{HMJ-3}

The expression is polynomial because each primitive factor has final exponent zero or one.

Consequently

\[
\boxed{
\mathcal J_{\mathbf n}
=
Q_L
\prod_{\varnothing\ne S\subseteq[r]}
Q_{g_S}^{(-1)^{|S|}}.
}
\tag{HMJ-4}

## 4. Exact higher mixed-mode count

Since `deg Q_m=m-1` and

\[
\sum_{\varnothing\ne S}(-1)^{|S|+1}=1,
\]

we obtain

\[
\boxed{
\deg\mathcal J_{\mathbf n}
=
L-
\sum_{\varnothing\ne S\subseteq[r]}
(-1)^{|S|+1}g_S.
}
\tag{HMJ-5}

For `r=2` this reduces to

\[
[m,n]+(m,n)-m-n.
\]

## 5. When is there no mixed interaction?

The top primitive denominator `L` itself occurs in `J_n` unless `L|n_i` for some input.  But every `n_i|L`, so this is equivalent to `n_i=L`.

Hence

\[
\boxed{
\mathcal J_{\mathbf n}=1
\iff
\exists i,\ n_i=L.
}
\tag{HMJ-6}

Thus higher mixed spectrum is absent exactly when one input already dominates all others in the divisibility order.

If no input equals `L`, then `Psi_L` itself is a nontrivial factor of the interaction polynomial.

## 6. Endpoint mass remains blind to all higher mixed interactions

Let `d` occur in (HMJ-2).  Such a `d` cannot be a prime power.  If `d=p^a`, then since `d|L`, some input `n_i` attains at least exponent `a` at prime `p`; therefore `d|n_i`, contradicting mixedness.

So every primitive mixed denominator contains at least two distinct primes.  The primitive endpoint-mass law gives

\[
|\Psi_d(0)|=1.
\]

Therefore

\[
\boxed{|\mathcal J_{\mathbf n}(0)|=1.}
\tag{HMJ-7}

Complement symmetry gives the other endpoint as well:

\[
\boxed{|\mathcal J_{\mathbf n}(4)|=1.}
\tag{HMJ-8}

Hence arbitrary-order mixed spectral interaction is invisible to the positive endpoint-mass observer.

## 7. Reciprocal moments see the interaction exactly

Let

\[
Z_s(M)=P_s(M^2)
\]

be the full reciprocal spectral moment polynomial.  Logarithmic-derivative additivity applied to (HMJ-4) gives

\[
\boxed{
Z_s^{\rm mix}(\mathbf n)
:=\sum_{\mathcal J_{\mathbf n}(\alpha)=0}\alpha^{-s}
=
P_s(L^2)
-
\sum_{\varnothing\ne S\subseteq[r]}
(-1)^{|S|+1}P_s(g_S^2).
}
\tag{HMJ-9}

The constant coefficient of `P_s` cancels by inclusion-exclusion.  Writing

\[
P_s(X)=a_{s,0}+\sum_{j=1}^{s}a_{s,j}X^j,
\]

we get

\[
\boxed{
Z_s^{\rm mix}(\mathbf n)
=
\sum_{j=1}^{s}a_{s,j}
\left[
L^{2j}
-
\sum_{\varnothing\ne S}
(-1)^{|S|+1}g_S^{2j}
\right].
}
\tag{HMJ-10}

The left side is intrinsically nonnegative because all mixed finite roots lie in `(0,4)`.

For `s=1`,

\[
\boxed{
Z_1^{\rm mix}(\mathbf n)
=\frac1{6}
\left[
L^2-
\sum_{\varnothing\ne S}
(-1)^{|S|+1}g_S^2
\right].
}
\tag{HMJ-11}

This vanishes exactly when the interaction polynomial is trivial.

## 8. Higher interaction interpretation

The construction separates two different observations:

```text
positive endpoint mass:
    every purely mixed primitive factor contributes 1
    -> all higher interactions recoalesce completely

reciprocal spectral moments / support:
    every genuinely new mixed denominator contributes positive data
    -> higher interaction remains visible
```

So even at arbitrary arity,

`POSITIVE_MASS_RECOALESCENCE != ABSENCE_OF_HIGHER_BRANCH_STRUCTURE`.

The pairwise join defect is only the first nontrivial member of this inclusion-exclusion interaction hierarchy.

Freeze:

`DIVISIBILITY_JOIN -> HIGHER_MIXED_PRIMITIVE_SPECTRUM`.

`NO_DOMINATING_INPUT -> NONTRIVIAL_MIXED_FACTOR`.

`ALL_MIXED_ENDPOINT_MASSES = 1`.

`RECIPROCAL_MOMENTS = HIGHER_INTERACTION_OBSERVERS`.
