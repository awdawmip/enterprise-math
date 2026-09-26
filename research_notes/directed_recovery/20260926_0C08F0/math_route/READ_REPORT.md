# Read-only intake: complete Shor output rather than local moment closure

Frozen local Git head: `0852cad130c1d877174d235687cf60c19f318c58`.
Global knowledge read: `6dff66ce260d85fc0244598cae4c527ccc133e4f`.
This report records source inspection, not a fresh scientific computation or acceptance.

## Exact endpoint already implemented

`stage80/fixed_phase.py` defines the existing ACTUAL_TYPED_BRC_ONLY circuit executor:

- `prepare_fixed(N,a,t,dim)` inherits actual native H4 preparation and full reversible modular multiplication; its inputs do not include the order or factors.
- `run_qft(state,den,t,bank,dim)` retains work, spectator and all completion modes.
- `law(state,den,t)` returns all integer squared masses `nums[k]` with common denominator `den**2`, proving their sum equals that denominator.
- The denominator is dyadic; reduction only removes common powers of two.
- The stage80 source explicitly retains a full-space gate error certificate and its circuit telescoping bound.
- `stage78/shor_benchmark.py:classical_postprocess` checks returning exponents by actual BRC modular powers, then uses the actual BRC Euclid trace. It does not claim a verified returning exponent is necessarily the minimal order.

This is already a finite, generally exponential, complete probability computation. Stage87's 39 scalars are for its declared two-label, one-phase future language and are not an additional precondition for this full Shor endpoint law.

## Distinct possible closure route

Use the declared finite schedule and full endpoint/history measure as the primary object. A uniform induction over the actual gate/instrument composition can establish exactness of a finite recursive simulator, while a separate trace/total-variation argument transfers the existing full-space compilation bound through readout and classical postprocessing. This does not require expanding a fixed local moment interface whenever the future circuit is enlarged.

The current code does not expose an exact sampling API. It explicitly says no sampling/new random seed in its prior acceptance. An optional external random-tape adaptor can be specified separately from native BRC dynamics; a dyadic terminal distribution admits finite exact inversion using a uniformly distributed integer in `[0,den**2)`. This would close a software sampling interface, not derive an internal physical Born rule or justify a new native random source.

## Sources inspected

- `stage78/shor_benchmark.py`, `stage78/README.md`, `stage78/PROOF.md`
- `stage79/phase_compiler.py`
- `stage80/fixed_phase.py`, `stage80/PROOF.md`, `stage80/TEST_CONTRACT.json`, `stage80/BRC_CONTRACT.json`
- `stage85/predictive_reader.py`
- `stage87/operator_moments.py`, `stage87/PROOF.md`, `stage87/BOUNDARY_CONTRACT.json`, `stage87/REFERENCES.md`

No external trigonometric, ordinary QFT or higher-precision replacement was run. No remote writes were made.
