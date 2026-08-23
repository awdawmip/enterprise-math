# FQ010 — Observation-Resolution Countermodels

Researcher-ID: `EM-FQ010-CA2555`

## Purpose

`R_type` is canonical relative to the exact component observation `tau`, but FQ010 must not confuse that relative universal property with a proof that component identity is the only possible observation resolution relevant to scale.

Three exact resolutions are therefore compared without using the current length formula as a selector.

Let `U` be the token carrier with component multiplicities `(n_c)` and total token count

`N=sum_c n_c`.

## 1. Finer observation — occurrence identity

Retain every token occurrence as distinct:

`obs_fine(x)=x`.

Its kernel is the diagonal relation

`R_fine=Delta_U={(x,x):x in U}`.

This relation is canonical under token renaming. Its ordinary finite cardinality is

`Q_fine=|Delta_U|=N=sum_c n_c`.

On one axis,

`Q_fine(n,0)=n`,

so it fails axis-square calibration for `n>1`.

In a two-channel sector `Q_fine(a,b)=a+b`, whose mixed second difference is `0`.

Thus occurrence resolution captures transition/word-count scale, not the FQ008 square calibration.

## 2. Component-typed observation

Retain exactly the supplied component type:

`obs_comp=tau`.

Its kernel is

`R_type={(x,y):tau(x)=tau(y)}`.

The maximality theorem proves this is the unique greatest equivalence relation preserving the exact component observation.

Its cardinality is

`Q_comp=|R_type|=sum_c n_c^2`.

On a two-channel sector,

`Q_comp(a,b)=a^2+b^2`.

Therefore it satisfies both:

- axis-square calibration;
- zero mixed second difference.

## 3. Coarser observation — forget component identity

For nonempty `U`, take the constant observation

`obs_coarse(x)=*`.

Its kernel is the universal relation

`R_coarse=U x U`.

For the empty carrier use the empty relation.

Its cardinality is

`Q_coarse=N^2=(sum_c n_c)^2`.

On one axis this still satisfies

`Q_coarse(n,0)=n^2`.

But on a two-channel sector

`Q_coarse(a,b)=(a+b)^2=a^2+b^2+2ab`,

so

`Delta_a Delta_b Q_coarse = 2`,

not `0`.

Thus axis square alone cannot distinguish component resolution from fully coarse resolution; transverse independence removes the coarse cross-component pairs.

## 4. Exact discriminator

At axis multiplicity `n=2`:

- fine: `2`;
- component: `4`;
- coarse: `4`.

For the mixed second difference:

- fine: `0`;
- component: `0`;
- coarse: `2`.

Therefore the **joint** FQ008 conditions distinguish the component-kernel cardinality from these two canonical neighboring resolutions:

- axis square rejects the finer occurrence count;
- transverse independence rejects the coarser universal-pair count.

This is a nontrivial comparison, not merely formula restatement.

## 5. What is N0-forced and what is an N2 choice?

N0 supplies enough structure to define all three relations:

- token equality gives the diagonal;
- component typing gives `R_type`;
- the token carrier gives the universal relation.

N0 additionally gives a universal property only to `R_type` **relative to preserving exact component observation**.

N0 does not by itself state that line scale must stop at exactly that observation resolution. Selecting which observation should feed the scale readout is therefore an N2 semantic-resolution decision unless independently justified.

## 6. Does line semantics independently favor component resolution?

The allowed downstream calibration source

`definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@9866e523b7e7f134497d8aca9ba2b6a093600257`

contains a non-scalar statement independent of its length formula:

`ENTERPRISE_LINE_IDENTITY = NATIVE_COMPONENT_TRACE`.

The trace quotient identifies shuffle-equivalent paths while preserving component content. This provides independent downstream evidence that the line object itself is observed at component-content resolution rather than occurrence identity or total component erasure.

This evidence is used only after `R_type` and all three countermodels are constructed. It therefore does not leak the current scalar formula into the Foundation premise.

However, component-trace semantics still does not uniquely select **cardinality** among all possible scalar valuations of `R_type`. The scale-role step remains N2.

## Result

`OBSERVATION_RESOLUTION_ALTERNATIVES_PRESSURE_TESTED = PASS`.

`COMPONENT_RESOLUTION_IS_RELATIONALLY_CANONICAL_RELATIVE_TO_TAU = TRUE`.

`COMPONENT_RESOLUTION_IS_THE_ONLY_N0_DEFINABLE_RESOLUTION = FALSE`.

`NONSCALAR_LINE_TRACE_CALIBRATION_FAVORS_COMPONENT_RESOLUTION = TRUE`.

`CARDINALITY_SCALE_ROLE_STILL_REQUIRES_SEMANTIC_SELECTION = TRUE`.
