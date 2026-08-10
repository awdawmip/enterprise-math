# R005-C Internal Prime Capability Packet

Task: `RS-R005-INTERNAL-PRIME-TOOLKIT-HARVEST`  
Audited canonical snapshot: `main@4b0782e76fe2ac6ac263d324373ab1d3974007de`  
Execution mode: internal harvest/toolization only; no new prime theorem developed.

> Repository note: `research_tasks/R005C_INTERNAL_PRIME_TOOLKIT_HARVEST_20260810.md` was not present on the audited `main`. The formal task text supplied by the user is therefore the execution authority for this harvest; no replacement taskbook was created.

## Answer

Enterprise Math already has a reusable prime capability layer, but it is not one homogeneous theorem family. The stable core is:

1. classical bounded exact primality and prime enumeration baselines;
2. exact least-prime-factor / visible-factor witnesses;
3. square-basin factor precision, first-factor shells, minimal survivor-prime horizon, and proof slack;
4. exact P017 direct/Möbius/carry/binary-carry square-basin prime-count identities;
5. bounded centered-prime/slack coordinate conversion under its explicit size hypothesis;
6. canonical P018/P023 one-step power-free semantic action basis;
7. a provenance/status registry that prevents WIP and classical baselines from being silently promoted.

The important negative result of the harvest is equally concrete: the prime primitive-generator / Omega-word / prime-support compiler family is not yet canonical. It lives on Draft #333 and must not be confused with the merged #249 power-free one-step action basis. Separately, the divisor-token route belongs to the P017/P018 owner-local Drafts #191/#170, not to #333. R005-A experiments on Draft #364 are capability probes, not theorem owners or canonical prime infrastructure.

## Public callable surface

`enterprise_math.prime_toolkit` exposes only thin owner adapters:

- `bounded_primality(n)` — classical exact bounded baseline;
- `bounded_prime_enumeration(limit)` — classical exact bounded prime list;
- `least_factor_witness(n)` — least prime divisor, with an explicit warning when a prime returns itself;
- `least_visible_factor(n, cutoff)` — compatible least-visible factor (`0` means unresolved, not prime);
- `first_factor_shell(k, prime)` — exact first-factor shell in the consecutive-square basin;
- `proof_factor_horizon(k)` — exact minimal survivor-prime horizon plus slack, explicitly marked a-posteriori;
- `square_basin_certificate(k)` — cross-normalized direct/Möbius/carry/binary-carry exact count;
- `centered_prime_slack_coordinates(k)` — conditional centered-prime/slack conversion preserving the owner size hypothesis;
- `power_free_action_basis(N, r)` — merged #249 one-step semantic basis, explicitly distinguished from Draft #333 prime instruction compilation;
- `list_methods(...)` / `method_record(...)` — machine-readable provenance/status queries.

Every mathematical call returns `PrimeToolResult`, carrying `method_id`, source status, mathematical status, toolization status, exactness, source refs, normalized value, and any semantic warning. Entering the toolkit therefore does not upgrade theorem status.

## Canonical versus WIP

### Canonical / callable now

- P017 square-basin Möbius/carry executable line: owner PR #12.
- P018 factor precision / least-visible-factor / first-factor-shell / survivor horizon line: owner PRs #40, #49, #51 and current regression surfaces.
- P018 centered-prime-radius executable layer: owner integration PR #270, with the size-hypothesis counterexample retained as a regression boundary.
- P018/P023 power-free one-step action basis: merged owner PR #249, current Python regression present.

The #249 owner PR historically included a Lean proof path, but that old path was not present on the audited main. R005-C therefore does **not** label this `LEAN_CHECKED_MAIN`; it records the historical proof provenance separately from current-main executable status.

### Canonical code, not promoted by this facade

- `legendre.py` anchor-transfer helpers are present on main, but the precise introduction-owner commit and a dedicated current regression surface were not pinned during this harvest.
- `prime_gap_slack.py` is canonical and consumed by centered-radius code; historical provenance #54 says the Stage-7 code/regression was already canonical before #270. Exact introduction provenance remains an audit item.

Both remain registry-visible as `NEEDS_AUDIT` rather than being opportunistically publicized.

### WIP / application-local only

- Draft #333: prime primitive generator basis, Omega-word compiler, prime-support quotient-word compilation. These are a second-layer instruction compiler, not a replacement statement for #249.
- Draft #191 + Draft #170: CG12 arbitrary composite-divisor signed capacity plus exact Bonferroni-defect → squarefree/full-block divisor-token interface. This is an owner-local P017/P018 WIP route and is registry-visible, but it is not executable from the Prime Toolkit.
- No standalone `centered-prime compiler` API was recovered. The canonical centered-prime result is a coordinate converter; R005-C does not relabel it as a compiler.
- Draft #241: P025 arithmetic-Wronskian witness-budget specialization. Exact within owner hypotheses, application-local and noncanonical.
- Draft #364: R005-A bounded oracle/benchmark and `WitnessCover.lean` skeleton. Capability evidence only; no general coverage/existence theorem.
- Historical quotient-root denominator-fiber concept: no auditable current-main symbol was recovered under that name, so it remains `NEEDS_AUDIT` rather than being guessed into an API.

## Semantics guarded by the facade

Three misuses are now mechanically harder:

1. `least_visible_factor(...)=0` is unresolved, never a primality certificate.
2. `proof_factor_horizon(k)` is the exact minimal cutoff found from the actual basin composite classification; it is not an independent ex-ante bound that proves Legendre-type existence.
3. centered radius equals slack+1 only in the owner theorem range. The existing `k=10` counterexample to the over-strong global identity remains part of the regression boundary.

No confirmed `TOOLIZATION_EXPOSED_SEMANTIC_BUG` was found in the selected callable owner surfaces. Representation differences and theorem preconditions were normalized/warned rather than relabeled as bugs.

## INTERNAL PRIME CAPABILITY PACKET for R005-A

### Already available internally

Use the toolkit rather than rebuilding experiment-local versions for:

- bounded exact primality / bounded prime enumeration;
- least prime divisor and cutoff-visible factor witness;
- exact square-basin first-factor shells;
- exact minimal basin factor horizon and slack diagnostics;
- exact square-basin direct/Möbius/carry/binary-carry count cross-check;
- centered-prime/slack coordinates when the size hypothesis is satisfied;
- bounded one-step quotient-root semantic action basis via r-power-free integers;
- status/provenance discovery for noncanonical prime compiler and divisor-token WIP layers.

### Canonical status boundary

Canonical executable status belongs to the merged main owner surfaces above. Draft #333, #191/#170, and #364 remain WIP even where their tests or proof artifacts are useful. R005-A should consume their registry status, not import their implementations as if they were main.

### Obvious traditional capability gaps

The current internal classical baseline is intentionally small-scale. The most visible missing infrastructure is a robust, status-preserving exact factor-oracle backend for larger bounded integers. Prime enumeration is likewise correct but not a high-throughput segmented sieve. These are infrastructure gaps, not missing Enterprise Math theorems.

### Highest-value external reseed candidate

Priority 1 is an audited classical factor-witness backend combining a deterministic bounded primality decision with practical nontrivial-factor discovery and explicit certification semantics. It should sit behind the same facade status schema and remain labeled `CLASSICAL_BASELINE`. R005-C does not select or import an external implementation because Deep Research is disabled and external prior-art/tool audit belongs to R005-A's external-seeding work.

Secondary candidates are a segmented prime enumerator and restoration/relocation of a current-main Lean bridge for the #249 action-basis theorem if its historical proof has been conserved elsewhere.

## Files

- `src/enterprise_math/prime_method_inventory.json` — machine-readable inventory and centralized `proposal_candidates`.
- `src/enterprise_math/prime_toolkit.py` — thin status-preserving facade/registry.
- `tests/test_prime_toolkit.py` — focused adapter/status regressions.
- this packet — handoff to R005-A and future researchers.

No theorem-owner implementation was copied, no new taskbook was generated, and no WIP branch implementation was imported into main.
