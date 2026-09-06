# PCF7 complexity/failure classification — Driver revision closure return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication-ID: `TP2-8F7443BCAF2BC5243574`  
Researcher-ID: `EM-PCF7-4D82A1`  
Claim-ID: `chatgpt-pcf7-complexity-revision-20260906-1517-4d82a1`  
Execution record: `ER-B0D034F578B4FA13B70B`  
Dispatch source: `control_plane/chatgpt_dispatch_receipt.json` / `chatgpt-20260906-1508-task-research-claim-v1`

## 1. Terminal verdict

`SUCCESS / DRIVER_REVISION_MATHEMATICALLY_CLOSED`

The only mathematical defect identified by Driver review `DR-8183213860B7A72A2BD3`
has been repaired at its exact authorized boundary.

The parent PCF7 conclusions remain unchanged:

- `SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED` for the frozen public polynomial-prefix campaign model;
- `SQRT_SCALE_OR_WORSE_PROVED` for the concrete `L=N` lift under the frozen recurrence implementation;
- frozen fixed public probe families remain `BENCHMARK_BASELINE_ONLY`;
- portfolio status remains `COMPLEXITY_FRONTIER_FROZEN`;
- no generic factorization speedup, universal factoring lower bound, Working Truth,
  Foundation consequence, or canonical-promotion claim is introduced.

## 2. Exact before/after statement

### Before — rejected wording

Section 7 compressed the frozen fixed probes to the product of all **nonzero** probe
integers, chose hidden primes outside that finite prime support, and then concluded
that every fixed-family gcd is `1`.

That final sentence is false for the zero probe.

### After — corrected wording

Let `a` be any frozen fixed probe value.

- If `a != 0` and both hidden primes `p,q` avoid the prime support of `a`, then
  `gcd(pq,a)=1`.
- If `a=0`, then `gcd(pq,0)=pq=N`.

Therefore every fixed-probe output on the avoided-support semiprime family is
trivial, in `{1,N}`, and **no proper factor** `1<d<N` is returned.

This is the complete mathematical delta.

## 3. Exact proof

For the frozen seed range `s=0,...,63`, the four public probe integers are

`a1=s^2+1`, `a2=s^2+s+1`, `a3=|s^6-1|`, `a4=s^6+1`.

There are `64*4=256` labeled probe instances.

On nonnegative integer seeds,

- `s^2+1 > 0`;
- `s^2+s+1 > 0`;
- `s^6+1 > 0`;
- `|s^6-1|=0` iff `s=1`.

Hence there are exactly `255` nonzero probe instances and exactly one zero
instance, `|1^6-1|=0`.

Let `C*` be the product of the absolute values of all 255 nonzero frozen probe
integers. Choose primes `p,q` outside the finite prime support of `C*`, and set
`N=pq`. For every nonzero frozen probe `a`, neither `p` nor `q` divides `a`, so
`gcd(N,a)=1`. For the unique zero probe, `gcd(N,0)=N`. Thus no probe produces a
proper divisor.

Because the excluded prime set is finite, infinitely many choices of hidden primes
remain. The existing balanced-semiprime construction can therefore be retained
without changing the main PCF7 obstruction.

## 4. Deterministic replay and concrete witness

The existing checker was intentionally **not modified**.

Bound checker:

- path: `research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`
- Git blob SHA-1: `sha1:b2a53c365f442fb2915cd869b77b62d9ce8a9ec8`
- SHA-256: `sha256:8a878f62fd213177036d14704dcd4efd19cad5b7e6f40dd96f3f91531b3492d9`

Fresh exact replay:

`PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

The checker's fixed-support construction already excludes zero only from the
prime-support product and asserts `gcd=1` only under `if v:`. Its bytes therefore
already encode the correct nonzero branch semantics.

For the checker witness

`N=10007*10009=100160063`,

the corrected local values include

- `s=0`: `|s^6-1|=1`, gcd `1`;
- `s=1`: `|s^6-1|=0`, gcd `N=100160063`;
- `s=2`: `|s^6-1|=63`, gcd `1`.

The complete 255-nonzero/1-zero census is independently reproduced by PR `#1298`.

## 5. Evidence chain and why no third maintenance theorem is created

This parent revision closes by integrating already-frozen maintenance evidence
rather than manufacturing a third mathematical variant:

1. predecessor Result: `RR-A9A5ADD3931B3F3EDFAB`;
2. Driver disposition: `REQUEST_REVISION / NARROW EXACT-STATEMENT CORRECTION`;
3. maintenance publication: `TP2-C4DB35B43FE7334D2B63`;
4. original correction: PR `#1137`, Result `RR-87B7B98EEFD0D8525BEC`;
5. same-day fresh re-verification: Result `RR-B379539A0F286A7509E2` on
   `ed751fe7fd8ddbab1a85313bd098f94c6d20d29d`;
6. independent replication: PR `#1298` at
   `fa787241802ad4ad90d29d089e5a0665ec66916d`.

The present Result belongs to the **parent task** because the canonical dispatcher
explicitly returned this parent publication under the unresolved Driver disposition.
It does not supersede or rewrite the immutable child evidence.

## 6. BRC observer audit

The defect can be stated as a minimal BRC information-loss error.

The coarse observer `C* = product(nonzero probe values)` retains enough information
to prove `gcd(N,a)=1` for nonzero probes whose prime support is avoided, but it
erases whether a labeled probe was exactly zero. The minimal repair coordinate is

`ZERO_FLAG(a) = [a=0]`.

Keeping this one-bit branch coordinate restores the exact two-branch statement:
nonzero avoided-support probe -> `1`; zero probe -> `N`.

No stronger theorem follows from this observer repair.

## 7. Preserved boundaries

Unchanged byte-for-byte or theorem-for-theorem:

- Theorem 6.1 polynomial-prefix infinite balanced-family obstruction;
- exact worst-case proper-split probability `0` for that declared campaign model;
- `L=N` recurrence-stage and bit-complexity classification;
- T1–T5 at their accepted no-proper-factor strength;
- sealed PCF2 benchmark counts;
- all guards against a universal factorization lower bound;
- all guards against claiming a new factorization speedup.

No benchmark suite was rerun and no candidate algorithm was enlarged.

## 8. Hard-target disposition

`FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED / DRIVER_REVISION_CLOSED_AT_EXACT_FIXED_PROBE_ZERO_VALUE_BOUNDARY`

Unresolved residue:

`NONE_WITHIN_AUTHORIZED_REVISION_SCOPE; DRIVER_REVIEW_AND_CONTROL_INTEGRATION_ONLY`

Recommended next control action:

Driver review this fresh parent revision Result against `DR-8183213860B7A72A2BD3`.
If accepted, retain the original PCF7 complexity/failure classifications with only
the fixed-probe sentence repaired to the exact `{1,N}` trivial-output statement.
