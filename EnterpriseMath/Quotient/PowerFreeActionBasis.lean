import EnterpriseMath.Quotient.RootAdjacentBoundary
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every positive integer admits an `r`-power-free decomposition

`q = b * t^r`

for every positive root order `r`.

The proof intentionally avoids prime factorization.  If `q` is not already
`r`-power-free, remove one nontrivial `u^r` divisor.  The remaining cofactor is
positive and strictly smaller, so strong induction terminates.  This is the
existence half needed by the bounded future-action basis theorem. -/
theorem exists_rPowerFree_decomposition
    {r q : ℕ}
    (hr : 1 ≤ r)
    (hq : 1 ≤ q) :
    ∃ b t : ℕ,
      1 ≤ b ∧ 1 ≤ t ∧ RPowerFree r b ∧ q = b * t ^ r := by
  revert hq
  induction q using Nat.strong_induction_on with
  | h q ih =>
      intro hq
      by_cases hFree : RPowerFree r q
      · exact ⟨q, 1, hq, by omega, hFree, by simp⟩
      · have hFactor : ∃ u : ℕ, 2 ≤ u ∧ u ^ r ∣ q := by
          unfold RPowerFree at hFree
          push_neg at hFree
          exact hFree
        obtain ⟨u, hu, hUDvd⟩ := hFactor
        rcases hUDvd with ⟨c, hqFactor⟩
        have huPow : 2 ≤ u ^ r := by
          calc
            2 ≤ u := hu
            _ = u ^ 1 := by simp
            _ ≤ u ^ r := Nat.pow_le_pow_right (by omega) hr
        have hcPos : 1 ≤ c := by
          by_contra hnot
          have hcZero : c = 0 := by omega
          subst c
          simp at hqFactor
          omega
        have hcLt : c < q := by
          nlinarith [hqFactor, huPow, hcPos]
        obtain ⟨b, v, hbPos, hvPos, hbFree, hcEq⟩ := ih c hcLt hcPos
        refine ⟨b, u * v, hbPos, Nat.mul_pos (by omega) (by omega), hbFree, ?_⟩
        calc
          q = u ^ r * c := hqFactor
          _ = u ^ r * (b * v ^ r) := by rw [hcEq]
          _ = b * (u * v) ^ r := by
            rw [mul_pow]
            ring

/-- The power-free part of a positive decomposition always supplies an action
that distinguishes the corresponding adjacent exact-state boundary. -/
theorem rPowerFree_decomposition_supplies_boundary_action
    {r q : ℕ}
    (hr : 1 ≤ r)
    (hq : 1 ≤ q) :
    ∃ b t : ℕ,
      1 ≤ b ∧ 1 ≤ t ∧ RPowerFree r b ∧ q = b * t ^ r ∧
        EnterpriseMath.IntegerRoot.root r ((q - 1) / b) ≠
          EnterpriseMath.IntegerRoot.root r (q / b) := by
  obtain ⟨b, t, hbPos, htPos, hbFree, hqEq⟩ :=
    exists_rPowerFree_decomposition hr hq
  refine ⟨b, t, hbPos, htPos, hbFree, hqEq, ?_⟩
  exact (root_quotient_adjacent_jump_iff hr hq hbPos).2 ⟨t, htPos, hqEq⟩

end EnterpriseMath.Quotient
