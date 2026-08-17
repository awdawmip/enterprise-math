# R059D Stage AN Report — BRC Pushforward Measure and Persistent Distortion

Researcher-ID: `EM-R059D-AN-4C2B91`

Task-ID: `RS-R059D-STAGE-AN-BRC-PUSHFORWARD-MEASURE-PERSISTENT-DISTORTION`

Owner branch: `research/r059d-stage-an-brc-pushforward-measure-persistent-distortion`

Frozen parent: `c6be0626889b67763b56e7faebf2cd2185f0211c`

Taskbook source: `e15ff710fb36f4149739880267e9284fb3409969`

## Primary disposition

`BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__PERSISTENT_TWO_LIMIT_DISTORTION_ESTABLISHED`

The stronger finite-radius statement

`mu_r proportional to nu_r iff r in {1,2}`

is also proved exactly for all integer radii.

## Measure decomposition

AM gives canonical closed source fibers `F_(r,k)` over the already-canonical AL target elementary turns `e_k`. Define

`nu_r({e_k})=1`

and

`mu_r({e_k})=Arc_perp(F_(r,k))=r*Delta_(r,k)`.

Boundary-ray overlaps have zero source arc measure, so

`Circ_perp(r)=sum_k mu_r({e_k})`,

while

`C_E(r)=T_r=sum_k 1`.

Thus BRC puts two distinct measures on the same target cycle: source-arc pushforward and native turn counting.

The global mean source weight is

`bar_w_r=Circ_perp(r)/T_r=2*kappa_perp*r/T_r`,

so

`bar_w_r -> kappa_perp/kappa_E`.

`kappa_perp` remains source typed; `kappa_E^2=12`, `kappa_E>0` remains the target-native theorem.

## Exact local formula

For consecutive target rays `p=(a,b), q=(c,d)` in the source compatibility embedding,

`tan Delta = sqrt(3)*(ad-bc)/(2ac+2bd+ad+bc)`.

The three target primitive symbols have exact source-side formulas recorded in `R059D_STAGE_AN_LOCAL_WEIGHT_FORMULA.json`.

## Sharp nonproportionality

- `r=1`: D6 gives six equal source fibers.
- `r=2`: sector reflection gives twelve equal fibers.
- `r=3`: first two fibers have `tan Delta/sqrt(3)` equal to `1/5` and `3/13`.
- `r=4`: first two fibers have `1/7` and `1/6`.
- every `r>=5`: the first canonical turn is symbol 2 and the second is symbol 1 because `rho_1=3r-13>0`; their coefficients are
  `1/(2r-1)` and `(r-1)/(2r^2-r+3)`, and equality would force `r=-1`.

Therefore

`mu_r proportional to nu_r iff r in {1,2}`.

## Persistent refinement distortion

The first axis turn satisfies

`tan Delta_axis(r)=sqrt(3)/(2r-1)`

and hence

`w_axis(r)=r*Delta_axis(r)->sqrt(3)/2`.

For each radius choose the canonical central symbol-2 turn at the AH left-half termination. Its start satisfies

`m=a+b=M_N(r)=r+J_N(r)` and `d=a-b in {1,2}`,

so

`tan Delta_mid(r)=2sqrt(3)m/(3m^2+d^2-2d)`.

Since `M_N(r)/r -> beta`, `3beta^2=4`, `beta>0`,

`w_mid(r)=r*Delta_mid(r)->1`.

The limits differ:

`1-sqrt(3)/2>0`.

Hence BRC metric distortion persists under radial refinement. The local source-weight field cannot converge uniformly to any constant, even if the candidate constant is allowed to depend on radius.

## Defect field and renormalization

With

`d_(r,k)=w_(r,k)-bar_w_r`,

one has exactly

`sum_k d_(r,k)=0`.

D6 and reflection symmetries are inherited from AM. The distinguished defects remain separated asymptotically by `1-sqrt(3)/2`.

The global factor

`lambda_r=bar_w_r`

matches total source circumference by construction, but fails locally for every `r>=3`, and no scalar sequence can make the local weights uniformly exact asymptotically.

A positive limiting mean-square variance or full continuous macroscopic defect profile is not claimed; those stronger profile statements remain open and are not needed for persistent two-limit distortion.

## Semantic firewalls

- source arc measure is source typed;
- target turn counting is target native;
- source angles/sqrt(3)/source integration never select or tune the target orbit;
- AL canonicality is never reopened;
- `kappa_perp` is not identified with `kappa_E`;
- no theorem about standard real pi is added;
- AM relational BRC fibers remain relational, not replaced by a bijective point map.

## Validation

The frozen checker validates:

- every `r=1..1024`;
- checkpoints `2048,4096,8192`;
- exact target endpoint/count structure;
- exact axis tangent certificate;
- exact central-turn certificate;
- exact `r=3,4` nonuniform witnesses;
- the universal `r>=5` canonical `21` prefix over the replay range;
- source weighted-sum coverage;
- equal-weight controls at `r=1,2`;
- nonproportionality at every replayed `r>=3`;
- D6 and reflection symmetry;
- zero-sum defect identity;
- target generator source/runtime firewall.

Finite replay is implementation evidence only. The all-radius and asymptotic theorems are symbolic and were frozen before replay.

## Stop condition

`STOP_FOR_DRIVER_REVIEW`

No AO or later stage is consumed.
