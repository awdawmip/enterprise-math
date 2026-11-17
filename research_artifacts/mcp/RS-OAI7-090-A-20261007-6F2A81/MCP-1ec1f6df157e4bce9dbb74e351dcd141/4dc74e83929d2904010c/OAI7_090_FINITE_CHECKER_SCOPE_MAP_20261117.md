# OAI7-090-A: finite certificate checker / analytic obligations, source-scope audit (2026-11-17)

Task: `RS-OAI7-090-A-20261007-6F2A81`; publication `TP2-79BD2127769C593E5315`.
Status: source-level audit draft; checker has not been executed in this environment, and this is not a proof review of the entire paper.

## Immutable source pins

- `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`
- `preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`, Git blob `23768a5c2d88e100399bb5c4347447e86a7160cb`.
- The paper's `build/main.tex`, blob `dad316cc2ad861a7482d79b46b6f840ed83d2a5e`.
- `verification/README.md`, blob `e2b9d904c74538450cea628476bcd6c772776c23`.

The README's documented execution is `python3 -I verification/check_certificate.py` with assertions enabled; zero exit and no output is the expected success signature. Neither the README nor the metadata is an execution receipt.

## Correspondence between checker assertions and the finite certificate

The relevant result is the paper's Lemma `lem:finite-certificate`, five numbered parts (main.tex around lines 1178–1400), with its explicit arithmetic appendix (around 2158–2280).

| Code procedure / assertion family | Paper proposition actually certified |
| --- | --- |
| `I`, `IQ`, `P`, `expo`, `ar`, `pit`, and interval assertions | Fixed-grid 10^60 denominator outward enclosures, complex rectangular intervals, Machin-type pi bracket and exponential truncation bounds, as described in the appendix's arithmetic justification |
| `getinv`: pivot bounds `0.12 < abs(pivot) < 1.74`, inverse norms `<16.16`, `<3.89` | Lemma finite-certificate part 1: the two 20×20 Gauss–Jordan systems `I-R` and `I+R` |
| `approxnorm(data[i]) < 2.58, 2.80` | Part 1: sup over parameter polytope of `||A_1 e||` and `||A_2 e||`; combination of first two columns before absolute values matters |
| `envtable` node tests `Q`, `D`, `svals` | Part 2: periodic node bounds on `Q_n,D_n` and 15 midpoint lower bounds for `P(s)/(s-m)^2` |
| `envtable` jet coefficient maps `W`, `Waves.coeff`, geometric period factors, alias and omitted-target sums | Part 3: `||W||<119`, four jet-envelope bounds, repetition factor and two omitted-target bounds |
| `envtable` curvature `Waves.curv` and `Waves.terr` at 5 listed radii and 14 signed half-cells | Part 4: raw curvature envelopes and the two Taylor remainder thresholds |
| `powsol`, `coeffpoly`, `bern`, `vmin`, `test` | Part 5: `T_2` and the modified negative `T_1` side signs uniformly over the declared parameter polytope and `tau in [0,1]`, with the exceptional `m=y=1` tests |

The ordinary sign-table count is **27 degree-20 polynomial tests**, 21 Bernstein coefficients each, across 14 signed half-cells: 28 naive side/half-cell tests minus one exceptional side-one case. The exception has **four degree-at-most-22 tests**, 23 rows each. Therefore the complete table requires exactly `27×21+4×23=659` Bernstein coefficient lower-bound checks. The source loops over the prescribed half-cells and implements this structure in `powsol`, using the convex minimum `vmin` on the parameter polytope.

The checker also performs `near` value comparisons for sanity anchors, including `Q_1,D_1`, selected `A_i` coordinates and the exceptional Bernstein row; these are reproducibility anchors rather than extra analytic theorems.

## Analytical obligations left beyond this Python checker

1. Establish the finite-atom interpolation identities and frequency-space representation, including the compatibility of the Laurent construction, jet maps and analytic variables.
2. Prove operator/derivative bounds uniform over the **entire infinite tail** (not merely the finite sums inserted into the checker), and contraction/inversion of the full correction system (paper Section `sec:infinite`).
3. Transfer the finite sign tables and Taylor/curvature envelopes to the **exact corrected interpolants** throughout each interval between all interpolation nodes; check the first-node exceptional interval and the unbounded tail (Section `sec:global-signs`).
4. Verify Fourier nonnegativity, pointwise Gaussian minorant and contact/zero conditions for all radii and all positive Gaussian parameters (including reciprocal duality for `0<alpha<1`).
5. Prove the centered-disk density Fourier comparison and the positive-mixture passage to completely monotone potentials, including singular or divergent energies (Section `energy:section`).

These are proof obligations of the paper, not assertions executed by `check_certificate.py`. The source README explicitly distinguishes the finite certificate from analytic propagation and energy transfer. A successful checker run alone establishes the finite arithmetic appendix at the pinned program/inputs, conditional on the arithmetic enclosure justification; it does not run the above analytic arguments.

## Highest-value follow-up for the exact task

Under a current authenticated owner, run the exact pinned script in an isolated Python 3 standard-library environment with assertions enabled, record interpreter version, command, exit code/stdout/stderr, code blob and wall time. Independently scrutinize the interval exponential remainder bound under the asserted `abs(w/1024)<=1` and the derivation of the parameter-polytope row minimum `eq:polytope-row-minimum`; then attach each program assertion block to Lemma 1–5 and document any unmatched finite inequality. Do not merge the paper's analytic proof scope with the checker receipt.
