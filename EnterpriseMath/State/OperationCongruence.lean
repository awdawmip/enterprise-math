import Mathlib.Data.Fin.Basic
import Mathlib.Logic.Function.Basic

namespace EnterpriseMath.OperationCongruence

open Function

/-- An observation kernel is compatible with one `k`-ary operation exactly when
coordinatewise observational equality forces observational equality of outputs. -/
def ObservationCompatible
    {α β : Type*} {k : ℕ}
    (O : α → β) (μ : (Fin k → α) → α) : Prop :=
  ∀ x y : Fin k → α,
    (∀ i : Fin k, O (x i) = O (y i)) →
      O (μ x) = O (μ y)

/-- A `k`-ary operation descends through an observation when its observed output
is determined solely by the tuple of observed inputs. -/
def OperationDescends
    {α β : Type*} {k : ℕ}
    (O : α → β) (μ : (Fin k → α) → α) : Prop :=
  ∃ ν : (Fin k → β) → β,
    ∀ x : Fin k → α, O (μ x) = ν (fun i ↦ O (x i))

/-- Any descended operation makes the observation kernel compatible. -/
theorem operationDescends_compatible
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (h : OperationDescends O μ) : ObservationCompatible O μ := by
  obtain ⟨ν, hν⟩ := h
  intro x y hxy
  rw [hν x, hν y]
  congr 1
  funext i
  exact hxy i

/-- Under a surjective observation, operation-kernel compatibility constructs an
exact descended operation on the coarse state space. -/
theorem compatible_operationDescends
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (hO : Surjective O) (hcomp : ObservationCompatible O μ) :
    OperationDescends O μ := by
  classical
  choose lift hlift using hO
  refine ⟨fun observed ↦ O (μ (fun i ↦ lift (observed i))), ?_⟩
  intro x
  apply hcomp
  intro i
  exact (hlift (O (x i))).symm

/-- P018-T169 relation core: for a surjective precision observation, exact
multi-ary descent is equivalent to congruence of the observation kernel. -/
theorem operationDescends_iff_compatible
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (hO : Surjective O) :
    OperationDescends O μ ↔ ObservationCompatible O μ := by
  constructor
  · exact operationDescends_compatible
  · exact compatible_operationDescends hO

/-- The descended operation is unique when the observation is surjective. -/
theorem descended_operation_unique
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (hO : Surjective O)
    {ν₁ ν₂ : (Fin k → β) → β}
    (h₁ : ∀ x : Fin k → α, O (μ x) = ν₁ (fun i ↦ O (x i)))
    (h₂ : ∀ x : Fin k → α, O (μ x) = ν₂ (fun i ↦ O (x i))) :
    ν₁ = ν₂ := by
  classical
  choose lift hlift using hO
  funext observed
  let x : Fin k → α := fun i ↦ lift (observed i)
  have hx : (fun i ↦ O (x i)) = observed := by
    funext i
    exact hlift (observed i)
  calc
    ν₁ observed = ν₁ (fun i ↦ O (x i)) := by rw [hx]
    _ = O (μ x) := (h₁ x).symm
    _ = ν₂ (fun i ↦ O (x i)) := h₂ x
    _ = ν₂ observed := by rw [hx]

/-- Binary compatibility written without `Fin 2`, for convenient use in the
precision/carry layer. -/
def BinaryObservationCompatible
    {α β : Type*} (O : α → β) (μ : α → α → α) : Prop :=
  ∀ a a' b b' : α,
    O a = O a' → O b = O b' → O (μ a b) = O (μ a' b')

/-- Compatibility when only the left input is replaced inside its observation
fiber. -/
def LeftObservationCompatible
    {α β : Type*} (O : α → β) (μ : α → α → α) : Prop :=
  ∀ a a' b : α, O a = O a' → O (μ a b) = O (μ a' b)

/-- Compatibility when only the right input is replaced inside its observation
fiber. -/
def RightObservationCompatible
    {α β : Type*} (O : α → β) (μ : α → α → α) : Prop :=
  ∀ a b b' : α, O b = O b' → O (μ a b) = O (μ a b')

/-- P018-T170 binary core: full two-input compatibility is equivalent to the two
one-coordinate elementary-translation tests. -/
theorem binaryCompatible_iff_coordinatewise
    {α β : Type*} (O : α → β) (μ : α → α → α) :
    BinaryObservationCompatible O μ ↔
      LeftObservationCompatible O μ ∧ RightObservationCompatible O μ := by
  constructor
  · intro h
    constructor
    · intro a a' b haa'
      exact h a a' b b haa' rfl
    · intro a b b' hbb'
      exact h a a b b' rfl hbb'
  · rintro ⟨hleft, hright⟩ a a' b b' haa' hbb'
    exact (hleft a a' b haa').trans (hright a' b b' hbb')

end EnterpriseMath.OperationCongruence
