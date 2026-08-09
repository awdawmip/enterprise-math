# P025 Supplement 06 — Prime-Local Absorption Obstruction Spectrum

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 04–05  
Hard block: `NONE`

## 1. From one gcd to a local obstruction spectrum

Supplement 05 proved

\[
\eta_{\min}
=
\gcd_{\text{cross-block }p,q}
K_{p,q},
\qquad
K_{p,q}
=
\frac{R e_p e_q}{g p q},
\]

where

\[
R=\operatorname{rad}(abc),
\qquad
e_p=v_p(abc),
\]

and `g` is the content of the raw additive-relation row.

A gcd is global notation for independent local prime obstructions. The present supplement resolves `eta_min` into those local coordinates.

## 2. P025-T19 — exact local valuation formula

For every prime `ell`, define the local load of a cross-block pair `p,q` by

\[
\boxed{
A_\ell(p,q)
=
v_\ell(R)
+v_\ell(e_p)
+v_\ell(e_q)
-v_\ell(g)
-\mathbf 1_{p=\ell}
-\mathbf 1_{q=\ell}.
}
\]

Then every `A_ell(p,q)` is a non-negative integer and

\[
\boxed{
 v_\ell(\eta_{\min})
=
\min_{\text{cross-block }p,q}
A_\ell(p,q).
}
\]

### Proof

By P025-T15,

\[
K_{p,q}=\frac{R e_p e_q}{g p q}
\]

is a positive integer. Taking the ordinary `ell`-adic valuation gives exactly the displayed formula for `A_ell(p,q)`. Since the valuation of a gcd is the minimum valuation of its entries,

\[
v_\ell(\eta_{\min})
=
\min v_\ell(K_{p,q}),
\]

which is the claimed identity. ∎

## 3. P025-D03 — absorption obstruction spectrum

Define

\[
\boxed{
\mathcal O_{\rm abs}(a,b,c)
=
\{(\ell,v_\ell(\eta_{\min})):
 v_\ell(\eta_{\min})>0\}.
}
\]

Then

\[
\boxed{
\eta_{\min}
=
\prod_{(\ell,r)\in\mathcal O_{\rm abs}}
\ell^r.
}
\]

Perfect absorption is equivalent to an empty obstruction spectrum.

Equivalently,

\[
\boxed{
\eta_{\min}=1
\iff
\text{for every prime }\ell,
\text{ some cross pair }p,q\text{ has }A_\ell(p,q)=0.
}
\]

Thus failure of perfect absorption is local in the precise sense that some prime `ell` remains present in **every** normalized cross-support minor.

## 4. Two distinct sources of local obstruction

The formula separates two mechanisms.

### 4.1 First-order support obstruction

If `ell|R`, the term `v_ell(R)=1` contributes a support-level unit. A cross pair containing `ell` can cancel that unit through the denominator indicator.

Whether cancellation is complete also depends on valuation exponents and the additive-row content.

### 4.2 Second-order valuation obstruction

Even if

\[
\ell\nmid R,
\]

one can still have

\[
v_\ell(\eta_{\min})>0
\]

because `ell` divides the valuation integers `e_p` in every relevant cross pair strongly enough to survive the normalization by `g`.

Hence the obstruction spectrum can contain primes that are not prime divisors of `abc` at all.

This motivates the project diagnostic language

\[
\boxed{
\text{first-order support }\{p:p\mid abc\}
\quad\text{versus}\quad
\text{second-order support of valuation exponents }\{\ell:\ell\mid v_p(abc)\}.
}
\]

Prime factors of valuation exponents are ordinary arithmetic data; P025 claims no novelty for studying exponent patterns. The new role under test is that this second-order support becomes an exact certificate-precision obstruction coordinate.

## 5. P025-N05 — high abc quality does not force perfect absorption

A tempting conjecture after the first high-quality examples was that exceptional/high-quality abc triples might automatically have `eta_min=1`. This is false.

### Counterexample A — support-local obstruction

\[
1+512=513.
\]

Here

\[
512=2^9,
\qquad
513=3^3\cdot19,
\qquad
R=114.
\]

The exact support formula gives

\[
\eta_{\min}=3,
\qquad
\mathcal O_{\rm abs}=\{(3,1)\}.
\]

At the same time

\[
\boxed{513^4>114^5,}
\]

so standard abc quality is greater than `5/4`.

Thus even a rational-exponent high-quality event does not force perfect absorption.

### Counterexample B — obstruction prime outside radical support

An even more revealing example is

\[
1+242=243,
\]

with

\[
242=2\cdot11^2,
\qquad
243=3^5,
\qquad
R=66.
\]

The additive row has content `g=1`. The two normalized cross terms are

\[
K_{2,3}=55,
\qquad
K_{11,3}=20.
\]

Therefore

\[
\boxed{\eta_{\min}=5.}
\]

The obstruction prime `5` is not in

\[
\operatorname{supp}(R)=\{2,3,11\};
\]

it is supplied by the valuation exponent

\[
v_3(243)=5.
\]

Moreover

\[
\boxed{243^{10}>66^{13},}
\]

so quality is greater than `13/10`.

This simultaneously falsifies two naive reductions:

1. high abc quality does not imply `eta_min=1`;
2. absorption obstructions are not determined by radical prime support alone.

## 6. P025-T20 — one-plus-squarefree prime-power obstruction spectrum

Under P025-T17,

\[
1+b=p^m,
\]

with `b>1` squarefree, gives

\[
\eta_{\min}=m.
\]

Therefore the local obstruction spectrum is exactly the ordinary prime factorization of the **valuation exponent** `m`:

\[
\boxed{
\mathcal O_{\rm abs}(1,b,p^m)
=
\{(\ell,v_\ell(m)):\ell\mid m\}.
}
\]

This is the cleanest family showing second-order support in isolation.

For example,

\[
1+31=2^5
\]

has

\[
R=62,
\qquad
\eta_{\min}=5,
\qquad
\mathcal O_{\rm abs}=\{(5,1)\},
\]

although `5` divides neither `31` nor `2`.

## 7. Relation to P018 factor precision

P018's canonical factor-precision line observes tested prime divisors of the **state integer** `n`, for example

\[
D_y(n)=\{p\le y:p\text{ prime},\ p\mid n\}.
\]

That is a first-order factor-witness precision system.

The present obstruction spectrum is not the same object. It can require prime factors of the integers

\[
v_p(n),
\]

which are metadata about multiplicity rather than prime divisors of `n` itself.

So P025 provides evidence for a possible higher-order factor descriptor, but it does **not** modify P018 or claim that such a hierarchy is a new foundation layer. The correct next step is to test whether this higher-order support is useful outside the current Wronskian certificate language.

## 8. Relation to P023 task-relative precision

The distinction is again future-language dependent.

- If the future only asks for radical support, exponent-prime factors may be discarded.
- If it asks for `eta_min`, the normalized local loads are sufficient.
- If it asks for the whole Pareto witness frontier, local obstruction data are insufficient because search radius still depends on witness geometry.

Thus

\[
\boxed{
\text{same fine integer state}
\to
\text{different minimal retained arithmetic features}
\text{ for different certificate languages}.
}
\]

This remains a specialization of P023's generic query-generated precision calculus.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_absorption_local.py`
  - exact `ell`-local load formula;
  - absorption obstruction spectrum;
  - perfect-absorption local criterion;
  - exact high-quality counterexample helper.
- `tests/test_abc_absorption_local.py`
  - support-local and exponent-only obstruction examples;
  - exact spectrum reconstruction;
  - high-quality counterexample regression;
  - bounded scan recovering several `quality>1` / `eta_min>1` triples.

Finite scans are falsification/regression tools only.

## 10. Current conclusion

The P025 witness line now has a clean separation:

\[
\boxed{
\text{radical support}
\to
\text{valuation structure}
\to
\text{local absorption obstruction spectrum}
\to
\eta_{\min}
\to
\text{full norm/absorption Pareto frontier}.
}
\]

The first three levels are exact arithmetic summaries of increasingly rich future certificate languages. None replaces the next one universally.

## 11. Next frontier

No hard block exists. Continue with:

1. classify local obstruction patterns by support-block sizes and valuation vectors;
2. derive sharp bounds on `eta_min` from the exponent vector before any witness search;
3. compare obstruction spectrum with the Pareto radius at which the obstruction floor is first attained;
4. test whether iterating “prime support of valuation exponents” produces useful higher-order structure or merely redundant arithmetic encoding;
5. reread Pasten's lattice determinant/Geometry-of-Numbers proof against this local spectrum and downgrade any rediscovered component to prior art;
6. search for consequences of small `eta_min` **conditional on** independent norm control, rather than confusing absorption tightness with the abc conjecture itself.
