# Prime Coordinate Factor Information-Leakage Audit — Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT`  
Publication-ID: `TP2-FFE7E8757053C4F4030A`  
Researcher-ID: `EM-PCF1-FC7357`  
Claim-ID: `chatgpt-pcf1-20260827-1605`

## Verdict

`AUDIT_COMPLETE_WITH_ADMISSIBLE_SET`

Hard target `PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_COMPLETE` is met at research-return strength.

All 15 whitelisted route entries were classified. The exact program boundary is:

- prime-indexed BRC objects are not admissible constructors for an unfactored composite input;
- Prime Fusion has exact gcd decoders, but its source cell/root/idempotent guarantees depend on data that already encode the channel split;
- a nontrivial idempotent modulo the target is equivalent to a nontrivial coprime split, so it must be generated rather than supplied;
- fixed public Prime Fusion polynomial probes remain admissible N-blind baselines, but uniform-seed support is fixed-degree and square-root-scale on balanced semiprimes;
- packet/path, relational-axis, invariant-shell, prime-wall and local-filament data are admissible only when their complete construction is factor-blind and all support cost is charged.

The missing program object is frozen as `N_ONLY_ASYMMETRY_GENERATOR`.

## Artifacts

- `research_artifacts/PCF1_information_leakage_audit/audit_bundle.json`
- `research_artifacts/PCF1_information_leakage_audit/downstream_gate.json`
- `research_artifacts/PCF1_information_leakage_audit/EVIDENCE_REPORT.md`
- `scripts/check_pcf1_information_leakage_audit.py`

Authoring-time checker result:

`PCF1_AUDIT_CHECK_PASS routes=15 idempotent_H<=250 probe_primes<=43 H91=PASS`

PCF1 can release its dependency for the sealed benchmark, hidden-factor separation spectrum, N-native p-adic-to-GCD bridge and Prime Fusion N-blind realization. Critical-cofactor support compression retains its separately published all-m dependency.

This return claims no factorization speedup and no lower bound. It closes only the frozen information-leakage/input-model audit.
