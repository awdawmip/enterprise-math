import Mathlib.Logic.Function.Iterate

namespace EnterpriseMath.ObservationClosure

open Function

/-- Two states have identical observations through the finite horizon `0..n`. -/
def SameObservedThrough {α β : Type*} (O : α → β) (F : α → α)
    (n : ℕ) (x y : α) : Prop :=
  ∀ i : ℕ, i ≤ n → O (F^[i] x) = O (F^[i] y)

/-- The observation kernel is forward compatible with one deterministic endomap. -/
def ObservationCompatible {α β : Type*} (O : α → β) (F : α → α) : Prop :=
  ∀ ⦃x y : α⦄, O x = O y → O (F x) = O (F y)

@[simp] theorem sameObservedThrough_zero_iff
    {α β : Type*} (O : α → β) (F : α → α) (x y : α) :
    SameObservedThrough O F 0 x y ↔ O x = O y := by
  constructor
  · intro h
    simpa using h 0 le_rfl
  · intro h i hi
    have : i = 0 := Nat.eq_zero_of_le_zero hi
    subst i
    simpa using h

/-- Looking farther into the future can only refine observational equivalence. -/
theorem sameObservedThrough_mono
    {α β : Type*} {O : α → β} {F : α → α}
    {m n : ℕ} {x y : α} (hmn : m ≤ n)
    (h : SameObservedThrough O F n x y) :
    SameObservedThrough O F m x y := by
  intro i hi
  exact h i (hi.trans hmn)

/-- P018-T161 relation form: one extra observed step is current observation
agreement plus horizon-`n` agreement after one deterministic step. -/
theorem sameObservedThrough_succ_iff
    {α β : Type*} (O : α → β) (F : α → α)
    (n : ℕ) (x y : α) :
    SameObservedThrough O F n.succ x y ↔
      O x = O y ∧ SameObservedThrough O F n (F x) (F y) := by
  constructor
  · intro h
    constructor
    · simpa using h 0 (Nat.zero_le _)
    · intro i hi
      have hs := h i.succ (Nat.succ_le_succ hi)
      simpa [Function.iterate_succ_apply] using hs
  · rintro ⟨hzero, htail⟩ i hi
    cases i with
    | zero => simpa using hzero
    | succ i =>
        have hin : i ≤ n := Nat.succ_le_succ_iff.mp hi
        have hs := htail i hin
        simpa [Function.iterate_succ_apply] using hs

/-- A dynamically compatible observation preserves equality for every finite
future iterate. -/
theorem observationCompatible_all_future
    {α β : Type*} {O : α → β} {F : α → α}
    (hcomp : ObservationCompatible O F) :
    ∀ n : ℕ, ∀ ⦃x y : α⦄, O x = O y → O (F^[n] x) = O (F^[n] y) := by
  intro n
  induction n with
  | zero =>
      intro x y hxy
      simpa using hxy
  | succ n ih =>
      intro x y hxy
      rw [Function.iterate_succ_apply, Function.iterate_succ_apply]
      exact ih (hcomp hxy)

/-- Dynamic closure is exactly the statement that horizon-zero equivalence does
not split after one more observed step. -/
theorem observationCompatible_iff_zero_stable
    {α β : Type*} (O : α → β) (F : α → α) :
    ObservationCompatible O F ↔
      ∀ x y : α,
        SameObservedThrough O F 0 x y ↔ SameObservedThrough O F 1 x y := by
  constructor
  · intro hcomp x y
    constructor
    · intro hzero
      have hxy : O x = O y := (sameObservedThrough_zero_iff O F x y).mp hzero
      intro i hi
      interval_cases i <;> simp_all [ObservationCompatible, Function.iterate_succ_apply]
    · exact sameObservedThrough_mono (Nat.zero_le 1)
  · intro hstable x y hxy
    have hzero : SameObservedThrough O F 0 x y :=
      (sameObservedThrough_zero_iff O F x y).mpr hxy
    have hone := (hstable x y).mp hzero
    have hsucc := (sameObservedThrough_succ_iff O F 0 x y).mp hone
    simpa using (sameObservedThrough_zero_iff O F (F x) (F y)).mp hsucc.2

/-- If one finite predictive relation is unchanged by adding one more observed
step, that relation is already forward compatible. -/
theorem stable_horizon_forward_compatible
    {α β : Type*} {O : α → β} {F : α → α} {n : ℕ}
    (hstable : ∀ x y : α,
      SameObservedThrough O F n x y ↔ SameObservedThrough O F n.succ x y) :
    ∀ ⦃x y : α⦄,
      SameObservedThrough O F n x y →
        SameObservedThrough O F n (F x) (F y) := by
  intro x y hxy
  have hsucc := (hstable x y).mp hxy
  exact (sameObservedThrough_succ_iff O F n x y).mp hsucc |>.2

/-- P018-T162/T164 relation core: once a finite horizon relation is stable, its
members have equal observations at every later finite time.  No infinite limit
or topology is used. -/
theorem stable_horizon_all_future
    {α β : Type*} {O : α → β} {F : α → α} {n : ℕ}
    (hstable : ∀ x y : α,
      SameObservedThrough O F n x y ↔ SameObservedThrough O F n.succ x y)
    {x y : α} (hxy : SameObservedThrough O F n x y) :
    ∀ k : ℕ, O (F^[k] x) = O (F^[k] y) := by
  have hforward := stable_horizon_forward_compatible (O := O) (F := F) hstable
  have hiter : ∀ k : ℕ, ∀ ⦃a b : α⦄,
      SameObservedThrough O F n a b →
        SameObservedThrough O F n (F^[k] a) (F^[k] b) := by
    intro k
    induction k with
    | zero =>
        intro a b hab
        simpa using hab
    | succ k ih =>
        intro a b hab
        rw [Function.iterate_succ_apply, Function.iterate_succ_apply]
        exact ih (hforward hab)
  intro k
  have hk := hiter k hxy
  simpa using hk 0 (Nat.zero_le n)

end EnterpriseMath.ObservationClosure
