# Migration 16 — exact power-of-two phase carriers through uint32

Status: locally validated prerequisite extension; no Phase32 caller/default/main cutover.
Baseline remote: `7d1749e175614b6d24b8a95a0354c5c383702f64` (M14).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

The existing `certified_hex.py` BRC/dyadic/shared-radical observer was hard-coded to
65,536 phase positions. M16 extends that same implementation to an explicit exact
power-of-two `phase_modulus` in `4..2**32`. The default remains 65,536 and all
retained default tests/results are unchanged. No second quantizer or number family
is introduced.

For a carrier `M=2**k`, the observer constructs `k-2` positive binary half-angle
roots starting from the exact cardinal source cos(pi/2)=0, sin(pi/2)=1. One phase
tick is therefore pi/2**(k-1), without materializing pi. All root/division work
continues through the existing Enterprise Math BRC facade; outward dyadic intervals,
root-polynomial residuals, shared-radical cardinal ties and unresolved-boundary
semantics remain unchanged.

`PolarSource`, `phase_bounds`, `certified_population` and `exact_diagnostics` accept
the explicit modulus. Source records persist it, and `verify_cell_record` replays
the recorded modulus rather than assuming 65,536. Cardinal quarter/half/three-quarter
sources are derived from the modulus exactly. Invalid/non-power-of-two, boolean,
float or greater-than-uint32 moduli are rejected before execution.

The first implementation used direct `//4` for quadrant width. Numerical tests
passed, but the exact-arithmetic policy correctly rejected those two new quotient
materializations. They were replaced by the existing BRC-backed `_floor(...,4)`.
The final policy gate passes. This is a useful structural witness: mathematically
obvious integer division still obeys the project BRC transport contract.

## Validation

148 retained M12 arithmetic/machine tests pass with zero failures/errors/skips and
the retained M12 `tests.json` SHA256 remains
`5beb9d6ece83a48768c9e39f36b120fe54ee8571621bd148f3ae0ab6cc8eb119`.
Six new tests pass, for 154 total validated tests. They cover default-carrier
backward compatibility, high-precision noncardinal oracle containment, exact
uint32 cardinal/shared-radical ties, population/diagnostics at modulus 2**32,
record replay/tamper rejection and invalid modulus inputs. The exact-policy checker
passes `certified_hex.py` and `angular_dispersion.py`.

A finite synthetic matrix uses `tick[n]=n*2654435761 mod 2**32` for populations
1,024 and 4,096 at scales 1/2, 1 and 3/2. All six populations are fully certified
at the initial 64-bit budget; no unresolved identities occur. This schedule is
NOT `phase32_lab`'s composite valuation phase construction, so these are carrier
checks only, not actual Phase32 caller admission or a universal termination claim.

The high-precision oracle initially reported a tiny ~1e-142 value for an exactly
zero cardinal cosine; the test was corrected to keep exact cardinals under integer
certificates and use the transcendental oracle only for noncardinal phases. The
production arithmetic was not weakened to match oracle noise.

## BRC/tool reuse and geometry boundary

Reuse resolution: `EXTEND_EXISTING_TOOL`. Existing BRC division/root, interval
arithmetic and certified-cell laws are reused unchanged; only the phase carrier
parameterization is extended. Geometry remains the declared polar A2 observer,
not native X6/P000, and numerical equality still does not collapse identities or
branch provenance.

This slice does not modify `phase32_lab.py`, its floating `position/quantize`, CV,
product-error or V2 adapter callers. Those are the next numerical migration unit.
The browser BigInt port also remains fixed at its prior carrier in this slice.

## M15 admission-track boundary

The previously planned production `workbench.html`/full-root-package admission
remains separate and incomplete. Static connector checks confirm the production
workbench blob and root-package metadata/import targets, but the current connector
returns repository text rather than a local materialized file; manually copying a
large base64 bridge was abandoned when transcript truncation made byte integrity
uncertain. The incomplete local bridge was deleted and an unreferenced staging
commit was never attached to the candidate branch. M15 admission is NOT passed.

## Next

Wire the actual `phase32_lab` caller to this generic exact carrier while preserving
its own nearest-A2 axial lexicographic tie rule, exact uint32 phase source and all
identity/provenance fields. Start with opt-in certified cells and exact CV²/product
readouts; do not infer exact pitch from its legacy float configuration and do not
switch defaults before caller regression. Browser Phase32 and M15 production
package/native-browser admission remain separate.
