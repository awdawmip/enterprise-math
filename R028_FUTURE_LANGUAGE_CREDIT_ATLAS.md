# R028 Future-Language Credit Atlas

Researcher-ID: `EM-R028-4D91AF`  
Status: `NOT_CANONICAL`

For `U_0 superset U_1 superset ...`, define `F_t=K(U_t)`.

## Monotone objects

`F_t subseteq F_{t+1}`: target precision coarsens.

For fixed current encoding `E`:

- `M(E=>F_t)` nonincreasing;
- `B(E=>F_t)` nonincreasing;
- `P(E,F_t)` shrinks by set inclusion;
- fixed-feature pair coverage cannot increase.

Released distinctions at step `t`:

`Released_t=P(E,F_t) \ P(E,F_{t+1})`.

## Non-monotone attribution object

An individual feature's marginal `ΔM` or `ΔB` can increase after the target coarsens. Global bottleneck migration and fixed-width ceiling plateaus are sufficient mechanisms.

Therefore “credit release” should mean release of **required distinctions/total debt**, not a theorem that every feature's scalar marginal decreases.

## Hindsight boundary

For a realized suffix `u* in U`,

`F_U subseteq F_real`.

Hence realized debt is no larger, but `REALIZED_SUFFIX_CREDIT=0` does not imply ex-ante safe deletion. Online deletion requires `DECLARED_LANGUAGE_CREDIT=0` at the correct carrier.

## Recoalescence boundary

On supports:

`F_U^supp=ker(supportSignature_U)`.

A support distinction is released exactly when the two support signatures become equal; canonical R023 then gives suffix-safe forgetful recoalescence.
