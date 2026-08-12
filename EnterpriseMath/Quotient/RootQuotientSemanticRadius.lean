import EnterpriseMath.Quotient.RootQuotientInstructionMetricClosedForms
import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import EnterpriseMath.Quotient.RootQuotientPrimeHorizonGeometry
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Worst-case arbitrary-ISA instruction length over the canonical bounded
semantic specification.

This is the exact semantic radius induced by a primitive presentation `G` in
the additive instruction word metric. -/
noncomputable def rootQuotientSemanticInstructionRadius
    (r N : ℕ) (G : Set ℕ) : ℕ∞ :=
  ⨆ b : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N},
    rootQuotientInstructionLength G b.1

/-- Radius bound is exactly the pointwise bound on every canonical semantic
instruction. -/
theorem rootQuotientSemanticInstructionRadius_le_iff
    {r N : ℕ} {G : Set ℕ} {R : ℕ∞} :
    rootQuotientSemanticInstructionRadius r N G ≤ R ↔
      ∀ b : ℕ,
        b ∈ RootQuotientNontrivialPowerFreeBasis r N →
          rootQuotientInstructionLength G b ≤ R := by
  constructor
  · intro hRadius b hb
    let x : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} := ⟨b, hb⟩
    have hPoint : rootQuotientInstructionLength G x.1 ≤
        rootQuotientSemanticInstructionRadius r N G := by
      dsimp [rootQuotientSemanticInstructionRadius]
      exact le_iSup (fun y : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} =>
        rootQuotientInstructionLength G y.1) x
    exact hPoint.trans hRadius
  · intro hPoint
    dsimp [rootQuotientSemanticInstructionRadius]
    apply iSup_le
    intro x
    exact hPoint x.1 x.2

/-- Separation is exactly a semantic-radius bound in the arbitrary ISA word
metric. -/
theorem separatesRootQuotientWordsUpTo_iff_semanticRadius_le
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hGPos : PositiveRootQuotientGenerators G) :
    SeparatesRootQuotientWordsUpTo r N h G ↔
      rootQuotientSemanticInstructionRadius r N G ≤ (h : ℕ∞) := by
  rw [separatesRootQuotientWordsUpTo_iff_semantic_instructionLength_le
    hr hGPos]
  exact (rootQuotientSemanticInstructionRadius_le_iff).symm

/-- The prime-only exact horizon `L_r(N)` is precisely the semantic radius of
the bounded prime ISA. -/
theorem rootQuotientSemanticInstructionRadius_primeBasis_eq_horizon
    {r N : ℕ} :
    rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeBasis N) =
      (rootQuotientPrimeHorizon r N : ℕ∞) := by
  let L := rootQuotientPrimeHorizon r N
  apply le_antisymm
  · apply (rootQuotientSemanticInstructionRadius_le_iff).2
    intro b hb
    rw [rootQuotientInstructionLength_primeBasis_eq_primeFactorCount
      (by omega) hb.2.1]
    have hCount : rootQuotientPrimeFactorCount b ≤ L :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := L)).1 le_rfl
        b (by omega) hb.2.1 hb.2.2
    exact_mod_cast hCount
  · by_cases hLZero : L = 0
    · subst L
      exact bot_le
    · have hLPos : 0 < L := Nat.pos_of_ne_zero hLZero
      obtain ⟨b, hbPos, hbN, hbFree, hbCount⟩ :=
        exists_powerFree_boundary_at_rootQuotientPrimeHorizon hLPos
      have hbTwo : 2 ≤ b := by
        by_contra hNot
        have hbOne : b = 1 := by omega
        have hZero : rootQuotientPrimeFactorCount b = 0 := by
          simp [hbOne, rootQuotientPrimeFactorCount]
        rw [hbCount] at hZero
        omega
      let x : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} :=
        ⟨b, hbTwo, hbN, hbFree⟩
      have hPoint : rootQuotientInstructionLength (RootQuotientPrimeBasis N) x.1 ≤
          rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeBasis N) := by
        dsimp [rootQuotientSemanticInstructionRadius]
        exact le_iSup (fun y : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} =>
          rootQuotientInstructionLength (RootQuotientPrimeBasis N) y.1) x
      rw [rootQuotientInstructionLength_primeBasis_eq_primeFactorCount hbPos hbN,
        hbCount] at hPoint
      simpa [L] using hPoint

/-- The canonical capacity-`k` complete dictionary has semantic radius exactly
`ceil(L_r(N)/k)`. -/
theorem rootQuotientSemanticInstructionRadius_omegaFiltered_eq_ceilDiv
    {r N k : ℕ}
    (hkPos : 1 ≤ k) :
    rootQuotientSemanticInstructionRadius
        r N (RootQuotientOmegaFilteredBasis r N k) =
      ((rootQuotientPrimeHorizon r N ⌈/⌉ k : ℕ) : ℕ∞) := by
  let L := rootQuotientPrimeHorizon r N
  let D := L ⌈/⌉ k
  apply le_antisymm
  · apply (rootQuotientSemanticInstructionRadius_le_iff).2
    intro b hb
    rw [rootQuotientInstructionLength_omegaFiltered_eq_ceilDiv
      hkPos (by omega) hb.2.1 hb.2.2]
    have hCount : rootQuotientPrimeFactorCount b ≤ L :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := L)).1 le_rfl
        b (by omega) hb.2.1 hb.2.2
    have hLBudget : L ≤ k * D := by
      dsimp [D]
      exact (ceilDiv_le_iff_le_mul (by omega)).1 le_rfl
    have hCountBudget : rootQuotientPrimeFactorCount b ≤ k * D :=
      hCount.trans hLBudget
    have hCeil : rootQuotientPrimeFactorCount b ⌈/⌉ k ≤ D :=
      (ceilDiv_le_iff_le_mul (by omega)).2 hCountBudget
    exact_mod_cast hCeil
  · by_cases hLZero : L = 0
    · have hDZero : D = 0 := by simp [D, hLZero]
      rw [hDZero]
      exact bot_le
    · have hLPos : 0 < L := Nat.pos_of_ne_zero hLZero
      obtain ⟨b, hbPos, hbN, hbFree, hbCount⟩ :=
        exists_powerFree_boundary_at_rootQuotientPrimeHorizon hLPos
      have hbTwo : 2 ≤ b := by
        by_contra hNot
        have hbOne : b = 1 := by omega
        have hZero : rootQuotientPrimeFactorCount b = 0 := by
          simp [hbOne, rootQuotientPrimeFactorCount]
        rw [hbCount] at hZero
        omega
      let x : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} :=
        ⟨b, hbTwo, hbN, hbFree⟩
      have hPoint : rootQuotientInstructionLength
          (RootQuotientOmegaFilteredBasis r N k) x.1 ≤
          rootQuotientSemanticInstructionRadius
            r N (RootQuotientOmegaFilteredBasis r N k) := by
        dsimp [rootQuotientSemanticInstructionRadius]
        exact le_iSup (fun y : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} =>
          rootQuotientInstructionLength
            (RootQuotientOmegaFilteredBasis r N k) y.1) x
      rw [rootQuotientInstructionLength_omegaFiltered_eq_ceilDiv
        hkPos hbPos hbN hbFree, hbCount] at hPoint
      simpa [L, D] using hPoint

/-- In the binary/high-root regime, bounded primes plus macro `4` have semantic
radius exactly the base-three closed-form horizon. -/
theorem rootQuotientSemanticInstructionRadius_primeFour_eq_horizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeFourBasis N) =
      (rootQuotientPrimeFourHorizon N : ℕ∞) := by
  let H := rootQuotientPrimeFourHorizon N
  apply le_antisymm
  · have hSep := primeFourBasis_separates_at_exact_horizon hr hN hBinary
    exact
      (separatesRootQuotientWordsUpTo_iff_semanticRadius_le
        (r := r) (N := N) (h := H)
        (G := RootQuotientPrimeFourBasis N)
        (by omega) rootQuotientPrimeFourBasis_positive).1 hSep
  · have hHEq : H = 1 + Nat.log 3 (N / 2) := by
      dsimp [H]
      exact rootQuotientPrimeFourHorizon_eq hN
    have hHPos : 1 ≤ H := by rw [hHEq]; omega
    let b := 2 * 3 ^ (H - 1)
    have hDivPos : N / 2 ≠ 0 := by omega
    have hPow : 3 ^ Nat.log 3 (N / 2) ≤ N / 2 :=
      Nat.pow_log_le_self 3 hDivPos
    have hbN : b ≤ N := by
      dsimp [b]
      rw [hHEq]
      have hExp : 1 + Nat.log 3 (N / 2) - 1 = Nat.log 3 (N / 2) := by omega
      rw [hExp]
      have hScaled : 2 * 3 ^ Nat.log 3 (N / 2) ≤ 2 * (N / 2) :=
        Nat.mul_le_mul_left 2 hPow
      exact hScaled.trans (by omega)
    have hbPos : 1 ≤ b := by dsimp [b]; positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    let x : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} :=
      ⟨b, by dsimp [b]; omega, hbN, hbFree⟩
    have hPoint : rootQuotientInstructionLength (RootQuotientPrimeFourBasis N) x.1 ≤
        rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeFourBasis N) := by
      dsimp [rootQuotientSemanticInstructionRadius]
      exact le_iSup (fun y : {b : ℕ // b ∈ RootQuotientNontrivialPowerFreeBasis r N} =>
        rootQuotientInstructionLength (RootQuotientPrimeFourBasis N) y.1) x
    rw [rootQuotientInstructionLength_primeFour_eq_weightedCost hN hbPos hbN] at hPoint
    have hCost : rootQuotientPrimeFourCost b = H := by
      dsimp [b]
      exact primeFourCost_two_mul_three_pow_pred hHPos
    rw [hCost] at hPoint
    simpa [H] using hPoint

/-- Unified semantic-radius summary of the three canonical exact presentations. -/
theorem rootQuotientSemanticRadius_three_closedForms
    {r N k : ℕ}
    (hr : 2 ≤ r)
    (hkPos : 1 ≤ k)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeBasis N) =
        (rootQuotientPrimeHorizon r N : ℕ∞) ∧
      rootQuotientSemanticInstructionRadius
          r N (RootQuotientOmegaFilteredBasis r N k) =
        ((rootQuotientPrimeHorizon r N ⌈/⌉ k : ℕ) : ℕ∞) ∧
      rootQuotientSemanticInstructionRadius r N (RootQuotientPrimeFourBasis N) =
        (rootQuotientPrimeFourHorizon N : ℕ∞) :=
  ⟨rootQuotientSemanticInstructionRadius_primeBasis_eq_horizon,
    rootQuotientSemanticInstructionRadius_omegaFiltered_eq_ceilDiv hkPos,
    rootQuotientSemanticInstructionRadius_primeFour_eq_horizon hr hN hBinary⟩

end EnterpriseMath.Quotient
