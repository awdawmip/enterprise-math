import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberIntermediateNoGo

open EnterpriseMath.BranchRecoalescence

/-- Full descended state required by a deepest history readout. -/
structure DeepTransportState where
  color : Fin 3
  intermediate : ℕ
  endpoint : ℕ
  deriving DecidableEq

/-- Forget the unique uncut intermediate vertex but retain color and final endpoint. -/
def coloredEndpoint (s : DeepTransportState) : Fin 3 × ℕ :=
  (s.color, s.endpoint)

/-- The intermediate vertex reached by the unique uncut action. -/
def intermediateVertex (s : DeepTransportState) : ℕ :=
  s.intermediate

/-- First explicit deepest history at `Y=10`, with labels `(2,17,19)`. -/
def witnessA : DeepTransportState :=
  ⟨0, 500, 1⟩

/-- Second explicit deepest history at `Y=10`, with labels `(3,11,17)`. -/
def witnessB : DeepTransportState :=
  ⟨0, 333, 1⟩

/-- The two arithmetic histories have the same colored final endpoint. -/
theorem witness_coloredEndpoint_eq :
    coloredEndpoint witnessA = coloredEndpoint witnessB := by
  rfl

/-- Their unique uncut intermediate vertices are different. -/
theorem witness_intermediate_ne :
    intermediateVertex witnessA ≠ intermediateVertex witnessB := by
  norm_num [witnessA, witnessB, intermediateVertex]

/--
Arithmetic certificate for the collision:
`(2,17,19)` and `(3,11,17)` each have exactly one label at most `10`,
both products lie below `10^3`, both final quotients equal `1`, but the
uncut-action quotients are `500` and `333`.
-/
theorem arithmetic_collision_certificate :
    2 ≤ 10 ∧ 10 < 17 ∧ 10 < 19 ∧
      2 * 17 * 19 ≤ 10 ^ 3 ∧
      10 ^ 3 / (2 * 17 * 19) = 1 ∧
      10 ^ 3 / 2 = 500 ∧
      3 ≤ 10 ∧ 10 < 11 ∧ 10 < 17 ∧
      3 * 11 * 17 ≤ 10 ^ 3 ∧
      10 ^ 3 / (3 * 11 * 17) = 1 ∧
      10 ^ 3 / 3 = 333 := by
  norm_num

/-- Color plus final endpoint cannot recover the uncut intermediate vertex. -/
theorem coloredEndpoint_not_recovers_intermediate :
    ¬ Recovers coloredEndpoint intermediateVertex := by
  intro h
  have hsame : intermediateVertex witnessA = intermediateVertex witnessB :=
    noResurrection h witness_coloredEndpoint_eq
  exact witness_intermediate_ne hsame

/-- A concrete field readout that distinguishes the two intermediate vertices. -/
def intermediateBooleanReadout (s : DeepTransportState) : Bool :=
  s.intermediate = 500

/-- The colored endpoint cannot recover all field readouts of the intermediate vertex. -/
theorem coloredEndpoint_not_recovers_intermediateBooleanReadout :
    ¬ Recovers coloredEndpoint intermediateBooleanReadout := by
  intro h
  have hsame : intermediateBooleanReadout witnessA =
      intermediateBooleanReadout witnessB :=
    noResurrection h witness_coloredEndpoint_eq
  norm_num [intermediateBooleanReadout, witnessA, witnessB] at hsame

end EnterpriseMath.DeepChamberIntermediateNoGo
