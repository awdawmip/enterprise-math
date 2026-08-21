# R005-A — Enterprise Prime Algorithm Lab research checkpoint

Status: `STRUCTURAL PRIME TOOLKIT CANDIDATE / NOT CANONICAL`
Date: `2026-08-10`
Baseline: `main@4695eb20d92cc3b7ae0c6034e36a1c358325b6b2`
Program: `R005 — Enterprise Prime Toolkit`
Track: `A — Classical Algorithm Transduction`

This checkpoint implements the R005-A handoff as bounded exact research. It does **not** rename classical algorithms as Enterprise Math inventions, does **not** change theorem ownership, and does **not** promote a canonical shared prime API.

## 1. Current verdict

Do not classify this round as `TRANSLATION_ONLY / NO FOUNDATION PROMOTION`.

Recommended status:

`STRUCTURAL PRIME TOOLKIT CANDIDATE / FOUNDATION FEEDBACK YES / CANONICAL PROMOTION NOT YET`

The reason is structural rather than terminological. The bounded exact harness supports:

1. a prime-sound witness/rejection-support cover criterion;
2. an exact pseudoprime-as-uncovered-fiber identity;
3. a unique least root-factor witness basis on `X_N`;
4. a strict separation between rejection strength and observation-partition refinement;
5. bounded Miller–Rabin witness bases as a minimum-set-cover antichain rather than a generic unique least basis;
6. an Atkin XOR/toggle counterexample to pure monotone support elimination;
7. explicit output-minimal versus future-safe state boundaries for wheel/segmented sieves;
8. a working Pratt witness-reduction DAG/tree verifier model.

No new classical primality algorithm, asymptotic speedup, universal deterministic Miller–Rabin threshold, APR/ECPP unification theorem, or certificate compression theorem is claimed.

## 2. Repository audit

At the baseline commit:

- `src/enterprise_math/legendre.py` contains genuinely general helpers `primes_up_to(limit)` and bounded deterministic `is_prime(n)`, but also substantial square-basin/P017/P018-specific logic. Do not promote the whole module.
- `src/enterprise_math/centered_prime_radius.py` and `src/enterprise_math/prime_gap_slack.py` are P018/application-owner surfaces and should remain there.
- P018/P023 power-free action basis has a special unique-least-basis theorem. R005-A shows that uniqueness is **not** generic for witness bases: bounded Miller–Rabin supports can have several different minimum covers.
- P017 already separates least factor-horizon semantics from other earliest-separator notions; R005-A keeps those minimality notions distinct.

Candidate future promotion, only after the shared interface stabilizes:

- `primes_up_to(limit)`;
- deterministic bounded `is_prime(n)` with an explicit contract;
- a generic trial-factor witness;
- a generic finite observation/support explorer.

Do not automatically promote centered radius, prime-gap slack, square-basin carry logic, P003 obstruction witnesses, or the P018/P023 theorem itself.

## 3. Unified prime-sound observation model

Let a finite truth domain be

`X = P ⊔ C`,

where `P` is the prime set and `C` the composite set in the bounded domain.

For a prime-sound witness/test `w`, let

`T_w : X -> {PASS, FAIL}`

with `T_w(p)=PASS` for every `p in P`.

Define its composite rejection support

`E_w = {c in C : T_w(c)=FAIL}`.

For a family `W`, define the joint signature

`Sigma_W(n) = (T_w(n))_{w in W}`.

Then the all-pass composite fiber is

`U_W = C \ union_{w in W} E_w`.

### T-A1 — prime-sound descent / cover criterion

`PRIME/COMPOSITE` descends through the joint signature if and only if

`union_{w in W} E_w = C`,

equivalently `U_W` is empty.

Proof: all primes are all-pass by prime-soundness. If a composite is uncovered it has the same all-pass signature as every prime. Conversely, full composite coverage excludes every composite from the all-pass fiber.

Therefore, in this language:

`pseudoprime = uncovered composite in the current all-pass fiber`.

Adding a witness is exact support contraction.

## 4. T-A2 — unique least root-factor basis

On `X_N={2,...,N}`, for each prime `p` define a root-factor observer that rejects `n` exactly when

`p | n` and `p^2 <= n`.

Then a witness family is primality-safe if and only if it contains every prime `p <= sqrt(N)`.

Hence the unique least basis is

`B_N = {p prime : p <= sqrt(N)}`.

Sufficiency follows because every composite has a prime divisor at most its square root. Necessity follows because omitting `p` makes `p^2` an all-pass composite collision.

This also gives the clean negative boundary: a raw divisibility bit `1[p|n]` cannot distinguish `p` from `p^2`; e.g. `2` versus `4`. Sieve support needs proper-factor/horizon or candidate-generation semantics before it can serve as a primality language.

## 5. T-A3 — rejection strength is not partition refinement

For prime-sound binary tests, a smaller pass set means stronger rejection power. That does **not** imply that the resulting two-block partition refines the weaker test's two-block partition.

Concrete bounded witness:

- `341` passes Fermat base 2 but fails strong Miller–Rabin base 2;
- `9` fails both;
- primes pass both.

Thus MR2 is stronger as a rejection filter, while the one-bit Fermat2 and MR2 partitions are generally incomparable.

Toolkit consequence: keep two separate relations:

1. acceptance/rejection-strength preorder;
2. observation-partition refinement order.

If a refinement chain is required, use a cumulative signature such as `(Fermat2, MR2)` or a staged three-state observer.

## 6. T-A4 — bounded Miller–Rabin bases are exact set covers

Fix a bounded composite universe `C_N` and candidate base set `A`. For each base `a`, let `E_a` be the composites rejected by strong Miller–Rabin base `a`.

By T-A1, a subset `B ⊆ A` is bounded-primality-safe exactly when

`union_{a in B} E_a = C_N`.

So bounded minimum-base search is an exact set-cover problem over rejection supports.

For candidate bases

`[2,3,5,7,11,13,17,19,23,29]`

at `N=100000`, no single base is safe. Exact strong-pseudoprime counts are:

- base 2: 16
- base 3: 23
- base 5: 16
- base 7: 21
- base 11: 25
- base 13: 24
- base 17: 34
- base 19: 34
- base 23: 28
- base 29: 25

Minimum safe pairs in this candidate family are:

`(2,3), (2,5), (2,7), (2,13), (3,5), (5,11), (5,13), (5,19), (7,13), (7,23), (7,29), (11,29), (13,19), (19,29)`.

At `N=1000000`, the minimum safe pairs in the same 10-base candidate set shrink to exactly:

`(2,3)` and `(2,5)`.

The first joint strong pseudoprime for bases `(2,3)` is `1373653`, so the bounded safety breaks there when the domain is extended.

This is a bounded exact/candidate-set result, not a claim of a new universal deterministic Miller–Rabin theorem.

Structural consequence: unlike the existing P018/P023 forced initial action basis, MR minimum bases can form an inclusion antichain. Unique-least-basis behavior must not be generalized from CF055/P018/P023 to arbitrary witness systems.

## 7. Lucas versus modular-exponentiation witnesses

The reference harness includes a strong Lucas–Selfridge observer. Through `N=100000`:

- no tested odd prime fails;
- there are 12 strong Lucas pseudoprimes;
- the first are `5459, 5777, 10877, 16109, 18971, 22499, 24569, 25199, 40309, 58519, 75077, 97439`;
- the bounded Lucas pseudoprime fiber is disjoint from the strong MR base-2 pseudoprime fiber in this domain.

Concrete complementarity:

- `2047`: MR2 PASS, Lucas FAIL;
- `5459`: Lucas PASS, MR2 FAIL.

This supports a cross-language rejection-support explorer. It does not by itself establish any global combined-test theorem.

## 8. T-A5 — support elimination and the Atkin XOR boundary

Prime-sound monotone eliminators have state evolution

`S -> S \ E_w`.

Composition is therefore deletion by a union of supports and is commutative and idempotent.

This captures the external elimination semantics of trial/root witnesses, Eratosthenes, and probable-prime rejectors.

But it does not capture the quadratic-form phase of the Sieve of Atkin.

Exact counterexample: `65` has two qualifying representations in the first Atkin quadratic form:

`65 = 4*2^2 + 7^2`

and

`65 = 4*4^2 + 1^2`.

Atkin toggles twice, returning the candidate to OFF. `65` is composite and is not removed merely because it is a multiple of a square in the cleanup phase. Replacing XOR by monotone union/add-support would therefore retain a false candidate.

The Prime Algorithm Grammar must add an explicit

`support_toggle / XOR`

operator; `support_elimination` alone is not universal.

## 9. Segmented sieve and future-safe state

For a prime `p`, the first mark in segment `[L,H]` is

`max(p^2, ceil(L/p)*p)`.

After `L >= p^2`, the local offset is controlled by `L mod p`. Before/crossing the activation boundary, residue alone is insufficient.

For `p=5`:

- `[10,14]` and `[25,29]` have the same `L mod 5`;
- the first has no legal mark because the `p^2=25` activation has not been reached;
- the second marks `25`.

So a composition-safe local state needs residue/offset plus activation context, or an equivalent repaired state.

## 10. Wheel: output-minimal state versus future-safe state

For a fixed wheel modulus `M`, a single survivor bit is sufficient if the only question is whether the current integer survives.

It is not future-safe under translation.

For `M=6`, both `1` and `5` initially survive. After adding `delta=2`:

- `1+2=3` fails;
- `5+2=7` survives.

Therefore the minimal final-output quotient can be strictly coarser than a quotient safe for future candidate transitions. A CRT residue or equivalent transition state is justified only when future operations require it.

## 11. AKS boundary

A naive small-domain exact AKS reference is included with:

1. perfect-power rejection;
2. multiplicative-order search;
3. gcd sweep;
4. polynomial congruence in `Z_n[X]/(X^r-1)`.

It is cross-checked against the independent exact oracle in the harness.

AKS fits the outer observation/signature/truth-descent architecture, but its internal primitive is genuinely polynomial quotient/congruence state. It should not be relabeled as an ordinary residue witness.

## 12. T-A6 — Pratt certificates as witness-reduction DAGs

The harness builds and independently verifies Pratt certificates.

Nodes are prime claims; edges reduce a claim `p` to the prime factors of `p-1` plus modular witness obligations; terminal `2` is mechanically accepted. Soundness is by induction on certificate depth.

DAG-distinct-node statistics for sample certificates:

- `3`: nodes 2, depth 1, max branching 1
- `5`: nodes 2, depth 1, max branching 1
- `7`: nodes 3, depth 2, max branching 2
- `97`: nodes 3, depth 2, max branching 2
- `997`: nodes 6, depth 4, max branching 3
- `4999`: nodes 5, depth 2, max branching 4

This is enough to motivate a generic certificate protocol. It is **not** enough to claim that APR and ECPP have already been reduced to the same exact implemented verifier interface.

## 13. Prime Algorithm Grammar revision

The original candidate vocabulary remains useful:

- integer root
- quotient
- remainder/residue
- gcd
- exact divisibility
- modular multiplication
- modular exponentiation
- finite polynomial congruence
- support elimination
- witness relation
- certificate reduction

R005-A adds two required concepts:

- `support_toggle / XOR` — forced by Atkin;
- `transition / future-state context` — forced by segmented and wheel future-safety examples.

## 14. Proposed minimal shared API (proposal only)

Do not create these canonical modules in this checkpoint. Candidate design:

`prime_baseline.py`
- `primes_up_to(limit)`
- deterministic-contract `is_prime(n)`
- `trial_factor_witness(n)`
- `segmented_primes(lo, hi)`

`prime_observation.py`
- signatures/fibers
- rejection supports
- pseudoprime fibers
- bounded primality-safety test
- minimum/inclusion-minimal witness bases

`prime_witness.py`
- explicit Fermat/MR/Lucas observers returning probable-pass or composite-witness states, never a misleading generic `is_prime=True`.

`prime_certificate.py`
- generic certificate protocol
- Pratt generator/verifier first
- APR/ECPP adapters only after exact implementations exist.

## 15. Prior-art boundary

Classical ownership remains with the classical literature, including:

- Rabin, *Probabilistic algorithm for testing primality*, JNT 12 (1980).
- Agrawal–Kayal–Saxena, *PRIMES is in P*, Annals of Mathematics 160 (2004).
- Atkin–Bernstein, *Prime sieves using binary quadratic forms*, Mathematics of Computation 73 (2004).
- Adleman–Pomerance–Rumely, *On distinguishing prime numbers from composite numbers*, Annals of Mathematics 117 (1983).
- Pratt, *Every Prime Has a Succinct Certificate*, SIAM Journal on Computing 4 (1975).
- Atkin–Morain, *Elliptic curves and primality proving*, Mathematics of Computation 61 (1993).

R005-A does not claim priority for Eratosthenes/wheel/segmented sieves, Miller–Rabin, AKS, Pratt/APR/ECPP, partition refinement, set cover, or generic witness optimization.

The current Enterprise Math contribution candidate is the exact project-level synthesis of precision/quotient/witness semantics, its root-factor least-basis theorem, the two-order separation, the unique-least-versus-antichain boundary, the XOR boundary, and the output-minimal-versus-future-safe state boundary. External novelty beyond that requires a separate literature audit.

## 16. Foundation Feedback candidates

- `FF-R005A-1`: prime-sound witness families are rejection-support covers; pseudoprimes are uncovered composite all-pass fibers.
- `FF-R005A-2`: rejection-strength preorder is distinct from observation-partition refinement.
- `FF-R005A-3`: unique least witness basis is not generic; MR bounded bases can form a minimum-cover antichain.
- `FF-R005A-4`: Atkin forces XOR/toggle into the operator grammar.
- `FF-R005A-5`: final-output-minimal state may be strictly coarser than future-safe state.

## 17. Next research steps

1. Formalize T-A1/T-A2/T-A3 in Lean before any Foundation promotion.
2. Stabilize a bounded witness-support/set-cover explorer across Fermat/MR/Lucas families.
3. Study Pratt tree-to-DAG sharing and certificate obligation counts before claiming certificate compression.
4. Perform a dedicated external novelty audit for the exact formulations before promoting any theorem as new beyond the project.

## Final answer to R005-A

Enterprise Math is **already doing more than renaming classical prime algorithms**: the common rejection-support/fiber/cover core produces exact theorems and exact negative boundaries.

It is **not yet a finished canonical Prime Toolkit** and has **not yet produced a new classical primality algorithm**.

Current status:

`STRUCTURAL PRIME TOOLKIT CANDIDATE`

`FOUNDATION FEEDBACK YES`

`CANONICAL PROMOTION NOT YET`
