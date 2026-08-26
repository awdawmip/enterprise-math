import EnterpriseMath.Quotient.OperationCongruence

namespace EnterpriseMath.FutureQuotient

open Function

/-- A deterministic partial operation is compatible with an observation exactly
when states in one observation fiber agree on both definedness and the observed
target whenever the operation is defined.  `Option.map O` packages those two
requirements into ordinary equality. -/
def PartialObservationCompatible
    {α β : Type*} (O : α → β) (F : α → Option α) : Prop :=
  ∀ x y : α, O x = O y → Option.map O (F x) = Option.map O (F y)

/-- A deterministic partial operation descends through an observation when its
observed `Option` output is determined solely by the observed input. -/
def PartialOperationDescends
    {α β : Type*} (O : α → β) (F : α → Option α) : Prop :=
  ∃ ν : β → Option β,
    ∀ x : α, Option.map O (F x) = ν (O x)

/-- Any descended partial operation preserves the observation kernel, including
operation definedness. -/
theorem partialOperationDescends_compatible
    {α β : Type*} {O : α → β} {F : α → Option α}
    (h : PartialOperationDescends O F) :
    PartialObservationCompatible O F := by
  obtain ⟨ν, hν⟩ := h
  intro x y hxy
  rw [hν x, hν y, hxy]

/-- Under a surjective observation, partial-operation compatibility constructs
an exact descended partial operation on the quotient state space. -/
theorem compatible_partialOperationDescends
    {α β : Type*} {O : α → β} {F : α → Option α}
    (hO : Surjective O) (hcomp : PartialObservationCompatible O F) :
    PartialOperationDescends O F := by
  classical
  choose lift hlift using hO
  refine ⟨fun observed ↦ Option.map O (F (lift observed)), ?_⟩
  intro x
  exact hcomp x (lift (O x)) (hlift (O x)).symm

/-- Exact descent of a deterministic partial operation is equivalent to
compatibility of the observation kernel when the observation is surjective. -/
theorem partialOperationDescends_iff_compatible
    {α β : Type*} {O : α → β} {F : α → Option α}
    (hO : Surjective O) :
    PartialOperationDescends O F ↔ PartialObservationCompatible O F := by
  constructor
  · exact partialOperationDescends_compatible
  · exact compatible_partialOperationDescends hO

/-- The descended partial operation is unique under a surjective observation. -/
theorem descended_partial_operation_unique
    {α β : Type*} {O : α → β} {F : α → Option α}
    (hO : Surjective O)
    {ν₁ ν₂ : β → Option β}
    (h₁ : ∀ x : α, Option.map O (F x) = ν₁ (O x))
    (h₂ : ∀ x : α, Option.map O (F x) = ν₂ (O x)) :
    ν₁ = ν₂ := by
  classical
  choose lift hlift using hO
  funext observed
  let x : α := lift observed
  have hx : O x = observed := hlift observed
  calc
    ν₁ observed = ν₁ (O x) := by rw [hx]
    _ = Option.map O (F x) := (h₁ x).symm
    _ = ν₂ (O x) := h₂ x
    _ = ν₂ observed := by rw [hx]

/-- Totalize a partial operation by adjoining the already-observable `none`
state.  The new state is absorbing; this is a compiler construction, not an
additional physical-state hypothesis. -/
def totalizePartial {α : Type*} (F : α → Option α) : Option α → Option α
  | none => none
  | some x => F x

/-- Ordinary total compatibility of the observable-`Option` totalization. -/
def TotalizedPartialCompatible
    {α β : Type*} (O : α → β) (F : α → Option α) : Prop :=
  ∀ x y : Option α,
    Option.map O x = Option.map O y →
      Option.map O (totalizePartial F x) =
        Option.map O (totalizePartial F y)

/-- A partial operation is observation-compatible exactly when its absorbing
`none` totalization is compatible for the lifted `Option.map O` observation.
Thus definedness-sensitive partial semantics reduce to ordinary total-function
kernel compatibility once `none` is explicitly observable. -/
theorem partialCompatible_iff_totalized
    {α β : Type*} (O : α → β) (F : α → Option α) :
    PartialObservationCompatible O F ↔ TotalizedPartialCompatible O F := by
  constructor
  · intro h x y hxy
    cases x with
    | none =>
        cases y with
        | none => rfl
        | some y => simp at hxy
    | some x =>
        cases y with
        | none => simp at hxy
        | some y =>
            simp only [Option.map_some, Option.some.injEq] at hxy
            simpa [totalizePartial] using h x y hxy
  · intro h x y hxy
    have hs : Option.map O (some x) = Option.map O (some y) := by
      simpa using hxy
    simpa [TotalizedPartialCompatible, totalizePartial] using h (some x) (some y) hs

/-- The ordinary total-operation case is the special case where the partial
operation always returns `some`. -/
theorem partialCompatible_some_iff
    {α β : Type*} (O : α → β) (f : α → α) :
    PartialObservationCompatible O (fun x ↦ some (f x)) ↔
      ∀ x y : α, O x = O y → O (f x) = O (f y) := by
  constructor
  · intro h x y hxy
    have hs := h x y hxy
    simpa using hs
  · intro h x y hxy
    simpa using h x y hxy

end EnterpriseMath.FutureQuotient
