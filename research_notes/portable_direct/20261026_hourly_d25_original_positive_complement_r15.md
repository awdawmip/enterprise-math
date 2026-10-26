# D25/LIFT — Exact positive-rank original-series complement and nonzero p=733 source port

2026-10-26. Continuation of original-parameter diagonal bridge `20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15.md` (consume, not recredit). Requested Research lane `chatgpt-research-hourly-enterprise-math-20260923`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Next smallest unfinished question

The previous exact original-series source bridge proved the normalized original cutoff from the **negative ranks** `L<=n<=0` plus a separately ordered high–high sector. The actual finite bivariate carrier also has **positive ranks** `1<=n<=N=2m-1`; these correspond to ordered low–high pairs below the original cutoff. Can this distinct positive port be computed by its own exact source operator, with no unrecorded upper finite boundary, to support future nontrivial observer composition?

Use the previous *original-parameter* definitions: `p=6m+1>=7`, `theta=-p/6`, `f_r(theta)=2^r r_r`, `beta_r=f_r(theta)/p^2` for `r>2m`, and

```text
V_n^h = sum_(1<=j,ell<=2m; ell-j=n) j^h f_j(theta) beta_(p-ell),
Z_n = 2V_n^1-(p-n)V_n^0,
(p-n)Z_n-(p-n-1/2)Z_(n+1)=E_n,
Z_(N+1)=0.
```

Here `E_n` is **the actual two-ended finite face** normalized by `p^2`, as in the preceding paper. Positive ranks are external ordered carrier indices, not native Enterprise spatial axes.

## New all-digit positive-rank Ward telescope

Set `mu_0=0` and recursively, for `1<=n<=N`,

```text
mu_n = [ 2^n + (p-n+1/2)mu_(n-1) ]/(p-n).                  (1)
```

All denominators `p-n` are `p`-adic units because `1<=n<=N<p`. Hence `mu_n in Z_(p)`. **Exactly**, not just modulo `p^k`,

```text
sum_(n=1..N) 2^n Z_n = sum_(n=1..N) mu_n E_n.               (2)
```

Proof: in the RHS expand the inherited genuine source recurrence and collect `Z_n`. The coefficient of each `Z_n` is `(p-n)mu_n-(p-n+1/2)mu_(n-1)=2^n`. The outer `Z_(N+1)` coefficient vanishes only because the actual carrier cutoff says `Z_(N+1)=0`. No finite face is erased.

Define `U_+=sum_(1<=n<=N)2^n V_n^0`, `K_+=sum2^n V_n^1`. The *original-series* ordered **subcutoff low–high complement** is

```text
C_(LH,<) = 2 sum_(1<=j<ell<=2m)
               [6(j+p-ell)+1] r_j r_(p-ell).
```

These are exactly the pairs `j+(p-ell)<p` and their reversed order. Because `(6p+1-6n)V_n^0=V_n^0+12V_n^1-6Z_n`, equations (1)–(2) prove

```text
C_(LH,<)/p^2 =
    2^(1-p) [ U_+ + 12 K_+
             -6 sum_(n=1..N) mu_n E_n ].                   (3)
```

This equality is **exact in Z_(p)** for all target primes and all p-adic digits. The true right cutoff, positive-rank finite faces, original subcutoff population and independent original cutoff `Q_p` are preserved as distinct objects.

The associated nonzero positive source **does not** enter `Q_p` merely by being present in the carrier; a future cross-sector observer must specify a valid coupling before transporting it. Equation (3) is not a proof of WZ cancellation, infinity identification, or the original CM/Frobenius target. It is an all-digit input/source interface for the previously unsummed complement.

## Executed exact certificate

The checker `20261026_hourly_d25_original_positive_complement_r15_check.py` imports the preceding separately published original-bridge checker for the genuine `E_n`, `f_r`, and `r_r` definitions; it then independently forms the **ordered original recurrence** `r_r` and the `j<ell` complement, not merely the final source sum. Executed **PASS for 23 primes**, all `p=6m+1` primes `7<=p<=211` plus `p=733`, with all positive-rank adjoint identities and the independent ordered complement modulo `p^3`.

At `p=733`, the normalized subcutoff low–high complement is

```text
C_(LH,<)/733^2 = 204955275 mod 733^3,
sum_(n=1..N) mu_n E_n = 73541419 mod 733^3.
```

The complement is `412 mod 733`, so the positive-rank observer is genuinely nonzero. At `p=13`, the same values are `1715` and `2144` modulo `13^3`. These are **new precisely scoped complement/source observations**, not recredit of previous ordered-`Q` outputs. They cannot be substituted for the earlier Hasse-gauge infinity contributions without a proven source map.

BRC **COMPOSE_APPLIED**: finite signed rank with ordered pair provenance, original-series parameter normalization, distinct lower/upper finite faces, p-adic valuation and the above-/below-cutoff observer are retained; no false compression of the separate high–high corner or native X6 state. P000 and active residual-fidelity worldview unchanged.

## Next uncompleted unit and control

The next exact unit is to combine the authentic six-label signed 3+2+1 Hasse transport with both **all-digit original-series** positive/negative Green operators, and test whether a genuine `k-1,k-2` cross-label source syzygy cancels *both* observer deficits. A diagonal original cutoff alone does not reconstruct the six labelled sources. If no syzygy exists in the actual joint carrier, produce a fully labelled nonzero counterexample; do not infer a free-carrier no-go as a theorem of the actual constrained Hasse data.

Native Research remains unauthorised in the last authenticated service status (`research_authority_granted=false`, service `0.6.11`), and the old typed continuation fault `INVALID_ARGUMENT / CONTROL_QUOTA` has no successful replacement receipt. Historic session/staging are protected; no new Source CLAIM/OPEN/checkpoint/freeze or Driver acceptance is implied. Existing control owner `enterprise-math#1558`. Mother D25/LIFT/JT2 **OPEN**: `H0/B0`, original `[X]U mod p^2`, Frobenius `eta`, `kappa`, native CM experiment, independent review and source acceptance remain missing.
