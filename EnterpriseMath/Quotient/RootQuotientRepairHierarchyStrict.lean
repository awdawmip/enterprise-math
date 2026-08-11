import EnterpriseMath.Quotient.RootQuotientRelativeRepairStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- At one execution step, every nontrivial reachable product must be a literal
stored instruction. -/
theorem rootQuotientProductReachableWithin_one_iff_mem_of_two_le
    {S : Set ℕ} {t : ℕ}
    (ht : 2 ≤ t) :
    RootQuotientProductReachableWithin 1 S t ↔ t ∈ S := by
  constructor
  · rintro ⟨w, hwLen, hwS, hProd⟩
    cases w with
    | nil =>
        simp [rootQuotientWordProduct] at hProd
        omega
    | cons a w =>
        have hTailZero : w.length = 0 := by
          simp at hwLen
          omega
        have hwNil : w = [] := List.length_eq_zero.mp hTailZero
        subst w
        have hEq : t = a := by
          simpa [rootQuotientWordProduct] using hProd
        rw [hEq]
        exact hwS a (by simp)
  · intro htS
    exact ⟨[t], by simp, by
      intro a ha
      have hEq : a = t := by simpa using ha
      simpa [hEq] using htS,
      by simp [rootQuotientWordProduct]⟩

/-- Minimal finite example where divisor hitting is strictly weaker than exact
bounded-depth repair. -/
def RootQuotientStrictRepairTargets : Finset ℕ := {12, 20}

def RootQuotientStrictRepairCandidates : Set ℕ := ({4, 12, 20} : Set ℕ)

/-- One candidate type (`4`) hits both target divisor neighborhoods. -/
theorem singleton_four_is_divisorCover_strictExample :
    RootQuotientRepairDivisorCover
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates
      ({4} : Set ℕ) := by
  constructor
  · intro g hg
    have hgEq : g = 4 := by simpa using hg
    subst g
    simp [RootQuotientStrictRepairCandidates]
  · intro t ht
    simp [RootQuotientStrictRepairTargets] at ht
    rcases ht with rfl | rfl
    · exact ⟨4, by simp, by norm_num⟩
    · exact ⟨4, by simp, by norm_num⟩

/-- Exact one-step repair is feasible with the two literal target instructions. -/
theorem twelve_twenty_is_exactRepair_strictExample :
    RootQuotientRelativeRepairPresentation
      (∅ : Set ℕ)
      1
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates
      ({12, 20} : Set ℕ) := by
  refine ⟨by simp, ?_, ?_⟩
  · intro g hg
    simp at hg
    rcases hg with rfl | rfl <;>
      simp [RootQuotientStrictRepairCandidates]
  · intro t ht
    simp [RootQuotientStrictRepairTargets] at ht
    have hMem : t ∈ ({12, 20} : Set ℕ) := by
      simpa using ht
    simpa using
      (rootQuotientProductReachableWithin_one_iff_mem_of_two_le
        (S := ({12, 20} : Set ℕ))
        (t := t) (by omega)).2 hMem

/-- Any exact one-step repair dictionary for the example must store both literal
targets, hence has cardinality at least two. -/
theorem two_le_ncard_of_exactRepair_strictExample
    {S : Set ℕ}
    (hS : RootQuotientRelativeRepairPresentation
      (∅ : Set ℕ)
      1
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates
      S) :
    2 ≤ S.ncard := by
  have hReach12 : RootQuotientProductReachableWithin 1 S 12 := by
    have := hS.2.2 12 (by simp [RootQuotientStrictRepairTargets])
    simpa using this
  have hReach20 : RootQuotientProductReachableWithin 1 S 20 := by
    have := hS.2.2 20 (by simp [RootQuotientStrictRepairTargets])
    simpa using this
  have h12 : 12 ∈ S :=
    (rootQuotientProductReachableWithin_one_iff_mem_of_two_le
      (S := S) (t := 12) (by omega)).1 hReach12
  have h20 : 20 ∈ S :=
    (rootQuotientProductReachableWithin_one_iff_mem_of_two_le
      (S := S) (t := 20) (by omega)).1 hReach20
  have hSub : ({12, 20} : Set ℕ) ⊆ S := by
    intro g hg
    simp at hg
    rcases hg with rfl | rfl <;> assumption
  have hCard : ({12, 20} : Set ℕ).ncard ≤ S.ncard :=
    Set.ncard_le_ncard hSub hS.1
  norm_num at hCard ⊢
  exact hCard

/-- **Strict repair-hierarchy witness.**

A one-element divisor cover exists, while every exact horizon-one repair needs
at least two stored types and the two-target literal dictionary attains two.
Hence divisor cover is genuinely a lower relaxation of exact residual-word
repair, not an equivalent reformulation in general. -/
theorem repair_divisorCover_is_strictly_weaker_than_exactRepair :
    RootQuotientRepairDivisorCover
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates
      ({4} : Set ℕ) ∧
    RootQuotientRelativeRepairPresentation
      (∅ : Set ℕ)
      1
      RootQuotientStrictRepairTargets
      RootQuotientStrictRepairCandidates
      ({12, 20} : Set ℕ) ∧
    (∀ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (∅ : Set ℕ)
        1
        RootQuotientStrictRepairTargets
        RootQuotientStrictRepairCandidates
        S →
      2 ≤ S.ncard) := by
  exact ⟨singleton_four_is_divisorCover_strictExample,
    twelve_twenty_is_exactRepair_strictExample,
    fun S hS => two_le_ncard_of_exactRepair_strictExample hS⟩

end EnterpriseMath.Quotient
