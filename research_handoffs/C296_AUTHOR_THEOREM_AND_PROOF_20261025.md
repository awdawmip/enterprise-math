# Enterprise Math C296 — 125 exact 256-bit root brackets by outward integer intervals

**2026-10-25; AUTHOR_UNREVIEWED / NO_CLAIM / NOT_ADMITTED.**
**Scope:** C195/H168 **79-node positive-rational auxiliary** model, `Q=2^128`, normalized `f(v)=F(v)/Q`. No theorem here transfers to native GF(2)-BRC, Heartbeat X6 or P000.

## Pinned source and input

GLOBAL_KNOWLEDGE_V1 `main@45aa95910fe2809e438d5b3cb8d2e37e8e5a1a1f`; Enterprise Math canonical control `main@5ea0d75fdb6f1b110a3fb6f3c67a2589d6e81c42`. The **distinct frozen mathematical evidence** is the unmerged author commit `014e5b8444ee1b4ace1175566075cd12951e168e`, carrying C275 original function, C284 interval records, C288 path de-duplication, C293 evidence, and C295 128-bit integers. All same-label factors are retained.

Let the 125 fixed paths be `v_i(t)=w_i+t*d_i`. For each original C295 bracket integer `k128[i]`, store C296's unsigned 128-bit suffix `s[i]` and define `k256[i]=2^128*k128[i]+s[i]`. The compact suffix file records the exact SHA256 of its raw 2000 bytes, parent C295's 2000 bytes, and the reconstructed 4000-byte full K256 array; see `C296_125_K256_SUFFIX128_CERTIFICATE.b64`.

## A mathematical lemma (exact enclosure for positive rational products)

Fix P>=0. For a strictly positive rational `r=n/d` with n,d positive integers, set
`start_P(r)=(floor(2^P*n/d),ceil(2^P*n/d))`.
For rational x>=0 known to satisfy `L/2^P <= x <= H/2^P`, define
`mul_(n/d)(L,H)=(floor(L*n/d),ceil(H*n/d))`.
Then the resulting integers satisfy
`L'/2^P <= x*n/d <= H'/2^P`.

**Proof.** Multiply the original two-sided inequality by the positive `n/d`. Integer floor never exceeds the exact lower product; integer ceil never falls below the exact upper product. Induct across all factors, and sum interval endpoints across terms. No roundoff assumption, cancellation, floating-point comparison or hidden mathematical continuity premise is used.

In the C275 auxiliary model the 79 terms are strictly positive at all certified valid endpoints. The implementation `C296_DYADIC_INTERVAL_SIGNS.py` starts each original fixed or moving contribution from a positive exact rational, multiplies its original positive factors with outward floor/ceil, and sums all 79 interval results. A fixed-source coefficient is precomputed by exact regrouping of its *same-label* factors, not by dropping branch identity or pretending to perform native BRC arithmetic. Consequently for each rational v,
`L_P(v)/2^P <= f(v) <= H_P(v)/2^P`.
Therefore `H_P(v)<2^P => F(v)<Q` and `L_P(v)>2^P => F(v)>Q` are rigorous **integer** strict-sign certificates.

## New theorem and complete finite proof certificate

The 125 suffixes yield integers `k256[i]` with
`0<=s[i]<2^128`, `(k128[i]<<128)<=k256[i]`, and
`k256[i]+1 <= (k128[i]+1)<<128`.
For all 125 i, endpoints
`v_i^- = v_i(k256[i]/2^256)`, `v_i^+ = v_i((k256[i]+1)/2^256)`
have been checked with the original valid-domain predicate and against the corresponding C288 coordinate box.

**Exhaustive exact check:** at fixed outward precision P=448, for all i,
`H_448(v_i^-)<2^448<L_448(v_i^+)`,
and the certified normalized endpoint margins strictly exceed `2^-268`.
Thus
`F(v_i^-)<2^128<F(v_i^+)`: **125 strict dyadic brackets of width 2^-256**. All 250 original C295 endpoints were independently rechecked at P=320, yielding all strict signs and certified normalized margin `>2^-142`. Therefore **500/500 exact endpoint inequalities PASS**. The standalone remote verifier `C296_VERIFY_128_256_OUTWARD.py` reads the old C295 certificate and the new C296 suffix, checks their content SHA256, reconstructs all 256-bit endpoints, reruns every outward enclosure, and checks both margin inequalities. Its expected result is `C296_REMOTE_PORTABLE_125x2_128_AND_256_PASS`. It uses only Python standard library, plus the exact C295 ancestor files in this research branch.

By continuity, every one of the 125 paths contains a threshold root in its open 256-bit bracket. At each parameter midpoint, error from **some** root is `<2^-257`; combining the prior C288 author-level bound `||d_i||_1<1/40` yields auxiliary coordinate error `<2^-257/40`. The previous C288 author-level proof that its coordinate boxes are mutually disjoint supports **at least 125 distinct auxiliary real roots**, conditional on that frozen result. Root *uniqueness* or *simplicity* would additionally require the separate unadmitted C285 monotonicity proof; signs alone do not imply those claims.

## Exhaustive verification and resource limits

For **each** input precision 128 and 256: 250 normalized endpoint intervals, 19,750 individually positive branch initializations, 153,000 positive-factor directed integer multiplications; all checks PASS. At b=128 / P=320 the measured per-operation maximal widths were: interval state **335 bits**, exact rational factor operands **1,886 bits**, temporary product **2,071 bits**. At b=256 / P=448: **463, 3,422, 3,735 bits** respectively. These are tracked integer operation widths, not the total Python process memory.

A second author-level implementation independently recomputed the entire original 79-branch **full rational sum** for every 256-bit endpoint, checking 250/250 strict signs and verifying all exact sums lie inside their 448-bit intervals. The final fully reduced normalized `Fraction` numerator and denominator reached **100,989 bits**. Independent means a different computational implementation, **not** an independent Source Driver or mathematically admitted review.

A same-machine comparative timing (includes shared setup, illustrative not a universal cost theorem) gave at 128 bits 0.633s outward vs 7.842s full rational (**12.38x**); at 256 bits 0.793s outward vs 17.867s full rational (**22.53x**). The finite certificate proves sufficiency of P=320 and P=448 **at these 500 endpoints only**. A uniform guard-bit theorem for arbitrary precision or arbitrary auxiliary inputs remains open.

The full portable bundle additionally contains generation code (`mpmath` secant is strictly **candidate discovery**, not proof), JSON exact inputs, independent fraction checks, raw audit and SHA256 manifest. This GitHub branch contains the compact self-verifying essential proof and reuses the frozen C295 source rather than copying prior files again.

## Provenance, authority, next question

Actual GitHub identity `awdawmip` supports scoped author branch publication. Native `em_control_tasks` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Hence current live owner **not established**, native session/CLAIM/checkpoint/Result **not obtained**, and no Source Driver approval or canonical `main` promotion has occurred. Saving this author-only research handoff does not assert native execution permissions or change P000.

**C297:** derive a source-bound a priori upper bound on accumulated directed-interval error for arbitrary target precision b from circuit length, factor magnitudes, rational input heights and threshold separation. Establish a genuine bit-complexity theorem and test b=384; separately preserve unresolved GF(2)-BRC phase, port, provenance and future-observation bridge.

`C296_AUTHOR_EXACT_256 / 125_PATHS / 500_INTEGER_SIGNS / 250_INDEPENDENT_FRACTION_SIGNS_256 / NO_CLAIM / NOT_ADMITTED`
