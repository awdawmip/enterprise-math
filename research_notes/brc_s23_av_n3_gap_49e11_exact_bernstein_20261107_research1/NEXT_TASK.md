# Continuation: decide exact S23 AV n=3 minimax value

Date: 2026-11-07. Frozen scientific source `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent Draft PR #1777. Predecessor certified gap `1.79833236e-7`; current author-side all-real certificate gap `49/100000000000=4.9e-10`.

**Scientific target.** `δ₃` for the conditional-AV shared-parameter three-observation model lies between `5211/21952` and `8142187516807/34300000000000`.

**Primary route.** Test exact equality `δ₃=5211/21952` (or its failure). Characterize the equality face at the fiber `z=1/4` and the one-sided derivatives at `(1/2,1/2)`, `(5/7,7/8)`. Solve constrained rational kernel feasibility across the nearby boundary `c=7/8`, then produce an all-real Bernstein certificate at the *exact fiber value* if feasible. If obstruction, construct finite rational support with signed TV dual multipliers that certifies a strictly stronger lower bound for every stochastic `4×10` matrix.

**Alternative.** Improve the present rational 4×10 primal and certify a smaller strict gap by the standalone exact verifier. Do not repeat unchanged earlier 48-leaf or current 54-leaf certificates solely to generate activity.

**Independent check.** Re-derive the tensor Bernstein coefficient transform and polynomial degrees, confirm exact row sums, 27-output lifting, and validate an independent exact implementation or formal checker. The current source certificate was locally executed; independent review pending.

**Mother bridge.** Separately test an admissible encoder/decoder/observer mapping from the six-source ten-label `R_beh(k,10)` mother objective to this AV observer, retaining branch identity, shared parameters and multiplicity.

**Durable evidence.** This folder's PROOF.md, VERIFY.py, RUN_EVIDENCE.txt; GitHub Draft PR #1777, current immutable commit to be reported in the PR thread. GitHub identity `awdawmip` has write access; native control returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`, hence formal active owner/CLAIM/activity not confirmed. These are author-side mathematical artifacts pending independent review.
