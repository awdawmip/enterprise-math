# R061 Stage 3 — Standard Symmetrization Metric Construction

Researcher-ID: `EM-R061S3-2F9622`

This file records the metric facts used only for classification.

## d_max

`d_max(P,Q)=max(ell(P->Q),ell(Q->P))`.

Symmetry and positivity are immediate. For a triangle, each directed leg to the third endpoint is bounded by the corresponding sum of directed legs, hence

`max(ell_PR,ell_RP) <= max(ell_PQ+ell_QR, ell_RQ+ell_QP) <= max(ell_PQ,ell_QP)+max(ell_QR,ell_RQ)`.

Therefore `d_max` is a metric.

## d_sum

`d_sum(P,Q)=ell(P->Q)+ell(Q->P)`.

Add the forward and reverse Stage 2 directed triangle inequalities. Therefore `d_sum` is a metric. Any positive scalar multiple, including the arithmetic mean, is also a metric.

## d_2 and symmetric monotone norms

For `d_2(P,Q)=sqrt(ell_f^2+ell_r^2)` the general monotone-norm lemma applies. The same proof applies to every symmetric monotone norm `Phi`.

## Finite exact audit

On the Stage 2 `81`-vertex patch the deterministic checker performs exact radical comparisons on all `81^3=531441` ordered triples.

Failure counts: directed Stage 2 triangle `0`; reverse-directed triangle `0`; `d_max` `0`; `d_2` `0`; `d_sum` `0` by exact componentwise directed inequalities.

This finite audit supports, but does not replace, the general proof.
