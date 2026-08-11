import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import EnterpriseMath.Quotient.RootQuotientSpareMacroDivisibility
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Split a literal word over a union alphabet into a spare subword and a base
subword.  Because quotient-word products live in the commutative monoid of
positive denominators, the two subsequences may be regrouped without changing
the compiled product. -/
theorem exists_split_rootQuotientWord_over_union
    {G S : Set ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (G ∪ S) w) :
    ∃ u v : List ℕ,
      u.length + v.length = w.length ∧
      RootQuotientWordOver S u ∧
      RootQuotientWordOver G v ∧
      rootQuotientWordProduct u * rootQuotientWordProduct v =
        rootQuotientWordProduct w := by
  induction w with
  | nil =>
      exact ⟨[], [], by simp, by simp [RootQuotientWordOver],
        by simp [RootQuotientWordOver], by simp [rootQuotientWordProduct]⟩
  | cons a w ih =>
      have haUnion : a ∈ G ∪ S := hw a (by simp)
      have hwTail : RootQuotientWordOver (G ∪ S) w := by
        intro g hg
        exact hw g (by simp [hg])
      obtain ⟨u, v, hLen, huS, hvG, hProd⟩ := ih hwTail
      by_cases haS : a ∈ S
      · refine ⟨a :: u, v, ?_, ?_, hvG, ?_⟩
        · simp [hLen]
        · intro g hg
          simp at hg
          rcases hg with rfl | hgU
          · exact haS
          · exact huS g hgU
        · rw [rootQuotientWordProduct]
          calc
            (a * rootQuotientWordProduct u) * rootQuotientWordProduct v =
                a * (rootQuotientWordProduct u * rootQuotientWordProduct v) := by
                  rw [Nat.mul_assoc]
            _ = a * rootQuotientWordProduct w := by rw [hProd]
            _ = rootQuotientWordProduct (a :: w) := by
              simp [rootQuotientWordProduct]
      · have haG : a ∈ G := by
          rcases haUnion with haG | haS'
          · exact haG
          · exact (haS haS').elim
        refine ⟨u, a :: v, ?_, huS, ?_, ?_⟩
        · simp [hLen]
        · intro g hg
          simp at hg
          rcases hg with rfl | hgV
          · exact haG
          · exact hvG g hgV
        · rw [rootQuotientWordProduct]
          calc
            rootQuotientWordProduct u * (a * rootQuotientWordProduct v) =
                a * (rootQuotientWordProduct u * rootQuotientWordProduct v) := by
                  ac_rfl
            _ = a * rootQuotientWordProduct w := by rw [hProd]
            _ = rootQuotientWordProduct (a :: w) := by
              simp [rootQuotientWordProduct]

/-- **Exact multi-spare reachability convolution.**

Reachability over a union alphabet is the multiplicative convolution of the two
bounded reachability balls:

`R_h(G ∪ S) = ⋃_{j+k≤h} R_j(S) * R_k(G)`.

This is the many-spare analogue of the one-spare factorization theorem. -/
theorem rootQuotientProductReachableWithin_union_iff_exists_convolution
    {G S : Set ℕ} {t h : ℕ} :
    RootQuotientProductReachableWithin h (G ∪ S) t ↔
      ∃ j k a b : ℕ,
        j + k ≤ h ∧
        RootQuotientProductReachableWithin j S a ∧
        RootQuotientProductReachableWithin k G b ∧
        a * b = t := by
  constructor
  · rintro ⟨w, hwLen, hwUnion, hProd⟩
    obtain ⟨u, v, hLen, huS, hvG, hSplit⟩ :=
      exists_split_rootQuotientWord_over_union hwUnion
    let j := u.length
    let k := v.length
    let a := rootQuotientWordProduct u
    let b := rootQuotientWordProduct v
    refine ⟨j, k, a, b, ?_, ?_, ?_, ?_⟩
    · dsimp [j, k]
      omega
    · exact ⟨u, le_rfl, huS, rfl⟩
    · exact ⟨v, le_rfl, hvG, rfl⟩
    · dsimp [a, b]
      exact hSplit.trans hProd.symm
  · rintro ⟨j, k, a, b, hjk, haReach, hbReach, hProd⟩
    obtain ⟨u, huLen, huS, haProd⟩ := haReach
    obtain ⟨v, hvLen, hvG, hbProd⟩ := hbReach
    refine ⟨u ++ v, ?_, ?_, ?_⟩
    · rw [List.length_append]
      omega
    · intro g hg
      rw [List.mem_append] at hg
      rcases hg with hgU | hgV
      · exact Or.inr (huS g hgU)
      · exact Or.inl (hvG g hgV)
    · calc
        t = a * b := hProd.symm
        _ = rootQuotientWordProduct u * rootQuotientWordProduct v := by
          rw [← haProd, ← hbProd]
        _ = rootQuotientWordProduct (u ++ v) :=
          (rootQuotientWordProduct_append u v).symm

/-- **Multi-spare divisor-cover necessity.**

If a target is outside the horizon-`h` ball of a base ISA `G` but becomes
reachable after adjoining an arbitrary spare family `S`, then at least one
actual spare instruction divides the target.

Thus every base-hard target must be hit by the divisor neighborhood of the
stored spare family. -/
theorem exists_spare_divisor_of_union_reachable_not_base
    {G S : Set ℕ} {t h : ℕ}
    (hReach : RootQuotientProductReachableWithin h (G ∪ S) t)
    (hNoBase : ¬RootQuotientProductReachableWithin h G t) :
    ∃ g : ℕ, g ∈ S ∧ g ∣ t := by
  obtain ⟨w, hwLen, hwUnion, hProd⟩ := hReach
  by_contra hNoSpare
  push_neg at hNoSpare
  apply hNoBase
  refine ⟨w, hwLen, ?_, hProd⟩
  intro a haWord
  have haUnion := hwUnion a haWord
  rcases haUnion with haG | haS
  · exact haG
  · have haDvd : a ∣ t :=
      word_member_dvd_compiled_product haWord hProd
    exact (hNoSpare a haS haDvd).elim

/-- Finite-family form: a spare family that repairs every base-hard target is a
divisor hitting set for that target family. -/
theorem spare_family_divisor_covers_base_hard_targets
    {G S : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hReach : ∀ t ∈ T,
      RootQuotientProductReachableWithin h (G ∪ S) t)
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t) :
    ∀ t ∈ T, ∃ g : ℕ, g ∈ S ∧ g ∣ t := by
  intro t ht
  exact exists_spare_divisor_of_union_reachable_not_base
    (hReach t ht) (hNoBase t ht)

end EnterpriseMath.Quotient
