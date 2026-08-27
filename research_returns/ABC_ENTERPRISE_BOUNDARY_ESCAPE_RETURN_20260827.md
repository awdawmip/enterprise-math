# ABC Enterprise Boundary-Escape Regime — Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-ABC-ENTERPRISE-BOUNDARY-ESCAPE`  
Publication-ID: `TP2-CD1E2741D7E41F56418B`  
Claim-ID: `chatgpt-abc3-20260827-1634`

## Verdict

`EXACT_OBSTRUCTION`

The boundary regime is frozen in the intrinsic coordinate
\[
x=\frac{\min(a,b)}c,
\]
but the publication's required exact \(\beta\)-to-\(x\) conversion is not reproducible because the canonical parent definition of \(\beta\) is absent from the taskbook and its only pinned source reference.

Primary blocker code:

`BETA_NORMALIZATION_NOT_DURABLY_FROZEN`

## Load-bearing results

1. For every fixed \(\delta>0\), the band \(x\le\delta\) contains primitive infinite families with the smaller addend still linear in \(c\). Hence no fixed ratio band implies \(m\le c^{1-\eta_0}\) for any fixed \(\eta_0>0\).
2. The correct power-small condition is exactly
   \[
   m\le c^{1-\eta_0}
   \iff x\le c^{-\eta_0}.
   \]
3. In a fixed-ratio band, boundary information alone does not activate a uniform power-small theorem; the generic Stewart–Yu envelope remains available:
   \[
   \log c\le\kappa R^{1/3}(\log R)^3.
   \]
4. In the power-small band, Pasten Theorem 1.4(1) gives the unconditional subexponential envelope
   \[
   \log c\le\eta_0^{-1}\exp\!\bigl(\kappa\sqrt{(\log R)\log_2R}\bigr).
   \]
5. The ultra-thin family \((1,n,n+1)\) lies in every sufficiently deep fixed boundary band. A near-abc quality bound on this family is exactly the consecutive-radical lower bound
   \[
   \operatorname{rad}(n(n+1))\ge(n+1)^{1/(1+\varepsilon)},
   \]
   which is not supplied by the imported unconditional estimates.

## Exact uncovered gap

- **Source gap:** restore the exact durable parent formula \(\beta=B(m/c)\), then the numerical threshold conversion is \(m/c=B^{-1}(\beta)\) with orientation fixed by the restored formula.
- **Arithmetic gap:** after that adapter is restored, a fixed geometric boundary threshold still does not by itself imply a fixed power-small exponent; a scale-dependent boundary threshold corresponding to \(m/c\le c^{-\eta_0}\) is required to invoke the current small-addend theorem uniformly.

## Artifacts

- `research_artifacts/ABC_ENTERPRISE_BOUNDARY_ESCAPE/ABC_BOUNDARY_REGIME_ENVELOPE_20260827.md`
- `scripts/check_abc_enterprise_boundary_escape.py`

Authoring-time checker result:

`ABC_BOUNDARY_ESCAPE_CHECK_PASS consecutive_n<=2000 fixed_band_witnesses=4 eta_star=PASS`

This return uses no abc-conjectural input and makes no near-abc quality claim.
