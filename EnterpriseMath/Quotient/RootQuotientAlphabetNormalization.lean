import EnterpriseMath.Quotient.RootQuotientLeastPhase
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Remove identity instructions from a quotient word.  They consume execution
slots but do not change the compiled denominator. -/
def rootQuotientEraseIdentityWord (w : List ℕ) : List ℕ :=
  w.filter (fun g => g != 1)

/-- Removing identity instructions preserves the ordinary product. -/
theorem rootQuotientEraseIdentityWord_prod
    (w : List ℕ) :
    (rootQuotientEraseIdentityWord w).prod = w.prod := by
  induction w with
  | nil => simp [rootQuotientEraseIdentityWord]
  | cons a w ih =>
      by_cases ha : a = 1
      · simp [rootQuotientEraseIdentityWord, ha, ih]
      · simp [rootQuotientEraseIdentityWord, ha, ih]

/-- Removing identity instructions never increases word length. -/
theorem rootQuotientEraseIdentityWord_length_le
    (w : List ℕ) :
    (rootQuotientEraseIdentityWord w).length ≤ w.length := by
  simpa [rootQuotientEraseIdentityWord] using
    List.length_filter_le (fun g : ℕ => g != 1) w

/-- Every surviving instruction in the identity-erased word came from the
original word and is nontrivial. -/
theorem mem_rootQuotientEraseIdentityWord_iff
    {g : ℕ} {w : List ℕ} :
    g ∈ rootQuotientEraseIdentityWord w ↔ g ∈ w ∧ g ≠ 1 := by
  simp [rootQuotientEraseIdentityWord]

/-- Normalize an arbitrary positive primitive alphabet to the finite canonical
semantic candidate set. -/
def RootQuotientSemanticNormalization
    (r N : ℕ) (G : Set ℕ) : Set ℕ :=
  G ∩ RootQuotientNontrivialPowerFreeBasis r N

/-- Semantic normalization only removes primitive instructions. -/
theorem rootQuotientSemanticNormalization_subset
    {r N : ℕ} {G : Set ℕ} :
    RootQuotientSemanticNormalization r N G ⊆ G := by
  intro g hg
  exact hg.1

/-- Semantic normalization remains positive when the original alphabet is
positive. -/
theorem rootQuotientSemanticNormalization_positive
    {r N : ℕ} {G : Set ℕ}
    (hG : PositiveRootQuotientGenerators G) :
    PositiveRootQuotientGenerators
      (RootQuotientSemanticNormalization r N G) := by
  intro g hg
  exact hG g hg.1

/-- Every instruction appearing in a word divides the compiled product. -/
theorem word_member_dvd_compiled_product
    {w : List ℕ} {g b : ℕ}
    (hg : g ∈ w)
    (hProd : b = rootQuotientWordProduct w) :
    g ∣ b := by
  have hgDvd : g ∣ w.prod := List.dvd_prod hg
  rw [← rootQuotientWordProduct_eq_prod] at hgDvd
  simpa [hProd] using hgDvd

/-- Pointwise normalization theorem.

For a required bounded power-free semantic denominator `b`, every positive
word over an arbitrary alphabet can be replaced, without increasing its
length, by a word over the normalized finite semantic alphabet.  Identity
instructions are deleted; every remaining instruction divides `b`, hence is a
bounded power-free divisor. -/
theorem rootQuotient_reachable_normalize_to_semanticBasis
    {r N h b : ℕ} {G : Set ℕ}
    (hG : PositiveRootQuotientGenerators G)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b)
    (hReach : RootQuotientProductReachableWithin h G b) :
    RootQuotientProductReachableWithin h
      (RootQuotientSemanticNormalization r N G) b := by
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  let w' := rootQuotientEraseIdentityWord w
  have hwLen' : w'.length ≤ h :=
    (rootQuotientEraseIdentityWord_length_le w).trans hwLen
  have hwProd' : b = rootQuotientWordProduct w' := by
    rw [rootQuotientWordProduct_eq_prod,
      rootQuotientEraseIdentityWord_prod]
    simpa [rootQuotientWordProduct_eq_prod] using hProd
  have hwNorm :
      RootQuotientWordOver
        (RootQuotientSemanticNormalization r N G) w' := by
    intro g hgW'
    have hgData :=
      (mem_rootQuotientEraseIdentityWord_iff (g := g) (w := w)).1 hgW'
    have hgW : g ∈ w := hgData.1
    have hgNeOne : g ≠ 1 := hgData.2
    have hgG : g ∈ G := hwG g hgW
    have hgPos : 1 ≤ g := hG g hgG
    have hgTwo : 2 ≤ g := by omega
    have hgDvd : g ∣ b := word_member_dvd_compiled_product hgW hProd
    have hgN : g ≤ N :=
      (Nat.le_of_dvd (by omega) hgDvd).trans hbN
    have hgFree : RPowerFree r g :=
      rPowerFree_of_dvd_of_rPowerFree hgDvd hbFree
    exact ⟨hgG, hgTwo, hgN, hgFree⟩
  exact ⟨w', hwLen', hwNorm, hwProd'⟩

/-- Global normalization theorem: every positive separating primitive alphabet
can be intersected with the finite canonical semantic candidate set without
losing separation at the same horizon. -/
theorem rootQuotient_separator_normalize_to_semanticBasis
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientSemanticNormalization r N G) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := h)
    (G := RootQuotientSemanticNormalization r N G)
    hr (rootQuotientSemanticNormalization_positive hG)).2
  intro b hbPos hbN hbFree
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h) (G := G) hr hG).1 hSep
      b hbPos hbN hbFree
  exact rootQuotient_reachable_normalize_to_semanticBasis
    hG hbPos hbN hbFree hReach

end EnterpriseMath.Quotient
