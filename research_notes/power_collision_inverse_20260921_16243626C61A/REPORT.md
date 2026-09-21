# POWER feedback III: exact inverse-orbit collision readout

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (local continuation key, not an authenticated platform ID)
Progress-Event-ID: `power-collision-inverse-20260921-16243626C61A`
Status: `PROVED_SCOPED_DERIVATIONS + BOUNDED_EXECUTABLE_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`

## Question and exact source reuse

Continue the positive POWER feedback: can the collision coefficient be computed without keeping every element of the generated subgroup as a separate mass state?

Frozen POWER reference: `awdawmip/power@6d784d3990afae602a03745173c3f2a16a076b0c:src/power/algebra/group_ring_order.py`, Git blob `11d4adf3ff6e56c440cfdd7974be6c28f8ff068a`. Its unchanged bytes were recovered from the earlier local review artifact and hash-checked before execution.

EM source read: `7085a98fc76cbdf48c671febd01ccea70f505eb2`. Existing `src/enterprise_math/brc_control_mass.py`, Git blob `e8811e5f194fc57b294be7255214361fe99395d5`, was copied byte-for-byte and executed unchanged through `ControlMassQuotient.compile` on exact mass-only adapters. This is `REUSE_EXECUTED`, not just a catalogue lookup. The adapter exposes precisely state_count, blocks and forget_effects().total_mass; it does not invent geometric/control-port semantics.

Reuse classification: T0 positive BRC mass + T4 collision observer + T6 observer-safe quotient, `DOMAIN_OPERATOR_CANDIDATE / EXTEND_EXISTING_INTERFACE`. No new top-level family, accepted-tool registration, task CLAIM or Driver/Steward admission is asserted. P000 is unchanged; no physical/geometry interpretation is needed here.

## 1. Exact scope and aggregation law

Let G=<a> be the cyclic subgroup of units modulo n, with order r (used in proofs, NOT supplied to the online algorithm). Put

    T_g = 2[e] + [g] + [g^-1],
    C_m = product(j=0..m-1) T_(a^(2^j)),
    K_(2^m) = coefficient_[e](C_m).

The carrier is a nonnegative integer histogram on G. Total branch mass is 4^m. The observer is the identity coefficient after every prefix; allowed subsequent operations are products of inverse-symmetric kernels T_g. Oriented +/- atom identities, arbitrary unequal weights and arbitrary new observables are outside this lease.

Partition G into inverse orbits [u]={u,u^-1}. For a mass histogram c, retain

    A(c)([u]) = sum(v in [u]) c(v).

Because G is abelian, inversion swaps the +g and -g transitions. Thus every state in [u] sends exactly the same total weight into every target orbit. The quotient row has weight 2 to [u], 1 to [ug], and 1 to [ug^-1], with coincident targets ADDING their weights.

Therefore A(T_g c)=bar(T_g) A(c). The identity orbit is a singleton, so the identity coefficient is exactly preserved after any sequence of allowed kernels, for arbitrary starting positive masses. This is strong mass lumpability plus an independently checked observer condition, not an assertion of atomwise equivalence.

The online solver stores an orbit's TOTAL mass. It must not divide this total by two. The self-inverse orbits, including identity and possibly the element of order two, are singletons and are handled without special fractional weights.

## 2. Constructive compression without an order oracle

`src/enterprise_math/group_ring_inverse_quotient.py` maintains keys (u,u^-1), sorted as two residues, and one integer mass per orbit. It computes a^-1 once. Thereafter multiplying both entries updates the inverse pair, so no per-state modular inverse is required. It does not enumerate G before quotienting and does not use r to select the representation.

At saturation, the number of keys is

    (r + gcd(r,2))/2 = floor(r/2)+1.

The algorithm returns every prefix K, retained key counts and full-support counts. A hard state cap returns BUDGET_EXHAUSTED with the last COMPLETE prefix and no certified final order. Small explicit m is a valid mass query, not an exact-order claim. The inherited sufficient condition Q>=n^2 certifies nearest-integer order recovery; a modular roundtrip is an additional check, not a standalone minimality certificate.

### Exact fixed-suffix shortcut

When the actual generator g_j equals identity, all later dyadic generators also equal identity and every remaining kernel is 4[e]. The solver multiplies the scalar readouts by four without rebuilding/scaling all dictionary entries. This is a valid fixed-suffix simplification. A conventional full-state implementation can use the SAME shortcut; speed due to it must not be credited solely to inverse-orbit merging.

## 3. A sharp lower bound, ONLY for the declared richer continuation language

Suppose a representation must preserve identity-return mass from every starting group state under every repetition of T_a. Identify states as a^j and define d(j)=min(j,r-j).

After k updates, the identity coefficient from a^j is zero for k<d(j), and positive for k=d(j): no path with steps -1,0,+1 traverses that cyclic distance sooner, and a shortest path exists. Inverse states have identical return sequences by symmetry. Distinct inverse orbits have distinct distances and therefore different first-positive times.

Consequently the inverse-orbit partition is the COARSEST state partition preserving all these returns: floor(r/2)+1 classes are necessary and sufficient. More generally, the matrix of returns for representative distances 0..floor(r/2) at times 0..floor(r/2) is triangular with positive diagonal. Its rank is floor(r/2)+1. An exact linear-state realization for all initial masses and this continuation language needs at least that dimension, even over Q.

This is NOT a lower bound for all order-finding algorithms, all nonlinear encodings, baby-step/giant-step, or factorization. In particular, the fixed ordered dyadic suffix is a WEAKER language than arbitrary repetition of T_a; it is not ruled out by this theorem.

## 4. Two explicit information-loss witnesses

### Total mass plus current K is insufficient

Modulo 7, with a=3, compare c1=delta_3+delta_5 and c2=delta_2+delta_4. Both are inversion-symmetric, have total mass 2 and current identity coefficient 0. After T_3 their identity coefficients are 2 and 0. Thus (total mass, current K) is not a state closed under future updates.

### Oriented or biased updates invalidate the merge

The states 3 and 5 are inverses modulo 7. The +3 atom sends them to 2 and 1, which belong to different inverse orbits. The unchanged BRC checker also rejects the inverse partition for weights +:2 and -:1 on this population. A symmetric combined kernel is not an atomwise certificate.

## 5. Fixed terminal-only observation remains a constructive research direction

For a fixed remaining sequence g_j,...,g_(m-1), define the exact backward response

    h_m(u) = 1_(u=e),
    h_j(u) = 2h_(j+1)(u) + h_(j+1)(u*g_j) + h_(j+1)(u*g_j^-1).

Then final K=sum_u c_j(u)h_j(u). At that CUT, equality of h_j is the coarsest state partition preserving only this terminal linear functional for arbitrary c_j. This is not automatically a stepwise lumpable partition, nor a cheap way to compute h_j.

The difference is real: for r=4 and a two-step dyadic window Q=4, the terminal kernel has coefficient 4 at all four group states. Only that final observer needs one class, whereas the arbitrary-repetition language requires three inverse classes.

The useful next mathematical unit is an exact, cheaply constructible arithmetic description of these fixed-suffix response classes, without supplying an unknown order or paying full subgroup-enumeration cost first. Merely renaming h_j as a scalar state does not solve its construction cost.

## 6. Local validation and measured costs

Local environment: Python 3.13.5, Linux x86_64, sparse source checkout. The original BRC mass checker and original POWER reference were hash-verified. No full EM/POWER repository test suite was run.

- 25 targeted pytest tests passed, including exact pair-count definitions, all-prefix masses, self-inverse classes, unsafe biased/atomwise use, invalid input and explicit budget state.
- 588 default-window comparisons with the unchanged POWER generator all matched K, order and support.
- 2,940 explicit-window comparisons with unchanged POWER all matched K and support.
- The minimal partition / triangular rank witness was checked for every r=1..100.
- A matched full-support implementation with the same identity-tail shortcut also matched all 588 default cases.

Raw, machine-readable measurements and reproduction entrypoint: `results.json`, `validate.py` in this directory. Timing is a median of three calls; tracemalloc runs separately and measures Python allocations, not process RSS. These are small single-host measurements, not asymptotic performance proof.

| n, a | r -> inverse classes | Original peak bytes -> quotient | Original ms / quotient ms / lightweight full+tail ms |
|---|---:|---:|---:|
| 1009, 11 | 1008 -> 505 | 219040 -> 164928 | 5.218 / 4.907 / 3.900 |
| 10007, 5 | 10006 -> 5004 | 2139288 -> 1679084 | 60.748 / 62.181 / 54.902 |
| 65537, 3 | 65536 -> 32769 | 15176964 -> 10602252 | 540.930 / 58.237 / 51.741 |

Interpretation: key count is almost halved, but storing both inverse residues means RAM is NOT halved. Peak traced allocation fell about 21.5%-30.1% against unchanged POWER; against the lightweight full+tail baseline, only about 8.9%-17.3%. The quotient was about 12.6%-25.8% SLOWER than that lightweight baseline in these three runs. The large speed difference against unchanged POWER for the 2-power-order example is mainly avoidable identity-tail work, not a generic Shor-like speedup.

These larger benchmark moduli are prime and were chosen to inspect subgroup-state costs, not to demonstrate composite factorization; correctness tests also include composite moduli. Neither an RSA-270 run nor any RSA factorization breakthrough is claimed.

## 7. Bit-cost and admission boundary

With B=bit_length(n), stored residues take O(B) bits and masses take O(m) bits. The generic saturated computation remains O(m*r) row updates up to constants, with modular-multiplication and mass-addition bit costs still present. State storage remains O(r*(B+m)) bits. A halving of coefficient slots does not produce polynomial time in log(n).

The mathematical ingredients are ordinary group symmetry / lumpability, finite path counting and linear observation rank. Broader primary-source context: C.Y. Amy Pang, *Lumpings of Algebraic Markov Chains arise from Subquotients*, arXiv:1508.01570v3 (2018). That general literature is acknowledged; this return claims a concrete scoped EM/POWER specialization, implementation, falsifiers and measurements, not historical priority.

## Reproduction

    PYTHONPATH=src pytest -q tests/test_group_ring_inverse_quotient.py
    PYTHONPATH=src python research_notes/power_collision_inverse_20260921_16243626C61A/validate.py --power-source /path/to/frozen/group_ring_order.py --out results.json

The reference path must have the pinned POWER Git blob above. Dependency `brc_control_mass.py` must match the pinned existing EM blob. Source/test hashes are in `MANIFEST.json`. An accompanying Git bundle preserves the sparse execution environment and initial prototype history. Persistence on main is provenance only; independent review, Lean and Foundation admission have not occurred.
