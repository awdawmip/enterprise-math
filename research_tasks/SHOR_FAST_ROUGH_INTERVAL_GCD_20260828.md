<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SHOR-FAST-ROUGH-INTERVAL-GCD",
  "title": "Shor bridge prime-sensitive FAST_ROUGH_INTERVAL_GCD",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "After B^2 small-factor clearing and the exact prime-sensitive LCM-jump/Mobius-factorial reduction, the only unresolved high-prime primitive is to compute gcd(d, product_{x<p<=y} p) for B^2-rough d and B^2<=x<y<=B^3 in B^(1+o(1)) time; independent harmonic-block evaluation costs B^(3/2+o(1)).",
  "next_action": "Exploit cross-block cancellation before generic consecutive-product evaluation, starting from the B-rough survivor product and factor-revealing rational Mobius-factorial representations; either obtain an exact deterministic B^(1+o(1)) interval-GCD algorithm or prove a rigorous obstruction for the frozen candidate models and isolate the smallest surviving primitive.",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SHOR-FAST-ROUGH-INTERVAL-GCD",
  "parent_objective_id": "OBJ-SHOR-DETERMINISTIC-N16-CLASSICAL-BRIDGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "identity_lane": "SHOR",
  "claim_lease_minutes": 240,
  "evidence_status": "EXACT_PRIME_SENSITIVE_REDUCTION / EXACT_MOBIUS_PROJECTOR / EXACT_MOBIUS_UNIQUENESS / INDEPENDENT_BLOCK_N14_BARRIER / B1_INTERVAL_GCD_OPEN",
  "last_progress_ref": "GLOBAL_KNOWLEDGE:7f7de8361475d989dcbbf2cf3816f0cef6c70e5e",
  "last_progress_at": "2026-08-28T10:27:55+08:00",
  "dependencies": [
    "research_runtime_state_machine.json@main",
    "research_task_publication_contract_v2.json@main",
    "research_taskbook_policy.json@main"
  ],
  "source_refs": [
    "GLOBAL_KNOWLEDGE:c302ce7b329d1251cd7325da7489c8a555361f47",
    "GLOBAL_KNOWLEDGE:2a9ee13e5a5372f82bc901b62f235dc4e46d2666",
    "GLOBAL_KNOWLEDGE:7f7de8361475d989dcbbf2cf3816f0cef6c70e5e"
  ],
  "tags": [
    "Shor bridge",
    "deterministic factoring",
    "N^(1/6)",
    "prime-sensitive packets",
    "LCM jump",
    "Mobius factorial projector",
    "rough interval gcd",
    "cross-block cancellation",
    "Strassen"
  ],
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Research Task — Shor bridge prime-sensitive FAST_ROUGH_INTERVAL_GCD

## Repository placement

- Suggested owner branch after a valid claim: `research/shor-fast-rough-interval-gcd`.
- Required return: `research_returns/SHOR_FAST_ROUGH_INTERVAL_GCD_RETURN_20260828.md`.
- Optional exact experiments/certificates: `artifacts/shor_fast_rough_interval_gcd/`.
- This task is self-contained at the mathematical frontier below. The global-knowledge source refs are provenance, not a requirement to reconstruct omitted lemmas.

## Mother question

Let `B>=2`, let `d` be an integer all of whose prime divisors exceed `B^2`, and let

\[
B^2\le x<y\le B^3.
\]

Can one deterministically compute

\[
\boxed{
G_B(x,y;d)
=
\gcd\!\left(d,\prod_{x<p\le y}p\right)
}
\]

in

\[
\boxed{B^{1+o(1)}}
\]

bit operations, uniformly for `d<=B^{O(1)}` (in the factoring application, `d<=B^6`), without being given the factorization of `d` and without enumerating all primes up to `B^3`?

A solution must be exact. A randomized or heuristic average-case speedup is useful evidence but is not the hard target.

If this primitive is achieved at the stated complexity, give the complete reduction showing how `B=N^{1/6+o(1)}` yields a deterministic `N^{1/6+o(1)}` factorization route after the standard small-factor clearing step. Do not claim the end-to-end exponent until every preprocessing, interval split, arithmetic operation, and output-recovery cost is included.

## Frozen inputs and scope

### A. Scale and low-factor clearing

Use the factoring scale

\[
N=B^6,
\qquad
\sqrt N=B^3.
\]

A deterministic Strassen/Pollard--Strassen small-factor routine may be used to remove all prime divisors `<=B^2` in `B^{1+o(1)}` time. After that step the current modulus `d` is `B^2`-rough. The present task starts at that boundary; it is not a task to reprove the classical small-factor routine.

For a remaining composite integer, some prime divisor is at most `sqrt(N)=B^3`. Therefore after the low layer has been cleared, locating factors in `(B^2,B^3]` is sufficient for the high layer.

### B. Prime-sensitive LCM-jump packet

Let

\[
L(n)=\operatorname{lcm}(1,\ldots,n),
\qquad
J_t=\frac{L(B(t+1))}{L(Bt)},
\qquad B\le t<B^2.
\]

For a width-`B` interval, `J_t` is squarefree as a product of prime bases whose prime powers first cross that interval. In particular

\[
P_t:=\prod_{Bt<p\le B(t+1)}p
\quad\text{divides}\quad J_t.
\]

The extra factors come only from higher prime-power jumps. Their total logarithmic mass over the high layer is lower order (`O(B^{3/2})`) compared with the prime mass `Theta(B^3)`.

The exact multiplicative telescope is

\[
\prod_{t=a}^{b}J_t
=
\frac{L(B(b+1))}{L(Ba)}.
\]

Do not assume that the natural additive difference of neighboring LCM prefixes preserves new high primes. It does not: if a new prime `p` enters at the upper prefix, then `p` divides the ratio but does not divide the ordinary prefix difference.

### C. GCD-only relaxation

For factor isolation, exact interval residues are stronger than necessary. The recursive split logic only needs

\[
\gcd\!\left(d,\prod_{i=a}^{b}A_i\right).
\]

Accordingly, the present task targets the GCD projector directly. It is not necessary to compute the enormous exact integer `L(y)/L(x)`, its full residue modulo `d`, or a full explicit prime list.

### D. Exact truncated Mobius--factorial projector

Define the rational quantity

\[
T_B(z)
=
\prod_{1\le k\le B}
\left(\left\lfloor\frac zk\right\rfloor !\right)^{\mu(k)},
\qquad z\le B^3.
\]

For every prime `p>B^2`, set `X=floor(z/p)`. Then `X<=B` and `p^2>z`, hence

\[
v_p(T_B(z))
=
\sum_{k\le X}\mu(k)\left\lfloor\frac Xk\right\rfloor
=
\mathbf 1_{X\ge1}
=
\mathbf 1_{p\le z}.
\]

Therefore for `x<y<=B^3`,

\[
\boxed{
 v_p\!\left(T_B(y)/T_B(x)\right)
 =
 \mathbf 1_{x<p\le y}
}
\qquad(p>B^2).
\]

After reducing the rational expression, every denominator prime is `<=B^2`; thus every denominator is a unit modulo a `B^2`-rough `d`. Consequently

\[
\gcd\!\left(d,T_B(y)/T_B(x)\right)
=
G_B(x,y;d)
\]

in the natural modular-rational sense.

### E. Mobius weights are forced in the harmonic-factorial ansatz

For

\[
R_c(z)
=
\prod_{1\le k\le B}
\left(\left\lfloor\frac zk\right\rfloor !\right)^{c_k},
\]

exact high-prime prefix projection requires

\[
\sum_{k\le X}c_k\left\lfloor\frac Xk\right\rfloor=1
\qquad(1\le X\le B).
\]

Taking first differences gives

\[
\sum_{k\mid X}c_k=[X=1],
\]

so Mobius inversion uniquely forces

\[
\boxed{c_k=\mu(k)}.
\]

Do not spend the task searching for a sparser coefficient vector inside this same harmonic-factorial basis unless a premise of the uniqueness argument is explicitly changed and justified.

### F. B-rough-survivor interpretation

For `p>B^2`, every multiple `jp<=B^3` has `j<=B`. Among integers `m<=B^3` satisfying `gcd(m,B!)=1`, the only multiple of `p` is `p` itself. Hence on a `B^2`-rough modulus the target is GCD-equivalent to

\[
\gcd\!\left(
 d,
 \prod_{\substack{x<m\le y\\\gcd(m,B!)=1}}m
\right).
\]

This is the second canonical representation to attack. It removes false hits `2p,...,Bp` by the small-cofactor sieve rather than by explicit primality recognition.

### G. Frozen square-root baseline / closed shortcut

Sharing the nested factorial prefixes gives a harmonic-block decomposition with block lengths on the order of

\[
\frac{z}{r(r+1)}.
\]

If consecutive blocks are evaluated independently by generic fast factorial/product or baby-step/giant-step machinery, the total cost is

\[
\widetilde O\!\left(
\sum_{r\le B}\sqrt{\frac{z}{r(r+1)}}
\right)
=
B^{3/2+o(1)}
\]

for `z=Theta(B^3)`, i.e. the `N^{1/4+o(1)}` scale. Treat this independent-block route as closed for the target exponent.

Likewise, do not reopen the previously closed universal-carrier routes (Pascal/Vandermonde low-degree collapse, generic CRT/LLL rank gain, ordinary digit relabeling, or an exact-LCM-ratio computation) unless a new theorem shows how they compute this smaller GCD primitive below the frozen baseline.

### H. Allowed research directions

The first two preferred interfaces are:

1. **Cross-block rough-survivor cancellation:** compute only the factor-relevant residue/GCD of the `B`-rough survivor product without explicitly producing every survivor or every harmonic block.
2. **Factor-revealing rational evaluation:** reorganize `T_B(y)/T_B(x)` so that a nonunit denominator/numerator intermediate immediately yields a nontrivial gcd, allowing early factor extraction without full factorial-channel evaluation.

Other methods are allowed if they solve the same exact primitive and their total complexity is proved. External literature on fast factorials, product trees, multipoint evaluation, combinatorial sieves, prime-counting/product algorithms, or deterministic factor detection may be used with exact citations and version/date.

### I. Forbidden hidden costs

A claimed `B^{1+o(1)}` algorithm fails the task if it hides any of the following:

- a precomputed list of all primes up to `B^3`;
- factoring `d` as an oracle;
- `Theta(B^2)` or larger packet materialization;
- `Theta(B^3)` candidate scanning;
- independent evaluation of `Theta(B)` long factorial blocks at aggregate `B^{3/2+o(1)}` cost;
- construction of intermediate integers with `Theta(B^3)` bits followed by arithmetic treated as unit cost;
- a quantum order-finding/QFT primitive;
- a conjectural distributional assumption promoted to a theorem.

All arithmetic-cost claims must specify the integer/modular bit lengths involved.

## Hard target and required outputs

### Outcome A — exact B^(1+o(1)) algorithm

Produce a deterministic algorithm that, for every legal `(B,d,x,y)`, returns exactly `G_B(x,y;d)` and prove total bit complexity `B^{1+o(1)}`. The proof must include preprocessing, all modular products/inversions, gcds, recursion, representation conversion, and factor-recovery costs.

Then give an end-to-end factoring reduction at scale `N=B^6` and state exactly which published classical ingredients are reused. The return must separate the newly proved primitive from inherited results.

### Outcome B — exact candidate-model obstruction

If Outcome A is not reached, a terminal negative result is accepted only if it proves a rigorous lower bound/no-go for a clearly frozen model that contains both canonical candidate implementations actually tested in this task, rather than merely reporting slow code. The obstruction must explain why cross-block cancellation cannot beat `B^{3/2-o(1)}` (or another proved bound) in that model and must identify a strictly smaller surviving primitive or additional arithmetic datum that escapes the proof.

A barrier for one narrow encoding alone is progress but not sufficient for the terminal negative outcome unless the other canonical interface is also classified.

### Required return

Write one terminal report to

`research_returns/SHOR_FAST_ROUGH_INTERVAL_GCD_RETURN_20260828.md`.

It must contain:

1. verdict `B1_ALGORITHM`, `EXACT_MODEL_BARRIER`, or `UNRESOLVED_EXACT_FRONTIER`;
2. complete algorithm/pseudocode or exact obstruction theorem;
3. proof of correctness for every `B^2`-rough modulus, including composite `d`;
4. full asymptotic bit-complexity ledger;
5. exact treatment of rational denominators and nonunit intermediate values;
6. reproducible finite tests sufficient to catch sign, floor, interval-endpoint, and denominator mistakes;
7. a section `Closed shortcuts respected` addressing the frozen dead ends above;
8. if unresolved, exactly one smallest remaining primitive with a proof that solving it suffices for `FAST_ROUGH_INTERVAL_GCD`.

Hard target state:

`FAST_ROUGH_INTERVAL_GCD_B1_ALGORITHM_OR_EXACT_CROSS_BLOCK_OBSTRUCTION`

## Research value to preserve

This task isolates the current prime-sensitive bottleneck after the Shor-to-local-clock reduction, smooth saturation, R2/R3 carrier audits, LCM-jump construction, and exact Mobius-factorial projection. It is substantially smaller than the higher-rank divisor-cover conjecture: the task asks only for factor-relevant interval GCD information on a `B^2`-rough modulus.

A `B^{1+o(1)}` solution would remove the present `B^{3/2+o(1)}` square-root barrier and, after a complete end-to-end audit, would be a candidate route to deterministic `N^{1/6+o(1)}` integer factorization. A rigorous obstruction is also high value because it would close the two strongest prime-sensitive representations currently known and prevent repeated attempts that merely disguise independent factorial-block evaluation.

## Success, kill, and return criteria

**SUCCESS-A:** an exact deterministic `B^{1+o(1)}` implementation and proof for `FAST_ROUGH_INTERVAL_GCD`, plus the complete factoring reduction and complexity audit.

**SUCCESS-B:** a rigorous obstruction covering both the rough-survivor and factor-revealing Mobius-factorial candidate models, with an explicit smaller surviving primitive outside the obstruction.

**KILL a candidate representation** immediately if an exact reduction shows that its best possible realization in the frozen model requires independent long-block evaluation, enumerates `B^{1+Omega(1)}` objects, or hides an equivalent factorization/prime-list oracle. Do not repair a killed representation by renaming the same operations.

**RETURN unresolved** if neither terminal outcome is proved. The unresolved return is still required to freeze the smallest remaining exact primitive, all failed constructions with proofs/certificates, and the strongest verified complexity upper/lower bounds. Do not claim `N^{1/6}` from finite experiments or from an oracle whose implementation remains open.

Task completion is terminal only for this task. It does not by itself declare the broader Shor/classical bridge objective complete.
