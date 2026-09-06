import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberIntermediateNoGo

open EnterpriseMath.BranchRecoalescence

/-- State retaining color, one distinguished intermediate vertex, and final endpoint. -/
structure DeepTransportState where
  color : Fin 3
  intermediate : ℕ
  endpoint : ℕ
  deriving DecidableEq

/-- Forget the distinguished intermediate vertex but retain color and final endpoint. -/
def coloredEndpoint (s : DeepTransportState) : Fin 3 × ℕ :=
  (s.color, s.endpoint)

/-- The intermediate vertex reached by the distinguished action. -/
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

/-- Their distinguished intermediate vertices are different. -/
theorem witness_intermediate_ne :
    intermediateVertex witnessA ≠ intermediateVertex witnessB := by
  norm_num [witnessA, witnessB, intermediateVertex]

/--
Arithmetic certificate for the collision: `(2,17,19)` and `(3,11,17)` each
have exactly one label at most `10`, both products lie below `10^3`, both final
quotients equal `1`, but the uncut-action quotients are `500` and `333`.
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

/-- Color plus final endpoint cannot recover the distinguished intermediate vertex. -/
theorem coloredEndpoint_not_recovers_intermediate :
    ¬ Recovers coloredEndpoint intermediateVertex := by
  intro h
  have hsame : intermediateVertex witnessA = intermediateVertex witnessB :=
    noResurrection h witness_coloredEndpoint_eq
  exact witness_intermediate_ne hsame

/-- A concrete Boolean field readout that distinguishes the intermediate vertices. -/
def intermediateBooleanReadout (s : DeepTransportState) : Bool :=
  decide (s.intermediate = 500)

/-- The colored endpoint cannot recover all Boolean readouts of the intermediate vertex. -/
theorem coloredEndpoint_not_recovers_intermediateBooleanReadout :
    ¬ Recovers coloredEndpoint intermediateBooleanReadout := by
  intro h
  have hsame : intermediateBooleanReadout witnessA =
      intermediateBooleanReadout witnessB :=
    noResurrection h witness_coloredEndpoint_eq
  norm_num [intermediateBooleanReadout, witnessA, witnessB] at hsame

/-- Full three-intermediate descended history state. -/
structure DeepThreeIntermediateState where
  color : Fin 3
  uncutIntermediate : ℕ
  overIntermediate₁ : ℕ
  overIntermediate₂ : ℕ
  endpoint : ℕ
  deriving DecidableEq

/-- Forget the two overcut intermediate vertices. -/
def uncutKey (s : DeepThreeIntermediateState) : Fin 3 × ℕ × ℕ :=
  (s.color, s.uncutIntermediate, s.endpoint)

/-- Read the first overcut intermediate vertex. -/
def firstOverIntermediate (s : DeepThreeIntermediateState) : ℕ :=
  s.overIntermediate₁

/-- Deep triple `(2,17,19)` at `Y=10`. -/
def branchWitnessA : DeepThreeIntermediateState :=
  ⟨0, 500, 58, 52, 1⟩

/-- Deep triple `(2,13,23)` at `Y=10`. -/
def branchWitnessB : DeepThreeIntermediateState :=
  ⟨0, 500, 76, 43, 1⟩

/-- The histories agree on color, uncut intermediate, and final endpoint. -/
theorem branchWitness_uncutKey_eq :
    uncutKey branchWitnessA = uncutKey branchWitnessB := by
  rfl

/-- Their first overcut intermediate vertices are different. -/
theorem branchWitness_firstOverIntermediate_ne :
    firstOverIntermediate branchWitnessA ≠
      firstOverIntermediate branchWitnessB := by
  norm_num [branchWitnessA, branchWitnessB, firstOverIntermediate]

/-- Exact arithmetic certificate for the second collision. -/
theorem branch_collision_certificate :
    2 ≤ 10 ∧ 10 < 17 ∧ 10 < 19 ∧
      2 * 17 * 19 ≤ 10 ^ 3 ∧
      10 ^ 3 / (2 * 17 * 19) = 1 ∧
      10 ^ 3 / 2 = 500 ∧
      10 ^ 3 / 17 = 58 ∧
      10 ^ 3 / 19 = 52 ∧
      2 ≤ 10 ∧ 10 < 13 ∧ 10 < 23 ∧
      2 * 13 * 23 ≤ 10 ^ 3 ∧
      10 ^ 3 / (2 * 13 * 23) = 1 ∧
      10 ^ 3 / 2 = 500 ∧
      10 ^ 3 / 13 = 76 ∧
      10 ^ 3 / 23 = 43 := by
  norm_num

/-- Color, uncut intermediate, and endpoint still cannot recover another branch. -/
theorem uncutKey_not_recovers_firstOverIntermediate :
    ¬ Recovers uncutKey firstOverIntermediate := by
  intro h
  have hsame : firstOverIntermediate branchWitnessA =
      firstOverIntermediate branchWitnessB :=
    noResurrection h branchWitness_uncutKey_eq
  exact branchWitness_firstOverIntermediate_ne hsame

/-- A Boolean readout supported at one overcut intermediate vertex. -/
def firstOverBooleanReadout (s : DeepThreeIntermediateState) : Bool :=
  decide (s.overIntermediate₁ = 58)

/-- The reduced uncut key cannot recover all Boolean branch readouts. -/
theorem uncutKey_not_recovers_firstOverBooleanReadout :
    ¬ Recovers uncutKey firstOverBooleanReadout := by
  intro h
  have hsame : firstOverBooleanReadout branchWitnessA =
      firstOverBooleanReadout branchWitnessB :=
    noResurrection h branchWitness_uncutKey_eq
  norm_num [firstOverBooleanReadout, branchWitnessA, branchWitnessB] at hsame

end EnterpriseMath.DeepChamberIntermediateNoGo
