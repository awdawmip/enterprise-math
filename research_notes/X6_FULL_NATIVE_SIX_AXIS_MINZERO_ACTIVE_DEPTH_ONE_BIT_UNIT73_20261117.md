# Unit73 — Full native six-axis X6: exactly one active quadratic comparison resolves double-depth signed BRC fibres

Date: 2026-11-17. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; Researcher `EM-X6-FB6990` using same authorized scientific source/frozen basis. **AUTHOR-EXACT / FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Theorem: native Z6, not a selected 3-axis plane

At the exact frozen P000 V5 signed native six-axis Cell torsor `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, the native displacement is `z∈Z⁶`. In the chosen raw Cell chart (not the final nonnegative Cell address), let

```
h=min_i z_i,       r_i=z_i-h,       min_i r_i=0,
G(z)=Σ_{i=1}^6 z_i²,   T(z)=Σ_{i=1}^6 |z_i|,
R=Σ_{i=1}^6 r_i,   Q=Σ_{i=1}^6 r_i²,
O_6(z)=(r,G,T).
```

The relative six-axis min-zero observer is the quotient by the global diagonal; the integer common depth `h` repairs this quotient to the full native signed X6 displacement. Expanding the native quadratic norm gives the exact *all-Z6* constraint
```
6h²+2Rh+(Q-G)=0,
D=R²+6(G-Q),
h_±=(-R ± sqrt(D))/6.
```
Consequently every passive observer fibre `O_6^{-1}(r,G,T)` contains at most **two** distinct native signed Cell displacements, obtained by retaining exactly the integer roots that satisfy both `G` and `T`.

For **any one named native signed primitive +axis step** `e_i`, the *active* quadratic increment is

```
Δ_i=G(z+e_i)-G(z)=2z_i+1=2(r_i+h)+1,
K_i=6+12r_i-2R.
```
If the passive fibre has two distinct admissible integer depths, then `D>0` and
```
6Δ_i-K_i=12h+2R= -2sqrt(D)  on h_-,
                       +2sqrt(D)  on h_+.
```
Thus the **single observer-calibrated comparison bit**
`b_i=sgn(6Δ_i-K_i)` reconstructs the full native signed six-axis displacement via
`h=(-R+b_i sqrt(D))/6`, `z=r+h(1,1,1,1,1,1)`. Any named axis works. The same one-bit result is **worst-case information-minimal** for exact native-state reconstruction: an observer fibre with two actual states cannot be injected into a zero-bit deterministic decoder, while the comparator provides an explicit two-valued inverse. All six native named coordinates and the actual chosen Cell start are retained in the operational statement. This is a static spatial algebraic action/readout, without assuming a heartbeat time evolution or a physical measurement device.

The natural unsigned shortest signed-path BRC multiplicity is independently
`N_BRC(z)=T! / ∏_{i=1}^6 |z_i|!`. Equality of BRC mass between two candidates is **not enough** to recover native state or any future named-axis operation; the active comparator separates even mass-identical fibres.

## Explicit original-model integer certificates

**Unequal-mass double fibre, both states in the executed cube:** `r=(0,0,2,4,4,5)`, `R=15,G=25,T=11`, `D=9`, depths `h_-=−3,h_+=−2`. Native displacements:

| signed native X6 | shortest N_BRC | Δ_0=G(z+e_0)−G(z) | 6Δ_0−K_0, K_0=−24 |
|---|---:|---:|---:|
| (−3,−3,−1,1,1,2) | 554,400 | −5 | −6 |
| (−2,−2,0,2,2,3) | 415,800 | −3 | +6 |

Both passive observer triples are identical; the last single bit selects the actual native Cell displacement.

**Equal-mass full-six-axis witness:** `r=(0,0,0,0,0,0)`, `G=54,T=18`, depths `−3,+3`, all six components of z are respectively `−3` and `+3`. Both have positive natural BRC multiplicity `137225088000`. Yet for axis 0 the native one-step deltas are `−5,+7`, `K_0=6`, and the two integer comparator margins are `−36,+36`. Even identical full unweighted path-count profiles cannot substitute the one-bit active Cell identity observation.

## Actual full-native finite computation

Independent original-metric integer checker: `research_checks/X6_UNIT73_FULL6_NATIVE_DEPTH_PROBE_CHECK_20261117.py`, Git commit `cc624c53bcf68c86e6025095cbe88d976325583c`, Git blob `1c5b9c4bdad06f3de2176029ff559f85053eab25`. Exact emitted JSON: `research_checks/X6_UNIT73_FULL6_NATIVE_DEPTH_PROBE_RESULTS_20261117.json`, commit `c7742a4c98cb42dfb2ae8731da5e4c8a89bd7493`, blob `12db8cb56780e442e1b2c83165cf8474422d66e7`, SHA256 `c3dad4d03ada52ee032638eeb13fc68db8394492f8ff362f844924cc88d83b07`.

**Executed input population:** all `7⁶=117649` native signed X6 displacements with each component in `[-3,3]`; `113086` distinct passive signatures. Solve the complete **unbounded integer depth quadratic** for every observed signature (candidate z may extend outside the finite sample): `9825` two-depth signatures, of which `4563` have both depths inside the original cube, `3423` have equal natural shortest positive BRC mass, `6402` have different mass. Every one of the six named native directions per global double fibre yields correct two candidate signs: **58950 exact native quadratic comparator checks; zero failures.**

Actual Python executed under normal, `-O`, `-OO`, and each emitted the same SHA256 above. Computation uses exact integer square roots, integer divisibility, factorials and no floating error. It is an **independent exact integer oracle applying the already-frozen X6 source norm formula**, not a replay of original R063 or Helly native benchmarks, nor a fresh import of the frozen `signed_brc.py`. Existing Unit62/71 original-source path-check certificates remain the authoritative prior execution coverage for those original objects.

## Mother-task reconciliation, provenance, next action

This extends Unit72's **selected named three-axis** action theorem to the entire actual native six-spatial-axis Heartbeat World. It supplies a concrete P000-consistent *operation-specific quotient-repair interface* for LP003, LP005, LP011, LP019, LP023 and LP026 downstream consumers. It does not assert an actual historical wrong caller from an algebraic possibility.

Exact historical LP011 allegedly wrong native singleton argmax and LP019 allegedly negative/subtracted positive N-BRC count source:line are still **UNRESOLVED_PROVENANCE**. The latest bounded original frozen source inspections reclassified `BRC_DOMINANT_DEGENERACY_QUOTIENT_20260903.md` lines 20–45 as maximal positive rational weight and `BRC_PURE_ALGEBRA_COLLAPSE_CREDIT_COORDINATE_TRANSFER_ANCHOR_20260816.md` lines 24–30 as signed **scalar algebraic collapse residual**, neither a wrong native signed-axis/BRC count call. The full 28-LP active consumer ledger still needs exact coverage and the separate independent Driver `REQUEST_REVISION`.

Research lane identity: `chatgpt-research-onhour-enterprise-math-20260923`, Source-issued SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`. Original Units69–71 native progress `onhour-20261117-0259-x6-unit69-71-native-progress-v1` is **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED** with authenticated Source readback. The new same-session run-resume original request `onhour-20261117-0430-x6-own-run-resume-after-unit72-v1` was submitted and initially QUEUED/RUNNING, and must be read to its real terminal result; neither Unit72 nor Unit73 was prematurely declared as native semantic publication. Once current authenticated own run and CLAIM are reauthorized, preserve Unit72/73 GitHub/Activity evidence through the existing native PROGRESS contract; without current authorization retain this independent author evidence and the original request. No new session, competing CLAIM, scheduler or notification change.
