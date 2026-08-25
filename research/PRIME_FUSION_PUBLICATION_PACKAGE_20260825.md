# Prime Fusion — Venue-Neutral Publication Package

Status: `FROZEN_PUBLICATION_PACKAGE / STRUCTURAL_EXPOSITORY_POSITIONING / NO_NEW_MATHEMATICS`  
Date: `2026-08-25`  
Researcher-ID: `EM-PFPUB-9D1ACE`  
Task-ID: `GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW`  
Owner branch: `review/prime-fusion-publication-attribution`

Primary publication disposition:

`PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

Lean/publication synchronization:

`F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

## 0. Publication boundary

This document reorganizes the frozen Prime Fusion theorem package for publication. It adds no theorem, changes no Foundation definition, and makes no historical-priority claim.

The source mathematical authority is the accepted corrected T1–T15 package. The publication review separates four questions that must not be conflated:

1. theorem truth at the frozen scope — already accepted by the prior Driver reviews;
2. independent evidence type — recorded row-by-row in the final evidence matrix;
3. Lean coverage — restricted to the F1 finite-algebra kernel actually merged to `main`;
4. attribution and publication claim strength — classified by the present review.

The strongest honest release form is a **structural/expository research note**, with a formalization-backed component as a secondary emphasis. The package should not be positioned as fifteen historically new theorems.

## 1. Venue-neutral abstract

Prime Fusion is a structural interface joining two classical quadratic norm channels,

`N(a,b)=a^2+b^2`,  
`C(a,b)=a^2-ab+b^2`,

with the low-order cyclotomic factors `Phi_4=X^2+1` and `Phi_3=X^2+X+1`, their product quotient algebra, Chinese-remainder channel decomposition, reciprocal/idempotent readouts, local reciprocity constraints, and finite corridor/adjacency statistics. We present fifteen retained theorem rows whose mathematical content has been independently audited with explicitly typed evidence. Most rows are standard consequences, compositions of classical ingredients, or project-specific repackagings; two exact combinations, T9 and T14, were not located in the prior-art search but are classified only as `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`, not as historically novel. A finite-algebra kernel covering T1–T6 and T10–T11 at the precise F1 scope is Lean-checked on `main`; this does not mean that all fifteen rows are formalized. A corrected mixed-phase theorem is stated only on the channel-oriented locus `M_{p,q}`, with the `H=91` four-versus-eight counterexample retained to prevent a false full-root interpretation. The contribution claimed here is therefore coherent organization, evidence typing, precise interface design, and bounded machine-checked support, not a new general theory of primes or an efficient factorization algorithm.

## 2. Introduction and positioning

The two forms `a^2+b^2` and `a^2-ab+b^2` are classical Gaussian and Eisenstein norm forms. Likewise, the cyclotomic factors `Phi_4` and `Phi_3`, polynomial/ring Chinese remainder theorem, quadratic reciprocity, finite-field root counts, and finite unimodular changes of variables are established mathematics. The publication value of Prime Fusion is not created by renaming those objects.

The package instead places these ingredients into one typed interface in which the same coefficient pair `(a,b)` feeds two arithmetic channels, a single pointed residue encodes the corresponding quotient data, an idempotent separates the channels, mixed local roots carry a controlled phase action, and the one-parameter corridor picture is linked exactly to the two-dimensional finite sieve by a unimodular bijection.

The attribution review therefore supports the following bounded contribution statement:

> Prime Fusion gives a coherent, evidence-typed organization of classical Gaussian/Eisenstein norm arithmetic, low-order cyclotomic CRT structure, channel readouts, and finite corridor/adjacency consequences, together with a Lean-checked finite-algebra kernel for the stated F1 scope.

It does **not** support the statement that the package consists of fifteen new number-theory theorems.

## 3. Grouped theorem package

### Family I — paired norm coordinates and primitive channel arithmetic

#### T1 — Simultaneous diagonal coordinates

Set `u=a+b` and `v=a-b`. Then

`2N=u^2+v^2`,  
`4C=u^2+3v^2`,

and conversely

`u^2=3N-2C`,  
`v^2=2C-N`.

In the retained interior scope, `C<N<2C`.

Publication attribution: `CLASSICAL_DIRECT_COROLLARY`.

#### T2 — Exact common-divisor law

For all integers `a,b`,

`gcd(N(a,b),C(a,b))=gcd(a,b)^2`.

Hence primitive cells have coprime channels.

Publication attribution: `CLASSICAL_DIRECT_COROLLARY`.

### Family II — cyclotomic fusion algebra, quotient, and channel readouts

#### T3 — Fusion algebra and discriminant 12

Let

`f=X^2+1=Phi_4(X)`,  
`g=X^2+X+1=Phi_3(X)`,  
`F=fg`.

The factors are comaximal in `Z[X]`, so

`R=Z[X]/(F) ~= Z[i] x Z[omega]`,

with `omega^2+omega+1=0`, and

`Disc(F)=12`.

For `xi=(i,omega)`, the component norms of `a+b xi` are `N(a,b)` and `C(a,b)`.

Publication attribution: `CLASSICAL_COMPOSITION`.

#### T4 — Primitive pointed quotient collapse

For primitive `(a,b)`, set `N=N(a,b)`, `C=C(a,b)`, `H=NC`. Then

`R/(a+b xi) ~= Z/NZ x Z/CZ ~= Z/HZ`.

The pointed residue

`r == -a*b^(-1) (mod H)`

satisfies `F(r)==0 (mod H)`.

The frozen Smith-normal-form strengthening remains a note, not a new theorem row.

Publication attribution: `CLASSICAL_COMPOSITION`.

#### T5 — Exact channel recovery

For the pointed residue,

`N=gcd(H,r^2+1)`,  
`C=gcd(H,r^2+r+1)`.

This is channel isolation by coprimality/CRT; it is not an efficient factoring-speedup claim.

Publication attribution: `CLASSICAL_DIRECT_COROLLARY`.

#### T6 — Reciprocal-trace Boolean collapse

For a root `r mod H`, put

`T=r+r^(-1)`,  
`e=-(r+r^(-1))`.

Then

`F(r)/r^2=T^2+T`,

so `e` is idempotent modulo `H`; in the primitive-cell specialization,

`N=gcd(e,H)`,  
`C=gcd(e-1,H)`.

The reciprocal substitution and CRT idempotent are classical mechanisms; the Boolean/channel interpretation is project-specific packaging.

Publication attribution: `PROJECT_SPECIFIC_REPACKAGING`.

#### T7 — Unordered cell reconstruction from `(H,e)`

Using

`N=gcd(e,H)`,  
`C=gcd(e-1,H)`,

set

`U=3N-2C`,  
`V=2C-N`.

Under the frozen orientation and primitivity hypotheses, an unordered positive cell exists exactly when `U` and `V` are perfect squares, in which case

`{a,b}={(sqrt(U)+sqrt(V))/2,(sqrt(U)-sqrt(V))/2}`.

Publication attribution: `PROJECT_SPECIFIC_REPACKAGING`.

#### T8 — Dual-prime finite-quotient characterization

Within the retained primitive interior scope, dual primality is equivalent to a canonically labelled quotient of the form

`F_p x F_q`,

with `p=N`, `q=C`; equivalently `H=NC` is square-free semiprime with the two factors attached to the fixed channel projections. This is a structural reformulation, not an algorithmic speedup.

Publication attribution: `CLASSICAL_COMPOSITION`.

### Family III — reciprocity, mixed phases, and local prime directions

#### T9 — Prime residue classes and reciprocity lock

For a dual-prime cell with `p=N>3`, `q=C>3`,

`p==1 (mod 8) <=> q==1 (mod 12)`,  
`p==5 (mod 8) <=> q==7 (mod 12)`,

and

`(p/q)=(q/p)=(2/p)=(-1/q)=chi_12(q)`.

The proof ingredients are classical quadratic reciprocity and supplementary laws plus the shared-coordinate constraints. The review did not locate a reliable exact antecedent for this combined lock; novelty is therefore **not established**.

Publication attribution: `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`.

#### T10 — Channel-oriented four mixed phases and order-12 orbit

Under the retained dual-prime hypotheses define

`M_{p,q}={x mod pq : x^2+1==0 (mod p) and x^2+x+1==0 (mod q)}`.

For the pointed phase `r`,

`ord_p(r)=4`,  
`ord_q(r)=3`,  
`ord_{pq}(r)=12`,

and the corrected exact statement is

`M_{p,q}={r,r^5,r^7,r^11}`.

These four phases form the `(Z/12Z)^x={1,5,7,11}` orbit of the pointed phase on the **oriented** locus.

This is not the full root set of `F=(X^2+1)(X^2+X+1)` modulo `pq` in general.

**Mandatory pressure witness.** For `(a,b)=(2,3)` one has `(p,q,H,r)=(13,7,91,60)` and

`M_{13,7}={18,44,60,86}`,

whereas the complete fused-root set modulo `91` is

`{9,16,18,44,60,74,81,86}`.

Thus the oriented locus has four elements while the full fused polynomial has eight roots.

Publication attribution: `CLASSICAL_COMPOSITION`.

#### T11 — Sixth-power phase-blind channel readout

For every `x in M_{p,q}`,

`x^6==-1 (mod p)`,  
`x^6==1 (mod q)`,

hence

`p=gcd(H,x^6+1)`,  
`q=gcd(H,x^6-1)`.

Publication attribution: `CLASSICAL_DIRECT_COROLLARY`.

#### T12 — Local prime-direction classification

For prime `l>3` and a pair primitive modulo `l`:

- `l|N` implies `l==1 or 5 (mod 12)`;
- `l|C` implies `l==1 or 7 (mod 12)`.

Thus `5 mod 12` may occur only in `N`, `7 mod 12` only in `C`, `11 mod 12` in neither, and `1 mod 12` may occur in either channel.

Publication attribution: `CLASSICAL_DIRECT_COROLLARY`.

### Family IV — corridors, local counting, adjacency, and finite-sieve averaging

#### T13 — Fixed-corridor local root count

For `a=t+k`, `b=t`, define

`F_k=2t^2+2kt+k^2`,  
`G_k=t^2+kt+k^2`.

For prime `l>3` with `l` not dividing `k`, the two root sets are disjoint and the union count is

`nu_l(k)=2+chi_-4(l)+chi_-3(l)`.

The frozen special cases for `l|k`, `l=2`, and `l=3` are retained. Every odd corridor is locally admissible. This is an exact local root-count statement and does not imply infinitely many simultaneous prime values.

Publication attribution: `CLASSICAL_COMPOSITION`.

#### T14 — Sector-local nearest-neighbor matching theorem

Inside the retained native sector, use carrier-neighbor steps `(1,0)`, `(0,1)`, `(1,1)`. For dual-prime cells with `N,C>3`, parity excludes the first two adjacency directions. Along the remaining `(1,1)` corridor, the mod-3 obstruction prevents three consecutive dual-prime cells. Therefore every sector-local connected component has size at most `2`.

This is sector-local only. No global three-sector seam theorem is claimed.

No exact published antecedent for this project-specific adjacency statement was located in the review; novelty is not established.

Publication attribution: `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`.

#### T15 — Finite-sieve corridor mean preservation

For a finite prime set `P`, let `M=prod(P)` and parameterize

`(a,b)=(t+k,t)`.

The map `(t,k)->(a,b)` is unimodular and hence bijective modulo `M`. Consequently the average over `k mod M` of the exact one-dimensional corridor survivor density equals the exact two-dimensional survivor density for `(N,C)` modulo `M` with the same finite normalization.

This is finite double counting under a bijection, not an asymptotic prime-density theorem.

Publication attribution: `PROJECT_SPECIFIC_REPACKAGING`.

## 4. Audit-readable T1–T15 map

| Row | Evidence type | Lean publication label | Attribution class |
|---|---|---|---|
| T1 | `INDEPENDENT_EXACT` | `LEAN_F1_MAIN` | `CLASSICAL_DIRECT_COROLLARY` |
| T2 | `INDEPENDENT_EXACT` | `LEAN_F1_MAIN` | `CLASSICAL_DIRECT_COROLLARY` |
| T3 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `LEAN_F1_MAIN_PARTIAL` | `CLASSICAL_COMPOSITION` |
| T4 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `LEAN_F1_MAIN_CORE` | `CLASSICAL_COMPOSITION` |
| T5 | `INDEPENDENT_EQUIVALENT_EXACT` | `LEAN_F1_MAIN` | `CLASSICAL_DIRECT_COROLLARY` |
| T6 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `LEAN_F1_MAIN` | `PROJECT_SPECIFIC_REPACKAGING` |
| T7 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `NOT_YET_LEAN_FORMALIZED` | `PROJECT_SPECIFIC_REPACKAGING` |
| T8 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `NOT_YET_LEAN_FORMALIZED` | `CLASSICAL_COMPOSITION` |
| T9 | `INDEPENDENT_EXACT` | `NOT_YET_LEAN_FORMALIZED` | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` |
| T10 | `INDEPENDENT_EXACT_AFTER_SCOPE_REPAIR` | `LEAN_F1_MAIN` | `CLASSICAL_COMPOSITION` |
| T11 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` | `LEAN_F1_MAIN` | `CLASSICAL_DIRECT_COROLLARY` |
| T12 | `INDEPENDENT_EXACT` | `NOT_YET_LEAN_FORMALIZED` | `CLASSICAL_DIRECT_COROLLARY` |
| T13 | `INDEPENDENT_EXACT` | `NOT_YET_LEAN_FORMALIZED` | `CLASSICAL_COMPOSITION` |
| T14 | `INDEPENDENT_EXACT` | `NOT_YET_LEAN_FORMALIZED` | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` |
| T15 | `INDEPENDENT_EXACT_STRONGER_FORM` | `NOT_YET_LEAN_FORMALIZED` | `PROJECT_SPECIFIC_REPACKAGING` |

Attribution count:

- `CLASSICAL_DIRECT_COROLLARY`: 5 rows;
- `CLASSICAL_COMPOSITION`: 5 rows;
- `PROJECT_SPECIFIC_REPACKAGING`: 3 rows;
- `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`: 2 rows;
- demonstrated historical novelty: 0 rows.

## 5. Evidence and formalization note

Publication-safe evidence statement:

`15/15 retained theorem rows independently audited`.

The evidence is heterogeneous. Some rows were blindly reconstructed; others were independently verified after statement exposure; T10 was accepted only after scope repair. Therefore the package must not say `15/15 blindly replicated`.

The F1 finite-algebra formalization was merged into `main` by commit

`9825c13ff368a1feda37f2baacc7a777d967b8db`.

Publication-safe Lean statement:

`the F1 finite-algebra kernel is Lean-checked on main`.

The F1 Driver review records successful warning-fatal build evidence, no `sorry`, no `admit`, no custom axioms, and preservation of the corrected T10 oriented-locus regression guard. F1 covers the finite-algebra kernel for T1–T6 and T10–T11 at its exact declared scope, with narrower coverage for T3/T4 than the full prose packaging. It does not formalize the full T7/T8 statements, T9, or T12–T15.

Accordingly the package must not say `all fifteen theorems are Lean-verified`.

## 6. Classical attribution summary

The nearest established mathematical objects are:

- Gaussian/Eisenstein norm forms and binary quadratic forms — T1, T2, T7, T9, T12;
- cyclotomic polynomials `Phi_4`, `Phi_3`, resultants/discriminants, and CRT — T3–T6, T8, T10–T11;
- finite-field quadratic root counts — T13;
- elementary graph matching language plus congruence obstruction — T14;
- finite unimodular change of variables and double counting — T15.

Standard anchors include Cox, Ireland–Rosen, Serre, Lemmermeyer, Washington, Apostol, Lidl–Niederreiter, the Stacks Project CRT lemma, and Diestel for graph terminology. Full metadata appears in `research/PRIME_FUSION_PUBLICATION_BIBLIOGRAPHY_20260825.bib`.

## 7. Limitations and forbidden promotions

This publication package does not establish or claim:

- infinitely many dual-prime cells;
- Bateman–Horn asymptotics as a theorem;
- an efficient factorization algorithm or factoring speedup;
- a global three-sector seam theorem;
- historical priority for T1–T15;
- that the complete fused-root set modulo `pq` consists of the four T10 oriented phases;
- that all fifteen theorem rows are Lean formalized;
- a promotion of Prime Fusion to L3/L4 merely from package completeness or formalization.

Any future research-paper positioning that relies on T9 or T14 as historically new results requires a dedicated specialist citation-tree review before the claim class may be strengthened.

## 8. Recommended article architecture

Primary architecture: **B — Structural/expository research note**.

Recommended flow:

1. paired Gaussian/Eisenstein channel setup and simultaneous coordinates;
2. cyclotomic product algebra and pointed quotient;
3. idempotent/phase readouts with corrected T10 negative control;
4. reciprocity and local prime-direction consequences;
5. corridor root counts, sector-local adjacency, and exact finite mean preservation;
6. evidence-typing and F1 Lean appendix;
7. limitations and prior-art ledger.

Secondary emphasis: **C — Formalization-backed note**, provided the exact F1 boundary is retained.

Architecture A, a theorem-centered research note claiming broad new number theory, is not supported by the current attribution record. Architecture D, no submission, is unnecessary if the bounded structural/expository positioning and claim guards are followed.

## 9. Final release classification

`PRIMARY_PUBLICATION_DISPOSITION = PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

`LEAN_PUBLICATION_SYNCHRONIZATION = F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

`T10_SCOPE = CHANNEL_ORIENTED_MIXED_LOCUS_M_PQ`

`T10_FULL_FUSED_ROOT_SET_CLAIM = false`

`T10_PRESSURE_WITNESS_H = 91`

`HISTORICAL_NOVELTY_ESTABLISHED = false`

`NEW_THEOREM_ROWS_ADDED = 0`
