# Prior art — R004 future-language representation compiler

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

This note separates the R004 compiler package from established quotient, p-adic, product, finite-abelian, exact-linear-algebra and normal-form mathematics. The project must not treat a closed-form finite compiler specialization as invention of the underlying algebra.

## 1. Generic future-safe quotient is upstream

The generic statement

`declared future signature -> coarsest safe equality = kernel of that signature`

belongs to the existing P023/FQ-004 future-compatible quotient layer. R004 does not re-own that theorem.

P024 already specializes the same principle to integer translation languages and reachable boundary orbits. R004's compiler work is therefore a consumer/specialization: it asks when specific future kernels admit a direct structured normal form instead of an opaque partition-refinement result.

## 2. P-adic valuations and prefix geometry are prior mathematics

The p-adic valuation laws are established [SRC-EOM-PADIC-VALUATION]. In particular, valuation is additive on products and satisfies the non-Archimedean minimum inequality on sums.

R004's one-axis compiler uses the finite fact that `v_p(x-c)` measures how many least-significant base-`p` digits of `x` and a center `c` agree. Organizing a finite center set by shared low-digit prefixes produces a finite trie. Prefix tries and p-adic congruence balls are established structures; R004 does not claim either as new.

The project-specific result is the exact normal form for the declared capped-valuation translation language:

`center token OR deepest occupied exit-parent token`,

with class count

`|centers| + # deficit trie nodes`.

Historical novelty of this exact packaging remains unverified.

## 3. Product kernels and CRT are prior mathematics

Chinese remainder decomposition, Cartesian product kernels and componentwise factorization are standard mathematics.

Therefore the theorem that a full product observable under componentwise dynamics factors through the marginal future kernels is not presented as a new abstract product theorem.

R004 uses it to establish an architectural negative boundary:

> correlated joint action labels alone do not require a joint repair state when all required future outputs remain componentwise.

Joint repair becomes necessary only after a genuine cross-axis observable/dynamical/witness coupling is introduced.

## 4. Linear relation states and rank are prior algebra

An integer matrix `A` defining

`R_A(x)=A x mod p^K`

is ordinary modular linear algebra. Full row rank modulo `p` implies a unit minor and surjectivity onto the relation module. Matrix rank, invertible minors and linear factorization are established prior mathematics.

R004's addition is a sufficiency/compiler statement at the application boundary:

`ambient future -> proved relation factorization -> induced relation action language -> minimal relation repair`.

Under full translations this yields exact future-safe state count `p^(Kr)` from ambient `p^(Kd)` and the integer exponent codimension `K(d-r)`. The algebraic ingredients are prior; the representation-compiler interpretation is project-local and `NOVELTY_UNVERIFIED`.

## 5. Group congruences and finite abelian decomposition are prior mathematics

For groups, congruences correspond to normal subgroups; in an abelian group every subgroup is normal. Thus a translation-invariant equivalence relation on `(Z/p^K Z)^d` becomes a quotient by the zero class. This is established universal/group algebra.

Official Mathlib documentation records that finite abelian groups decompose into direct sums of prime-power cyclic `ZMod` components [SRC-MATHLIB-FINITE-ABELIAN]. Mathlib also provides Smith-normal-form bases for submodules over PIDs [SRC-MATHLIB-SMITH-NORMAL-FORM] and finite free-module quotient decompositions via Smith coefficients [SRC-MATHLIB-FREE-MODULE-QUOTIENT].

R004 therefore does not claim finite abelian classification, Smith normal form, invariant factors or cyclic quotient decomposition as new.

## 6. Torsion-count recovery of exponent profile is an invariant use, not a new structure theorem

For a finite abelian p-group

`Q ~= direct_sum_i Z/p^(e_i) Z`,

the number of elements killed by `p^j` is

`T_j=p^(sum_i min(j,e_i))`.

Consequently finite differences of the exact `p`-power exponents of `T_j` recover how many cyclic factors have depth at least `j`, and hence the invariant exponent multiset.

This follows directly from the standard cyclic decomposition and is not claimed as a new classification theorem.

R004 uses these counts as a **compiler extraction method**: once a generic future kernel passes an additive-congruence gate, recover a structured quotient exponent profile without requiring a predeclared relation matrix or a real-valued logarithm.

## 7. Determinant / exterior linear-lift coordinates are prior linear algebra

A finite partition that is not a modular group congruence may still be the restriction of cosets of a rational subspace in an integer lift. Testing rational-span membership by exact rank, constructing codimension-one normals from cofactors, and representing quotient directions by minors/exterior coordinates are established exact linear algebra.

Mathlib formally exposes exterior algebras/exterior powers and determinants on finite free modules [SRC-MATHLIB-EXTERIOR-ALGEBRA; SRC-MATHLIB-DETERMINANT]. Bareiss-style fraction-free elimination is also established prior symbolic computation [SRC-BAREISS-1968-FRACTION-FREE].

R004 therefore does not claim exterior algebra, wedge products, cofactors, Plücker/minor coordinates or fraction-free determinants as inventions.

The project-specific result is the compiler gate:

`future partition -> intra-class difference span -> exact inter-class separation test -> determinant relation token`,

plus the exact cross-owner identity that the existing A3 weighted relation field satisfies

`Z_ij = -(rank-one determinant token)_ij`.

The A3 weighted closure law becomes the coordinate identity `m wedge (m wedge c)=0`. This is a reduction/recognition of the existing A3 object, not a replacement of A3 ownership.

## 8. A bare kernel cannot reconstruct typed quotient semantics

An equivalence kernel determines an unlabeled quotient set but does not determine which operations, relations, orders or witness semantics the future language requires on that quotient.

R004 records a minimal example: parity on `Z/4Z` has one fixed kernel, while both addition and multiplication descend through it, producing different quotient operation tables (XOR versus AND).

This is not a new theorem in universal algebra; it is a compiler-interface boundary. R004 uses it to require that the compiler retain the **typed future language** as semantic input rather than attempting to reconstruct intended operations from a partition alone.

## 9. Fail-closed compiler ladder is the project-specific architecture

The current R004 package is:

1. one p-power axis + arbitrary translations -> p-adic trie compiler;
2. product/full-vector future -> product of marginal compilers, even for correlated joint actions;
3. proved modular linear coupled future -> relation-rank compiler;
4. additive-congruence future kernel -> quotient module -> invariant exponent profile;
5. noncongruent finite partition -> integer-lift rational-span gate -> determinant relation token when possible;
6. rank-one positive-capacity determinant token -> exact A3 weighted relation field specialization;
7. only after these structured gates fail -> richer A3/A4 relation/witness state;
8. throughout, typed future operations/relations remain part of compiler input and must receive explicit descent certificates on output.

Every mathematical ingredient in these stages has substantial prior art. R004's research contribution under test is the **typed fail-closed compilation architecture**, exact finite specializations, state-complexity formulas, cross-owner reduction identities, and explicit boundaries controlling when the compiler may move to a richer state type.

No compiler result is `CANONICAL_MAIN` yet. Historical novelty of the combined architecture remains `NOVELTY_UNVERIFIED`.
