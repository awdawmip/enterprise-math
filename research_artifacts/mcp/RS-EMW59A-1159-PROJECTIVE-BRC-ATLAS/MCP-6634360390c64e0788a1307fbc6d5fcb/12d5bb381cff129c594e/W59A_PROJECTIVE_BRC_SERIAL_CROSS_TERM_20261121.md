# W59A projective BRC atlas: exact two-branch serial-composition defect
Status: TASK_RESEARCH / exact conditional algebraic lemma and source-screen / NOT_REVIEWED / NOT_FOUNDATION
Date: 2026-11-21
Task: RS-EMW59A-1159-PROJECTIVE-BRC-ATLAS
Scope: the explicitly declared quadratic rotation-transfer sector of the W59A free-research notes. No general native X6 transfer or arbitrary BRC Schur reduction is claimed.

## Existing results consumed
The 2026-09-05 oriented rational BRC chart gives z=b/a, z ⊕ w=(z+w)/(1-zw), q(z)=4z²/(1+z²), and q([n]z)=R_n(q(z)). It already notes that the unoriented quotient forgets sign and is not safe for arbitrary serial composition. The division-polynomial note derives this semiconjugacy via integer polynomials. The complement-sheet and Ramanujan notes address spectral field/trace observers. This note sharpens the already-identified information-loss frontier with the exact missing coordinate and a minimal one-step witness.

Sources (immutable):
- enterprise-math@d5c3274743f1e4eee66f3685e56bf3c0d5a516a7:research_notes/BRC_ORIENTED_RATIONAL_ROTATION_CHART_AND_SPECTRAL_QUOTIENT_20260905.md
- enterprise-math@fe0871e6ff11563dd961c064c373b99020978c7a:research_notes/BRC_ROTATION_FORMAL_GROUP_DIVISION_POLYNOMIALS_20260905.md
- enterprise-math@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c:research_notes/PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md
- enterprise-math@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c:research_notes/RAMANUJAN_SUMS_AS_PROJECTIVE_SPECTRAL_GALOIS_TRACES_20260905.md

## Proposition: exact one-step missing cross-observer
Let z,w be real finite oriented chart coordinates. For 1-zw ≠ 0 define z⊕w=(z+w)/(1-zw); the homogeneous expression extends to the projective chart boundary 1-zw=0. Put
  u=q(z)=4z²/(1+z²),  v=q(w)=4w²/(1+w²),
  D=(1+z²)(1+w²),  κ(z,w)=8zw/D.
Then, for the homogeneous definition of q after serial composition,
  q(z⊕w)=u+v-uv/2+κ,
  κ²=u(4-u)v(4-v)/4.
Proof: [(1-zw)²+(z+w)²]=D, so q(z⊕w)=4(z+w)²/D. Directly u+v-uv/2=4(z²+w²)/D. Their difference is κ=8zw/D. Also u(4-u)=16z²/(1+z²)², proving the quadratic identity.

Thus the pair of scalar inputs (u,v) admits generically TWO output branches:
  u+v-uv/2 ± sqrt(u(4-u)v(4-v))/2.
The sign is the relative orientation sign of zw. On a generic real fiber with z,w ≠0, replacing z by -z preserves (u,v) but switches the two outputs. At chart endpoints where one oriented coordinate vanishes, both values coincide. The square root expression states branch values, not a new allowed primitive BRC operation.

Exact rational witness:
  z=w=1/2 => u=v=4/5, κ=+32/25, q(z⊕w)=64/25;
  z=-1/2, w=1/2 => u=v=4/5, κ=-32/25, q(z⊕w)=0.
Both input spectral scalars are identical, while the composed scalar differs. This is an exact obstruction to representing unrestricted serial composition by a single-valued F(u,v), even *inside* the declared rotation subalgebra.

## Scoped positive result / minimal repair
For the ONE specified serial operation and output observer q, (u,v,κ) is sufficient, and away from the degenerate fiber κ=0 a relative sign bit is necessary if u,v are fixed. The pair of oriented homogeneous states [a:b] and [c:d], with real coefficient normalization, is the algebraically closed carrier under arbitrary serial products. No claim that κ alone remains sufficient for arbitrarily many later independent compositions: future sign correlations can require full frame/provenance.

For synchronous repetition of ONE oriented input, the existing identity q([n]z)=R_n(q(z)) remains an observer-safe descent; it is not a justification for dropping sheet data under mixing with independently selected w.

## Native integration and audit boundary
This is an exact auxiliary transfer-sector theorem, not a proof that all native BRC modules, P000 X6 spatial rotations or full projective spectral root-block carriers lie in this subalgebra. Native adoption requires an explicit typed Schur/port reduction, preserving ordered joint-path provenance, branch/frame data and declared future operations; a scalar quotient is permissible only for the exact certified observer and operation horizon. A native mapping has not been supplied here.

Verification: direct rational algebra above. Independently SymPy simplification of both displayed identities returned zero; the two rational witnesses were evaluated exactly. No Lean theorem, independent Driver review or canonical mathematical acceptance is asserted.

Next independent research: choose an actual current typed BRC Schur-reduced module and compare its full port/frame serial transfer with the quadratic chart. Either produce a witnessed embedding and exact q/κ observer transport, or isolate the first transfer coefficient/port relation violating that embedding. Preserve the historical W59A free-research author attribution and existing claims.
