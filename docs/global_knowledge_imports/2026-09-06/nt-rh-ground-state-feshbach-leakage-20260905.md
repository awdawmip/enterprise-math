# Ground-state Feshbach leakage criterion for Weil window propagation

Record ID: `FINDING-EM-NT-RH-GROUND-STATE-FESHBACH-LEAKAGE-20260905`
Type: `FINDING`
Status: `VERIFIED_REDUCTION`
Effective: `2026-09-05`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `Riemann hypothesis; Weil form; Feshbach map; ground state; rank-one update; boundary leakage; de Branges; Schur complement; BRC`
Entities: `T2_BLOCK_FINITE_CERTIFICATE; T6_OPERATION_SAFE_QUOTIENT; FINDING-EM-NT-WEIL-WINDOW-BOUNDARY-RESPONSE-20260905`
Sensitivity: `normal`
Confidence: `high for exact block reduction; research-level for RH application`

## Statement

When the old Weil-window block has a simple near-null ground state, do not control its inverse through the global minimum eigenvalue. Split the ground state off exactly, screen all higher modes into a complement response, and reduce the remaining positivity condition to a scalar ground-state leakage inequality **provided the screened complement remains quantitatively positive**.

The algebraic rank-one reduction below is exact. Subsequent 2026-09-06 numerical pressure tests show that, for square-shell Weil propagation, using only one retained ground mode is not a robust predictive-complete state: screening the remaining old modes can recreate a near-null shell direction. See `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`.

This is a standard two-stage Schur/Feshbach reduction applied with BRC port discipline; it is not a new generic tool family and not an RH proof.

## 1. Exact rank-one reduction

Let the old window block be positive and have a simple normalized ground eigenvector `phi`:

`A phi=lambda phi`, `lambda>0`.

Write

`A=lambda P + A_perp`,

where `P=|phi><phi|` and `A_perp` is the restriction to `phi^perp`.

For an old-to-new-shell coupling `B`, define

`v:=B* phi`,

`R_perp:=B* A_perp^(-1) B`,

and the complement-screened shell block

`E:=D-R_perp`.

The full old-window response is

`B* A^(-1) B = lambda^(-1) v v* + R_perp`.

Therefore the shell Schur complement is exactly

`S = E - lambda^(-1) v v*`.

Assume first that `E>0`. Then the rank-one update criterion gives

`S>0  <=>  <v,E^(-1)v> < lambda`.

For positive semidefiniteness replace `<` by `<=` with the usual kernel compatibility conditions.

Proof: conjugate by `E^(-1/2)` and use that `I-lambda^(-1)|w><w|` is positive definite iff `||w||^2<lambda`, where `w=E^(-1/2)v`.

## 2. Dimensionless leakage coordinate

Define

`rho := <v,E^(-1)v>/lambda`.

Then, once `E>0` is certified,

`full next-window positivity <=> rho<1`.

The vanishing old spectral margin is paired with exactly the same ground state's future-port visibility. A tiny `lambda` is not by itself an obstruction; only the normalized leakage ratio matters.

This is the precise repair to the crude inequality

`B* A^(-1)B <= ||B||^2/lambda`.

## 3. Multi-low-mode version

For a finite low-energy subspace `P` with old block `A_low=PAP`, let `A_high` be the complement and set

`E=D-B* A_high^(-1)B`.

After the high-mode response has been screened into `E`, positivity reduces to the finite Feshbach block

`A_low - P B E^(-1) B* P >0`,

or equivalently to the corresponding normalized finite matrix singular-value condition.

Thus a finite set of near-null modes can be retained explicitly while the safe high-energy complement is collapsed.

This is the exact mathematical basis for the `LOW MODES + CERTIFIED TAIL` response architecture. The 2026-09-06 evidence indicates that the required low-mode dimension is not fixed and may scale like the Landau-Widom/Shannon critical dimension.

## 4. First-zero compatibility

If `lambda=0` at a hypothetical first window of semidefinite failure, positive semidefiniteness of the enlarged block forces

`B*phi=0`.

So an exact old-window null mode can persist into a larger positive window only if it is invisible to the newly opened shell port.

In the positive approach to a first zero, the scalar `rho` remains a natural diagnostic for an isolated one-mode reduction, but it is not a complete state if the screened complement itself has near-null directions.

## 5. RH square-shell specialization

At square-shell step `n`, use

`A=A_n`, `B=B_n`, `D=D_n`.

The shell-coercivity theorem gives

`D_n >= (log n-C)I`

for large `n`.

The exact program is therefore:

1. choose a retained low-energy projector `P_n`;
2. certify the high/complement response

`E_n=D_n-B_n* A_high,n^(-1) B_n >0`;

3. solve the remaining finite Feshbach inequality on `P_n`.

The special rank-one choice `dim P_n=1` is algebraically valid but is no longer the preferred RH propagation target after the 2026-09-06 pressure test.

## 6. Real-zero / de Branges coordinate opportunity

Current certified work at support radius `L=0.8` proves that the ground state there is simple and even. The Connes–van Suijlekom real-zero theorem for lower-bounded convolution quadratic forms says that under the simple/isolated/even ground-state hypothesis the Fourier transform of the ground eigenfunction has only real zeros.

Therefore a retained one-dimensional low-mode port at that **same** certified window belongs to a much more rigid entire-function class than an arbitrary L2 vector.

However the exact square-shell chain is `L_n=log n`. The first square-shell block is `A_2=Q|H_log2`. The fact that `log2<0.8` certifies positivity of `A_2`, but the `L=0.8` ground eigenfunction is not the ground eigenfunction of `A_2` and must not be imported into the `n=2` Feshbach step.

A legitimate future direction is to construct corresponding real-zero/de Branges coordinates for the actual retained critical band at each square-shell window. What is missing is a theorem transporting that structure through window changes and controlling the finite response.

## 7. Landau-Widom scaling and 2026-09-06 update

The compact-window work observes the natural frequency

`T*(L)=2 pi exp(2L)`

and a Landau-Widom plunge. Classical time-band limiting has Shannon transition dimension

`N_Sh=2 L T/pi`.

Combining the two scales suggests

`N_Sh(L)=4 L exp(2L)`.

On 2026-09-06, floating multi-mode Feshbach pressure tests at square-shell steps `n=2,3,4` found complement-coercivity recovery crossovers roughly consistent with

`4 n^2 log n`:

- `n=2`: predicted `11.09`, observed crossover about `10-16`;
- `n=3`: predicted `39.55`, observed about `32-40`;
- `n=4`: predicted `88.72`, observed about `72-88`, with the screened floor essentially equal to the raw shell floor by `r=88`.

This is numerical structural evidence only. It motivates retaining a growing Landau-Widom critical band rather than a fixed number of low modes. Full details and numerical-source boundaries are recorded in `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`.

## 8. BRC / reuse resolution

Coverage verdict: `COMPOSE_EXISTING_TOOLS`.

- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` for two-stage block elimination and finite low-mode certificate.
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; the high complement is collapsed only after its exact future response has been retained.
- finite-dimensional Schur/rank-one infrastructure: standard existing algebra; no novelty claim.
- de Branges/real-zero coordinates: domain theorem adapter / research extension, not a BRC family.

Hard boundaries:

1. `GROUND STATE SIMPLE AT L=0.8 != SIMPLE FOR ALL L`.
2. `L=0.8 GROUND STATE != H_log2 GROUND STATE`.
3. `REAL FOURIER ZEROS OF A GROUND STATE != ZETA ZEROS`.
4. `E>0` must be proved before using the scalar rank-one criterion.
5. A shrinking `lambda` cannot be dropped from the state; it is part of the normalized leakage coordinate.
6. `RANK-ONE FESHBACH IDENTITY != RANK-ONE PREDICTIVE COMPLETENESS`.
7. Single-step leakage is not a Markov-complete state for arbitrary future shells unless the future operation family is declared and the corresponding multi-port response retained.

## Smallest unresolved unit

Replace the rank-one propagation target by a **critical-band Feshbach certificate**. For the first square-shell steps, construct the actual `H_log n` low-energy projectors and certify with interval arithmetic that retaining approximately the predicted critical dimension restores a quantitative high-complement shell floor. Then seek a theorem-level prolate/Weil comparison proving or falsifying the scale

`dim P_L ~ 4 L exp(2L)`.

This is the current smallest robust unit; do not repeat a direct `L=0.8` ground-vector leakage test as though it were the `n=2` square-shell step.

## Provenance

- Source kind: `exact linear-algebra derivation + current spectral literature + 2026-09-06 numerical pressure test`
- Source reference: `FINDING-EM-NT-WEIL-WINDOW-BOUNDARY-RESPONSE-20260905; arXiv:2608.24827v2; Connes–van Suijlekom real-zero theorem; HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
- Observed/recorded at: `2026-09-05; updated 2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `FINDING-EM-NT-WEIL-WINDOW-BOUNDARY-RESPONSE-20260905`
- Conflicts with: `none`
- Related: `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-HAAR-SCHUR-20260905; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-PORT-DECOMP-20260905`
