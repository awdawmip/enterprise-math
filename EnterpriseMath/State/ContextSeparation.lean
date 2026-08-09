import Mathlib.Data.List.Basic
import Mathlib.Logic.Function.Basic

namespace EnterpriseMath.ContextSeparation

/-- Apply elementary contexts from left to right.  Thus `[c₁,c₂]` acts as
`τ c₂ ∘ τ c₁`. -/
def applyContextPath
    {α C : Type*} (τ : C → α → α) : List C → α → α
  | [], x => x
  | c :: path, x => applyContextPath τ path (τ c x)

@[simp] theorem applyContextPath_nil
    {α C : Type*} (τ : C → α → α) (x : α) :
    applyContextPath τ [] x = x := rfl

@[simp] theorem applyContextPath_cons
    {α C : Type*} (τ : C → α → α) (c : C) (path : List C) (x : α) :
    applyContextPath τ (c :: path) x = applyContextPath τ path (τ c x) := rfl

/-- Two states remain observationally indistinguishable under every elementary-
context composition of length at most `n`. -/
def SameThrough
    {α β C : Type*} (O : α → β) (τ : C → α → α)
    (n : ℕ) (x y : α) : Prop :=
  ∀ path : List C, path.length ≤ n →
    O (applyContextPath τ path x) = O (applyContextPath τ path y)

@[simp] theorem sameThrough_zero_iff
    {α β C : Type*} (O : α → β) (τ : C → α → α) (x y : α) :
    SameThrough O τ 0 x y ↔ O x = O y := by
  constructor
  · intro h
    simpa using h [] (Nat.le_refl 0)
  · intro h path hlen
    have hnil : path = [] := by
      apply List.eq_nil_of_length_eq_zero
      exact Nat.eq_zero_of_le_zero hlen
    subst path
    simpa using h

/-- Looking through more context depth can only refine indistinguishability. -/
theorem sameThrough_mono
    {α β C : Type*} {O : α → β} {τ : C → α → α}
    {m n : ℕ} {x y : α} (hmn : m ≤ n)
    (h : SameThrough O τ n x y) : SameThrough O τ m x y := by
  intro path hlen
  exact h path (Nat.le_trans hlen hmn)

/-- P018-T172/T186 relation core: one more context-refinement depth is exactly
current horizon agreement plus horizon-`n` agreement after every elementary
one-hole translation. -/
theorem sameThrough_succ_iff
    {α β C : Type*} (O : α → β) (τ : C → α → α)
    (n : ℕ) (x y : α) :
    SameThrough O τ n.succ x y ↔
      SameThrough O τ n x y ∧
        ∀ c : C, SameThrough O τ n (τ c x) (τ c y) := by
  constructor
  · intro h
    constructor
    · exact sameThrough_mono (Nat.le_succ n) h
    · intro c path hlen
      have hcons : (c :: path).length ≤ n.succ := by
        simpa using Nat.succ_le_succ hlen
      simpa using h (c :: path) hcons
  · rintro ⟨hcurrent, hnext⟩ path hlen
    cases path with
    | nil =>
        exact hcurrent [] (Nat.zero_le n)
    | cons c rest =>
        have hrest : rest.length ≤ n := by
          exact Nat.succ_le_succ_iff.mp hlen
        simpa using hnext c rest hrest

/-- Every finite context-horizon relation is reflexive. -/
theorem sameThrough_refl
    {α β C : Type*} (O : α → β) (τ : C → α → α)
    (n : ℕ) (x : α) : SameThrough O τ n x x := by
  intro path hlen
  rfl

/-- Every finite context-horizon relation is symmetric. -/
theorem sameThrough_symm
    {α β C : Type*} {O : α → β} {τ : C → α → α}
    {n : ℕ} {x y : α} (h : SameThrough O τ n x y) :
    SameThrough O τ n y x := by
  intro path hlen
  exact (h path hlen).symm

/-- Every finite context-horizon relation is transitive.  This is the relation-
level source of the reverse strong-triangle law for first-separation depth. -/
theorem sameThrough_trans
    {α β C : Type*} {O : α → β} {τ : C → α → α}
    {n : ℕ} {x y z : α}
    (hxy : SameThrough O τ n x y)
    (hyz : SameThrough O τ n y z) :
    SameThrough O τ n x z := by
  intro path hlen
  exact (hxy path hlen).trans (hyz path hlen)

/-- If `x,z` are distinguished by context depth `n`, then at least one leg of
`x-y-z` is already distinguished by that same depth. -/
theorem not_sameThrough_triangle
    {α β C : Type*} {O : α → β} {τ : C → α → α}
    {n : ℕ} {x y z : α}
    (hxz : ¬ SameThrough O τ n x z) :
    ¬ SameThrough O τ n x y ∨ ¬ SameThrough O τ n y z := by
  by_contra h
  push Not at h
  exact hxz (sameThrough_trans h.1 h.2)

end EnterpriseMath.ContextSeparation
