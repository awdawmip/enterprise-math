# Historical source capsule: CM(-24) hostile audit and blind-packet journal

Status: `HISTORICAL_SOURCE_TRANSFER_ONLY / NOT_CURRENT_MATHEMATICAL_ACCEPTANCE`.

- Original repository: `awdawmip/chatgpt-global-knowledge`.
- Original immutable commit: `bfc1300130dad2d07916ec3d37d4bc67eb9fc9de`.
- Original path: `journal/enterprise-math/2026-08-27/20260827T212500+0800-degree6-cm24-hostile-audit-and-blind-packet.md`.
- Original Git blob SHA1: `3ab188a104798e1b9ebee5775226b4889245a197`.
- Original file SHA256: `bfac134e4a0da0019556a496df82a1dc280187345038120a84c60b4fea2aaa58`.
- Original Progress-Event-ID: `EM-FREE-1LAVKW-20260827-DEGREE6-CM24-HOSTILE-AUDIT`.
- Immutable source: [original journal](https://github.com/awdawmip/chatgpt-global-knowledge/blob/bfc1300130dad2d07916ec3d37d4bc67eb9fc9de/journal/enterprise-math/2026-08-27/20260827T212500%2B0800-degree6-cm24-hostile-audit-and-blind-packet.md).
- Imported at (UTC): `2026-09-08T17:19:07.106129+00:00`.

The complete original journal follows byte-for-byte after the delimiter. Its dated PASS, self-audit, replay and closure statements remain historical source claims. This import performs no SymPy or other mathematical replay, independent reconstruction, theorem acceptance, formal Result/Driver review, or parent closure. Any field statements and later corrections remain in their original separate journals.

This is a later recovery of the originating source. It must not be inserted into the earlier blind raw freeze or retroactively described as an input to that execution or as a comparison already completed. The original session is UNKNOWN; the Progress-Event-ID supplies a historical identity label only, not a present session or claim. No research mode is inferred from the identifier.

<!-- ORIGINAL_GK_JOURNAL_BYTES_BEGIN -->

# Hostile audit of explicit degree-6 CM(-24) map and blind reconstruction packet

Progress-Event-ID: `EM-FREE-1LAVKW-20260827-DEGREE6-CM24-HOSTILE-AUDIT`
At: `2026-08-27T21:25:00+08:00`
Scope: `enterprise-math / Ramanujan-Borwein x Fermat24 normalization`
Source: `conversation / exact ramification and field audit`
Kind: `CHECKPOINT|HANDOFF`

## Event

After exact symbolic replay of the explicit map, a separate structural audit checked genus, quotient degree, ramification, target nonsingularity, field of definition, and Riemann-Hurwitz consistency.

### 1. Source genus and intermediate elliptic quotient

For

`D:w^4=(R+2)^2 R(R^2-3)`,

the cyclic degree-4 cover of the R-line has local exponent data

- exponent 2 at `R=-2`;
- exponent 1 at `R=0,+sqrt(3),-sqrt(3)`;
- exponent 3 at infinity.

Riemann-Hurwitz gives

`2g(D)-2=-8+(2+3+3+3+3)=6`,

hence `g(D)=4`.

With

`t=w^2/(R+2)`,

one obtains

`E0:t^2=R^3-3R`.

The double cover `D->E0` has exactly six branch points: the three `t=0` points, the two points above `R=-2`, and the point at infinity. The double-cover genus formula again gives `g(D)=4`.

### 2. Principal differential zero divisor and ramification

For

`phi=dR/w (1+k/t)`,
`k=-i 3^(1/4)(sqrt(6)-2)`,

zeros occur at

`t=-k`.

Since

`k^2=12sqrt(2)-10sqrt(3)=Q`,

the E0 coordinates satisfy

`R^3-3R-Q=0`.

The cubic discriminant is

`108-27Q^2=216(-73+30sqrt(6))`,

which is nonzero and positive in the chosen real embedding. Therefore there are three distinct E0 points and two D lifts over each, giving exactly six simple zeros of phi.

Because a degree-d map from a genus-4 curve to an elliptic curve has ramification degree `2g-2=6`, these six zeros exactly exhaust the ramification divisor of the degree-6 map. There is no hidden extra ramification.

### 3. Target and field

The target is

`E_*:Y^2=C X(X-1)(X-lambda*)`,

with nonzero C and `0<lambda*<1` in the distinguished real embedding. Hence it is nonsingular.

Its j-invariant is exactly

`2417472+1707264sqrt(2)`,

the principal discriminant `-24` CM value.

The explicit map is defined over

`L=Q(i,3^(1/4),sqrt(2))`.

The source genus-4 model itself is defined over Q; the extension L records the chosen principal CM embedding, fourth-root differential normalization, and target twist.

### 4. Degree consistency

The exact branch norm factorizations show that the two `L(7O)` sections defining X have one and only one common base point. After cancellation, `X:E0->P1` has degree 6.

Since both `D->E0` and `E_*->P1` are degree 2 and `x o f = X o pi`, degree multiplicativity gives

`deg f=6`.

The differential ramification count above independently agrees with this map.

## Blind reconstruction packet

The following packet is sufficient for an independent execution to reconstruct or refute the hard final bridge without seeing the explicit X formula.

### Allowed input

1. Source curve:
   `D:w^4=(R+2)^2 R(R^2-3)`.
2. Intermediate coordinate:
   `t=w^2/(R+2)`, hence `t^2=R^3-3R`.
3. Principal differential direction:
   `phi=dR/w (1+k/t)`,
   `k=-i 3^(1/4)(sqrt(6)-2)`.
4. Target modulus:
   `lambda*=35+24sqrt(2)-20sqrt(3)-14sqrt(6)`.
5. Hard target:
   construct an algebraic map `D->E` of degree 6 with target j equal to the principal CM(-24) value and pullback invariant differential proportional to phi.
6. Coefficient field bound:
   search inside `Q(i,3^(1/4),sqrt(2))`.

### Withheld during blind reconstruction

Do not read the explicit-map journal entries

- `20260827T203744+0800-explicit-degree6-fermat-cm24-correspondence.md`;
- `20260827T205000+0800-explicit-degree6-cm24-symbolic-replay-pass.md`;
- theorem-package v2 explicit formula section.

### Required independent outputs

1. An explicit degree-6 x-coordinate or a proof no such map exists.
2. Exact branch divisor / common-base-point analysis.
3. Exact function-field identity for the target elliptic equation.
4. Exact pullback differential coefficient.
5. Independent derivation of the squared period scaling.

A reconstruction agreeing with the withheld formula up to target automorphism, source automorphism, algebraic unit, or equivalent line-bundle presentation counts as PASS.

## Verdict

`CURRENT SELF-AUDIT = PASS`.

`INDEPENDENT BLIND REPLICATION = NOT YET PERFORMED`.

No canonical Foundation promotion is implied by this checkpoint.

## Next

Route this packet to a separate independent research execution. Until that happens, treat theorem-package v2 as mathematically closed but independently unaudited.
