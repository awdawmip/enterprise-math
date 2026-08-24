# Prime Fusion Theorem Package — Evidence-Typed Final

Status: `FROZEN / REVIEW_READY / NOT_CANONICAL_FOUNDATION / TASK_RESEARCH`  
Date: `2026-08-24`  
Researcher-ID: `EM-PFFINAL-0AA882`  
Task-ID: `GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE`  
Owner branch: `integration/prime-fusion-evidence-typed-package`  
Historical source text: `research/PRIME_FUSION_THEOREM_PACKAGE_20260823.md@e5138e17f8c4009f5e357f43326f2812c9df1359`  
Final evidence authority: `driver_reviews/PRIME_FUSION_15_THEOREM_FINAL_EVIDENCE_RECONCILIATION_20260824.md@e19ee6713be002dd9c346261173d39fd8d54f9dc`  
Source foundation: `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`  
Scope: one native sector `S_12`; cyclic sector copies are symmetric, but no unproved cross-seam global-neighbor claim is made.

## 0. Freeze discipline and evidence typing

For an interior sector cell with positive integer coordinates `(a,b)` define

`N(a,b)=a^2+b^2`,

`C(a,b)=a^2-ab+b^2`.

`N` is the current sector-local native squared-length readout. `C` is a classical triangular-carrier quadratic readout used here as a second channel. A **dual-prime cell** means that `N(a,b)` and `C(a,b)` are both ordinary primes.

This final package retains exactly theorem rows `T1`–`T15`. It adds no `T16` or `T17` and introduces no new mathematical claim. The evidence record is intentionally typed:

`PRIME_FUSION_ALL_RETAINED_THEOREM_ROWS_INDEPENDENTLY_AUDITED = true`

but

`PRIME_FUSION_ALL_15_BLINDLY_REPLICATED = false`.

Blind reconstruction and statement-exposed independent verification are not collapsed into one label. The exact row-level statuses are frozen in `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv`.

---

## T1 — Simultaneous diagonal coordinates

Evidence: `INDEPENDENT_EXACT`.

Put `u=a+b`, `v=a-b`. Then

`2N=u^2+v^2`, `4C=u^2+3v^2`.

Conversely,

`u^2=3N-2C`, `v^2=2C-N`.

Hence every interior cell satisfies `C<N<2C`, with strictness for nondegenerate dual-prime cells.

## T2 — Exact common-divisor law

Evidence: `INDEPENDENT_EXACT`.

For all integers `a,b`,

`gcd(N(a,b),C(a,b))=gcd(a,b)^2`.

In particular primitive cells have coprime channels.

## T3 — Fusion algebra and discriminant 12

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

Let

`f=X^2+1`, `g=X^2+X+1`, `F=fg`.

Because the two factors are comaximal in `Z[X]`,

`R=Z[X]/(F) ~= Z[i] x Z[omega]`,

where `omega=[X]` satisfies `omega^2+omega+1=0`. Moreover

`Disc(F)=12`.

For `xi=(i,omega)`, the component norms of `a+b xi` are exactly `N(a,b)` and `C(a,b)`.

## T4 — Primitive pointed quotient collapse

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

For a primitive cell, set `N=N(a,b)`, `C=C(a,b)`, `H=NC`. Then

`R/(a+b xi) ~= Z/NZ x Z/CZ ~= Z/HZ`.

The natural pointed residue is

`r == -a*b^(-1) (mod H)`,

and it satisfies `F(r)==0 (mod H)`.

**Frozen strengthening note; not a new theorem row.** If `d=gcd(a,b)`, the Gaussian and Eisenstein component additive quotients have Smith invariant factors `(d,N/d)` and `(d,C/d)`. Hence component cyclicity holds iff `d=1`; primitivity is the exact cyclicity criterion.

## T5 — Exact channel recovery

Evidence: `INDEPENDENT_EQUIVALENT_EXACT`.

For the pointed residue in T4,

`N=gcd(H,r^2+1)`,  
`C=gcd(H,r^2+r+1)`.

No cross-channel factor can leak because the two local polynomials are coprime at every integer input.

## T6 — Reciprocal-trace Boolean collapse

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

For a unit `r mod H` with `F(r)=0`, let

`T=r+r^(-1)`.

Since `F` is reciprocal,

`F(r)/r^2=T^2+T`.

Thus

`e:=-(r+r^(-1))`

is idempotent modulo `H`. For a primitive cell,

`N=gcd(e,H)`,  
`C=gcd(e-1,H)`.

The quartic fusion equation therefore collapses through reciprocal trace to a Boolean channel idempotent.

**Frozen strengthening note; not a new theorem row.** The unit hypothesis is redundant: `F(r)=0 mod H` already forces `r` to be a unit. For arbitrary `H>=2`, the same idempotent yields a universal coprime factor split `A=gcd(e,H)`, `B=gcd(e-1,H)`, with `AB=H`.

## T7 — Unordered cell reconstruction from `(H,e)`

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

Given an idempotent `e mod H`, put

`N=gcd(e,H)`, `C=gcd(e-1,H)`.

Assume `NC=H`, `gcd(N,C)=1`, and `C<N<2C`. Then a positive primitive unordered cell exists exactly when

`U=3N-2C`, `V=2C-N`

are perfect squares. In that case

`{a,b}={(sqrt(U)+sqrt(V))/2,(sqrt(U)-sqrt(V))/2}`.

The square roots automatically have the same parity because `U==V==N (mod 2)`.

**Frozen strengthening note; not a new theorem row.** Idempotence already makes `NC=H` and `gcd(N,C)=1` automatic. For the positive-cell reconstruction gate, `N>C` together with the square conditions is the minimal orientation requirement; strict interiority away from the diagonal is the additional condition `V>0`, equivalently `N<2C`.

## T8 — Dual-prime finite-quotient characterization

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

For an interior primitive cell with both channels greater than `1`, dual primality is equivalent to

`R/(a+b xi) ~= F_p x F_q`

with distinct primes `p=N`, `q=C`. Equivalently, the total norm is the square-free semiprime `pq` with the two prime factors attached to the canonical channel components. This is a structural reformulation, not an algorithmic speedup claim.

**Frozen strengthening note; not a new theorem row.** The algebraic equivalence `N,C both prime <=> H=NC is a square-free semiprime` holds on the larger nonzero nonnegative cell family. The abstract ring shape `F_p x F_q` by itself does not remember which factor is the Gaussian channel and which is the Eisenstein channel; canonical labels come from the fixed product projections / central idempotents.

## T9 — Prime residue classes and reciprocity lock

Evidence: `INDEPENDENT_EXACT`.

For an interior dual-prime cell with `p=N>3`, `q=C>3`, exactly one branch occurs:

`p==1 (mod 8) <=> q==1 (mod 12)`,  
`p==5 (mod 8) <=> q==7 (mod 12)`.

Moreover

`(p/q)=(q/p)=(2/p)=(-1/q)=chi_12(q)`,

with `chi_12(q)=+1` on `q==1 mod 12` and `-1` on `q==7 mod 12`.

## T10 — Channel-oriented four mixed phases and the order-12 automorphism orbit

Evidence: `INDEPENDENT_EXACT_AFTER_SCOPE_REPAIR`.

Under the retained dual-prime hypotheses, let `p=N`, `q=C`, `H=pq`, and let the pointed residue `r` satisfy the oriented local conditions

`r^2+1==0 (mod p)`,  
`r^2+r+1==0 (mod q)`.

Then

`ord_p(r)=4`, `ord_q(r)=3`, hence `ord_H(r)=12`.

Define the **channel-oriented mixed locus**

`M_{p,q}={x mod pq : x^2+1==0 (mod p) and x^2+x+1==0 (mod q)}`.

The corrected exact statement is

`M_{p,q}={r,r^5,r^7,r^11}`.

These four phases form the free `(Z/12Z)^x={1,5,7,11}` orbit of the pointed phase. The shared-coefficient pair is exactly

`{r,r^11}={r,r^(-1)}`,

corresponding to `(a,b)` and `(b,a)`. The other inversion pair `{r^5,r^7}` is algebraically valid inside the same oriented mixed locus but is not the same-coefficient swap pair.

This theorem **does not** claim that these four elements are the complete root set of

`F(X)=(X^2+1)(X^2+X+1)`

modulo `pq`. Other local factor choices can contribute additional roots.

### T10 pressure witness / regression guard

For

`(a,b)=(2,3)`, `(p,q,H,r)=(13,7,91,60)`,

the channel-oriented mixed locus is

`M_{13,7}={18,44,60,86}`,

while the complete fused root set of `F mod 91` is

`{9,16,18,44,60,74,81,86}`.

Thus the oriented locus has four roots and the full fused polynomial has eight roots.

Machine-readable freeze guards:

`T10_SCOPE = CHANNEL_ORIENTED_MIXED_LOCUS_M_PQ`  
`T10_FULL_FUSED_ROOT_SET_CLAIM = false`  
`T10_PRESSURE_WITNESS_H = 91`

## T11 — Sixth-power phase-blind channel readout

Evidence: `INDEPENDENT_EXACT_STATEMENT_EXPOSED`.

For every `x in M_{p,q}` under the source dual-prime hypotheses,

`x^6==-1 (mod p)`,  
`x^6==+1 (mod q)`.

Therefore all four oriented mixed phases have the same sixth power modulo `H`, and

`p=gcd(H,x^6+1)`,  
`q=gcd(H,x^6-1)`.

Channel recovery is phase-blind; phase recovery is a later layer. This conclusion uses the two local equations and does not require completeness of the T10 orbit among all roots of `F mod H`.

**Frozen strengthening note; not a new theorem row.** For coprime channels `A,B` on the same oriented local locus,

`gcd(AB,x^6+1)=A*gcd(B,2)`,  
`gcd(AB,x^6-1)=B*gcd(A,2)`.

The displayed source formulas are the odd dual-prime specialization.

## T12 — Local prime-direction classification

Evidence: `INDEPENDENT_EXACT`.

Let `l>3` be prime and `(a,b)` primitive modulo `l`.

If `l|N`, then `-1` is a square modulo `l`, hence `l==1 or 5 (mod 12)`.

If `l|C`, then `-3` is a square modulo `l`, hence `l==1 or 7 (mod 12)`.

Consequently `5 mod 12` primes can occur only in `N`, `7 mod 12` only in `C`, `11 mod 12` in neither, and `1 mod 12` is the only unramified class that may occur in either channel.

## T13 — Fixed-corridor local root count

Evidence: `INDEPENDENT_EXACT`.

Parameterize a corridor by `a=t+k`, `b=t`:

`F_k=2t^2+2kt+k^2`,  
`G_k=t^2+kt+k^2`.

Even `k` makes `F_k` identically even up to the finite value-2 degeneracy. For odd `k`, every prime modulus leaves a survivor class. More precisely, for prime `l>3`:

- if `l|k`, the union of roots is `{0}` and `nu_l(k)=1`;
- if `l` does not divide `k`, the two root sets are disjoint because `2G_k-F_k=k^2`, and
  `nu_l(k)=2+chi_-4(l)+chi_-3(l)`, namely `4,2,2,0` for `l mod 12=1,5,7,11`.

Also `nu_2=0`, `nu_3=1`. Therefore every odd corridor is locally admissible. This does not prove infinitely many simultaneous primes.

## T14 — Sector-local nearest-neighbor matching theorem

Evidence: `INDEPENDENT_EXACT`.

Inside `S_12`, use carrier-neighbor steps `(1,0),(0,1),(1,1)`. For dual-prime cells with `N,C>3`, opposite parity of `a,b` excludes dual-prime adjacency in the first two directions. Every possible edge lies on a fixed `(1,1)` corridor. Along three consecutive corridor points, `u=a+b` advances by `2`, so one has `u==0 mod 3`; since `4C=u^2+3v^2`, that point has `3|C` and, outside the finite `C=3` degeneracy, is not dual-prime. Hence every sector-local connected component has size at most `2`.

This theorem is sector-local only; no cross-seam global-neighbor statement is asserted.

## T15 — Finite-sieve corridor mean preservation

Evidence: `INDEPENDENT_EXACT_STRONGER_FORM`.

For any finite prime set `P`, put `M=prod(P)`. Parameterize `(a,b)=(t+k,t)`. The map

`(t,k)->(a,b)`

has determinant `-1` and is a bijection modulo `M`. Therefore the average, over `k mod M`, of the exact one-dimensional corridor survivor density equals the exact two-dimensional survivor density for `(N,C)` modulo `M`, with the same multiplicative normalization. This is an exact finite-level downward-collapse mean law, not an asymptotic prime theorem.

**Frozen strengthening note; not a new theorem row.** The independently proved all-function unimodular slice identity applies to every function on `(Z/MZ)^2`; the source survivor-density law is a special case.

---

## Final proved / conjectural boundary

This package claims exactly `T1`–`T15`. It does **not** claim:

- infinitely many dual-prime cells;
- Bateman–Horn asymptotics;
- global three-sector seam matching;
- shortest-vector defect-spectrum formulas;
- empirical angle-limit laws;
- historical novelty;
- factoring speedup.

The deterministic checker family and the final composed checker are audit/reproducibility evidence only; finite computation is not a substitute for the already frozen exact proofs.

## Final package pointers

- Evidence matrix: `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv`
- Dependency graph: `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md`
- Composed checker: `experiments/prime_fusion_final_package_checker.py`
- Manifest: `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json`
- Frozen return: `research_returns/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_RETURN_20260824.md`

`THEOREM_ROW_COUNT = 15`  
`INDEPENDENT_AUDIT_COVERAGE = 15/15`  
`FINAL_PACKAGE_CLASSIFICATION = PRIME_FUSION_FINAL_PACKAGE_FROZEN`
