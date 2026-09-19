# PFSS2 second-order conditional-null return

Date: 2026-09-16
Researcher-ID: EM-PFSS2-71565A
Research-Activity-ID: RA-20260916-PFSS2-864f46b6e9f1
Task: RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL
Publication: TP2-D44C166C4C87CEC167E7
Taskbook Git blob: sha1:2d3fac6df6bd26aba8a4695346898150882e95de
Execution record: ER-6E7133A0CAAE69091AA7
Claim: PFSS2-20260916-864F46B6E9F1
Winning raw-JSON Issue 240 comment: 5696624508
Execution branch: research/pfss2-20260916-864f46b6e9f1

## Verdict and precise completion boundary

**NULL_MODEL_MISSPECIFICATION.** The frozen conditional null A is a point mass on every required observable at the first three discovery scales. The prescribed standardization divides zero by zero, so no discovery feature can honestly be selected and frozen. Both required null ensembles were nevertheless completed with 4096 replicates each, fully replayed, and independently audited. An exact two-shift witness proves a material A/B covariance mismatch without relying on Monte Carlo precision.

This is a completed task-scope diagnosis of the proposed test, NOT evidence that a new semiprime residual exists or is absent. It does not revise the parent negative result, establish a prime theorem, promote Working Truth, or constitute independent Driver acceptance. Registry terminal-verdict vocabulary: AUDIT_COMPLETE; mathematical/experimental classification: NULL_MODEL_MISSPECIFICATION.

The two reserved holdout scales, 300000000 and 1000000000, remain **UNOPENED**. They were neither enumerated nor used to choose parameters. No valid discovery freeze existed, so evaluating them could not complete the registered significance gate. They are preserved for a separately authorized redesign, not described as failed replications.

## Frozen design and source boundaries

The execution protocol was published before computational discovery at commit `4de8bf5f9ea4c14f4c653a52c4075551c65f38b7`, path `research_notes/pfss2_20260916_71565a/protocol.json`. It explicitly forbids a variance floor, a zero-over-zero convention, bin/scale deletion and surrogate replacement; an undefined discovery statistic triggers the misspecification branch before holdouts.

Discovery X = (1000000, 3000000, 10000000, 30000000, 100000000); widths = (1/100, 3/1000, 1/1000); 32 fixed bins. For each exact prime p with p^4>X and p^2<=U=floor(X*(d+a)/d), the nonsquare integer q interval is [max(p+1,floor(X/p)+1), floor(U/p)]. Prime squares are separately recorded. All eligible p channels, including zero-count channels, are retained. The coordinate is u=log(p)/log(X), xi=1+log(u/(1-u))/log(3), with bin=min(31,max(0,floor(32*xi))). The narrow upper-shell xi>1 overflow is folded into bin31 and separately reported; it does not affect the support obstruction.

A uses nonempty microcells [floor((1025/1024)^j), floor((1025/1024)^(j+1))). Within each cell and admissible residue modulo 210, it preserves the exact prime count and uniformly chooses that many available positions without replacement. B uses nonempty bands [210*floor((65/64)^j),210*floor((65/64)^(j+1))); it rotates the entire observed prime configuration by one uniformly selected multiple of 210. [0,210) is fixed. Integer endpoints are computed with exact powers, not floating boundary decisions. A and B each use one shared q-indicator per replicate for all scales and widths; overlap covariance is therefore retained, not replaced by independent bin noise.

R=4096. Replicate r uses MT19937 seed 2026091601+r for A and 2026091602+r for B; deterministic strata consume no draws. Means and unbiased variances use exact integer sums, sums of squares and numerator R*sum(x^2)-sum(x)^2, divided by R*(R-1). The required statistic is z=(O-mu)/sigma, C[eta,b]=sum_X z/sqrt(5), T=max over all 96 |C|. Undefined values remain undefined; the implementation never substitutes nanmax.

Reuse: the parent's `sieve_primes` function was copied unchanged and executed from `scripts/check_prime_factor_semiprime_shell_residual_validation.py` at source commit `27a06aa03dda082879863c0aa55c8caa623cef0d`. Parent permutation nulls, 24-bin design and its 1e-12 variance floor were NOT reused. Current toolbox/method routing was inspected; incomplete connector code-search results are not claimed to prove repository-wide absence. This is a task-specific conditional-kernel implementation, not a proposed new global tool family.

BRC reuse is observer-typed: the carrier consists of location-labeled conditional prime configurations; the observer is the exact shell-occupancy vector, and future operations are the frozen interval queries. A singleton conditional fiber fixes every such observer. Positive counts, Boolean support and signed centered residuals are different types. No recurrence, cancellation theorem or infinite-scale extrapolation is imported.

## Exact support obstruction

Lemma. An integer half-open interval of length strictly less than 210 contains at most one integer in each residue class modulo 210. Conditioning its prime count separately in every admissible residue therefore determines its entire prime indicator. Nonadmissible integers above 7 cannot be prime; the small primes are fixed. Every statistic of the conditioned indicator has variance zero.

For a microcell with a_j=floor((1025/1024)^j)<=M, writing t=(1025/1024)^j gives t<M+1 and

    a_(j+1)-a_j = floor(frac(t)+t/1024) <= ceil((M+1)/1024).

The inequality follows because frac(t)<1. This provides a simple exact bound, independently checkable without enumerating the microcell endpoints.

| X | smallest eligible prime p | largest q, widest shell | maximum microcell width / bound |
|---:|---:|---:|---:|
| 1000000 | 37 | 27297 | 27 |
| 3000000 | 43 | 70465 | 69 |
| 10000000 | 59 | 171186 | 168 |

All are below 210. Consequently A fixes all 96 required counts at each of these three scales, including their covariance with every other count. Increasing the replicate count cannot repair this obstruction. It is not a zero-variance numerical tolerance decision.

## Completed numerical results

Each scale contains 3 widths x 32 bins = 96 cells.

| X | zero-variance cells, A | zero-variance cells, B |
|---:|---:|---:|
| 1000000 | 96 | 80 |
| 3000000 | 96 | 56 |
| 10000000 | 96 | 33 |
| 30000000 | 81 | 18 |
| 100000000 | 60 | 6 |
| Total | 429 / 480 | 193 / 480 |

There are **236 cells with A variance zero and B variance positive**. A has 0 fully defined C features of 96; B has 16 of 96. The prescribed full T and its family-wise threshold are undefined under both families. Null ranks, selected-feature effect sizes and holdout p-values are therefore NOT_AVAILABLE_UNDEFINED_STATISTIC, not zero or nonsignificant. Complete per-cell observations, means, variances, z/null entries and 5x5 cross-scale covariance numerators are preserved in the bundle.

Exact nonsquare observed shell totals, in width order 1/100,3/1000,1/1000:

| X | totals |
|---:|---|
| 1000000 | 683, 203, 69 |
| 3000000 | 2125, 628, 209 |
| 10000000 | 6519, 1948, 659 |
| 30000000 | 18133, 5409, 1804 |
| 100000000 | 58530, 17462, 5818 |

The reference sieve ends at 1012410; the largest queried q is 1000000. A has 124732 nonempty cell-residue strata, of which 68171 are singletons and 34352 have 0<k<N. This last count confirms that A is not globally implemented as the identity: randomization exists at larger discovery q, while the lower-scale collapse is structural.

## Exact covariance mismatch witness

At X=1000000, width=1/100 and zero-based bin1, only p=37 contributes. Its q interval is [27028,27297]. A fixes its occupancy at 25. The containing B band is [26880,27300), containing 41 observed primes, and has exactly two allowed shifts: 0 and 210. The two occupancies are 25 and 31. Hence the exact B mean is 28 and its exact population variance is 9, versus A variance 0.

The 4096 B replicates produced 25 in 2046 repetitions and 31 in 2050 repetitions: empirical mean 28.0029296875 and unbiased variance 150994800/16773120 = 9.002189217032967. This matches the exact two-point null law. The witness is selected as the first A-zero/B-positive cell in fixed scale/width/bin order for diagnosis only; it is NOT a claimed residual survivor.

## Validation and reproducibility

45 deterministic trial-division interval checks passed. Four selected replicas (0,1,17,4095) from each family passed all applicable cell-count, wheel-residue, cyclic-gap-multiset and independent sorted-position/prefix-query comparisons. Both complete 4096-replicate runs were then repeated and their integer output matrices matched byte-for-byte. A separate standard-library-only checker below proves the support bounds and recomputes the two-shift witness without the reference sieve, NumPy or Numba; its local run returned PASS.

Full executable and raw matrices are stored privately in Google Drive file `1gVn4c9iHlK47oD_clufFnOHcRX8L-OSJ`, title `PFSS2_71565A_reproducibility_bundle_20260916.zip`. Observed URL: https://drive.google.com/file/d/1gVn4c9iHlK47oD_clufFnOHcRX8L-OSJ/view?usp=drivesdk . The uploaded ZIP was fetched back through the authenticated connector and its complete bytes rehashed locally: identical SHA-256, 2447756 bytes. Metadata readback reports shared=false; no sharing permissions were changed. This file ID is a retrieval pointer; the SHA-256 below, not a mutable Drive title, is the content identity.

ZIP SHA-256: `fa73cc42c5171204985eef762513f52944f4b91acf2722f2a6311eb17e76b7c4`.

| ZIP member | SHA-256 |
|---|---|
| experiment.py | c8135743cc87fa828820334c31b7bb44fb0cad3571a51141aaa45140e4f70d94 |
| run.log | 7efafba43ebb2ef9e246d03369695477e7b0d7319288c2cca7bb3a02e14a5107 |
| output/result.json | 2a7750c7fa656dee5bef7afe18406be67bffbe38f949ca65736ab4c3bb106cf2 |
| output/covariance.json | 7a67a5a24d37919c4cf2e3d2d2002540767b2edb05fc54f5d461f95544860031 |
| output/support_certificate.json | 872d2c28091f08f4e2a44bef11470ef4bd79f3e8e2386c31a11cba877cc9eafd |
| output/counts.json | 76b70e833e5a1a00e4f03afa5d95d74001bf5dc780adeb4c66b724f6a1dc1034 |
| output/witness.json | 5ed530499f2cd14df025684e7bd19a94decb702156db3dc1d19bcef58cbae091 |
| output/exact_witness.json | e8ed750510021dbf9f77ab7008cc3d6bbcceadc8692db79218bee343b07063f9 |
| output/full_replay.json | b76cbe8a073b2d87d7cc92f70e6bbbbd67bb00731b54cc95a088c1d30ae24b94 |
| output/A_samples.npy | 14cde5a644b1ee3f739499ac38cf0929a2b9218315a961f647e9343fe340a8b8 |
| output/B_samples.npy | 81e0dfcde626767fd1e2e3f51487ce4fd0bbaac35c04489e090b6d5fe61ae0c0 |

Run `python experiment.py --out replay --replicates 4096` after extraction. Reference environment: Python3.13.5, NumPy2.3.5, Numba0.65.1. Canonical little-endian int64 matrix SHA-256 (without NPY header): A=`edf3d02d589825a294d1aa711ef1d3ec31b7b77e3c4ced83802122e643428e6a`; B=`3730ace19ce8d1f700b58e9a48090b73d55e8d23ed8d81f9c2901b515a012005`. Exact witness/proof checks do not depend on RNG-version reproducibility.

### Independent certificate checker

```python
#!/usr/bin/env python3
"""Independent, standard-library-only PFSS2 support and covariance certificate."""
import json
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def check():
    bounds = []
    for X, expected_p, expected_bound in [(10**6,37,27),(3*10**6,43,69),(10**7,59,168)]:
        p = 2
        while p**4 <= X or not prime(p):
            p += 1
        M = (X * 101 // 100) // p
        # If a=floor((1025/1024)^j)<=M, the next floor minus a is
        # at most ceil((M+1)/1024). Every such cell has <=1 point/residue.
        width_bound = (M + 1 + 1023) // 1024
        assert p == expected_p and width_bound == expected_bound and width_bound < 210
        bounds.append({'X':X,'p_min':p,'q_max':M,'width_upper_bound':width_bound})
    numerator = denominator = 1
    previous = 210
    found = False
    for j in range(1000):
        endpoint = 210 * (numerator // denominator)
        if (previous, endpoint) == (26880, 27300):
            found = True
            break
        if endpoint != previous:
            previous = endpoint
        numerator *= 65
        denominator *= 64
    assert found
    X, p, left, right = 10**6, 37, 26880, 27300
    lo, hi = X//p + 1, (X*101//100)//p
    source = [q for q in range(left,right) if prime(q)]
    counts = [sum(lo <= left+(q-left+shift)%(right-left) <= hi for q in source)
              for shift in (0,210)]
    assert (lo,hi)==(27028,27297) and len(source)==41 and counts==[25,31]
    assert sum(counts)/2 == 28 and sum((c-28)**2 for c in counts)/2 == 9
    return {'status':'PASS','bounds':bounds,'B_band':[left,right],
            'interval':[lo,hi],'source_primes':len(source),'shift_counts':counts,
            'A_exact_variance':0,'B_exact_population_variance':9,'holdout_queries':0}

if __name__ == '__main__':
    print(json.dumps(check(),indent=2))
```

Extracted checker SHA-256 including final newline: `c8b0c445e6cf7f64d88852b52c4f03b3c239b58f9bd2524065a62b6987f3085a`.

## Handoff recommendation and unresolved residue

Submit the exact support/covariance obstruction to Driver review as a task-local null-model-misspecification return. Do not mark the arithmetic hypothesis REFUTED or ACCEPTED. Do not silently rescue the test by variance flooring, deleting scales, or calling a structural zero a successful density correction. The existence of a higher-order residual remains unresolved; testing it requires a separately frozen design with nondegenerate randomization support and a defined statistic. No successor task or Foundation promotion is authorized by this report.

Control verification used the canonical dispatch packet plus complete authenticated Issue240 delta, exact publication/execution bindings and immutable artifact readbacks. A whole-repository runtime audit was not executed in this connector-only environment and is not claimed. The initial fenced comment 5696591033 was non-event prose under the canonical parser; raw comment5696624508 is the actual claim. Full deterministic replay is internal validation, not independent external research review.
