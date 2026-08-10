import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import Mathlib.Data.ENat.Basic
import Mathlib.Data.Nat.Find
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Infinite-valued shortest word length for compiling one denominator from a
primitive quotient ISA.  Unreachable denominators have length `∞`.

Unlike presentation-to-presentation compiler expansion, this is an additive
word metric on multiplicative semantic actions: the identity denominator has
length zero and multiplying targets concatenates words. -/
noncomputable def rootQuotientInstructionLength
    (G : Set ℕ) (b : ℕ) : ℕ∞ :=
  if hExists : ∃ h : ℕ, RootQuotientProductReachableWithin h G b then
    (Nat.find hExists : ℕ)
  else
    ⊤

/-- Finite instruction length is equivalent to eventual reachability. -/
theorem rootQuotientInstructionLength_ne_top_iff
    {G : Set ℕ} {b : ℕ} :
    rootQuotientInstructionLength G b ≠ ⊤ ↔
      ∃ h : ℕ, RootQuotientProductReachableWithin h G b := by
  classical
  unfold rootQuotientInstructionLength
  split_ifs with hExists
  · exact ⟨fun _ => hExists, fun _ => ENat.natCast_ne_top _⟩
  · simp [hExists]

/-- Reachability is monotone in the execution horizon. -/
theorem rootQuotientProductReachableWithin_mono_horizon'
    {G : Set ℕ} {b h j : ℕ}
    (hhj : h ≤ j)
    (hReach : RootQuotientProductReachableWithin h G b) :
    RootQuotientProductReachableWithin j G b := by
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  exact ⟨w, hwLen.trans hhj, hwG, hProd⟩

/-- Exact finite-radius characterization of the instruction word metric. -/
theorem rootQuotientInstructionLength_le_natCast_iff
    {G : Set ℕ} {b h : ℕ} :
    rootQuotientInstructionLength G b ≤ (h : ℕ∞) ↔
      RootQuotientProductReachableWithin h G b := by
  classical
  unfold rootQuotientInstructionLength
  split_ifs with hExists
  · let m := Nat.find hExists
    have hmReach : RootQuotientProductReachableWithin m G b :=
      Nat.find_spec hExists
    constructor
    · intro hLe
      have hmLe : m ≤ h := by
        exact_mod_cast hLe
      exact rootQuotientProductReachableWithin_mono_horizon' hmLe hmReach
    · intro hReach
      have hmLe : m ≤ h := Nat.find_min' hExists hReach
      exact_mod_cast hmLe
  · constructor
    · intro hLe
      have hTop : (h : ℕ∞) = ⊤ := top_unique hLe
      exact (ENat.natCast_ne_top h hTop).elim
    · intro hReach
      exact (hExists ⟨h, hReach⟩).elim

/-- The multiplicative identity has instruction length zero over every ISA. -/
theorem rootQuotientInstructionLength_one
    {G : Set ℕ} :
    rootQuotientInstructionLength G 1 = 0 := by
  apply le_antisymm
  · exact
      (rootQuotientInstructionLength_le_natCast_iff
        (G := G) (b := 1) (h := 0)).2
        ⟨[], by simp, by simp [RootQuotientWordOver], by simp [rootQuotientWordProduct]⟩
  · exact bot_le

/-- Every literal primitive instruction has word length at most one. -/
theorem rootQuotientInstructionLength_le_one_of_mem
    {G : Set ℕ} {g : ℕ}
    (hg : g ∈ G) :
    rootQuotientInstructionLength G g ≤ 1 := by
  apply (rootQuotientInstructionLength_le_natCast_iff
    (G := G) (b := g) (h := 1)).2
  exact ⟨[g], by simp, by
    intro a ha
    have hEq : a = g := by simpa using ha
    simpa [hEq] using hg,
    by simp [rootQuotientWordProduct]⟩

/-- Additive triangle inequality on semantic multiplication.

The shortest instruction word for a product is no longer than concatenating
shortest words for the two factors.  Unreachable factors contribute `∞`. -/
theorem rootQuotientInstructionLength_mul_le_add
    {G : Set ℕ} {a b : ℕ} :
    rootQuotientInstructionLength G (a * b) ≤
      rootQuotientInstructionLength G a +
        rootQuotientInstructionLength G b := by
  classical
  by_cases haExists : ∃ h : ℕ, RootQuotientProductReachableWithin h G a
  · by_cases hbExists : ∃ j : ℕ, RootQuotientProductReachableWithin j G b
    · let h := Nat.find haExists
      let j := Nat.find hbExists
      have haReach : RootQuotientProductReachableWithin h G a := Nat.find_spec haExists
      have hbReach : RootQuotientProductReachableWithin j G b := Nat.find_spec hbExists
      have habReach : RootQuotientProductReachableWithin (h + j) G (a * b) :=
        rootQuotientProductReachableWithin_mul haReach hbReach
      have hLe : rootQuotientInstructionLength G (a * b) ≤ ((h + j : ℕ) : ℕ∞) :=
        (rootQuotientInstructionLength_le_natCast_iff).2 habReach
      have haLen : rootQuotientInstructionLength G a = (h : ℕ∞) := by
        simp [rootQuotientInstructionLength, haExists, h]
      have hbLen : rootQuotientInstructionLength G b = (j : ℕ∞) := by
        simp [rootQuotientInstructionLength, hbExists, j]
      rw [haLen, hbLen]
      simpa using hLe
    · have hbTop : rootQuotientInstructionLength G b = ⊤ := by
        simp [rootQuotientInstructionLength, hbExists]
      rw [hbTop]
      simp
  · have haTop : rootQuotientInstructionLength G a = ⊤ := by
      simp [rootQuotientInstructionLength, haExists]
    rw [haTop]
    simp

/-- Bounded compiler implementation of an alphabet is exactly a uniform bound
on the implementation-ISA word metric over all target instructions. -/
theorem rootQuotientAlphabetCompilesWithin_iff_instructionLength_le
    {H G : Set ℕ} {h : ℕ} :
    RootQuotientAlphabetCompilesWithin h H G ↔
      ∀ g : ℕ, g ∈ G → rootQuotientInstructionLength H g ≤ (h : ℕ∞) := by
  constructor
  · intro hCompile g hg
    exact (rootQuotientInstructionLength_le_natCast_iff).2 (hCompile g hg)
  · intro hMetric g hg
    exact (rootQuotientInstructionLength_le_natCast_iff).1 (hMetric g hg)

/-- Exact task-correctness interpretation in the arbitrary ISA word metric:
separation within `h` iff every canonical semantic instruction lies inside the
instruction-metric ball of radius `h`. -/
theorem separatesRootQuotientWordsUpTo_iff_semantic_instructionLength_le
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hGPos : PositiveRootQuotientGenerators G) :
    SeparatesRootQuotientWordsUpTo r N h G ↔
      ∀ b : ℕ,
        b ∈ RootQuotientNontrivialPowerFreeBasis r N →
          rootQuotientInstructionLength G b ≤ (h : ℕ∞) := by
  rw [separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis hr hGPos]
  exact rootQuotientAlphabetCompilesWithin_iff_instructionLength_le

/-- Recompiling one ISA through another scales the semantic instruction metric
by at most the compiler expansion factor `j`, provided `j` is positive.

This is the bridge between the additive action metric and multiplicative
presentation refinement. -/
theorem rootQuotientInstructionLength_recompile_le
    {H G : Set ℕ} {j b : ℕ}
    (hj : 1 ≤ j)
    (hCompile : RootQuotientAlphabetCompilesWithin j H G) :
    rootQuotientInstructionLength H b ≤
      (j : ℕ∞) * rootQuotientInstructionLength G b := by
  classical
  by_cases hExists : ∃ h : ℕ, RootQuotientProductReachableWithin h G b
  · let h := Nat.find hExists
    have hReach : RootQuotientProductReachableWithin h G b := Nat.find_spec hExists
    have hRecompiled : RootQuotientProductReachableWithin (h * j) H b :=
      rootQuotientProductReachableWithin_recompile hCompile hReach
    have hLe : rootQuotientInstructionLength H b ≤ ((h * j : ℕ) : ℕ∞) :=
      (rootQuotientInstructionLength_le_natCast_iff).2 hRecompiled
    have hLenG : rootQuotientInstructionLength G b = (h : ℕ∞) := by
      simp [rootQuotientInstructionLength, hExists, h]
    rw [hLenG]
    simpa [Nat.mul_comm] using hLe
  · have hTop : rootQuotientInstructionLength G b = ⊤ := by
      simp [rootQuotientInstructionLength, hExists]
    rw [hTop]
    have hjNeZero : (j : ℕ∞) ≠ 0 := by
      exact_mod_cast (show j ≠ 0 by omega)
    rw [ENat.mul_top hjNeZero]
    exact le_top

end EnterpriseMath.Quotient
