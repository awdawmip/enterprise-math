# Native Enterprise C3 primorial-shell resonance versus Hardy-Littlewood null

Status: `FREE_RESEARCH_NULL_COMPARISON / NEGATIVE_NOVELTY_RESULT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_CRT_PROJECTED_PRIME_EQUIDISTRIBUTION_20260823.md`

## 1. Question

The CRT collapse tower makes the prime-fiber distribution look increasingly regular. Test whether the whole-shell full-bright count contains a stable residual not already explained by the classical Hardy-Littlewood local model.

For shell r, the C3 fibers are

`B_r+t`, `B_r+t+r`, `B_r+t+2r`, `0<=t<r`.

Let `T(r)` be the number for which all three entries are prime.

## 2. Classical matched null

For the offset set `{0,r,2r}`, let

`nu_q(r)=1` if `q|r`,

and `nu_q(r)=3` otherwise, with the usual small-prime interpretation.

The truncated singular series is

`S_Q(r)=product_{q<=Q} (1-nu_q(r)/q)/(1-1/q)^3`.

The matched smooth prediction is

`E_Q(r)=S_Q(r) * integral_0^r dt / [log(B_r+t) log(B_r+t+r) log(B_r+t+2r)]`.

The product is numerically stable by `Q=500000` for the shells reported below.

This is a classical prime-tuple null, not an Enterprise theorem.

## 3. Exact finite counts versus prediction

For exact primorial shells where the labels remain below `2^64`, deterministic primality enumeration gives:

| d | r=P_d | actual T(r) | HL prediction | actual/predicted |
|---|---:|---:|---:|---:|
| 2 | 6 | 1 | ~0.54037 | ~1.8506 |
| 3 | 30 | 0 | ~0.91593 | 0 |
| 4 | 210 | 3 | ~2.63353 | ~1.13916 |
| 5 | 2310 | 18 | ~12.32972 | ~1.45989 |
| 6 | 30030 | 95 | ~83.11265 | ~1.14303 |
| 7 | 510510 | 794 | ~789.23347 | ~1.00604 |
| 8 | 9699690 | 9330 | ~9276.08717 | ~1.00581 |

At d=7 and d=8 the relative discrepancy is only about 0.6 percent.

Using a crude Poisson scale `sqrt(E)` as a diagnostic, the discrepancies are well within ordinary counting fluctuation; in particular the d=7 and d=8 residuals are substantially below one such standard-deviation scale.

## 4. Projection-correlation ablation

On the exact d=8 primorial shell, projection from U(P_8) to U(P_7) initially showed a mild deficit of lower states with three or more bright lifts relative to an independent-lift binomial null.

This candidate residual was tested on two additional shells carrying the same first eight prime channels:

- `r=2P_8`: 16642 bright fibers;
- `r=3P_8`: 22596 bright fibers.

The apparent deficit does not persist. The grouped lift-multiplicity chi-square against the simple binomial baseline drops from about 7.84 at `P_8` to about 0.082 at `2P_8` and about 2.28 at `3P_8`.

Therefore the initial adjacent-lift anomaly is rejected as a stable native signal.

## 5. Verdict

The currently tested observables show:

1. strong visual/algebraic regularization in the native CRT collapse coordinates;
2. near-uniform lower-dimensional shadows;
3. whole-shell counts quantitatively compatible with the classical Hardy-Littlewood singular-series model;
4. no stable adjacent-projection correlation residual in the first ablation.

Freeze:

`NATIVE_COORDINATE_REGULARIZATION = REAL`.

`ARITHMETIC_NOVELTY_BEYOND_CLASSICAL_LOCAL_SIEVE = NOT YET DETECTED`.

This is an important negative result. It means the coordinate system is useful for exposing the known local structure cleanly, but no claim of a new prime law should be made from these statistics.

## 6. Next route

The next search should avoid merely re-measuring local congruence density. Candidate observables must depend on the collapse map itself, for example:

- information loss between adjacent CRT levels;
- persistence/branching of the same bright fiber under dimension extension;
- correlations between shell index changes and downward-collapse classes after singular-series normalization;
- alternative native allocation/collapse rules whose residuals differ from the classical AP null.

Any next candidate must be compared against a matched singular-series baseline from the outset.
