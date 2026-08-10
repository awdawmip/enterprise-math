# Prime-Ideal Criterion for Branch-Safe Coefficient Quotients

Status: `RESEARCH BRIDGE / NONCANONICAL`

The coefficient branch-mixing examples admit an exact generic criterion.

## 1. Product-zero branch semantics

Suppose an exact coefficient ring R is an integral domain and a world law uses

`f g=0`

as a logical encoding of

`f=0 OR g=0`.

Collapse coefficients through a quotient

`R -> R/I`.

The quotient preserves this product-zero branch implication for **all** coefficient values iff

`ab in I -> a in I or b in I`

for all `a,b in R`.

But this is exactly the definition that I is a prime ideal.

Therefore

`product-zero branch semantics descends through R/I`

iff

`I is prime`

iff

`R/I is an integral domain`.

## 2. Integer modular specialization

For R=Z and nontrivial finite quotient

`Z -> Z/MZ`,

the ideal `M Z` is prime exactly when M is a prime integer.

Hence generic product/disjunction semantics is locally branch-safe exactly at prime moduli.

- mod p: safe for product-zero branch logic;
- mod `p^e`, `e>1`: not generically safe;
- mod composite M with multiple prime factors: not generically safe.

The exact world `I=(0)` is also prime because Z is a domain; the modulus-one zero ring is a trivial collapsed boundary and is not treated as a faithful logical world.

## 3. More numeric precision need not mean more logical precision

Along one p-adic numeric chain:

`mod p -> mod p^2 -> mod p^3 -> ...`

state/residue information becomes finer by divisibility.

Yet only the first nontrivial quotient mod p is a field. Every deeper `Z/p^e Z` has zero divisors.

Therefore the precision vector can move in opposite directions:

- **numeric p-adic precision** increases;
- **generic product-branch faithfulness** drops from true to false once `e>1`.

This is a concrete proof that one scalar "precision level" cannot summarize every semantic capability of a quotient.

## 4. Local branch safety is still not global branch coherence

Prime moduli remove zero-divisor branch mixing inside each local field, but the selected branch can still vary with p.

Thus two separate requirements remain:

1. **local algebraic safety** — the coefficient quotient kernel is prime, so each local product-zero state has at least one local branch label;
2. **cross-precision witness coherence** — the branch labels selected at different precision components descend to one common exact/global witness.

The profinite ghost passes the first condition prime by prime but fails the second.

So prime-ideal safety is necessary for faithful local disjunction semantics, but not sufficient for exact global witness descent.

## 5. Restricted factor families can be safer than the generic quotient

If only a special constrained set of factor values can occur, a quotient with zero divisors may accidentally remain safe on that restricted image. The prime-ideal criterion is the **uniform all-values theorem**.

Project routing should therefore distinguish:

- generic coefficient-law safety of the quotient itself;
- route-specific safety on the actually reachable factor-value subset.

This parallels the distinction between a generic safe-operation algebra and a smaller task-relative safe operation family.

## 6. Prior-art boundary

Prime ideals, integral domains, quotient rings and zero divisors are standard prior algebra. The Enterprise Math value is the precision interpretation:

> **a coefficient collapse can preserve polynomial syntax while failing the logical branch law encoded by that syntax; uniform branch-safe descent is exactly a prime-ideal condition.**