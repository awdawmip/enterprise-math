# R061 Stage 3 — Bidirectional Length Spectrum

Researcher-ID: `EM-R061S3-2F9622`

For an unordered endpoint pair define

`SPEC_E(P,Q) = multiset{ ell_E(P->Q), ell_E(Q->P) }`.

For exact computation one may equivalently store

`QSPEC_E(P,Q) = multiset{ ell_E(P->Q)^2, ell_E(Q->P)^2 }`

because square root is injective on nonnegative values.

## Orbit theorem

The ordered directed-gauge pair is

`(ell_f,ell_r)`.

Endpoint swap acts by `(ell_f,ell_r)->(ell_r,ell_f)`. Its exact orientation-free orbit is the multiset `SPEC_E`.

Hence `SPEC_E` is the minimal lossless orientation-free scalar-data quotient of the two frozen directed gauges. Any orientation-free datum that preserves both gauge values factors through this swap orbit.

The multiset does not choose which member is “the” segment length.

## Properties

- endpoint-swap symmetry: exact;
- translation invariance: exact because both directed gauges depend only on translated displacement decode;
- positivity: `{0,0}` exactly for `P=Q`, otherwise both entries are positive;
- scaling: `SPEC_E(P,P+k(Q-P)) = k SPEC_E(P,Q)` for integer `k>=0`;
- cyclic covariance: cyclic component relabeling preserves the spectrum;
- axis gluing: chart duplication does not duplicate a gauge entry;
- oriented recovery: once one member of `BSEG_E` is selected by endpoint order, its associated directed gauge is recovered exactly.

## Mandatory spectra

- one positive-axis tick: `SPEC={1,sqrt(2)}`;
- opposite direction of that same carrier axis: the same unordered spectrum `{1,sqrt(2)}`;
- translated `(1,1)`: `D_f=(1,1,0)`, `D_r=(0,0,1)`, so `SPEC={1,sqrt(2)}`;
- translated `3-4-5`: `D_f=(3,4,0)`, `D_r=(1,0,4)`, so `SPEC={sqrt(17),5}`;
- reversal-symmetric example: `D_f=(2,1,0)`, `D_r=(0,1,2)`, so `SPEC={sqrt(5),sqrt(5)}`;
- radical example: `D_f=(2,3,0)`, `D_r=(1,0,3)`, so `SPEC={sqrt(10),sqrt(13)}`.

The checker hashes all `3321` unordered pairs on the Stage 2 patch to

`e1e8b729506277d662a5654d7cf076f860687dc8073984a296d96d3bc85fca6a`.
