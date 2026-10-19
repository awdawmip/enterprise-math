# Conjecture Backfill Audit — Generation 3

Date: `2026-09-07`
Generation: `BACKFILL-20260907-G3`
Scope: active-task frontiers plus the latest BRC multiplier/collapse research chain after G2.

## Summary

G3 finds one high-confidence omitted conjectural theorem already driving a formal Enterprise BRC research task. It also finds that much of the newest BRC multiplier pipeline is *not* conjectural: the recent square-content, mod-8, pairwise transport, table-free tail, linear-deep-tail and square-gap components are presented with exact theorem/certificate scope, while their benchmark utility remains empirical.

G3 therefore adds one theorem asset and strengthens the scanner so it does not over-register every experimental or predictive BRC artifact.

Historical completeness is not claimed. This is a generational audit.

## Registered asset

### CJ-TH-20260907-001 — Inert-plus terminating Jacobi-jet supercongruence certificate

**Frozen statement.** For every prime `p ≡ 13 or 19 (mod 24)`, write `p=6m+1`. With `Phi_m`, `Psi_m`, `a` and the reflected scalar `R_p` defined by the frozen Enterprise BRC half-coupling Jacobi-jet interface, the single terminating certificate

`(a + p Phi_xx/72)(Psi - p Psi_x/6) ≡ 1 + p R_p (mod p^2)`

holds at `(x,z)=(m,1/2)`.

Equivalent frozen forms are the parent pair `R0+R1` in the cited research artifact. The claim is intentionally restricted to the inert-plus prime classes used by the Enterprise task; it does not register all of Zhi-Wei Sun A14(ii) or all prime powers.

**Why this is a conjecture asset.**

- The project has exact termwise Jacobi-jet identities and an exact reduction of the parent `R0+R1` obligations to this single mod-`p^2` certificate.
- The artifact explicitly says no all-prime proof or counterexample was obtained.
- A finite regression checked 77 relevant primes below 2000 with zero `R0/R1` failures, but the artifact explicitly marks that as finite regression only.
- The same artifact identifies the inherited weighted target with the plus-class `a=1` specialization of Zhi-Wei Sun, *Open Conjectures on Congruences*, Conjecture A14(ii); no proof of the exact weighted 216-series supercongruence was located in the audited 2026 prior-art set.
- The current control plane already routes an active task to prove/refute/strictly reduce this Jacobi-jet certificate. That makes registration urgent: downstream work must carry conjectural provenance rather than treating the reduced target as a theorem.

**Falsifier.** Any exact counterexample prime in the registered congruence classes, or an exact derivation showing the frozen parent reduction/certificate fails under its own definitions.

**Promotion target.** An all-prime proof over the registered prime classes, preferably a terminating WZ/creative-microscoping certificate or a Frobenius/Jacobi-sum transversality proof. Because the scope is infinite over a prime class, finite exhaustive computation alone cannot promote the asset to `PROVED`.

**Priority.** `P0` prove/kill: it is already the smallest unresolved unit of an active formal research lane and has a very narrow exact algebraic interface.

## High-signal deliberate non-conjectures

### 1. `research_notes/BRC_SQUARE_GAP_CASCADE_20260907.md`

Classification: `PROVED_EXACT_FILTER_PLUS_EXPERIMENTAL_PERFORMANCE`.

The staged quadratic-residue/CRT cascade has exact zero-miss structural correctness for its stated square-gap test and a tiny explicit table. Runtime and crossover measurements are empirical engineering facts, not an unproved mathematical soundness claim.

### 2. `research_notes/BRC_LINEAR_DEEP_TAIL_20260907.md`

Classification: `PROVED_EXACT_TRANSPORT_PLUS_BENCHMARKED_UTILITY`.

The merged lane advertises an exact `N^(1/5)` deep-tail theorem, an affine order-one Pell predictor with certificate, and an unbounded mod-8 stream. Finite pipeline speed is benchmark evidence, not a conjecture.

### 3. Recent BRC exact multiplier-transport chain

Classification: `PROVED_OR_CERTIFIED_BRC_TOOLCHAIN`.

This includes the recent exact square-content reduction, dynamic 2-adic gap reduction, mod-8 sparse transport, arbitrary pairwise root/remainder transport, certified table-free multiplier tail and error-linearization/Pell-tail components. Their theorem/certificate scope belongs to the ordinary BRC toolbox, while performance crossover data remains empirical.

### 4. Squarefree-kernel multiplier compression

Classification: `REFUTED_CANDIDATE_NO_SURVIVING_RESTRICTED_LAW`.

The repository records a reproducible `m<=1000` compression experiment, cross-distribution validation and an explicit negative decision without production promotion. No narrower stable mathematical claim was identified in this G3 pass, so nothing is registered as a live conjecture.

### 5. Simple N-shadow adaptive routing

Classification: `NEGATIVE_EMPIRICAL_ROUTING_DECISION`.

The pairwise-transport research explicitly records a negative audit for the simple N-shadow routing proposal. It is not retained as a conjectural tool absent a frozen surviving scope.

## Scanner improvements introduced with G3

`conjecture_scanner_policy.json` and `docs/CONJECTURE_SCAN_AND_PROPAGATION.md` add:

1. confidence tiers `A_REGISTER / B_FREEZE_THEN_REGISTER / C_REVIEW_ONLY / D_EXCLUDE`;
2. hard false-positive classes for proved tools, performance-only evidence, directionless open questions, implementation gaps, raw observations and already-refuted candidates;
3. mandatory closeout surfaces including `unresolved`, `smallest_successor`, `no_claims` and `prior_art_boundary`, not merely prose markers;
4. explicit dependency essentiality (`ESSENTIAL`, `OPTIONAL_HEURISTIC`, `EXPERIMENT_SELECTION_ONLY`);
5. transition propagation for proof, restriction, refutation and supersession;
6. a cycle rule preventing mutually dependent conjectures from self-promoting;
7. active-task-first scan priority.

## Updated prove/kill queue

1. `CJ-TH-20260907-001` — active-task P0, narrow exact Jacobi-jet interface; prove/counterexample/strict reduction.
2. `CJ-TH-20260906-005` — finite N=8 threshold-inertia claim; interval/ball + certified LDL* can directly close bounded scope.
3. `CJ-TH-20260906-004` — exact dynamic four-STAR coefficient bridge.
4. `CJ-TH-20260906-002` — RH prime-response phase-space law.
5. `CJ-TH-20260906-003` — NS effective modulation dimension law.
6. `CJ-TL-20260906-001` — conditional on `CJ-TH-20260906-002`.
7. `CJ-TH-20260906-001` — restricted old-eigenbasis asymptotic.

## Next scan generation

G4 should move backward from active control-plane frontiers into older research artifacts that contain explicit `NO_PROOF`, `FINITE_REGRESSION`, `smallest_successor`, external-conjecture mappings, or conjecture-dependent tool registrations. The goal is to catch claims that became operational dependencies before the September 6 registry existed.
