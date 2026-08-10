# Prior art — R004 structural target cut compiler

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 20 must not be read as claiming Smith normal form, finite p-group structure, matroids over rings, valuated matroids, or Nakayama/local-ring reduction as Enterprise Math inventions.

## 1. Smith normal form and finite module structure are prior art

Mathlib's `Mathlib.LinearAlgebra.FreeModule.PID` formalizes Smith normal form for submodules of finite free modules over principal ideal domains and the corresponding diagonal inclusion structure [SRC-R004-STC-MATHLIB-SNF]. R004 uses the classical integer Smith form only as an exact backend for p-adic image cardinalities after reduction modulo `p^K`.

## 2. Residue-field generation over local rings is prior art

Nakayama's lemma gives the standard lifting principle that finite generation/surjectivity can be checked modulo the Jacobson radical under its hypotheses [SRC-R004-STC-STACKS-NAKAYAMA]. This is part of the background explaining why Supplement 19's exact-state reset problem reduces to mod-p linear independence. Supplement 20 explicitly shows that a general target quotient can contain additional higher-p-adic information even when residue rank is unchanged.

## 3. Matroids over rings and valuation rings are prior art

Fink and Moci introduced matroids over commutative rings and explain that over a DVR the structure contains valuated-matroid data; they emphasize that module/group structure can retain information lost by ordinary matroid rank or multiplicity-only summaries [SRC-R004-STC-FINK-MOCI-RING]. Their later work develops matroids over valuation rings and associated valuated-matroid/tropical structures [SRC-R004-STC-FINK-MOCI-VALUATION].

R004 therefore does not claim that p-adic/valuation-sensitive dependency data beyond an ordinary residue matroid is a new general phenomenon.

## 4. Project-local addition under test

The Supplement-20 package is narrower:

1. formulate preservation of a declared target quotient `Bx` after retaining coordinate-reset instructions as `ker A_H subseteq ker B_H`;
2. identify this exactly with `Row(B_H) subseteq Row(A_H)` and the missing-target module `D_H=(Row(A_H)+Row(B_H))/Row(A_H)`;
3. use `D_H` as a typed compiler defect object whose p-group exponent profile is a repair certificate;
4. isolate the field specialization as A-circuits resolved by stacked `[A;B]` coordinates, while proving that the relative-cut clutter need not itself be matroidal;
5. exhibit higher-p-adic target obligations invisible to mod-p rank, so Supplement 19 cannot simply be reused unchanged for general structure preservation.

Historical novelty of this exact Enterprise Math compiler bridge and its selected finite counterexamples remains `NOVELTY_UNVERIFIED`.
