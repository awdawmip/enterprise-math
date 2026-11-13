# Next R5 unit — mixed side-branch physical rectangle, after complete maximal-u/zero-w low-ratio solution

Source frontier: `FULL_LOW_RATIO_BRIDGE.md` (this folder) now proves exact four-observer Blackwell lift for **every** `0<=eta<=1/40`, `0<=theta<=1`, `p=1,q=0`, with all `0<=s<=g<=1` and source-target interpolation `h`. Its three exact anchors are `CERTIFICATES.json`; the executed 450-check output is `EXACT_FULL_OUTPUT.txt`. Scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.

## Current unresolved mathematical unit

For `eta=1/40` and `29/112<theta<1`, investigate the **full** physical `p,q` rectangle:
```text
x=(1,1,eta, (13/40+eta/80)*p,
   9eta/40+theta/10, (3/40+21eta/80)*q, theta/10).
```
Earlier evidence gives a common G-face interpolation for all p,q at theta<=29/112. The p=0,q=1 corner admits an all-theta F-face lift, and our maximal-u p=1,q=0 corner now admits an all-theta G/F switch. Endpoint lifts on different nonlinear seedless representations are **not automatically** a single seedless interpolation across arbitrary p,q. Find a calibrated kernel and target valid over a useful **open** interior p/q region, or a sharp scoped obstruction to a selected face.

Concrete first test: `eta=1/40, theta=1/2, p=q=1/2`. Search for exact lawful seedless y and rational 7x7 Q with all row-Q, column-Q, r-weighted column-P and two time equations. Compare F, G and interior `R=0` strategies, using exact rational reconstruction and a genuinely scoped dual if a linear face fails. An exact example discriminates the simplest mixed branch family. Then extend with an analytic 2D interpolation/family if possible. A failed F/G LP at one point is only a fixed-face finding.

## Secondary research

For `1/40<eta<46/705`, revisit the physical rectangle, especially mixed p/q and positive z. Exact low/high eta constructions may support a new seedless surface with verified calibration. Do not repeat the now-complete `0<=eta<=1/40,p=1,q=0` full-theta proof.

## Handoff and actual control state

Save symbolic proof or exact numerical certificate, explicit parameter scope, executed verifier and output. Native Source `em_control_tasks` and `em_session_start` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; no active owner/CLAIM was authenticated. Source-side preservation is author evidence pending independent review.
