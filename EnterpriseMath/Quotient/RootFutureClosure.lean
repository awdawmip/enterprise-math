import EnterpriseMath.Arithmetic.IntegerRoot
import EnterpriseMath.Quotient.OperationCongruence
import EnterpriseMath.Quotient.RootQuotientWordBasis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

/-- Distinct exact quotient states are separated by one explicit future quotient
before any positive-order root observation.

If `q₁ < q₂`, choose the future denominator `a = q₁ + 1`. Then `q₁ / a = 0`
while `q₂ / a >= 1`, so every positive-order natural root distinguishes the
two outputs. -/
theorem root_observation_future_separates
    {r q₁ q₂ : ℕ}
    (hr : 1 ≤ r)
    (hlt : q₁ < q₂) :
    root r (q₁ / (q₁ + 1)) ≠ root r (q₂ / (q₁ + 1)) := by
  have hr0 : r ≠ 0 := by omega
  have ha : 0 < q₁ + 1 := by omega
  have hleft : q₁ / (q₁ + 1) = 0 := Nat.div_eq_of_lt (by omega)
  have hq : q₁ + 1 ≤ q₂ := by omega
  have hright : 1 ≤ q₂ / (q₁ + 1) := by
    exact (Nat.le_div_iff_mul_le ha).2 (by simpa using hq)
  have hrootright : 1 ≤ root r (q₂ / (q₁ + 1)) := by
    exact (Nat.le_nthRoot_iff (n := r) hr0).2 (by simpa using hright)
  have hrootzero : root r 0 = 0 := by
    exact (EnterpriseMath.IntegerRoot.root_eq_iff (p := r) (n := 0) (k := 0) hr0).2 (by
      constructor
      · simp [zero_pow hr0]
      · simp)
  have hrootleft : root r (q₁ / (q₁ + 1)) = 0 := by
    rw [hleft]
    exact hrootzero
  omega

/-- Full future quotient signatures under a positive-order root observation are
injective in the exact quotient state.

Equivalently: the coarsest refinement of `root r` that is compatible with every
future floor quotient `q ↦ q / a`, `a >= 1`, is exact quotient equality itself.
This is the arithmetic specialization of P023 future-compatible refinement. -/
theorem root_observation_all_future_iff_exact
    {r q₁ q₂ : ℕ}
    (hr : 1 ≤ r) :
    (∀ a : ℕ, 1 ≤ a → root r (q₁ / a) = root r (q₂ / a)) ↔ q₁ = q₂ := by
  constructor
  · intro hfuture
    by_contra hne
    have hcases : q₁ < q₂ ∨ q₂ < q₁ := by omega
    cases hcases with
    | inl hlt =>
        have hsep := root_observation_future_separates hr hlt
        exact hsep (hfuture (q₁ + 1) (by omega))
    | inr hgt =>
        have hsep := root_observation_future_separates hr hgt
        exact hsep (hfuture (q₂ + 1) (by omega)).symm
  · rintro rfl
    intro a _ha
    rfl

/-- A finite separating future action always exists for unequal exact quotient
states. The witness can be taken to be one more than the smaller state. -/
theorem exists_root_observation_future_separator
    {r q₁ q₂ : ℕ}
    (hr : 1 ≤ r)
    (hne : q₁ ≠ q₂) :
    ∃ a : ℕ, 1 ≤ a ∧ root r (q₁ / a) ≠ root r (q₂ / a) := by
  have hcases : q₁ < q₂ ∨ q₂ < q₁ := by omega
  cases hcases with
  | inl hlt =>
      exact ⟨q₁ + 1, by omega, root_observation_future_separates hr hlt⟩
  | inr hgt =>
      exact ⟨q₂ + 1, by omega, (root_observation_future_separates hr hgt).symm⟩

end EnterpriseMath.Quotient
