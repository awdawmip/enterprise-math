# N-Coupled Non-Ring Singularization External Prior-Art Audit — Research Return

Task: `RS-N-COUPLED-NONRING-SINGULARIZATION-PRIOR-ART-AUDIT`  
Publication: `TP2-B3E71C5A80D49F26A164`  
Researcher-ID: `EM-NCASPA1-4B7D92`  
Claim: `chatgpt-ncaspa1-20260830-2254-4b7d92`

## 1. Terminal verdict

`SUCCESS / NONRING_CRT_BREAK_PRIOR_ART_CLASSIFIED`

Terminal class:

`NO_EXACT_DUPLICATE_FOUND_WITH_MULTIPLE_STRICT_OR_PARTIAL_ANTECEDENTS`

No audited source was found that jointly satisfies the full guarded interface:

1. public `N` only and factor-blind;
2. genuinely stateful / non-fixed-ring-term semantics;
3. one-sided hidden-CRT behavior;
4. every declared scalar projection before the selective-collapse layer remains `gcd`-clean (`1` or `N`);
5. no Pollard/Williams/ECM order-or-smoothness annihilation;
6. no rho/collision/cycle mechanism;
7. no congruence-of-squares / Fermat / CFRAC / QS / Dixon / NFS relation mechanism;
8. no Hensel/p-adic route that already names the hidden prime/maximal ideal;
9. no scalar zero-divisor, nonunit, idempotent or nontrivial square-root witness whose `gcd` already factors `N`.

This is **not** a novelty, priority, patentability, originality, or nonexistence result. It is an exact audit boundary over the searched surfaces.

## 2. Main conceptual finding: update-map naturality is not the same as process naturality

The parent accepted theorem proves that a **fixed finite** polynomial/localized-ring computation over `Z/NZ` is `N`-erased and CRT-product natural. The external audit shows that several classical factoring algorithms do not need to violate CRT naturality of each arithmetic update.

Pollard rho is the cleanest control. The recurrence

`x_(i+1)=f(x_i) mod N`

reduces to the same recurrence modulo the hidden `p` and `q`. Thus every fixed update is exactly CRT-natural. What creates useful asymmetry is the **history-dependent stopping functional**: two iterates collide modulo one hidden prime before they collide modulo the other, and `gcd(x_i-x_j,N)` detects that event.

The same distinction appears in order methods. For a fixed exponent `M`, `a^M-1` is again one fixed support integer; but a public process enlarges/changes `M`, tries new curves, or advances a smoothness schedule until one hidden group reaches its identity first.

Therefore the precise external lesson is:

> The first genuine escape from the parent `G_poly-loc` theorem can occur at the level of **variable-time process semantics, history, trial-family growth, or stopping/event logic**, even when every individual arithmetic update still commutes with CRT.

This does not relax the task firewall. The known process-level escapes found here are classical excluded mechanisms.

## 3. Order/smoothness family — strict or partial antecedents

### Pollard `p-1`

Public state: modular exponentiation under a smooth exponent schedule.

Selective event: for a hidden factor `p`, the schedule becomes a multiple of enough of `p-1`, so `a^M=1 mod p` before the analogous event holds on every hidden factor.

Extraction: `gcd(a^M-1,N)`.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Reason it is not an exact duplicate: this is precisely the excluded order-annihilation/smoothness route.

### Williams `p+1`

Williams replaces the multiplicative-group condition by a Lucas/algebraic-group condition tied to `p+1` (more precisely the relevant Lucas group order). The same information pattern holds: a public smooth index produces a distinguished identity/trace condition on one hidden channel first, followed by a gcd.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Guard: excluded Williams/order mechanism.

### Lenstra ECM

Lenstra explicitly derives ECM from Pollard `p-1` by replacing the multiplicative group with the group of points on a random elliptic curve.

This is the closest geometric antecedent in the audit. Public curve/point state evolves modulo `N`; the reductions modulo hidden factors have different curve-group orders. A public smooth scalar may kill the point on one hidden reduction but not the other, at which point a projective coordinate/failed inversion becomes a nonunit and a gcd splits `N`.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Why it matters: **non-ring/geometric state by itself is not enough** to define a new mechanism class. ECM already has that feature. Its decisive selective event is still hidden group-order smoothness, which the task explicitly excludes.

## 4. Collision/history family — strict or partial antecedent

### Pollard rho

Public inputs: `N`, a polynomial recurrence and seed.

State: iterate history plus a cycle-detection comparison schedule.

Selective event: equality modulo one hidden factor before equality modulo the other.

Extraction: `gcd(x_i-x_j,N)` or an equivalent batched product.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

A useful exact reconciliation with the parent theorem is:

- any **fixed finite prefix** exposes only finitely many fixed differences and hence only finite static support;
- the factoring method gains power by allowing the compared times to grow with the run.

Thus rho is not a counterexample to the parent's fixed finite-support theorem. It is an exact example of the kind of process-level escape that theorem intentionally leaves open — and it is separately excluded by the task.

## 5. Quotient/floor/canonical-state and relation families

### Continued-fraction factoring / CFRAC

Continued-fraction state uses canonical integer quotients/floors and accumulated convergent/relation information. This is squarely outside a fixed ring term and is therefore an important antecedent to the *state type* under investigation.

But its terminal mechanism is a square relation / congruence of squares and the factor comes from `gcd(X-Y,N)` or `gcd(X+Y,N)`.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Guard: excluded congruence-of-squares.

### Dixon and Quadratic Sieve

These methods collect smooth residues, retain exponent-parity history, and solve a linear system modulo `2` to produce a square relation.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

This is particularly relevant to the “typed non-scalar state” idea: a large relation matrix can remain non-factor-revealing row by row, yet its kernel yields a terminal relation. However, the relation is exactly a congruence-of-squares mechanism, so it is outside the surviving guarded class.

### Number Field Sieve

The NFS amplifies the same pattern: a large history of rational/algebraic smooth relations, sparse `F_2` linear algebra, then a square-root stage and gcd.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Guard: congruence-of-squares / relation factoring.

### Fermat / Lehman / Hart

These methods make canonical square-root/floor/ceiling and multiplier searches computationally explicit. They are genuine examples of non-ring integer-representative state, but their success event is an exact difference of squares.

Classification: `STRICT_OR_PARTIAL_ANTECEDENT`.

Guard: Fermat/congruence-of-squares family.

### Consequence for the open “carry/quotient” residue

No audited method was found whose **decisive** mechanism is merely canonical representative / quotient-remainder / carry state while simultaneously avoiding order, collision, square-relation, named p-adic place and direct nonunit extraction.

Classification for that narrowed class: `NO_MATERIAL_MATCH`.

Again: `NO_MATERIAL_MATCH != NOVELTY`.

## 6. p-adic / Hensel state — adjacent, not factor-blind N-only

Standard Hensel lifting starts with a specified prime `p` (or maximal ideal) and a root/factorization modulo `p`, then lifts it to higher powers.

This is a genuine non-ring/valuation-sensitive state machine, but it fails the target's information-access contract: for `N=pq`, selecting the relevant `p`-adic place already names the hidden channel.

Classification: `ADJACENT_METHOD`.

A future N-only valuation mechanism would therefore need to explain how a place is selected or represented **without** already producing a factor. Merely saying “use p-adics” does not meet the task.

## 7. Exact scalar support firewall

The literature search is complemented by three elementary exact lemmas.

Let `N=pq` for distinct primes.

### Lemma A — one-sided scalar zero is already a factor

If a scalar `s mod N` satisfies

`s=0 mod p`, `s!=0 mod q`,

then

`gcd(s,N)=p`.

The symmetric statement holds with `p,q` exchanged.

So an explicit scalar that is singular/nonunit on exactly one hidden CRT channel is **already the endpoint certificate**.

### Lemma B — nontrivial CRT idempotent is a complementary factor certificate

For `e^2=e mod pq`, each hidden field component is `0` or `1`. A nontrivial `e` therefore has CRT value `(0,1)` or `(1,0)`.

Hence

`{gcd(e,N), gcd(e-1,N)}={p,q}`.

Thus a nontrivial scalar selector does not satisfy the pre-collapse support firewall unless the appearance of `e` itself is declared to be the collapse/readout layer.

### Lemma C — nontrivial square root of unity is a factor certificate

If

`gamma^2=1 mod pq`, `gamma != +/-1 mod pq`,

then the hidden signs are opposite. Consequently

`{gcd(gamma-1,N), gcd(gamma+1,N)}={p,q}`.

This is the classical square-root/factoring equivalence boundary.

### Structural consequence

The genuinely surviving target cannot merely ask for “a scalar whose two hidden reductions differ.” If the difference is a one-sided nonunit or one of the standard complementary scalar witnesses, the factor is already exposed.

The surviving state must keep the asymmetric information **typed/non-scalar until the declared selective-collapse layer**, or else the support firewall is violated by definition.

## 8. Exact duplication table

| Mechanism class | Classification | Why not exact duplicate |
|---|---|---|
| Pollard `p-1` | `STRICT_OR_PARTIAL_ANTECEDENT` | order/smoothness annihilation |
| Williams `p+1` | `STRICT_OR_PARTIAL_ANTECEDENT` | order/smoothness annihilation |
| ECM | `STRICT_OR_PARTIAL_ANTECEDENT` | elliptic-group order/smoothness |
| Pollard rho | `STRICT_OR_PARTIAL_ANTECEDENT` | collision/cycle detection |
| CFRAC | `STRICT_OR_PARTIAL_ANTECEDENT` | congruence of squares |
| Dixon / QS | `STRICT_OR_PARTIAL_ANTECEDENT` | relation parity -> congruence of squares |
| NFS | `STRICT_OR_PARTIAL_ANTECEDENT` | relation matrix -> square-root/gcd stage |
| Fermat / Lehman / Hart | `STRICT_OR_PARTIAL_ANTECEDENT` | difference/congruence of squares |
| Hensel / ordinary p-adic lifting | `ADJACENT_METHOD` | relevant prime/maximal ideal is supplied |
| nontrivial square root / idempotent / scalar zero divisor | `STRICT_OR_PARTIAL_ANTECEDENT` | scalar witness itself is a gcd factor certificate |
| pure guarded carry/quotient residue | `NO_MATERIAL_MATCH` | no audited exact match after all guards |
| full joint target | `NO_MATERIAL_MATCH` | no audited source matches all features jointly |

No row licenses a novelty conclusion.

## 9. What remains genuinely open after the audit

The surviving mechanism class can now be stated more narrowly.

A serious candidate must satisfy all of:

1. **public `N` only** — no hidden `p/q`, candidate-prime selector or named p-adic place;
2. **stateful/non-fixed-term semantics** — otherwise the accepted `N`-erasure theorem applies;
3. **pre-collapse scalar cleanliness** — every declared scalar projection before collapse has gcd `1` or `N`;
4. **not group-order/smoothness** — no Pollard/Williams/ECM rename;
5. **not collision/history equality** — no rho rename;
6. **not square-relation factoring** — no Fermat/CFRAC/Dixon/QS/NFS rename;
7. **not direct nonunit/idempotent/root extraction**;
8. any useful hidden asymmetry must stay in a typed/non-scalar state until its declared collapse/readout.

The most important formulation correction for the mathematical sibling lane is:

> Do not require a positive mechanism to make every update map fail CRT product naturality. Classical evidence shows that a fixed update may remain product-natural while **variable-time stopping/history semantics** creates the useful one-sided event. The real protected target is a non-classical source of process-level hidden-channel asymmetry under the support firewall.

This refinement does not solve the mathematical task; it prevents it from rejecting a valid future candidate for the wrong reason.

## 10. Frozen evidence

Artifacts:

- `research_artifacts/N_COUPLED_NONRING_SINGULARIZATION_PRIOR_ART_AUDIT/source_ledger.json`
- `research_artifacts/N_COUPLED_NONRING_SINGULARIZATION_PRIOR_ART_AUDIT/claim_map.json`

Checker:

- `research_checks/N_COUPLED_NONRING_SINGULARIZATION_PRIOR_ART_AUDIT_CHECK_20260830.py`

Executed regression result:

`PASS {"claim_rows": 9, "nontrivial_idempotent_checks": 20, "nontrivial_sqrt_unity_checks": 20, "scalar_checks": 574, "semiprimes": 10, "sources": 12}`

The finite checker is a structural/regression certificate, not evidence for the literature classifications. The all-`p,q` scalar firewall lemmas are the elementary symbolic proofs in Section 7.

## 11. Driver recommendation

Freeze the audit boundary as:

`NO_EXACT_DUPLICATE_FOUND_WITH_MULTIPLE_STRICT_OR_PARTIAL_ANTECEDENTS`.

For the sibling mathematical task, require every proposed primitive to provide a short “classical-mechanism exclusion table” against:

- group-order/smoothness;
- collision/cycle;
- square-relation/congruence-of-squares;
- named-place p-adic lifting;
- direct scalar nonunit/idempotent/root extraction.

Also refine the phrase `CRT product-naturality break` into a two-level check:

- `UPDATE_MAP_CRT_NATURALITY`;
- `PROCESS_STOPPING_CRT_ASYMMETRY`.

A positive mechanism may live in the second category while the first remains natural. What must remain prohibited is classical excluded semantics or pre-collapse scalar support exposure.

No Working Truth, Foundation, universal factoring lower bound, or novelty authority is asserted.
