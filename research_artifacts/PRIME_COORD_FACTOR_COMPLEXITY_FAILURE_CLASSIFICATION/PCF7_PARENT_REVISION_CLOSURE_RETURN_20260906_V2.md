# PCF7 complexity/failure classification — canonical Driver revision closure return V2

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication-ID: `TP2-8F7443BCAF2BC5243574`  
Researcher-ID: `EM-PCF7-283667`  
Claim-ID: `chatgpt-pcf7-20260906-1520-revision-v2`  
Execution record: `ER-586DD6A098AF43C3EFB1`  
Owner scope: existing post-UNBLOCK live claim on Issue #240, recovered after control-plane reopen fix PR #1319.

## 1. Verdict

`SUCCESS / DRIVER_REVISION_MATHEMATICALLY_CLOSED_AT_EXACT_ZERO_PROBE_BOUNDARY`

This return closes only the narrow mathematical defect identified by Driver review
`DR-8183213860B7A72A2BD3`. The original PCF7 theorem boundaries remain unchanged:

- polynomial-prefix exact worst-case proper-split probability remains `0` in the declared model;
- the concrete `L=N` recurrence remains `SQRT_SCALE_OR_WORSE_PROVED`;
- frozen fixed public probes remain `BENCHMARK_BASELINE_ONLY`;
- portfolio status remains `COMPLEXITY_FRONTIER_FROZEN`;
- no generic factoring speedup, universal factoring lower bound, Working Truth,
  Foundation consequence, or canonical promotion is asserted.

## 2. Exact correction

For the frozen seed range `s=0,...,63`, define the four labelled probe values

`a1=s^2+1`, `a2=s^2+s+1`, `a3=|s^6-1|`, `a4=s^6+1`.

There are exactly `256` labelled probes. Exactly one is zero:
`a3(1)=|1^6-1|=0`; the other `255` are nonzero.

Let `C*` be the product of the absolute values of those 255 nonzero probes.
Choose hidden primes `p,q` outside the finite prime support of `C*`, and put `N=pq`.

Then:

- for every nonzero frozen probe `a`, neither `p` nor `q` divides `a`, hence
  `gcd(N,a)=1`;
- for the unique zero probe, `gcd(N,0)=N`.

Therefore every fixed-probe output is trivial, in `{1,N}`, and no proper factor
`1<d<N` is produced. Since only finitely many prime divisors are excluded, infinitely
many hidden-prime choices remain; the balanced-semiprime obstruction used by PCF7
is unchanged.

This is the complete mathematical delta. The rejected sentence “every fixed-family
gcd is 1” is replaced by the exact statement “every fixed-family gcd is in `{1,N}`,
and no proper factor occurs.”

## 3. BRC audit

The original error is a one-bit observer collapse.

The coarse observer `C*=product(nonzero probes)` preserves nonzero prime-support
information but discards whether a labelled probe was exactly zero. The minimal
BRC repair coordinate is

`ZERO_FLAG(a)=[a=0]`.

Keeping that branch label yields the exact two-state collapse:

- `ZERO_FLAG=0` with avoided prime support -> gcd state `1`;
- `ZERO_FLAG=1` -> gcd state `N`.

Thus BRC does not create a stronger factor theorem here; it identifies precisely
which information was erased and why the corrected conclusion is “trivial output”
rather than “gcd 1 everywhere.”

## 4. Deterministic replay

The existing checker is intentionally unchanged:

- path: `research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`
- Git blob SHA-1: `sha1:b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`
- SHA-256: `sha256:8a878f62fd213177036d14704dcd4efd19cad5b7e6f40dd96f3f91531b3492d9`

Exact replay remains:

`PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

For the fixed-probe witness `N=10007*10009=100160063`:

- `s=0`: `|s^6-1|=1`, gcd `1`;
- `s=1`: `|s^6-1|=0`, gcd `N`;
- `s=2`: `|s^6-1|=63`, gcd `1`.

The checker already omits zero only from the support product and asserts `gcd=1`
only when the probe value is nonzero, so no checker-byte modification is required.

## 5. Independent evidence chain

The closure is corroborated by already-frozen maintenance evidence:

1. predecessor parent Result `RR-A9A5ADD3931B3F3EDFAB`;
2. Driver disposition `DR-8183213860B7A72A2BD3 / REQUEST_REVISION`;
3. correction publication `TP2-C4DB35B43FE7334D2B63`;
4. PR #1137 / Result `RR-87B7B98EEFD0D8525BEC`;
5. fresh re-verification Result `RR-B379539A0F286A7509E2` at
   `ed751fe7fd8ddbab1a85313bd098f94c6d20d29d`;
6. independent replication PR #1298 at
   `fa787241802ad4ad90d29d089e5a0665ec66916d`, checker workflow PASS.

These sources independently agree on the 255-nonzero/1-zero census and the
`{1,N}` no-proper-factor conclusion.

## 6. Preserved boundaries

Unchanged:

- Theorem 6.1 polynomial-prefix infinite balanced-family obstruction;
- exact worst-case proper-split probability `0` for that declared campaign model;
- `L=N` recurrence-stage / bit-complexity classification;
- T1–T5 at their accepted no-proper-factor strength;
- sealed PCF2 benchmark counts;
- all guards against a universal factoring lower bound;
- all guards against claiming a new factoring speedup.

No benchmark generation is rerun and no candidate algorithm is expanded.

## 7. Control disposition

Hard-target disposition:

`FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED / DRIVER_REVISION_CLOSED_AT_EXACT_FIXED_PROBE_ZERO_VALUE_BOUNDARY`

Unresolved residue:

`NONE_WITHIN_AUTHORIZED_REVISION_SCOPE; DRIVER_REVIEW_AND_CONTROL_INTEGRATION_ONLY`

Recommended next control action:

Driver review this fresh parent Result against `DR-8183213860B7A72A2BD3`. If
accepted, retain the original PCF7 conclusions with only the fixed-probe wording
repaired to the exact `{1,N}` trivial-output statement.
