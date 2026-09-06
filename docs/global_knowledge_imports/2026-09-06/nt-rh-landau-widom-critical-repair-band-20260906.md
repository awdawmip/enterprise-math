# Landau–Widom critical repair-band hypothesis for Weil square-shell propagation

Record ID: `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
Type: `HYPOTHESIS`
Status: `TESTING`
Effective: `2026-09-06`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `Riemann hypothesis; Weil form; square-shell propagation; Feshbach; Schur response; Landau-Widom; prolate spheroidal; Shannon number; time-bandwidth; BRC repair coordinate`
Entities: `T2_BLOCK_FINITE_CERTIFICATE; T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA; T6_OPERATION_SAFE_QUOTIENT; FINDING-EM-NT-RH-GROUND-STATE-FESHBACH-LEAKAGE-20260905; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-HAAR-SCHUR-20260905`
Sensitivity: `normal`
Confidence: `medium-high as a numerical structural hypothesis; not a theorem and not an RH proof`

## Statement

The square-shell Weil response appears not to admit a predictive-complete **fixed-rank** low-energy reduction. Numerical pressure tests at the first three square-shell steps indicate that the smallest old-window low-energy subspace that must be retained before the screened shell block recovers its original coercive scale has dimension comparable to the classical Landau-Widom / Shannon time-bandwidth number

`d(L) := 2 L T*(L) / pi`,

with the compact-window frequency observed in current Weil work

`T*(L) := 2 pi exp(2L)`.

Therefore

`d(L) = 4 L exp(2L)`.

At the canonical square-shell points `L_n=log n`, this becomes

`d_n = 4 n^2 log n`.

Proposed structural law:

`PREDICTIVE-COMPLETE LOW-ENERGY REPAIR CARRIER DIMENSION ~ 4 L exp(2L)`.

This is currently a **testing hypothesis** supported by three finite numerical models and the independent prolate/Landau-Widom scale. No theorem presently identifies the Weil Schur repair rank with the Shannon number.

## 1. Why the rank-one route was too coarse

For one square-shell step write

`M = [[A,B],[B*,D]]`.

The exact rank-one Feshbach reduction around a simple old ground state `phi` is valid algebraically. However a high-frequency finite model of the first step `H_log2 -> H_log3` gave

- old ground eigenvalue around `1e-12` in the tested truncations;
- `D` shell floor around `2e-3`;
- rank-one normalized leakage `rho=<v,E^-1 v>/lambda` numerically within roughly `0.999 .. 1.001` depending on truncation/tail settings;
- after screening all old modes except the ground state, the complement-screened shell block `E` itself again had a near-zero eigenvalue around `1e-12`.

Thus screening the entire orthogonal complement into one response recreates a new near-null direction in the shell. The issue is not solely one ground-state leakage scalar.

This does **not** refute the exact rank-one Feshbach identity. It refutes its use as a robust fixed-rank predictive state in the tested Weil-window setting.

## 2. Multi-low-mode numerical experiment

Let `P_r` retain the first `r` old eigenmodes. Screen only the remaining high complement:

`E_r := D - B* A_high(r)^(-1) B`.

The experiment asks when `lambda_min(E_r)` recovers the natural scale of `lambda_min(D)`.

The arithmetic-side form was reconstructed in a support-exact mixed sine basis. Archimedean terms were integrated numerically; prime-power shifts and pole vectors were evaluated from the explicit formulas. These are **floating exploratory computations**, not interval certificates.

### Step n=2

`L=log2`, predicted Shannon dimension

`d_2=4*2^2*log2 ~= 11.09`.

Representative screened-shell floors:

- `r=1`: about `4e-12`;
- `r=2`: about `1.3e-10`;
- `r=4`: about `1.7e-9`;
- `r=6`: about `1.7e-7`;
- `r=8`: about `4e-5`;
- `r=12`: about `2e-4`;
- `r=16`: about `2e-3`, essentially the raw shell floor.

Observed repair crossover: roughly `r ~ 10-16`.

### Step n=3

`d_3=4*3^2*log3 ~= 39.55`.

Raw shell floor was about `9.7e-2`. The screened floor remained close to zero through small `r`, was about `1.3e-4` at `r=24`, about `3.6e-2` at `r=32`, and about `6.2e-2` at `r=40`.

Observed repair crossover: roughly `r ~ 32-40`.

### Step n=4

`d_4=4*4^2*log4 ~= 88.72`.

Raw shell floor was about `0.250`. Representative screened floors:

- `r=40`: `4.2e-6`;
- `r=56`: `1.1e-3`;
- `r=64`: `1.78e-2`;
- `r=72`: `0.112`;
- `r=80`: `0.158`;
- `r=88`: `0.245`;
- `r>=96`: about `0.246-0.250`.

Observed full-coercivity recovery: `r ~ 88`, essentially the predicted `88.72`.

### Three-point comparison

| `n` | `4 n^2 log n` | numerical repair crossover |
|---:|---:|---:|
| 2 | 11.09 | about 10-16 |
| 3 | 39.55 | about 32-40 |
| 4 | 88.72 | about 72-88 |

The agreement is strong enough to justify a focused hypothesis, but three numerical points are not a proof or asymptotic law.

## 3. Prolate / Landau-Widom interpretation

For a time interval of half-width `L` and frequency band `[-T,T]`, the classical time-band limiting operator has transition/critical dimension at the Shannon number

`N_Sh = 2 L T / pi`,

up to the familiar logarithmic-width plunge region.

Current compact-window Weil computations observe their near-null scale at

`T*(L)=2 pi exp(2L)`

and a Landau-Widom eigenvalue plunge law. Substituting this observed frequency gives exactly

`N_Sh(L)=4 L exp(2L)`.

This independently predicts the same dimension that appeared in the square-shell response experiment.

What is **not** yet proved is the bridge

`PROLATE CRITICAL DIMENSION -> WEIL SCHUR REPAIR DIMENSION`.

The new research task is to establish, weaken, or falsify that bridge.

## 4. BRC interpretation

Coverage verdict: `COMPOSE_EXISTING_TOOLS / EXTEND_DOMAIN_ADAPTER`.

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`. A low-energy complement may be collapsed only after retaining the future shell response. The numerical result shows that a one-dimensional port is not sufficient in the tested state.
- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` for multi-mode Feshbach/Schur elimination.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` conceptually for the theorem-supplied finite effective dimension / capacity threshold; no new T4 theorem is claimed.
- Prolate/Landau-Widom theory supplies the candidate domain capacity scale; it is not a new BRC family.

BRC lesson:

`SMALLEST CONVENIENT CARRIER != SMALLEST FUTURE-SAFE CARRIER`.

For this problem the repair coordinate may be a growing critical band rather than a scalar ground port.

## 5. Corrected base-window semantics

The square-shell chain is `L_n=log n`. Its first exact step is

`log2 -> log3`.

The certified `L=0.8` positivity result implies positivity of the smaller base window `H_log2`, but the `L=0.8` ground eigenfunction is **not** the ground eigenfunction of `A_2=Q|H_log2`.

Therefore any base-step leakage experiment must reconstruct/certify the `H_log2` low-energy band itself. One must not import the `L=0.8` ground vector into the `n=2` Schur step.

## 6. External numerical-source boundary

A public repository `Kuberwastaken/riemann` contains an independent arithmetic-side Weil numerical engine with sine bases, prime-power overlap matrices, pole directions, sweeps and profiles. Its visible experiments predate arXiv:2608.24827 and there is no verified provenance establishing it as Zhu's official certification code.

It was used only as a convention/reference check when reconstructing the exploratory model. No file from that repository is treated as the rigorous `L=0.8` certificate.

## 7. Consequences for the research route

### Downgrade

Do not pursue a theorem of the form

`ONE GROUND MODE + UNIFORM COARSE HIGH COMPLEMENT -> ALL WINDOWS`

as the primary RH route. The first-step numerical response is already critically saturated and the screened complement recreates near-null directions.

### New target

Construct a **critical-band Feshbach state** `P_L` of dimension near `4 L exp(2L)` and prove two properties:

1. `HIGH-COMPLEMENT COERCIVITY`: after screening modes outside `P_L`, the shell block has a quantitative positive floor comparable to its natural shell coercivity;
2. `FINITE CRITICAL RESPONSE`: the remaining old-shell interaction is represented by a finite matrix/operator on `P_L` plus shell ports, with exact arithmetic/Mellin structure retained.

At square-shell points this gives a finite but growing state of size `~4 n^2 log n`, polynomial in the natural multiplicative scale `n`, not fixed rank.

## 8. Smallest unresolved unit

Derive a theorem-level comparison between the Weil old-window high-energy projector and a prolate/time-band projector at band `T*(L)`, sufficient to prove a bound such as

`lambda_min(E_r) >= c * lambda_min(D)`

whenever

`r >= (1+epsilon) 4 L exp(2L)`

(or determine the correct replacement scale).

Before attempting RH closure, first certify the finite `n=2` and `n=3` repair curves with interval arithmetic to verify that the three-point phenomenon is not an integration/truncation artifact.

## Provenance

- Source kind: `exact Schur/Feshbach algebra + current literature + independent floating numerical experiment + repository coverage audit`
- Source reference: `arXiv:2608.24827v2; classical Landau-Widom/Slepian-Pollak time-band limiting; FINDING-EM-NT-RH-GROUND-STATE-FESHBACH-LEAKAGE-20260905; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-HAAR-SCHUR-20260905; public Kuberwastaken/riemann numerical engine (reference only)`
- Observed/recorded at: `2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `FINDING-EM-NT-RH-GROUND-STATE-FESHBACH-LEAKAGE-20260905`
- Conflicts with: `none`
- Related: `FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-PORT-DECOMP-20260905; FINDING-EM-NT-WEIL-WINDOW-BOUNDARY-RESPONSE-20260905`
