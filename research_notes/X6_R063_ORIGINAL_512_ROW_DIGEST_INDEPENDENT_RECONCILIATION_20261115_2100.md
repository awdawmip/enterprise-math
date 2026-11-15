# X6 / R063 Stage0 — Independent exact reconstruction of the original 512-row regression digest

Date: 2026-11-15 (Research lane). Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; author `EM-X6-FB6990`. Classification: **AUTHOR-EXECUTED / EXACT 512-ROW CERTIFICATE / UNREVIEWED / NOT_ADMITTED**.

## Original immutable object and question

The original R063 sector-local, two-generator positive-chart benchmark used loader `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` at Git blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592` and five original `part00..04.inc` blobs on branch `research/r063-stage0-path-valued-sqrt-2500`. Its exact historical row generator is `part02.inc` blob `b543e185ec415b512c0ca0421616404cc12a19a7`. The preserved regression artifact is `research_results/R063_STAGE0/R063_STAGE0_GENERAL_SQUARE_REGRESSION.json` blob `0a5627760b960ac1a139b20eedea43664a0fb900`; it stores the digest while omitting the actual 512 row bodies.

Question: can an independently implemented arithmetic reconstruction, using the **actual frozen row schema and canonical JSON hashing**, reproduce **the exact original 512-row digest**, including C2 true/false outcomes, C3/C4 outcomes and each radius's norm-fibre SHA256, rather than checking only the root-count totals?

## Result and mathematical justification

For each integer `r=1,...,512`, set `N=r²` and independently generate four root sets of **ordered nonnegative two-component** integer pairs:

- Direct oracle: `D_N={(a,b): 0<=a,b<=r, a²+b²=N}`, using exact integer square root.
- C2, unscaled square lift: for `(m,n) in D_r` with `m>=n`, form `(m²-n²,2mn)` and both ordered orientations.
- C3, primitive Euclid: include the two axis roots, then for `m>n>=1`, `gcd(m,n)=1`, opposite parity, `h=m²+n² | r`, insert `(k(m²-n²),2kmn)` and its swap, `k=r/h`. Classical primitive triple parametrization proves complete coverage.
- C4, independent Gaussian-integer prime allocation: factor `N`; use `(1+i)^e` for ramified 2, scalar `p^{e/2}` for inert primes `p=3 (mod 4)`, and each allocation `π^k * conjugate(π)^{e-k}` for every split prime `p=1 (mod 4)`, with all four units, keeping the nonnegative quadrant. Each split prime representation `p=a²+b²` is found only at the **prime level**, not by consulting `D_N`. Unique Gaussian factorization proves complete coverage for represented N.

Then recreate for each radius the original row fields `r,N,brute_branch_count,C2_exact,C3_exact,C4_exact,fiber_sha256` with exact key spelling and the original `sha256(json.dumps(obj,sort_keys=True,separators=(',', ':'),ensure_ascii=False).encode('utf-8'))`. Every C3 and C4 root set was actually compared against the independently enumerated `D_N`, with assertions for all 512 cases.

**Observed full 512-row result:**

| Item | Independent result | Original archived value |
|---|---:|---:|
| Radii tested | 512 | 512 |
| C2 mismatched radii | 484 | 484 |
| First C2 mismatch | `r=3,N=9`; missing `(0,3),(3,0)` | Exact match |
| C3 mismatches | 0 | 0 |
| C4 mismatches | 0 | 0 |
| Ordered nonnegative root occurrences | 1,820 | Additional independent tally |

Root-count distribution by radius: 2 roots for 239 radii; 4 for 220; 6 for 18; 8 for 4; 10 for 29; 16 for 2.

The independently reconstructed **whole-row digest matches the archived source exactly**:

```text
51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae
```

This is a stronger original-object external arithmetic reconciliation than the earlier 512-root-count certificate: it includes the complete per-radius C2 classifications and the original hashed row structure. It is still an independent reconstruction, not a new run of the six frozen original loader/part source objects or original 17 gates.

## Reproduction and source preservation

Reproducible standalone checker: `research_checks/X6_R063_ORIGINAL_512_ROW_DIGEST_INDEPENDENT_RECONCILIATION_20261115_2100.py`. Its independent exact algorithm was executed locally, exit 0, and the reconstructed digest, C2 failure count, first mismatch and norm-fibre population matched the archived immutable values. The committed shorter checker keeps the same four construction routes and row encoder; its repository publication must not be mistaken for an original native runner's process log. Distinguish local executed algorithm evidence from executable-file byte-equivalence when those are not directly checked.

Frozen P000 scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03` and CURRENT ACTIVE six-axis spatial worldview remain unchanged; the old R063 two-positive-generator calculation is a declared historical **sector chart**, not full P000 signed six-axis Cell enumeration.

## Next actionable original acceptance

The original same-object support [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains the accountable route for the full original program execution: unchanged original loader and five `.inc` blobs, `--N 2500 --regression-max-r 512`, discovery snapshot persisted and hashed before brute verification, all 17 native gates and actual 512-row output hashes. Compare this independently reconstructed original row digest to the newly emitted original-row digest. Use lossless integer parsing of path mass and independently check the path polynomial coefficient semantics.

Additional unresolved mother obligations: actual historical LP011 native signed argmax erroneous caller, LP019 natural-positive N-BRC signed subtraction erroneous caller, full 28-LP current consumer closure and independent Driver `REQUEST_REVISION`. No unsupported caller attribution or formal acceptance is asserted. The separately denied 17:00 prose operation is not retried.

Native Source unit and Activity binding: **PENDING_AUTHORIZED_ASSOCIATION**; local and GitHub mathematical publication are not Source semantic PROGRESS by themselves.
