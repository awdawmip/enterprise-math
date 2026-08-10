import EnterpriseMath.Quotient.PartialOperationCongruence

namespace EnterpriseMath.FutureQuotient

/-- Fiber-saturation of the domain of one deterministic partial operation. -/
def PartialDomainCompatible
    {α β : Type*} (O : α → β) (F : α → Option α) : Prop :=
  ∀ x y : α, O x = O y → (F x = none ↔ F y = none)

/-- Compatibility of observed targets whenever the partial operation is enabled
on both representatives. -/
def PartialTargetCompatible
    {α β : Type*} (O : α → β) (F : α → Option α) : Prop :=
  ∀ x y u v : α,
    O x = O y → F x = some u → F y = some v → O u = O v

/-- Partial safety splits exactly into a saturated enabledness domain plus target
compatibility on enabled representatives. -/
theorem partialCompatible_iff_domain_and_target
    {α β : Type*} (O : α → β) (F : α → Option α) :
    PartialObservationCompatible O F ↔
      PartialDomainCompatible O F ∧ PartialTargetCompatible O F := by
  constructor
  · intro h
    constructor
    · intro x y hxy
      have hm := h x y hxy
      constructor
      · intro hx
        cases hy : F y with
        | none => exact hy
        | some v => simp [hx, hy] at hm
      · intro hy
        cases hx : F x with
        | none => exact hx
        | some u => simp [hx, hy] at hm
    · intro x y u v hxy hxu hyv
      have hm := h x y hxy
      simpa [hxu, hyv] using hm
  · rintro ⟨hdom, htgt⟩ x y hxy
    cases hx : F x with
    | none =>
        have hy : F y = none := (hdom x y hxy).mp hx
        simp [hx, hy]
    | some u =>
        cases hy : F y with
        | none =>
            have hxnone : F x = none := (hdom x y hxy).mpr hy
            simp [hx] at hxnone
        | some v =>
            have huv : O u = O v := htgt x y u v hxy hx hy
            simp [hx, hy, huv]

/-- In particular, the enabled domain of a safe partial action is a union of
observation fibers. -/
theorem partialCompatible_domain_saturated
    {α β : Type*} {O : α → β} {F : α → Option α}
    (h : PartialObservationCompatible O F) :
    PartialDomainCompatible O F :=
  (partialCompatible_iff_domain_and_target O F).mp h |>.1

/-- Execute `F` and, if it is defined, continue with `G`. -/
def partialThen {α : Type*}
    (F G : α → Option α) : α → Option α :=
  fun x ↦ (F x).bind G

/-- The total identity action is safe for every observation. -/
theorem partialCompatible_identity
    {α β : Type*} (O : α → β) :
    PartialObservationCompatible O (fun x : α ↦ some x) := by
  intro x y hxy
  simpa using congrArg some hxy

/-- Safe deterministic partial operations are closed under causal/Kleisli
composition. -/
theorem partialCompatible_then
    {α β : Type*} {O : α → β}
    {F G : α → Option α}
    (hF : PartialObservationCompatible O F)
    (hG : PartialObservationCompatible O G) :
    PartialObservationCompatible O (partialThen F G) := by
  intro x y hxy
  have hfirst := hF x y hxy
  cases hx : F x with
  | none =>
      cases hy : F y with
      | none => simp [partialThen, hx, hy]
      | some v => simp [hx, hy] at hfirst
  | some u =>
      cases hy : F y with
      | none => simp [hx, hy] at hfirst
      | some v =>
          have huv : O u = O v := by
            simpa [hx, hy] using hfirst
          have hsecond := hG u v huv
          simpa [partialThen, hx, hy] using hsecond

/-- Left identity for causal partial-operation composition. -/
theorem partialThen_identity_left
    {α : Type*} (F : α → Option α) :
    partialThen (fun x : α ↦ some x) F = F := by
  funext x
  simp [partialThen]

/-- Right identity for causal partial-operation composition. -/
theorem partialThen_identity_right
    {α : Type*} (F : α → Option α) :
    partialThen F (fun x : α ↦ some x) = F := by
  funext x
  cases hx : F x <;> simp [partialThen, hx]

/-- Associativity of causal partial-operation composition. -/
theorem partialThen_assoc
    {α : Type*} (F G H : α → Option α) :
    partialThen (partialThen F G) H =
      partialThen F (partialThen G H) := by
  funext x
  cases hx : F x with
  | none => simp [partialThen, hx]
  | some u =>
      cases hu : G u <;> simp [partialThen, hx, hu]

/-- Total endomaps embed into the partial-operation monoid by `some`. -/
def totalAsPartial {α : Type*} (f : α → α) : α → Option α :=
  fun x ↦ some (f x)

/-- The embedding of total endomaps preserves composition. -/
theorem totalAsPartial_comp
    {α : Type*} (f g : α → α) :
    partialThen (totalAsPartial f) (totalAsPartial g) =
      totalAsPartial (g ∘ f) := by
  funext x
  simp [partialThen, totalAsPartial, Function.comp_apply]

/-- Ordinary safe total endomaps embed as safe partial endomaps. -/
theorem totalCompatible_embeds_partial
    {α β : Type*} {O : α → β} {f : α → α}
    (h : ∀ x y : α, O x = O y → O (f x) = O (f y)) :
    PartialObservationCompatible O (totalAsPartial f) := by
  intro x y hxy
  simpa [totalAsPartial] using congrArg some (h x y hxy)

/-- A small packaged safe partial endomap.  The preceding identity, closure and
associativity theorems supply its monoid laws without introducing a new
Foundation ontology. -/
structure SafePartialEndomap
    {α β : Type*} (O : α → β) where
  toPartial : α → Option α
  safe : PartialObservationCompatible O toPartial

/-- Identity element in the safe partial-operation family. -/
def SafePartialEndomap.identity
    {α β : Type*} (O : α → β) : SafePartialEndomap O where
  toPartial := fun x ↦ some x
  safe := partialCompatible_identity O

/-- Closed product in the safe partial-operation family. -/
def SafePartialEndomap.then
    {α β : Type*} {O : α → β}
    (F G : SafePartialEndomap O) : SafePartialEndomap O where
  toPartial := partialThen F.toPartial G.toPartial
  safe := partialCompatible_then F.safe G.safe

end EnterpriseMath.FutureQuotient
