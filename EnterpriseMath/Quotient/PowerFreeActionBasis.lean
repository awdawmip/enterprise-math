import EnterpriseMath.Quotient.RootAdjacentBoundary
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

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
          push Not at hFree
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
        root r ((q - 1) / b) ≠ root r (q / b) := by
  obtain ⟨b, t, hbPos, htPos, hbFree, hqEq⟩ :=
    exists_rPowerFree_decomposition hr hq
  refine ⟨b, t, hbPos, htPos, hbFree, hqEq, ?_⟩
  exact (root_quotient_adjacent_jump_iff hr hq hbPos).2 ⟨t, htPos, hqEq⟩

/-- A set of positive quotient actions separates exact states up to `N` when
every ordered pair `x<y<=N` is distinguished by at least one action in the set. -/
def SeparatesRootQuotientUpTo (r N : ℕ) (A : Set ℕ) : Prop :=
  ∀ ⦃x y : ℕ⦄, x < y → y ≤ N →
    ∃ a : ℕ, a ∈ A ∧ 1 ≤ a ∧ root r (x / a) ≠ root r (y / a)

/-- Containing every bounded `r`-power-free action is sufficient to separate
all exact states `0,...,N` through quotient-root observations. -/
theorem powerFree_actions_separate_up_to
    {r N : ℕ} {A : Set ℕ}
    (hr : 1 ≤ r)
    (hContains : ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b → b ∈ A) :
    SeparatesRootQuotientUpTo r N A := by
  intro x y hxy hyN
  let q := x + 1
  have hqPos : 1 ≤ q := by
    dsimp [q]
    omega
  have hqLeY : q ≤ y := by
    dsimp [q]
    omega
  obtain ⟨b, t, hbPos, htPos, hbFree, hqEq, hAdjacent⟩ :=
    rPowerFree_decomposition_supplies_boundary_action hr hqPos
  have htPowPos : 1 ≤ t ^ r := by
    have : 0 < t ^ r := pow_pos (by omega) r
    omega
  have hbLeQ : b ≤ q := by
    nlinarith [hqEq, hbPos, htPowPos]
  have hbLeN : b ≤ N := hbLeQ.trans (hqLeY.trans hyN)
  refine ⟨b, hContains b hbPos hbLeN hbFree, hbPos, ?_⟩
  have hr0 : r ≠ 0 := by omega
  have hXQ : x / b ≤ q / b := Nat.div_le_div_right (by omega)
  have hQY : q / b ≤ y / b := Nat.div_le_div_right hqLeY
  have hRootXQ : root r (x / b) ≤ root r (q / b) := root_monotone hr0 hXQ
  have hRootQY : root r (q / b) ≤ root r (y / b) := root_monotone hr0 hQY
  have hAdjacent' : root r (x / b) ≠ root r (q / b) := by
    simpa [q] using hAdjacent
  have hStrict : root r (x / b) < root r (q / b) :=
    lt_of_le_of_ne hRootXQ hAdjacent'
  exact ne_of_lt (hStrict.trans_le hRootQY)

/-- Necessity: every bounded `r`-power-free boundary forces its own action to
belong to any separating action set. -/
theorem separating_actions_contain_powerFree
    {r N : ℕ} {A : Set ℕ}
    (hr : 1 ≤ r)
    (hSep : SeparatesRootQuotientUpTo r N A) :
    ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b → b ∈ A := by
  intro b hbPos hbN hbFree
  have hPredLt : b - 1 < b := by omega
  obtain ⟨a, haA, haPos, hJump⟩ := hSep hPredLt hbN
  have haEq : a = b :=
    rPowerFree_boundary_forces_action hr hbPos haPos hbFree hJump
  simpa [haEq] using haA

/-- Exact bounded future-language criterion.

A positive quotient-action set separates every exact state in `0,...,N` through
`r`-th-root quotient observations if and only if it contains every positive
`r`-power-free integer up to `N`. -/
theorem separatesRootQuotientUpTo_iff_contains_powerFree
    {r N : ℕ} {A : Set ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientUpTo r N A ↔
      ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b → b ∈ A := by
  constructor
  · exact separating_actions_contain_powerFree hr
  · exact powerFree_actions_separate_up_to hr

/-- Canonical bounded action basis: exactly the positive `r`-power-free
integers up to `N`. -/
def PowerFreeActionBasis (r N : ℕ) : Set ℕ :=
  {b : ℕ | 1 ≤ b ∧ b ≤ N ∧ RPowerFree r b}

/-- The canonical power-free action basis separates the entire bounded exact
state domain. -/
theorem powerFreeActionBasis_separates
    {r N : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientUpTo r N (PowerFreeActionBasis r N) := by
  apply powerFree_actions_separate_up_to hr
  intro b hbPos hbN hbFree
  exact ⟨hbPos, hbN, hbFree⟩

/-- Every bounded separating action set contains the canonical power-free basis.
This is the inclusion-minimality / necessity statement behind the unique minimum
future-action language. -/
theorem powerFreeActionBasis_subset_of_separates
    {r N : ℕ} {A : Set ℕ}
    (hr : 1 ≤ r)
    (hSep : SeparatesRootQuotientUpTo r N A) :
    PowerFreeActionBasis r N ⊆ A := by
  intro b hb
  rcases hb with ⟨hbPos, hbN, hbFree⟩
  exact separating_actions_contain_powerFree hr hSep b hbPos hbN hbFree

/-- Any separating action set already contained in the canonical basis must be
exactly that basis.  Hence the power-free basis is the unique least separating
set under inclusion. -/
theorem separating_subset_powerFreeActionBasis_eq
    {r N : ℕ} {A : Set ℕ}
    (hr : 1 ≤ r)
    (hSep : SeparatesRootQuotientUpTo r N A)
    (hSub : A ⊆ PowerFreeActionBasis r N) :
    A = PowerFreeActionBasis r N := by
  apply Set.Subset.antisymm hSub
  exact powerFreeActionBasis_subset_of_separates hr hSep

end EnterpriseMath.Quotient
