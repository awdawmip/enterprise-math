# BRC transport/residual extension — extracted reusable result

Status: `RESEARCH_RESULT_EXTRACT / TOOL_CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-19`
Source research: `research_notes/brc_transport_extension_20260919_AD0416/RESEARCH_NOTE.md`

## Result

For finite positive-rational BRC branches carrying a total rational affine action, use atoms

`[w,A,b]`, with `w>0` and `x -> A x+b`.

Alternative composition recoalesces identical `(w,A,b)` atoms by multiplicity. Serial composition, first left then right, is

`[w,A,b] * [v,B,c] = [wv, BA, B b+c]`.

The law is associative and distributive. Forgetting affine effects is a homomorphism to the existing exact BRC `WeightHistogram` alternative/serial operations, so this is an extension of T0 BRC rather than a replacement carrier.

The weight/action association is essential: equal weight marginals plus equal action marginals do not determine future weighted observations.

For homogeneous second moment state

`M(mu)=sum_x mu(x) [x;1][x;1]^T`,

an affine effect histogram acts exactly by

`L_H(M)=sum_(w,A,b) multiplicity*w*Abar*M*Abar^T`.

Therefore fixed state-independent affine branch packets preserve exact degree-2 polynomial observations under arbitrary finite serial composition. In six spatial coordinates this symmetric homogeneous moment state has 28 independent rational entries. This is an observer-scoped exact contraction, not complete path-memory compression and not constant-bit memory.

## Typed failure boundaries

- Positive branch mass does not cancel merely because signed spatial displacement or first moment cancels.
- Degree-2 moments do not preserve occupancy, thresholds, fourth moments, or arbitrary nonlinear recall.
- Conditional/state-dependent weights, partial actions, typed ports, hidden-history access, or path-label-sensitive observers require a richer carrier or separate proof.
- Rational inverse/comparison matrices are readout tools; they do not license fractional native Cell moves.
- Mixed-radix quotient/remainder helpers preserve exact arithmetic identity but do not imply path dependence is universally necessary.

## Extracted tool

`src/enterprise_math/brc_transport.py`

Reusable interfaces:

- `Affine`
- `EffectHistogram`
- `MomentState`
- `point_moment`, `explicit_moment`
- `factor_defect`
- `euclidean_digits`, `recompose`

Regression tests: `tests/test_brc_transport.py`.

The executable source is discoverable as a T0 BRC subtool. It remains a research-extracted executable candidate pending ordinary independent review/admission; this file does not promote any theorem to Foundation.
