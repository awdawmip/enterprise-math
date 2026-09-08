# PCF7 fixed-probe zero-value statement correction — Independent Replication Review

Status: `REPLICATION COMPLETE / DRIVER HANDOFF`

Researcher-ID: `EM-PCF7FIX-B7C214`  
Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`  
Publication-ID: `TP2-C4DB35B43FE7334D2B63`  
Claim-ID: `CLAIM-PCF7FIX-20260906T0632Z-CHATGPT-03`  
Execution base: `326b7d51a840e184e3fe650ad59f694fcbe66c4d`

Replicated durable frontier: PR `#1137`, frozen Result `RR-87B7B98EEFD0D8525BEC`.

Hard target retained:

`PCF7_FIXED_PROBE_ZERO_VALUE_STATEMENT_CORRECTED_WITH_MAIN_THEOREM_PRESERVED`.

## 1. Verdict

The correction in PR #1137 is mathematically exact at the authorized maintenance scope.

There is exactly one zero fixed probe in the frozen `s=0,...,63` domain:

`|1^6-1|=0`.

For that branch,

`gcd(N,0)=N`,

not `1`.

For every nonzero fixed probe whose prime support is avoided by both hidden primes `p,q`,

`gcd(pq,a)=1`.

Therefore every fixed-probe output is trivial — either `1` or `N` — and no proper factor is returned.

No theorem-changing mismatch was found in PR #1137 / `RR-87B7B98EEFD0D8525BEC`.

## 2. BRC information-loss diagnosis

This local prose defect is a direct BRC-style observer failure.

The frozen population has `256` probe instances: four fixed probe families for each of `64` seeds. Their branch identity is

`(family, seed, exact integer value)`.

The original support argument compresses the nonzero probe values to their prime-support union/product. That observer is adequate for a branch with `a != 0`, because avoidance of the support implies neither hidden prime divides `a`.

It is **not** adequate for the branch `a=0`.

A zero integer does not have a finite prime-support payload usable in that product, so dropping zero before support construction erases the exact branch identity. If one then forgets that a zero branch existed, the invalid conclusion “all fixed-family gcds are 1” follows.

The minimal repair coordinate is simply:

`ZERO_FLAG(a) = [a=0]`.

After retaining it, the observer factors correctly:

- `a != 0` + hidden primes avoid support(`a`) -> `gcd(N,a)=1`;
- `a = 0` -> `gcd(N,a)=N`.

Neither branch yields `1<d<N`.

BRC resolution: `REUSE_APPLIED`.

## 3. Exact zero-probe census

For every nonnegative integer seed `s` in the frozen range:

- `s^2+1 > 0`;
- `s^2+s+1 > 0`;
- `s^6+1 > 0`;
- `|s^6-1|=0` iff `s^6=1`, hence iff `s=1`.

Thus among `64*4=256` probe instances:

- zero probes = `1`;
- nonzero probes = `255`.

The unique zero instance is the sixth-minus-one family at `s=1`.

## 4. Independent finite witness

Use the balanced primes

`p=10007`, `q=10009`,

so

`N=pq=100160063`.

An independent exact check verifies that neither `p` nor `q` divides any of the `255` nonzero frozen probe values. Consequently all `255` nonzero probe gcds equal `1`.

For the unique zero probe:

`gcd(100160063,0)=100160063=N`.

Therefore the full fixed family returns no proper factor on this witness.

This validates the corrected local conclusion without altering any polynomial-prefix theorem.

## 5. Existing checker semantics

The existing load-bearing checker remains byte-correct and must not be modified merely to match prose:

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Git blob:

`sha1:b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`.

Its semantics already distinguish the branches:

1. `fixed_probe_values()` removes zero values only from the finite prime-support construction;
2. the final fixed-probe loop executes the `gcd(N2,v)==1` assertion only under `if v`;
3. hence it never asserts `gcd(N,0)=1`.

The new independent checker additionally makes the zero branch explicit and replays the unchanged source checker:

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_STATEMENT_CORRECTION_REPLICATION_CHECK_20260906.py`.

## 6. Mathematical delta boundary

The only accepted mathematical delta is the sentence-level distinction:

**Before (incorrect):** avoiding the prime support of the nonzero fixed probes was described as making every fixed-family gcd equal to `1`.

**After (correct):** nonzero avoided-support probes give gcd `1`; a zero probe gives gcd `N`; both are trivial and no proper factor is returned.

Unchanged:

- PCF7 Theorem 6.1 / polynomial-prefix infinite balanced-semiprime obstruction;
- exact worst-case proper-split probability `0` for that declared polynomial-prefix campaign model;
- `L=N` recurrence-stage classification;
- T1–T5 at their already-frozen no-proper-factor strength;
- sealed PCF2 benchmark boundary;
- no universal factoring lower-bound claim;
- no generic factorization speedup claim.

## 7. Promotion guards

This replication does not create or support:

- a new factoring algorithm;
- a complexity lower bound for general factoring;
- a new benchmark claim;
- a novelty claim;
- Working Truth or Foundation promotion;
- canonical promotion.

It is an exact local statement repair only.

## 8. Driver recommendation

Replication verdict:

`PASS / REPRODUCED_EXACT_LOCAL_CORRECTION`.

Driver may accept PR #1137 / Result `RR-87B7B98EEFD0D8525BEC` at the exact local statement-repair strength. Do not widen the disposition into a new factoring theorem, lower bound, benchmark result, or promotion claim.
