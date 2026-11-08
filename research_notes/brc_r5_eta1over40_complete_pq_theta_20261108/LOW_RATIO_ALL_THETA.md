# R5 stronger theorem — complete low-ratio physical (η, θ, p, q) prism

Date: 2026-11-08 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Direct predecessor: this folder's `RESEARCH.md`, `CERTIFICATES.json`, `VERIFY.py`. Scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Normative context remains current-main read, not part of the scientific pins.

## Theorem (six/seven free real parameters)

For **all real** `0<=eta<=1/40`, `0<=s<=g<=1`, and `0<=theta,p,q,h<=1`, define

```text
x=(g,s,eta*s,
   s*(13/40+eta/80)*p,
   s*(9*eta/40+theta/10),
   s*(3/40+21*eta/80)*q,
   s*theta/10).
```

There exists one lawful seedless LR target `y` and one nonnegative **calibrated 7×7 BRC Blackwell kernel** `Q`, each independent of the terminal declaration, such that for **every** `d in [0,1]^7`, source `x_h=(1-h)*x+h*y` has precisely the same four observed quantities `(eP,eQ,TP,TQ)` as target `y` with the stochastic mapped declaration `d'`. The seven node likelihoods, mass map, time map and exact calibration equations are in `RESEARCH.md`. This theorem covers the **entire** low-ratio physical p/q/theta capacity rectangle, including mixed interior and irrational parameters. Previously, complete p/q/theta coverage was established only at eta=1/40.

Two seedless linear faces, `G={b=0,v=z}` and `F={z=a/10,v-z=9b/40}`, suffice. Their face-wise convexity preserves lawful flow inequalities, seven Q rows, seven Q columns, seven likelihood-weighted P columns and the two stopping times. Crucially, no source/target triple is convex-combined across different faces.

## Four new rational anchor certificates and moving θ-switch

The original `CERTIFICATES.json` contains the 15 exact rational eta=1/40 vertex kernels. The supplementary `ETA0_F_CERTIFICATES.json` contains **four** newly computed rational eta=0, theta=0 F-face kernels at `(p,q)=(0,0),(0,1),(1,1),(1,1/2)`. For eta=0, every FULL_HIST source is itself seedless on G, and at theta=1 it lies on **both G and F** (z=a/10, v=z, b=0). Therefore G identity triples are available for eta=0 at theta=0 and 1, and F identity triples are available at eta=0,theta=1.

Set

```text
lambda=40*eta ∈ [0,1],
Theta=1-lambda/4=1-10*eta ∈ [3/4,1].
```

At each specified `(p,q)` vertex, construct exact calibrated endpoint triples by **affine eta interpolation**:

1. **At theta=0**: for each G triangle vertex `(0,0),(1,0),(1,1/2)`, combine eta=0 source identity on G and eta=1/40 `G_t0` anchor with weights `(1-lambda,lambda)`. For each F quadrilateral vertex `(0,0),(0,1),(1,1),(1,1/2)`, combine the newly saved eta=0 `F_eta0_t0` anchor and existing eta=1/40 `F_t0` anchor with the same weights. Each result remains on its declared face and its source is the desired `x_eta(theta=0,p,q)`.

2. **At theta=Theta**: for each needed G or F vertex, combine the eta=0, theta=1 **identity** triple and the corresponding eta=1/40, theta=3/4 anchor on the **same face**, with weights `(1-lambda,lambda)`. Because the source is jointly affine in eta and theta at a fixed `(p,q)`, this gives exactly `x_eta(theta=Theta,p,q)`, not merely an approximation.

**Region A: `0<=theta<=Theta`.** Interpolate the two endpoint triples on the selected face with nonnegative weights `(1-t,t)`, `t=theta/Theta` (Theta>=3/4). For `q<=p/2`, use G face and triangle barycentric weights `(1-p,p-2q,2q)` on vertices `(0,0),(1,0),(1,1/2)`. For `q>=p/2`, use F face with `alpha=(q-p/2)/(1-p/2)` and quadrilateral weights `((1-alpha)(1-p),alpha(1-p),alpha*p,(1-alpha)p)` on vertices `(0,0),(0,1),(1,1),(1,1/2)`. All coefficients are nonnegative, sum to 1 and reproduce the requested source.

**Region B: `Theta<=theta<=1`.** The entire p/q square uses face F. The F anchor at `(eta,theta=Theta,p,q)` for each square corner arises from the eta=0, theta=1 identity and the existing eta=1/40,theta=3/4 F corner (including `p=1,q=0`) with weights `(1-lambda,lambda)`. At theta=1 every source `x_eta(1,p,q)` lies on F and has its diagonal identity kernel. For eta>0, interpolate the lower and upper F anchor at that corner with weight `t=(theta-Theta)/(1-Theta)`. At eta=0, Theta=1 and Region A already covers all theta, so no division by zero occurs. Finally, mix the F corner triples with `((1-p)(1-q),(1-p)q,p(1-q),pq)` on `(0,0),(0,1),(1,0),(1,1)`.

At both switching boundaries a face-consistent realization exists. No continuity of target selection across the p/q face switch is needed. For general `0<=s<=g<=1` append identity triples at `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)` with respective weights `1-g,g-s`, normalized weight `s`. Both identity triples lie on each face. Finally interpolate source with its target and its Q with the target diagonal by `(1-h,h)`. The calibrated weighted-row and column identities give declaration preservation for all d.

This is a constructive all-real proof from exact rational anchor identities and nonnegative barycentric coefficients, not a claim extrapolated from a finite numerical grid.

## Verification and scientific boundary

`VERIFY_ETA_BRIDGE.py` uses only the Python standard library `fractions.Fraction`, imports the previous exact seven-node mass/time checker and validates all four new rational F anchors together with the original eta=1/40 certificates, then checks **1,024** exact rational construction cases across eta, theta, mixed p/q, moving face-switch boundaries, g/s scaling and h interpolation. The actual local run output is saved as `EXACT_ETA_BRIDGE_OUTPUT.txt`. Float LP was used for sparse support discovery only; exact rational linear reconstruction and independent exact checker established the saved matrix identities.

The theorem is confined to the frozen four-stage seven-likelihood-node P/Q-BRC statistical experiment and declared four-observer readout. It preserves P000 and does not claim any new native X6 realization. This is author proof pending independent mathematical review/admission. Current native control read returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`; no active Owner/CLAIM was authenticated. Publication into a research branch is source persistence only.

The next unit is the as-yet-uncovered ratio interval `1/40<eta<46/705`, followed by arbitrary lawful FULL_HIST flows; see `NEXT_UNIT.md`.
