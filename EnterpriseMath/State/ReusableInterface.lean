import EnterpriseMath.State.OperationCongruence

namespace EnterpriseMath.ReusableInterface

open Function
open EnterpriseMath.OperationCongruence

/-- The raw observation factors through an interface exactly when interface
equality never identifies states that the raw observation distinguishes. -/
def ObservationFactorsThrough
    {α β γ : Type*} (O : α → β) (I : α → γ) : Prop :=
  ∀ ⦃x y : α⦄, I x = I y → O x = O y

/-- A candidate interface is reusable for one `k`-ary operation when it both
preserves the raw observation and has an operation-compatible kernel. -/
def ReusableFor
    {α β γ : Type*} {k : ℕ}
    (O : α → β) (I : α → γ) (μ : (Fin k → α) → α) : Prop :=
  ObservationFactorsThrough O I ∧ ObservationCompatible I μ

/-- P018-T213 relation core: equality at a reusable interface always implies
raw observational equality. -/
theorem reusable_eq_implies_observation_eq
    {α β γ : Type*} {k : ℕ}
    {O : α → β} {I : α → γ} {μ : (Fin k → α) → α}
    (h : ReusableFor O I μ) {x y : α} (hI : I x = I y) :
    O x = O y := by
  exact h.1 hI

/-- P018-T213 relation core: coordinatewise equality of reusable interface
states forces equality of the operation result at the same interface. -/
theorem reusable_operation_eq
    {α β γ : Type*} {k : ℕ}
    {O : α → β} {I : α → γ} {μ : (Fin k → α) → α}
    (h : ReusableFor O I μ)
    {x y : Fin k → α}
    (hI : ∀ i : Fin k, I (x i) = I (y i)) :
    I (μ x) = I (μ y) := by
  exact h.2 x y hI

/-- If a reusable interface is surjective onto its interface type, the declared
operation descends exactly to that interface state space. -/
theorem reusable_operation_descends
    {α β γ : Type*} {k : ℕ}
    {O : α → β} {I : α → γ} {μ : (Fin k → α) → α}
    (hI : Surjective I) (h : ReusableFor O I μ) :
    OperationDescends I μ := by
  exact compatible_operationDescends hI h.2

/-- The full fine state is always a reusable interface whenever the interface is
chosen as the identity map. -/
theorem identity_reusable
    {α β : Type*} {k : ℕ}
    (O : α → β) (μ : (Fin k → α) → α) :
    ReusableFor O (id : α → α) μ := by
  constructor
  · intro x y hxy
    simpa using congrArg O hxy
  · intro x y hxy
    congr 1
    funext i
    simpa using hxy i

end EnterpriseMath.ReusableInterface
