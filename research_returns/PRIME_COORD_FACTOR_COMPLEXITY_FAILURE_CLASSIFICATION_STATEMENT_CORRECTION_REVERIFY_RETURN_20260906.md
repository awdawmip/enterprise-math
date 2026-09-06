# PCF7 fixed-probe zero-value statement correction — independent re-verification return

Status: `FROZEN / HANDOFF_READY`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`  
Publication-ID: `TP2-C4DB35B43FE7334D2B63`  
Researcher-ID: `EM-PCF7FIX-5C2A91`  
Claim-ID: `CLAIM-PCF7FIX-20260906T0628Z-CHATGPT-01`  
Execution record: `ER-6E5D46858E71F8F5AC31`

## 1. Verdict

`SUCCESS / INDEPENDENT_REVERIFY / EXACT_LOCAL_STATEMENT_CORRECTION`

Hard target:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`

is satisfied at the maintenance scope of the immutable task publication.

This run does **not** claim a new factorization theorem, lower bound, benchmark result, novelty result, Working Truth, Foundation consequence, or canonical promotion. It independently verifies the already-prepared correction in PR #1137 / Result `RR-87B7B98EEFD0D8525BEC` and freezes a fresh evidence envelope under the present claim.

## 2. Exact correction

The only mathematical correction is:

- if a fixed probe value `a != 0` and both hidden primes avoid the prime support of `a`, then `gcd(N,a)=1`;
- if `a=0`, then `gcd(N,0)=N`;
- hence on the support-avoiding semiprimes every frozen fixed-probe output lies in `{1,N}`, so no proper factor is returned.

For seeds `s=0,...,63`, the unique zero-valued frozen probe is

`|1^6-1|=0`.

The quadratic probes `s^2+1`, `s^2+s+1`, and the positive sixth-power probe `s^6+1` are never zero on this seed range.

## 3. BRC observer audit

The relevant BRC carrier is the **labeled exact probe family**, not merely its nonzero prime-support product.

Population:
`256` labeled probes, with seed and probe type retained.

Carrier:
the exact integer value `a` together with its provenance `(seed, probe type)`.

Observer:
`a -> gcd(N,a)` followed by the proper-factor predicate `1 < gcd(N,a) < N`.

The compression

`C* = product of |a| over nonzero frozen probes`

is sufficient to encode the prime support of the **nonzero** branches, but it erases zero-valued branches entirely. The concrete information-loss witness is the labeled branch

`(s=1, |s^6-1|) -> 0`.

Therefore the original phrase “outside `supp(C*)`, every gcd is 1” did not factor through the compressed observer. The minimal repair is to preserve the zero/nonzero branch identity through the gcd observation. With that repair:

`nonzero avoided-support branch -> gcd 1`

and

`zero branch -> gcd N`.

BRC resolution: `REUSE_APPLIED`. No new BRC family or tool is introduced.

## 4. Fresh deterministic checker replay

The existing checker remains byte-correct:

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Git-blob SHA-1:

`sha1:b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`

SHA-256:

`sha256:8a878f62fd213177036d14704dcd4efd19cad5b7e6f40dd96f3f91531b3492d9`

Fresh replay output in this execution:

`PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

For the fixed-probe witness

`p=10007`, `q=10009`, `N=100160063`,

the unique zero branch gives

`gcd(100160063,0)=100160063=N`.

The checker already excludes zero from the nonzero support product and asserts `gcd=1` only when the probe value is nonzero, so **no checker byte change is authorized or needed**.

## 5. Before/after statement audit

Before:

`p,q outside supp(C*) => every fixed-family gcd = 1`.

After:

`p,q outside supp(C*) => every nonzero fixed probe gives gcd 1; every zero fixed probe gives gcd N; therefore every output is trivial and no proper factor is returned`.

`MATHEMATICAL_DELTA = ONLY_FIXED_PROBE_ZERO_VALUE_STATEMENT`.

## 6. Frozen unchanged boundaries

Unchanged:

1. PCF7 Theorem 6.1 and its infinite balanced polynomial-prefix obstruction;
2. exact worst-case proper-split probability `0` for the declared polynomial-prefix campaign model;
3. the `L=N` term-by-term recurrence classification;
4. T1–T5 at no-proper-factor strength;
5. the sealed PCF2 benchmark boundary and all 89-case values;
6. the guards against a generic factoring speedup or universal factoring lower bound;
7. all novelty, Working Truth, Foundation and canonical-promotion boundaries.

## 7. Evidence and handoff

Fresh certificate:

`research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_STATEMENT_CORRECTION/PCF7_FIXED_PROBE_ZERO_VALUE_BRC_REVERIFY_20260906.json`

Fresh execution record:

`research_execution_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION/ER-6E5D46858E71F8F5AC31.json`

The earlier PR #1137 correction is mathematically consistent with this independent replay. No broader mathematical change is required.

Unresolved residue within the Researcher maintenance scope:

`NONE`.

Next control-plane action remains Driver review at **local statement-repair strength only**.
