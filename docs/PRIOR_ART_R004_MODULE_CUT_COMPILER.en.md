# Prior art — R004 module cut compiler

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 19 turns one finite p-power future-language compiler into a representable-matroid obstruction problem. The matroid and local-ring mathematics are prior art.

## 1. Matroid circuits and duality are prior art

Mathlib's matroid library defines a circuit as a minimal dependent set and develops the associated circuit API [SRC-MATHLIB-MATROID-CIRCUIT].

Mathlib's duality module defines the dual matroid by taking complements of bases; complements of bases of `M` are exactly bases of `M*` [SRC-MATHLIB-MATROID-DUAL].

Therefore the statements "minimal dependent column supports are circuits" and "complements of column bases are bases of the dual matroid" are not Enterprise Math inventions.

## 2. Reduction modulo a local maximal ideal is prior algebra

`Z/p^K Z` is a finite local ring with nilpotent maximal ideal `(p)`. Nakayama/local-ring methods routinely recover generation/basis information from reduction modulo the maximal ideal [SRC-STACKS-NAKAYAMA].

Supplement 19 uses an even more elementary finite proof for injectivity of a restricted free-module matrix map: a nonzero kernel vector can be divided by its minimum p-adic valuation and reduced mod p; conversely a mod-p kernel vector lifts after multiplication by `p^(K-1)`.

No novelty is claimed for this local-ring reduction.

## 3. Project-local bridge

R004 claims only the typed compiler specialization:

1. exact carrier `(Z/p^K Z)^d`;
2. current linear observation `Ax`;
3. coordinate-reset future generators;
4. primitive-column assumption ensuring one reset reveals one retained coordinate;
5. retained quotient `(Ax,x|_S)`;
6. carrier cuts equal circuits of the column matroid of `A mod p`;
7. minimal Carrier Bases equal dual-matroid bases and have size `d-rank(A mod p)`.

Historical novelty of this compiler bridge/certificate package remains `NOVELTY_UNVERIFIED`.
