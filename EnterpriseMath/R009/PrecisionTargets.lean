import Mathlib

namespace EnterpriseMath.R009

/-- Preservation of the floor quotient by r. -/
def SafeAt (r : ℕ) (F : ℕ → ℕ) : Prop :=
  ∀ n m : ℕ, n / r = m / r → F n / r = F m / r

/-- `τ` is the first input where F reaches output block threshold t*r. -/
def IsFirstCrossing (r t : ℕ) (F : ℕ → ℕ) (τ : ℕ) : Prop :=
  t * r ≤ F τ ∧ ∀ n < τ, F n < t * r

/-- T27 frozen proposition, with nondecreasing maps represented by mathlib `OrderHom`. -/
def T27Statement : Prop :=
  ∀ r : ℕ, 2 ≤ r → ∀ F : ℕ →o ℕ,
    SafeAt r F ↔
      ∀ t τ : ℕ, IsFirstCrossing r t F τ → r ∣ τ

/-- Unboundedness in the form retained by repaired T28. -/
def UnboundedAboveNat (A : ℕ → ℕ) : Prop := ∀ n, ∃ k, n < A k

/-- T28 repaired frozen proposition. The boxed identity is a Galois connection. -/
def T28Statement : Prop :=
  ∀ A : ℕ → ℕ, A 0 = 0 → Function.StrictMono A → UnboundedAboveNat A →
    ∃ R : ℕ →o ℕ,
      GaloisConnection A R ∧
      ∀ r : ℕ, 2 ≤ r →
        (SafeAt r R ↔ ∀ t : ℕ, r ∣ A (t * r))

end EnterpriseMath.R009
