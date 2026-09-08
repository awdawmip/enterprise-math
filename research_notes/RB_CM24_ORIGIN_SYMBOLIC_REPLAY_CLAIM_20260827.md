# Historical source capsule: CM(-24) symbolic-replay claim journal

Status: `HISTORICAL_SOURCE_TRANSFER_ONLY / NOT_CURRENT_MATHEMATICAL_ACCEPTANCE`.

- Original repository: `awdawmip/chatgpt-global-knowledge`.
- Original immutable commit: `bfc1300130dad2d07916ec3d37d4bc67eb9fc9de`.
- Original path: `journal/enterprise-math/2026-08-27/20260827T205000+0800-explicit-degree6-cm24-symbolic-replay-pass.md`.
- Original Git blob SHA1: `8c10bcb07b6ae021987a5cd3328acba9f0264cc3`.
- Original file SHA256: `5c75649acab83359902b37e925ca7ed7a762f1d8521c9f2bce9845f2debe94b5`.
- Original Progress-Event-ID: `EM-FREE-1LAVKW-20260827-DEGREE6-CM24-SYMBOLIC-REPLAY`.
- Immutable source: [original journal](https://github.com/awdawmip/chatgpt-global-knowledge/blob/bfc1300130dad2d07916ec3d37d4bc67eb9fc9de/journal/enterprise-math/2026-08-27/20260827T205000%2B0800-explicit-degree6-cm24-symbolic-replay-pass.md).
- Imported at (UTC): `2026-09-08T17:19:07.106129+00:00`.

The complete original journal follows byte-for-byte after the delimiter. Its dated PASS, self-audit, replay and closure statements remain historical source claims. This import performs no SymPy or other mathematical replay, independent reconstruction, theorem acceptance, formal Result/Driver review, or parent closure. Any field statements and later corrections remain in their original separate journals.

This is a later recovery of the originating source. It must not be inserted into the earlier blind raw freeze or retroactively described as an input to that execution or as a comparison already completed. The original session is UNKNOWN; the Progress-Event-ID supplies a historical identity label only, not a present session or claim. No research mode is inferred from the identifier.

<!-- ORIGINAL_GK_JOURNAL_BYTES_BEGIN -->

# Exact symbolic replay passes for the explicit degree-6 CM(-24) correspondence

Progress-Event-ID: `EM-FREE-1LAVKW-20260827-DEGREE6-CM24-SYMBOLIC-REPLAY`
At: `2026-08-27T20:50:00+08:00`
Scope: `enterprise-math / Ramanujan-Borwein x Fermat24 normalization`
Source: `conversation / independent deterministic SymPy quotient-ring replay`
Kind: `CHECKPOINT`

## Event

The explicit degree-6 map frozen in preceding commit `6fbf6ac5b33aac8d356e51a896c8d12dae10e117` was independently replayed from its final algebraic formulas only. The replay did not use the prior Abel-Jacobi numerical samples or PSLQ values as a verifier.

The checker works in the exact algebraic setting

`alpha^4=3`, `sqrt(2)^2=2`, `t^2=R^3-3R`,

with map sections `N,D`, modulus

`lambda*=35+24sqrt(2)-20sqrt(3)-14sqrt(6)`,

Prym parameter

`k=-i alpha(sqrt(6)-2)`,

and curve scale

`C=-i alpha(9+3sqrt(2)+2sqrt(3)+4sqrt(6))/4`.

### Exact replay results

All four branch-section norm factorizations returned exact symbolic `True`:

1. `Norm(D)=-R(R-sqrt(3))(R+3sqrt(3)) Q2(R)^2`.
2. `Norm(N)=(R+2)^2(R+sqrt(3))(R+3sqrt(3)) cN Q1(R)^2`.
3. `Norm(N-D)=-(R+3sqrt(3)) Q3(R)^2`.
4. `Norm(N-lambda*D)=(R+3sqrt(3)) c4 Q4(R)^2`.

Thus the unique common base point and degree-6 branch structure are reproduced independently.

For the differential identity, write

`partial_E0=partial_R+[3(R^2-1)/(2t)]partial_t`,

`X=N/D`.

After clearing denominators and reducing modulo `t^2=R^3-3R`, the identity becomes two coefficient polynomials (the `1` and `t` components). Both vanish exactly over the algebraic extension:

`diff0=True`,
`diff1=True`.

Equivalently,

`(partial_E0 X)^2`
`=C (t+k)^2/[t^3(R+2)] X(X-1)(X-lambda*)`.

The final period-scaling identity also returns exact symbolic `True`:

`4 cP^2/C = 96 alpha(1+sqrt(2))(2-sqrt(3))`,

where

`cP=3(1-i)(sqrt(2)+sqrt(3))`.

Finally the Legendre j-invariant is exactly

`j(lambda*)=2417472+1707264sqrt(2)`,

the principal CM(-24) value.

## Classification

`EXPLICIT DEGREE-6 FERMAT/Prym -> PRINCIPAL CM(-24) MAP = EXACT SYMBOLIC REPLAY PASS`.

`FINAL ALGEBRAIC DIFFERENTIAL NORMALIZATION = EXACT SYMBOLIC REPLAY PASS`.

No numerical tolerance remains in the verification chain.

## Next

Freeze a revised typed Ramanujan-Borwein x Enterprise theorem-package candidate in which the former open bridges (1), (2), and (3) are all marked closed at their correct semantic layers. Keep canonical Foundation promotion separate and require an independent audit/replication before any promotion.
