# E002 Prior-Art Boundary: Hysteresis, Quantization, and On-Off Control

## 1. Scope

This note records the closest control-engineering neighbors currently used by E002. It does not attempt a complete history of hysteresis or relay control. Its purpose is to prevent Enterprise Math from claiming established control mechanisms merely because they are rewritten in finite-precision language.

The historical novelty of the integrated E002 interpretation remains `NOVELTY_UNVERIFIED`.

## 2. Hysteretic quantizers and chattering

Ceragioli, De Persis, and Frasca study discontinuities and hysteresis in quantized average consensus and explicitly introduce a hysteretic quantizer to cope with unwanted chattering [SRC-CERAGIOLI-DEPERSIS-FRASCA-2011-HYSTERESIS].

E002 therefore does not claim that adding memory to a quantized threshold rule in order to suppress repeated switching is new.

The E002 distinction is semantic and structural: it asks whether the width of the collapsed target region is already supplied by the represented precision state, and then separates that observation rule from the persistence response. That interpretation still has to prove engineering value beyond the established hysteretic-quantizer construction.

## 3. Quantized control with hysteresis

De Persis and Mazenc analyze quantized nonlinear control with delay and incorporate hysteresis in the quantized control mechanism to prevent chattering [SRC-DEPERSIS-MAZENC-2010-QUANTIZED-HYSTERESIS].

This is a close prior-art boundary because both programs combine finite quantization and hysteretic behavior. E002 must not present the mere coexistence of quantization plus hysteresis as novel.

The narrower Enterprise Math question is whether precision is treated as an explicit finite state coordinate rather than only a controller approximation/tuning device, and whether exact future-sufficiency obligations can be derived from the information discarded by that precision state.

## 4. Hysteretic on-off control and limit cycles

Kasis, Monshizadeh, and Lestas study on-off loads in power-grid frequency regulation, distinguish chattering from other dynamical behavior, and show that hysteretic policies can avoid chattering while limit-cycle behavior may still remain [SRC-KASIS-MONSHIZADEH-LESTAS-2021-ONOFF].

This is especially relevant to E002-T09. E002 proves eventual periodicity for its own finite deterministic thermostat map; it does not claim the general discovery that hysteretic on-off systems may oscillate.

The source also supplies an important conceptual warning: chatter suppression is not a convergence theorem.

## 5. Enterprise Math boundary

The currently defensible E002 contribution is not the relay law itself. It is the pressure test of the package

```text
intrinsic represented precision
+ target-centered collapse
+ state-persistence response
+ exact integer noise/switch certificates
+ task-relative future-sufficiency repair
```

against established hysteresis engineering.

The route should be considered unsuccessful if its precision parameter is merely tuned after the fact to reproduce a conventional deadband with no independently justified resolution meaning. It becomes more interesting only when the same finite precision coordinate is required elsewhere by sensing, representation, actuation, or another independently specified part of the world engine.

No priority claim is made until a dedicated historical search supports one.
