# D25: weighted-216 versus q-microscope-proved weighted-2304 — a source-faithful proof bridge

**2026-10-31 18:00 Asia/Hong_Kong · AUTHOR-SIDE / EXACT FINITE CHECK / EXTERNAL PROVED THEOREM CONSUMED / BRIDGE OPEN / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Mother objective: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` only, NEVER maintenance `chatgpt-hourly-enterprise-math-20260921`. P000 and ACTIVE residual-faithful worldview remain unchanged. This is classical external-number-theory readout, not a verified native X6/H0/B0 transfer.

## Two distinct original arithmetic sources

For every prime p>3, let

`A_p = Σ_{k=0}^{p−1} (6k+1)·C(2k,k)²·C(3k,k)/216^k`,

`B_p = Σ_{k=0}^{p−1} (8k+1)·C(4k,2k)·C(2k,k)²/2304^k`.

The **original frozen D25 claim** is `A_p ≡ p (mod p³)` for p≡13,19 (mod24). Define `A_p^half` and `B_p^half` by truncating the corresponding original sums at k=(p−1)/2. Neither A/B nor half/full truncations may be interchanged without proof.

## Reused externally published *theorem* — not our theorem

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358, DOI **10.1016/j.aim.2019.02.008**, arXiv:1803.01830, PROVE for every p>3:

`B_p ≡ B_p^half ≡ p·χ_{−3}(p) (mod p³)`,

where χ_{−3}(p)=+1 when p≡1(mod3) and −1 when p≡2(mod3). In particular χ=+1 on original D25 target classes. **This theorem is only about B, the weighted-2304 series.** We do NOT infer the original claim from it without the bridge below.

## Concrete reduced sufficient obligation (OPEN)

`A_p−B_p ≡ 0 (mod p³)` for every p≡13,19 (mod24) would imply original LIFT immediately by Guo–Zudilin. This is a proposed **joint finite WZ/CM or q-microscopy-compatible transformation target**, not a proved all-prime relation or an accepted Result. Existing signed R_p, exact p-adic carry, source weight, modulus and cutoff remain separate until a transformation correctly identifies them.

## Executed integer certificate: exactly 1,752 primes

We independently executed `d25_qmicroscope_bridge_exact_20261031.py` on *all* 1,752 primes 5≤p≤15,000 (445 frozen-target primes). For every tested p, it verified using exact integer modular arithmetic:

`A_p == B_p == B_p^half == p·χ_{−3}(p) (mod p³)`.

It also independently computed the original integer binomial sums of both series at p∈{5,7,13,19,31,37,67}; all direct sums matched modular-recursive evaluations. Each denominator for indices below p is a p-unit. **This is finite evidence, not proof for infinitely many primes.** Canonical witness-stream SHA256, using `(p,A_p,B_p,A_p^half,B_p^half);` tuples ordered by p:

`c44fd2f0c46acf0e28f8e3bd5326d53c3e82febd2660073754b8dd0065f48e56`.

Recurrences from the actual *unweighted* summands a,b:

`a_0=b_0=1;`
`a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3);`
`b_{k+1}/b_k=(4k+1)(2k+1)(4k+3)/(288(k+1)^3).`

The weights (6k+1) and (8k+1) are retained when summing. No floating-point estimates or assumed formal-series evaluations were used. Published program Git blob is independently matched to the locally actually executed source.

## Exact *negative* witness against naive half-cutoff transfer

| p | mod p³ | A_full = B_full = B_half | A_half | (A_full − A_half) mod p³ | tail / p² mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 2197 | 13 | 520 | 1690 | 10 |
| 19 | 6859 | 19 | 3629 | 3249 | 9 |
| 373 | 51895117 | 373 | 14887176 | 37008314 | 266 |

At p=19, B_half equals B_full modulo 19³ but A_half differs from A_full by 3249=9·19²≠0 modulo 19³. Therefore **the proven comparator half-truncation cannot simply be substituted for the original half-truncation**. The p=373 tail was already known from prior D25 integer-boundary work; it is CONSUMED, not re-attributed. In BRC terms, observed terminal scalar matches do not erase non-identical source ports/valuation strata; an allowed quotient must be proved for the exact future operation. No native-space dimension or Frobenius authority is inferred.

## Exact continuation, evidence debt, and Source boundary

**Highest previously verified scientific source frontier** stays frozen (accepted D24 first-digit UR plus D25 author-side Clausen/Green/signed-R source notes). This new evidence is an author-side external-prior-art bridge route and an executed finite certificate, **not a completed LIFT theorem**. The smallest next mathematical unit is to derive a genuine finite transformation/telescoper/CM/q-microscopic relation controlling `A_p−B_p` modulo p³ across both target residue classes, including nonzero A half-tails at 19/373; or produce an exact target counterexample.

**Native #1559 NOT_EXECUTED / PENDING_OWNER**: fixed-373 original H0/B0 divided-power [X]U mod139129, actual native rank, semilinear Frobenius eta, signed odd Hesse/Green, κ and independent reproduction remain unfulfilled. The scalar comparator is no substitute.

Research-only historical read-only recovery `awdawmip/kimi-query-bridge#6632` showed a session pointer but NO own current CLAIM/run; original dispatch `#6633`, request `research-onhour-20261031-0205-dispatch-r15`, FAILED `UPSTREAM_CODE_REVIEW_REQUIRED`. Do not replay original failed mutation. Current gateway 0.6.11 Site client remains read-only: `research_authority_granted=false`, `executor_binding_configured=false`; no new native checkpoint, researcher registration, Result, independent review, or Task admission is asserted. Frozen source, Research/maintenance separation and original schedule/notifications remain unchanged.
