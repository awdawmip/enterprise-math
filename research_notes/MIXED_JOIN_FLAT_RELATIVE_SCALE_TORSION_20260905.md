# Mixed join defect is the opposite reduced scale times a unit

Status: `FREE_RESEARCH / EXACT FINITE-INTEGRAL-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Closes the stronger module-level boundary left open in
`MIXED_JOIN_CROSS_RESULTANT_COUPLING_20260905.md`.
Depends on:
- mixed join factorization;
- primitive pullback semigroup;
- Frobenius congruence `R_p=u^p mod p`;
- exact mixed cross-resultant magnitude.

## 1. Exclusive ancestral algebra

Let

\[
g=(m,n),\qquad
m=ga,\qquad
n=gb,\qquad(a,b)=1.
\]

Define

\[
A(u):=A_{m|g}(u)=\frac{Q_m(u)}{Q_g(u)}.
\]

Then `A` is monic integral of degree

\[
r:=m-g.
\]

Let

\[
\mathcal A_{m|g}:=\mathbb Z[u]/(A(u)).
\]

This is a free abelian lattice of rank `r`.

The mixed join factor is

\[
\mathcal J(u)=\mathcal J_{m,n}(u)
=\frac{Q_{[m,n]}Q_g}{Q_mQ_n}.
\]

## 2. Pullback of the exclusive sector

For any divisor `c|b`, one still has

\[
(m,gc)=g
\]

because `(a,b)=1`.  Applying the primitive denominator pullback support law to the factor set of `A` gives

\[
\boxed{
\operatorname{Monic}(A(R_c(u)))
=A(u)J_c(u),
}
\tag{MJT-1}

where `J_c` is exactly the mixed join factor associated to the pair `(m,gc)`.

In particular `A|A(R_c)`, so substitution

\[
\bar u\mapsto R_c(\bar u)
\]

defines an integral ring endomorphism

\[
\sigma_c:\mathcal A_{m|g}\to\mathcal A_{m|g}.
\tag{MJT-2}

For `c=b`, `J_c=mathcal J_(m,n)`.

## 3. One prime step is p times a unit

Let `p|b`.  From (MJT-1),

\[
\operatorname{Monic}(A(R_p))=A J_p.
\]

Modulo `p`,

\[
R_p(u)\equiv u^p,
\]

and Frobenius gives

\[
A(R_p(u))\equiv A(u^p)\equiv A(u)^p.
\]

Cancel the nonzero polynomial `A` in `F_p[u]`:

\[
\boxed{
J_p(u)\equiv A(u)^{p-1}\pmod p.
}
\tag{MJT-3}

Hence in the quotient order

\[
\boxed{
J_p(\bar u)=p\varepsilon_p
}
\tag{MJT-4}

for some `epsilon_p in mathcal A_(m|g)`.

The mixed cross-resultant theorem specialized to the pair `(m,gp)` gives

\[
|\operatorname{Res}(A,J_p)|=p^r.
\]

This is the determinant of multiplication by `J_p(ubar)`.  Using (MJT-4),

\[
p^r|\det(m_{\varepsilon_p})|=p^r.
\]

Thus

\[
|\det(m_{\varepsilon_p})|=1,
\]

so

\[
\boxed{\varepsilon_p\in\mathcal A_{m|g}^\times.}
\tag{MJT-5}

Therefore

\[
\boxed{J_p(\bar u)\sim p.}
\tag{MJT-6}

## 4. Prime powers give one unit factor at every depth

From the pullback cocycle,

\[
J_{p^{j+1}}(u)
=J_{p^j}(u)\,J_p(R_{p^j}(u))
\]

up to the monic sign.

Pass to `mathcal A_(m|g)`.  The second factor is

\[
\sigma_{p^j}(J_p(\bar u)).
\]

A ring endomorphism sends units to units, so by (MJT-6)

\[
\sigma_{p^j}(J_p(\bar u))
=p\cdot\text{unit}.
\]

Induction gives

\[
\boxed{
J_{p^a}(\bar u)\sim p^a.
}
\tag{MJT-7}

Thus here depth `a` is retained because the mixed join factor contains all successive prime steps; this differs from the single primitive-factor jump `Psi_(mp^a)` whose normalized resultant sees only one p-layer.

## 5. General reduced scale b

Write

\[
b=\prod_p p^{a_p}.
\]

The phase maps commute, and the pullback cocycle lets the `J_b` class factor into the prime-power step classes, possibly after applying commuting substitution endomorphisms.  Every such substitution preserves units.

Therefore

\[
\boxed{
\mathcal J_{m,n}(\bar u)
=J_b(\bar u)
\sim\prod_p p^{a_p}
=b=\frac ng.
}
\tag{MJT-8}

inside `mathcal A_(m|g)`.

By symmetry, in

\[
\mathcal A_{n|g}:=\mathbb Z[u]/(Q_n/Q_g),
\]

\[
\boxed{
\mathcal J_{m,n}(\bar u)
\sim a=\frac mg.
}
\tag{MJT-9}

## 6. Exact flat quotient modules

Association by a unit identifies the generated ideals:

\[
\mathcal J_{m,n}(\bar u)\mathcal A_{m|g}
=b\mathcal A_{m|g}.
\]

Because the order has rank `m-g`,

\[
\boxed{
\mathcal A_{m|g}/\mathcal J_{m,n}(\bar u)\mathcal A_{m|g}
\cong
(\mathbb Z/b\mathbb Z)^{m-g}.
}
\tag{MJT-10}

Similarly,

\[
\boxed{
\mathcal A_{n|g}/\mathcal J_{m,n}(\bar u)\mathcal A_{n|g}
\cong
(\mathbb Z/a\mathbb Z)^{n-g}.
}
\tag{MJT-11}

Thus the Smith normal form is completely flat: every invariant factor on the `m`-exclusive side is the opposite reduced scale `b=n/g`, and conversely.

## 7. Recover the cross-resultant theorem

Taking orders of the quotient modules gives immediately

\[
|\operatorname{Res}(A_{m|g},\mathcal J)|
=b^{m-g},
\]

\[
|\operatorname{Res}(A_{n|g},\mathcal J)|
=a^{n-g}.
\]

So the previous determinant result is the cardinality shadow of the stronger module theorem.

## 8. Depth comparison with primitive prime-power coupling

For a single primitive jump

\[
\Psi_m\to\Psi_{mp^a},
\]

the quotient-algebra class is only

\[
p\cdot\text{unit},
\]

independent of `a`: one primitive resultant forgets jump depth.

By contrast the mixed join factor accumulates the whole sequence of prime steps and yields

\[
p^a\cdot\text{unit}.
\]

Therefore

```text
single primitive pairwise resultant:
    one p-layer, depth-blind

mixed join closure across all intermediate pullbacks:
    p^a layer, depth-retaining
```

This cleanly separates local pairwise coupling from accumulated scale provenance.

## 9. Interpretation

The mixed factor has three strikingly different properties:

\[
|\mathcal J(0)|=|\mathcal J(4)|=1,
\]

so it is endpoint-mass neutral;

it has positive internal reciprocal moments, so it has genuine spectral support;

and on each exclusive ancestral order it acts as the opposite reduced integer scale times a unit.

Hence

\[
\boxed{
\text{MIXED JOIN RELATIONAL CONTENT}
=\text{FLAT RELATIVE-SCALE TORSION LAYER}.
}
\]

Freeze:

`MIXED_JOIN_ON_m_EXCLUSIVE_ORDER ~ n/g`.

`MIXED_JOIN_ON_n_EXCLUSIVE_ORDER ~ m/g`.

`MIXED_JOIN_SMITH_LAYER = FLAT_RELATIVE_SCALE`.
