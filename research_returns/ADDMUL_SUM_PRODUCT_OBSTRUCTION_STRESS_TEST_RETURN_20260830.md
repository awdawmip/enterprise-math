# ADDMUL Sum–Product Obstruction Stress Test — Research Return

Task: `RS-ADDMUL-SUM-PRODUCT-OBSTRUCTION-STRESS-TEST`  
Publication: `TP2-280CC510CF8DCE72FA75`  
Researcher: `EM-AMOBSTR-82D4F1`  
Claim: `chatgpt-amobstr-20260830-1100-82d4f1`  
Execution branch: `research/addmul-sum-product-obstruction-stress-test-em-amobstr-82d4f1`  
Terminal verdict: `SUCCESS`  
Hard-target disposition: `BRIDGE_STRENGTH_HIERARCHY_AND_STRESS_SUITE_CONSTRUCTED`

## 1. Executive result

The useful negative control is **not** “addition and multiplication cannot be bridged.” That statement is false in many typed senses: quotients, valuations, multiplicative logarithms, ghost coordinates, local/formal charts, and finite exact embeddings all give legitimate bridges.

The correct control is:

> Every bridge must declare its strength, domain, two transported laws, injectivity/fibers, closure/undefined cases, exceptional set, hidden coordinates, and theorem assumptions. A bridge is rejected only when its claimed strength exceeds what those certificates support.

This task freezes a five-level hierarchy, elementary no-go lemmas, a fiber-aware sum–product transfer test, a minimal `BRIDGE_AUDIT_PACKET`, and an exact finite checker.

A crucial 2026 correction is incorporated: the classical near-quadratic Erdős–Szemerédi sum–product conjecture over **all finite real sets** was disproved by Bloom–Sawin–Schildkraut–Zhelezov (arXiv:2605.28781). Therefore near-quadratic real growth is not used as an axiom or universal obstruction. The stress layer uses only proved lower bounds in their exact scopes.

## 2. Bridge-strength hierarchy

### L5 — EXACT_INJECTIVE_CONJUGACY

A map `T:D -> Y` is injective on the declared domain, both operations transport exactly,

\[
T(x+y)=T(x)\oplus T(y),\qquad
T(xy)=T(x)\otimes T(y),
\]

and `T^{-1}` reconstructs the source from the image. Any domain restriction is part of `D`, not hidden in prose.

### L4 — EXACT_HOMOMORPHIC_IMAGE

Both laws descend exactly, but `T` is noninjective. The fiber relation

\[
x\sim_T y \iff T(x)=T(y)
\]

must be a congruence for both operations. The kernel/fiber structure is part of the theorem, not an implementation detail.

### L3 — FINITE_TYPED_EMBEDDING

The bridge is exact only on a declared finite set, cell, nilpotent/local neighborhood, or partial-operation domain. Closure, undefined pairs, and the enlargement needed to evaluate `x+y` or `xy` must be explicit.

### L2 — LOSSY_INVARIANT

Only selected identities survive. Typical example: `v_p(xy)=v_p(x)+v_p(y)` while addition retains only a min-plus skeleton plus cancellation depth. Collisions and missing unit/residue coordinates are expected.

### L1 — APPROXIMATE_PROBE

The bridge is statistical/asymptotic/numerical only. It requires an error metric, tested regime, and a prohibition against upgrading approximate agreement to an exact law.

A candidate that cannot meet even L1 is simply `REJECTED`; “lossy” is not a synonym for “wrong.”

## 3. Elementary obstruction lemmas

### Lemma A — same-law zero collapse

Let `R` have additive identity `0` and absorbing multiplication `x*0=0`. Suppose one map `T` and one target binary law `star` satisfy, for all `x,y`,

\[
T(x+y)=T(x)\star T(y),\qquad
T(xy)=T(x)\star T(y).
\]

Then `T` is constant.

**Proof.** Put `y=0`. Both right-hand sides are `T(x) star T(0)`, while the left-hand sides are `T(x)` and `T(0)`. Hence `T(x)=T(0)` for every `x`. No associativity, cancellation, or cardinality assumption is needed. ∎

This is the cheapest exact rejection of a claim that one unchanged coordinate turns both source operations into the **same** target law on a domain containing zero.

### Lemma B — absorbing zero forbids a nontrivial multiplicative map into a group

Let `(G,star)` be a group and suppose

\[
T(xy)=T(x)\star T(y)
\]

on a multiplicative domain containing an absorbing zero. Then `T` is constant.

Indeed,

\[
T(0)=T(0x)=T(0)\star T(x),
\]

and cancellation gives `T(x)=e`. Thus logarithm/discrete-log style bridges must remove zero (or weaken the target from a group/cancellative law).

### Lemma C — exact dual-law transport inherits ring identities on the image

Whenever both laws are exact, the image must inherit every equational identity that uses only the two transported operations and source constants that are in scope. In particular:

- additive identity and multiplicative identity transport to the corresponding identities on the image;
- the image of zero is multiplicatively absorbing;
- distributivity must hold on the image;
- additive cancellation is inherited under injective transport;
- multiplicative idempotents and zero divisors cannot silently disappear under injective transport;
- characteristic/additive order constraints transport.

These are low-cost table checks and should run before any asymptotic theorem.

### Lemma D — exact homomorphic image iff the fibers are operation congruences

For a finite closed domain, `T` induces a well-defined quotient addition and multiplication on `T(D)` exactly when equality of `T`-values is stable under both source operations.

For commutative operations this can be tested by currying each binary operation into all unary translations

\[
L^{+}_{a}(x)=a+x,\qquad L^{\times}_{a}(x)=ax
\]

and requiring every translation to descend through the `T`-fiber partition.

This task reuses `src/enterprise_math/operation_quotient.py::family_descends` for that exact test. No new general quotient engine is introduced.

## 4. Fiber-aware sum–product stress

Let `A` be a finite subset in a source ring, and suppose a bridge is exact on all sums/products generated by `A`.

If `T` is injective there, then

\[
|T(A)\oplus T(A)|=|A+A|,
\qquad
|T(A)\otimes T(A)|=|AA|.
\]

Thus any proved lower bound on `max(|A+A|,|AA|)` transfers exactly.

More generally, if every fiber of `T` on `(A+A)\cup(AA)` has size at most `M`, then

\[
|T(A+A)|\ge \frac{|A+A|}{M},\qquad
|T(AA)|\ge \frac{|AA|}{M}.
\]

Hence any source lower bound `Phi(|A|)` yields the collision-budget inequality

\[
\max\{|T(A)\oplus T(A)|,\ |T(A)\otimes T(A)|\}
\ge \frac{\Phi(|A|)}{M}.
\]

This is the correct way to stress a lossy bridge: a claimed low-growth representation is legal only if its measured fiber budget is large enough to absorb the source growth.

### 4.1 Real-set theorem gate

As of the 2026 literature used here, a proved general lower bound for finite real `A` is the Cushman 2025 estimate

\[
\max\{|A+A|,|AA|\}
\gg_{\varepsilon}
|A|^{4/3+10/4407-\varepsilon}.
\]

This can reject an injective bridge that claims both transported set-growths are uniformly `O(|A|)` on arbitrarily large real sets.

It **cannot** be replaced by the former conjectural near-quadratic bound. Bloom–Sawin–Schildkraut–Zhelezov (2026) construct arbitrarily large real sets for which both sum and product sets are at most `|A|^{2-c}` for an absolute `c>0`. Their construction uses algebraic integers in number fields whose degree grows with `|A|`; the same paper explicitly leaves bounded-degree settings, including the original integer setting, outside that disproof.

### 4.2 Prime-field theorem gate

For `A subset F_p` in the small-set regime, Mohammadi–Stevens prove a `5/4`-type lower bound when `|A|` is at most a constant multiple of `p^{1/2}`:

\[
\max\{|A\pm A|,|AA|\}\gtrsim |A|^{5/4}.
\]

The packet must record the characteristic and size hypothesis before using this. Dense/full-field examples have no superlinear expansion, and general extension fields require subfield-awareness.

### 4.3 What sum–product can and cannot prove here

Sum–product is a **pressure test on a claimed low-growth exact representation**, not a universal theorem that bridges do not exist.

It is inapplicable, or must be weakened, when:

- `T` is highly noninjective and the fiber budget is large;
- the bridge is defined only on a small/local/nonclosed domain;
- the target keeps extra coordinates;
- the source lies in an exceptional subring/subfield regime;
- only one source operation is transported exactly;
- the claim is approximate rather than exact.

## 5. Legal escapes that must be typed, not banned

1. **Subring/subfield restriction.** Exact two-operation structure can survive on a smaller closed domain. The restriction is part of the theorem.
2. **Logarithmic domain.** Multiplicative logarithms work on a multiplicative group after removing zero; source addition is generally not transported by the same simple law.
3. **Valuation quotient.** Multiplication becomes additive, but unit/residue information is collapsed and addition has cancellation defects.
4. **Ghost/extra coordinates.** Additional coordinates may preserve information while simplifying laws. Their count, reconstruction rule, and integrality domain must be explicit. Detailed Witt/ghost analysis belongs to A4.
5. **Noninjective congruence collapse.** Legal at L4 only if both operations descend to the fibers.
6. **Local/formal neighborhood.** Legal at L3 when closure/partiality and coefficient/denominator conditions are explicit.
7. **Approximate probe.** Legal at L1 with an error certificate.

These escapes reduce to five accounting costs: `DOMAIN`, `COLLISION`, `HIDDEN_COORDINATE`, `PARTIALITY`, `ERROR`. An exact global injective bridge has zero cost in all five slots.

## 6. Pretty but false overclaims

### Pseudo-bridge 1 — “one operation represents both”

Killed by Lemma A. On any source containing zero, exact use of the same target law for `+` and `*` forces the map to be constant.

### Pseudo-bridge 2 — “p-adic valuation linearizes the ring”

For positive integers,

\[
v_p(xy)=v_p(x)+v_p(y)
\]

is exact. But

\[
v_p(x+y)\ge \min(v_p(x),v_p(y))
\]

can be strict because of cancellation. The checker finds zero multiplication-transport failures and many min-skeleton failures; already `v_2(1+1)=1>0`.

Verdict: legitimate `L2_LOSSY_INVARIANT`, not L5.

### Pseudo-bridge 3 — “exponentiation unifies addition and multiplication”

For `T(n)=2^n`,

\[
T(a+b)=T(a)T(b)
\]

is exact. Forcing source multiplication through the same target multiplication would require `2^{ab}=2^{a+b}`, which fails generically. The checker sees zero first-law failures and 79 second-law failures on `{0,...,8}^2`.

Verdict: one-operation coordinate trick, not a two-operation bridge.

### Pseudo-bridge 4 — “discrete logarithm linearizes F_p”

Discrete log exactly sends multiplication on `F_p^*` to addition of exponents. But zero is excluded, `F_p^*` is not closed under source addition, and where the sum remains nonzero the same exponent-addition law does not encode source addition.

For `F_7^*` with primitive root `3`, the checker finds:
- multiplication failures: `0`;
- addition pairs leaving the domain: `6`;
- same-law addition failures among the remaining pairs: `25`.

Verdict: exact multiplicative-group bridge only.

## 7. Exact finite checker results

`research_checks/ADDMUL_SUM_PRODUCT_OBSTRUCTION_STRESS_TEST_CHECK_20260830.py` freezes the following exact witnesses.

### Quotient/congruence reuse

On `Z/8Z`, after currying addition and multiplication into unary translation families:

- identity partition: both operation families descend;
- parity partition `x mod 2`: both descend exactly, giving the legitimate quotient `Z/8Z -> Z/2Z`;
- residue `x mod 3`: does not descend.

Direct binary-table counts for `Z/8Z -> Z/3Z` are:
- addition failures: `28`;
- multiplication failures: `25`.

This separates a **lossy but exact quotient** from an arbitrary lossy map.

### Collision/growth packet

For `A={1,...,12}` in the integers:

\[
|A|=12,\qquad |A+A|=23,\qquad |AA|=59.
\]

After parity collapse:
- sumset image size `2`, max fiber `12`, collisions `21`;
- product-set image size `2`, max fiber `39`, collisions `57`.

The dramatic growth reduction is therefore not mysterious: the packet exhibits the collision budget that paid for it.

The checker was independently replayed with exact integer arithmetic; all frozen assertions pass.

## 8. Minimal BRIDGE_AUDIT_PACKET

The frozen artifact is:

`research_artifacts/ADDMUL_SUM_PRODUCT_OBSTRUCTION_STRESS_TEST/BRIDGE_AUDIT_PACKET_V1.json`

Required fields include:

- candidate ID and strength level;
- exact domain/codomain/map;
- injectivity and fiber/kernel certificate;
- both transported laws and their scope;
- images of identity/absorber elements;
- closure/partiality and exceptional set;
- hidden coordinates and reconstruction rule;
- elementary obstruction results;
- finite table metrics;
- sum–product theorem gate with all hypotheses;
- approximation error when relevant;
- final verdict.

This packet is intentionally task-local. It may be promoted later only after multiple returned tasks demonstrate reuse.

## 9. Deduplication and method harvest

Existing Enterprise Math machinery already contains the finite operation-family quotient closure needed for exact congruence testing. This task reuses it by currying binary ring operations into unary translations.

Method harvest:

`T6_OPERATION_SAFE_QUOTIENT = REUSE_APPLIED`

No new general-purpose core module is claimed.

The stress suite complements rather than duplicates:
- A1/A2: positive algebraic cross-effect/defect bridges;
- A4: ghost/multiscale coordinates;
- A5: valuation/tropical geometry;
- A6: additive/multiplicative spectral coupling.

A7 supplies the shared negative-control contract those positive routes can be audited against.

## 10. External theorem sources and status

External results are comparison/stress inputs only; they do not become Enterprise Math Working Truth by citation.

1. Adam Cushman, *A note on the Sum-Product Problem and the Convex Sumset Problem*, arXiv:2512.13849 (2025): proved real-set lower bound with exponent `4/3 + 10/4407 - epsilon`.
2. Thomas F. Bloom, Will Sawin, Carl Schildkraut, Dmitrii Zhelezov, *The sum-product conjecture is false for real numbers*, arXiv:2605.28781 (2026): disproves the near-quadratic conjecture over all real finite sets and supplies analogous constructions in other settings.
3. Ali Mohammadi, Sophie Stevens, *Attaining the exponent 5/4 for the sum-product problem in finite fields*, arXiv:2103.08252 / published work: small prime-field `5/4` lower bound.
4. Oliver Roche-Newton, Misha Rudnev, Ilya Shkredov, *New sum-product type estimates over finite fields*, Advances in Mathematics 293 (2016): earlier characteristic-dependent finite-field growth bounds.

## 11. Residue and recommendation

The hard target is met at the level requested: hierarchy, elementary witnesses, scoped sum–product gate, legal escapes, finite checker, and minimal audit packet are all explicit.

What is **not** proved is a universal classification of every possible notion of “simple target law.” Such a theorem would require a declared complexity class for target operations (for example affine, polynomial of bounded degree, finite-state, or bounded-coordinate laws). That should be a successor only if Driver review decides the current audit packet is insufficient for positive bridge returns.

Recommended control-plane action:

`DRIVER_REVIEW_AND_REUSE_BRIDGE_AUDIT_PACKET_ACROSS_A1_A2_A4_A5_A6_BEFORE_ANY_NEW_NO_GO_TASK`
