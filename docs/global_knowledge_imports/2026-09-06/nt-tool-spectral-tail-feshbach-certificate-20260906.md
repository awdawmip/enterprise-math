# Spectral-tail Feshbach certificate and minimal future-safe repair rank

Record ID: `FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906`
Type: `FINDING`
Status: `VERIFIED`
Effective: `2026-09-06`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `Schur complement; Feshbach reduction; spectral projector; low modes; tail certificate; response operator; predictive quotient; finite certificate; RH`
Entities: `T2_BLOCK_FINITE_CERTIFICATE; T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA; T6_OPERATION_SAFE_QUOTIENT`
Sensitivity: `normal`
Confidence: `high`

## Statement

Adopt `SPECTRAL_TAIL_FESHBACH_CERTIFICATE` as a reusable theorem adapter over existing Enterprise block/quotient machinery.

It supplies an exact criterion for when an infinite or very large high-energy complement can be safely collapsed while retaining only a finite low-energy repair subspace and its future coupling ports.

This is not a new top-level T-family.

## 1. Setup

Let `H` be the old-state Hilbert space and `K` a future/shell port space. Consider a self-adjoint block operator/form

`M = [[A, B], [B*, D]]`

with

- `A>0` on `H`;
- `D>0` on `K`;
- `B : K -> H` the declared future coupling.

Let `P` be an orthogonal spectral projector for `A` and put `Q=I-P`. Because `P` is spectral, `P,Q` reduce `A`:

`A = A_P direct_sum A_Q`.

Assume

`A_Q >= alpha I`, `alpha>0`,

and

`D >= delta I`, `delta>0`.

Define the high-complement response

`R_Q := B* Q A_Q^(-1) Q B`.

## 2. Exact and coarse high-tail certificates

Since

`A_Q^(-1) <= alpha^(-1) I`,

one has the operator inequality

`0 <= R_Q <= alpha^(-1) B*Q B`

and therefore

`R_Q <= (||QB||^2/alpha) I`.

Consequently the complement-screened future block

`E_P := D-R_Q`

satisfies

`E_P >= [delta-||QB||^2/alpha] I`.

Hence the finite sufficient condition

`||QB||^2 < alpha delta`

implies

`E_P>0`.

This is the coarse `SPECTRAL_TAIL_CERT`.

A sharper exact normalized tail coordinate is

`chi_exact(P) := ||D^(-1/2) R_Q D^(-1/2)||`.

Then

`E_P>0 <=> chi_exact(P)<1`.

Thus `chi_exact` is the natural future-visible tail response; `||QB||^2/(alpha delta)` is only its convenient majorant.

## 3. Finite Feshbach reduction after tail certification

Once `E_P>0`, eliminate the high complement `QH`. The remaining problem is the finite/retained block

`F_P := A_P - P B E_P^(-1) B* P`.

The original block is positive definite iff

`E_P>0` and `F_P>0`.

If `P` has finite rank `r`, the entire hard low-energy response is therefore represented by an `r`-dimensional Feshbach matrix/operator after a theorem-certified high-tail collapse.

This is the exact justification for the pattern

`LOW CRITICAL MODES + CERTIFIED HIGH TAIL`.

## 4. Minimal future-safe repair rank

Suppose `A` has ordered eigenpairs `(lambda_j,phi_j)` in the discrete regime relevant to the declared problem and let `P_r` project onto the first `r` eigenmodes.

Define the exact repair rank

`r_safe := min { r : chi_exact(P_r)<1 }`

when such an `r` exists.

A readily checkable sufficient repair rank is

`r_coarse := min { r : ||Q_r B||^2 < lambda_(r+1) delta }`,

where `D>=delta I`.

These definitions are **observer-relative**: changing the future coupling `B` changes the repair rank even when `A` is unchanged.

Therefore

`SPECTRAL DIMENSION != PREDICTIVE REPAIR DIMENSION`

unless a theorem connects the relevant spectral concentration to the declared future port.

## 5. BRC / Enterprise interpretation

Coverage verdict: `COMPOSE_EXISTING_TOOLS`.

- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` for block elimination, finite retained certificates and obstruction extraction.
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`. The high complement is discarded only after all future influence needed by the declared operation has been retained through `R_Q` or bounded by `chi_exact`/the tail majorant.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` at the level of theorem-supplied finite effective dimension/capacity; it does not itself choose the spectral projector.

The important BRC law is:

`LOW EIGENVALUE != KEEP IT` and `HIGH EIGENVALUE != DISCARD IT`.

A mode is safely discardable only when its **future-port response** is certified small relative to its energy denominator.

## 6. Relation to Landau-Widom / prolate critical dimensions

For classical time-band limiting, prolate eigenvalues have an effective transition near the Shannon number

`N_Sh = 2 L T / pi`,

with a logarithmic-width plunge region.

This theorem can suggest a finite candidate projector `P` only after a separate **spectral localization bridge** proves that the future coupling `B` is concentrated in the associated time-band subspace.

Thus the desired application pipeline is

`TIME-BAND THEOREM -> CANDIDATE CRITICAL PROJECTOR P`

plus

`COUPLING LOCALIZATION -> ||QB|| or chi_exact(P) small`

then

`SPECTRAL_TAIL_FESHBACH_CERT -> SAFE HIGH COMPLEMENT COLLAPSE`.

Without the middle localization theorem, quoting a Shannon number does not certify a repair rank.

## 7. RH square-shell specialization

For the square-shell Weil form,

`A=A_n`, `B=B_n`, `D=D_n`,

and existing work gives a shell lower bound

`D_n >= (log n-C)I`

for large `n`.

The new exact target is therefore to construct a spectral projector `P_n` satisfying

`chi_exact(P_n)<1`

or the sufficient bound

`||Q_n B_n||^2 < lambda_(r+1)(A_n) [log n-C]`.

The 2026-09-06 floating experiments suggest that a candidate repair dimension may scale like

`4 n^2 log n`,

the Landau-Widom/Shannon number obtained from the observed compact-window frequency `T*(log n)=2 pi n^2`.

That scaling is recorded separately as a testing hypothesis. The present theorem is unconditional linear/operator algebra and does not assert the scaling.

## 8. Hard boundaries

1. `chi_exact(P)<1` concerns only the declared next/future port represented by `B`; it is not automatically a Markov-complete state for arbitrary later operations.
2. A spectral projector must actually reduce `A`; arbitrary coordinate truncation introduces off-diagonal old-old terms and needs a more general block treatment.
3. `||QB||^2 < alpha delta` is sufficient, not necessary. Failure of the coarse bound does not falsify positivity.
4. A finite numerical estimate of `chi_exact` is a theorem only with certified operator/tail enclosures.
5. A prolate/Shannon dimension is not a Weil repair dimension without a theorem controlling the coupling tail.

## Provenance

- Source kind: `exact mathematical derivation + current tool-reuse audit`
- Source reference: `standard Schur/Feshbach calculus; T2/T6 Enterprise interfaces; HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
- Observed/recorded at: `2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `none`
- Conflicts with: `none`
- Related: `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906; FINDING-EM-NT-RH-GROUND-STATE-FESHBACH-LEAKAGE-20260905; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-HAAR-SCHUR-20260905`
