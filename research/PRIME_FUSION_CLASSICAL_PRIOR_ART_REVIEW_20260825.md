# Prime Fusion — Classical Prior-Art Review

Status: `FROZEN_PUBLICATION_REVIEW / NO_NEW_MATHEMATICS`  
Date: `2026-08-25`  
Researcher-ID: `EM-PFPUB-7C3E91`  
Task-ID: `GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW`  
Owner branch: `review/prime-fusion-publication-attribution`

## 0. Review boundary

This review does not reopen the accepted truth of T1–T15. It asks only what the frozen statements are closest to in the classical literature, whether an exact antecedent was located, and what publication claims are supportable.

Frozen source authority:

- `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md` at blob `055bdaaca81c5ac7ab350a71acf3b69fe5e564a9`;
- `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv` at blob `3c9f6fa670f9405eebbab6eae5d5374c2de4a037`;
- `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md` at blob `54d1fbb8c3fb657ac55f556c982501386a8eaf25`;
- `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json` at blob `6b388f3b17eddf1443de12ec6cf9f6db3e6999c2`;
- F1 Driver review at commit `d94be81c99bb9b300969a7a8cabb26299e248941`;
- `EnterpriseMath/PrimeFusion.lean` on `main@9825c13ff368a1feda37f2baacc7a777d967b8db`.

A missing exact hit is not evidence of novelty. The classifications deliberately avoid `NOVEL`.

## 1. Literature search coverage

The search was organized by mathematical family rather than by Enterprise vocabulary alone. Search clusters included:

1. Gaussian/Eisenstein norms, primitive representations, binary quadratic forms, and simultaneous use of `a^2+b^2` with `a^2-ab+b^2`;
2. `Phi_4`, `Phi_3`, cyclotomic resultants, polynomial CRT, quotient-product rings, and discriminant product formulas;
3. Gaussian and Eisenstein principal quotients, cyclicity under `gcd(a,b)=1`, Smith/Hermite normal form, and integer CRT;
4. quadratic reciprocity and supplementary laws for `-1`, `2`, `3`, and `-3`, including roots of `x^2+1` and `x^2+x+1` modulo primes;
5. local orders 4, 3, and 12, CRT combinations, inversion, and `(Z/12Z)^x` actions;
6. finite-field quadratic root counts from discriminants and quadratic characters;
7. square-free residue-ring decompositions into products of finite fields;
8. unimodular changes of variables on `(Z/MZ)^2` and finite averaging/double counting;
9. graph matching language for components of degree at most one;
10. exact-phrase/formula searches for the T2 gcd identity, the T9 mod-8/mod-12 reciprocity lock, the T10 `{r,r^5,r^7,r^11}` orbit, T11 sixth-power gcd readout, T13 `2+chi_-4+chi_-3` count, and the T14/T15 project-specific formulations.

Primary/authoritative domains searched included AMS, Springer, Wiley, Cambridge University Press, the Stacks Project, Encyclopedia of Mathematics, WorldCat/Crossref-style bibliographic records, and broad scholarly web indexing. Exact-formula searches did not produce a reliable published antecedent for the full T9 or T14 statements; that negative result is recorded only as `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`, not as novelty.

## 2. Classical anchors

### 2.1 Quadratic forms, Gaussian/Eisenstein norms, reciprocity

The Gaussian form `a^2+b^2` and Eisenstein norm form `a^2-ab+b^2` are classical. Standard references include Cox, *Primes of the Form x^2+ny^2*, which treats the historical and structural theory of binary quadratic forms and reciprocity, and Ireland–Rosen, *A Classical Introduction to Modern Number Theory*, whose chapters cover quadratic reciprocity, finite fields, algebraic number theory, and quadratic/cyclotomic fields.

Cox metadata: David A. Cox, second edition, Wiley, 2013, DOI `10.1002/9781118400722`.  
Ireland–Rosen metadata: Kenneth Ireland and Michael Rosen, second edition, GTM 84, Springer, 1990, DOI `10.1007/978-1-4757-2103-4`.

Serre's *A Course in Arithmetic* supplies a classical reference point for finite fields, quadratic reciprocity, and quadratic forms; DOI `10.1007/978-1-4684-9884-4`. Lemmermeyer's *Reciprocity Laws: From Euler to Eisenstein* provides historical and technical coverage of quadratic and higher reciprocity; DOI `10.1007/978-3-662-12893-0`.

Consequences for Prime Fusion:

- T1 is an elementary linear change of variables applied simultaneously to two classical norm forms.
- T2 is an elementary divisibility corollary once the same coefficient pair is used in both forms.
- T9's ingredients are classical reciprocity and supplementary laws, but the exact shared-coordinate lock was not located as a standard named theorem.
- T12 is directly the familiar residue/splitting restriction for the Gaussian and Eisenstein settings, expressed in the project's channel vocabulary.

### 2.2 Cyclotomic factors, resultants, discriminants, and CRT

`x^2+1=Phi_4(x)` and `x^2+x+1=Phi_3(x)` are standard cyclotomic polynomials. Lawrence Washington's *Introduction to Cyclotomic Fields*, 2nd ed., Springer GTM 83 (1997), DOI `10.1007/978-1-4612-1934-7`, is a standard cyclotomic reference.

Tom M. Apostol's paper "Resultants of cyclotomic polynomials", *Proceedings of the American Mathematical Society* 24 (1970), 457–462, DOI `10.1090/S0002-9939-1970-0251010-X`, is a direct classical antecedent for resultant statements involving cyclotomic factors.

For pairwise comaximal ideals, the ring CRT is standard; Stacks Project Lemma 10.15.4 (`Tag 00DT`) states `R/(I_1...I_r) ≅ product R/I_i` under pairwise comaximality. This is the structural core used repeatedly in T3–T8 and T10–T11.

Consequences:

- T3 is a classical composition: two low-order cyclotomic factors + integral CRT + the standard discriminant/resultant product formula. The name "fusion algebra" is project-specific, not a new algebraic species.
- T4 combines standard principal-quotient lattice structure with CRT. Search results also recover the well-known Gaussian quotient fact that `Z[i]/(a+bi)` is cyclic of order `a^2+b^2` when `gcd(a,b)=1`; the analogous Eisenstein quotient follows from the same rank-two lattice/Smith-normal-form mechanism.
- T5 is factor isolation by CRT/Bezout.
- T6's reciprocal-trace substitution and CRT idempotent interpretation are standard mechanisms; the "Boolean collapse" formulation is project-specific packaging.
- T8 is the ordinary square-free/product-of-fields picture with fixed channel labels retained.

### 2.3 Finite fields and local roots

Lidl–Niederreiter, *Finite Fields*, 2nd ed., Cambridge University Press (1997), DOI `10.1017/CBO9780511525926`, is the main finite-field reference used here. It covers field structure and polynomials over finite fields; standard quadratic root counts are controlled by the discriminant and quadratic character.

Consequences:

- T10 uses the two roots of `Phi_4` on the `p` channel, the two roots of `Phi_3` on the `q` channel, local orders 4 and 3, and CRT. Hence the four *oriented* combinations are classical in mechanism. The set `{r,r^5,r^7,r^11}` is a convenient orbit description by the units modulo 12.
- T11 is a direct consequence of those local orders: sixth power gives `-1` on the order-4 channel and `+1` on the order-3 channel, followed by the same gcd isolation as T5.
- T13 is a standard finite-field discriminant/root-count calculation after the project chooses the one-parameter corridor.

No source located in this search supports replacing the corrected T10 oriented locus by the complete root set of `F=(x^2+1)(x^2+x+1)` modulo `pq`. The frozen `H=91` witness therefore remains mandatory: the oriented locus has four elements while the full fused root set has eight.

## 3. Theorem-by-theorem prior-art finding

| Row | Primary class | Confidence | Prior-art conclusion |
|---|---|---:|---|
| T1 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | Standard change of variables for two classical quadratic forms; simultaneous channel packaging is project-specific. |
| T2 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | Elementary gcd scaling/coprimality; no independent research-level novelty is indicated. |
| T3 | `CLASSICAL_COMPOSITION` | HIGH | Cyclotomic factors + resultant/discriminant + polynomial CRT. |
| T4 | `CLASSICAL_COMPOSITION` | HIGH | Principal quotient lattice structure + primitivity + CRT; pointed residue is packaging. |
| T5 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | CRT/Bezout factor isolation. |
| T6 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | Reciprocal substitution + CRT idempotents are classical; Boolean-channel language is the project contribution. |
| T7 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | Elementary inversion of the paired quadratic-form values after the idempotent split. |
| T8 | `CLASSICAL_COMPOSITION` | HIGH | Square-free/product-of-fields characterization plus canonical channel labels. |
| T9 | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` | MEDIUM | Exact shared-coordinate reciprocity lock not located; all proof ingredients are classical, so novelty is not established. |
| T10 | `CLASSICAL_COMPOSITION` | HIGH | Local cyclotomic roots/orders + CRT + unit orbit; oriented-locus scope is essential. |
| T11 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | Immediate local-order sixth-power signs + gcd recovery. |
| T12 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | Standard residue/splitting restrictions for `-1` and `-3`. |
| T13 | `CLASSICAL_COMPOSITION` | HIGH | Standard quadratic-character root counts applied to a project corridor. |
| T14 | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` | MEDIUM | Exact sector-local graph statement not located; proof is a short project-specific congruence consequence, so novelty remains unestablished. |
| T15 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | Finite-torus bijection/double counting under a unimodular map; downward-collapse interpretation is project-specific. |

## 4. Material overlap and novelty judgment

The review found substantial classical overlap across almost every mathematical ingredient. That overlap does **not** undermine the truth of T1–T15, but it does materially constrain publication positioning.

The strongest supportable contribution claim is not "fifteen new theorems". It is that Prime Fusion organizes a coherent, evidence-typed interface among:

- Gaussian and Eisenstein norm channels;
- low-order cyclotomic factors and CRT quotient structure;
- idempotent and phase readouts;
- local reciprocity constraints;
- a project-specific corridor/adjacency presentation;
- a Lean-checked finite-algebra kernel for part of the package.

T9 and T14 are the only rows for which this search did not locate an exact antecedent and for which `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` is justified. Neither is currently strong enough, on literature evidence alone, to support a historical novelty claim or a theorem-paper architecture centered on new number theory.

## 5. Release-form recommendation

Architecture A (`Research theorem note`) is not supported by the current attribution record: too much of the package is standard, direct, compositional, or interface-level repackaging, and the two exact-combination candidates lack novelty establishment.

Architecture B (`Structural/expository research note`) is supported and is the strongest honest primary architecture.

Architecture C (`Formalization-backed note`) is also supportable as a secondary emphasis, provided the Lean boundary is stated exactly: the F1 finite-algebra kernel is Lean-checked on main, but T7/T8 full statements, T9, and T12–T15 are not currently Lean formalized, and the T3 discriminant/named-factor packaging is narrower than the prose row.

Architecture D (`No submission`) is unnecessary if the package adopts bounded structural/expository claims and the mandatory claim guards.

Recommended primary disposition:

`PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`.

Lean synchronization:

`F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`.

## 6. Search limitations

This was a serious web-accessible prior-art review, but it is not a substitute for a subscription MathSciNet/zbMATH citation-tree search by a domain specialist. In particular, absence of an exact T9 or T14 hit must not be converted into a priority or novelty statement. Any later attempt to upgrade the release to a theorem-centered research paper should run a dedicated historical/citation review around those exact combinations before changing the claim class.
