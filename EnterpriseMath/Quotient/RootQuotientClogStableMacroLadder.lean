import EnterpriseMath.Quotient.RootQuotientCountedStableMacroLadder
import Mathlib.Data.Nat.Log
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Least exponent needed for the `i`-th prime direction to reach the stable
base selected by macro budget `s`. -/
noncomputable def rootQuotientStableMacroExponent
    (s i : ℕ) : ℕ :=
  Nat.clog (Nat.nth Nat.Prime i) (rootQuotientStablePrimeBase s)

/-- Minimal pure-prime-power macro attached to direction `i` under budget `s`. -/
noncomputable def rootQuotientStablePrimePowerMacro
    (s i : ℕ) : ℕ :=
  (Nat.nth Nat.Prime i) ^ rootQuotientStableMacroExponent s i

/-- Finite bounded family of the first `s` minimal prime-power macros. -/
noncomputable def rootQuotientClogStableMacroFinset
    (N s : ℕ) : Finset ℕ := by
  classical
  exact ((Finset.range s).image (rootQuotientStablePrimePowerMacro s)).filter
    fun g => g ≤ N

/-- Set-valued minimal-power stable macro family. -/
noncomputable def RootQuotientClogStableMacroSet
    (N s : ℕ) : Set ℕ :=
  ↑(rootQuotientClogStableMacroFinset N s)

/-- Exact membership description of the minimal-power stable macro family. -/
theorem mem_rootQuotientClogStableMacroSet_iff
    {N s g : ℕ} :
    g ∈ RootQuotientClogStableMacroSet N s ↔
      g ≤ N ∧
      ∃ i : ℕ, i < s ∧ g = rootQuotientStablePrimePowerMacro s i := by
  classical
  constructor
  · intro hg
    change g ∈ rootQuotientClogStableMacroFinset N s at hg
    simp only [rootQuotientClogStableMacroFinset, Finset.mem_filter,
      Finset.mem_image, Finset.mem_range] at hg
    rcases hg with ⟨⟨i, hi, hEq⟩, hgN⟩
    exact ⟨hgN, i, hi, hEq.symm⟩
  · rintro ⟨hgN, i, hi, rfl⟩
    change rootQuotientStablePrimePowerMacro s i ∈
      rootQuotientClogStableMacroFinset N s
    simp [rootQuotientClogStableMacroFinset, hi, hgN]

/-- A selected prime direction is strictly below the next-prime stable base. -/
theorem nthPrime_lt_stablePrimeBase_of_lt_budget
    {s i : ℕ}
    (hi : i < s) :
    Nat.nth Nat.Prime i < rootQuotientStablePrimeBase s := by
  simpa [rootQuotientStablePrimeBase] using
    (Nat.nth_lt_nth Nat.infinite_setOfPred_prime).2 hi

/-- Every selected minimal exponent is genuinely composite: it is at least two. -/
theorem one_lt_rootQuotientStableMacroExponent_of_lt_budget
    {s i : ℕ}
    (hi : i < s) :
    1 < rootQuotientStableMacroExponent s i := by
  let p := Nat.nth Nat.Prime i
  let q := rootQuotientStablePrimeBase s
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  have hpLtQ : p < q :=
    nthPrime_lt_stablePrimeBase_of_lt_budget hi
  apply (Nat.lt_clog_iff_pow_lt hpPrime.one_lt).2
  simpa [rootQuotientStableMacroExponent, p, q] using hpLtQ

/-- A minimal prime-power macro reaches the stable base by definition of
`Nat.clog`. -/
theorem stablePrimeBase_le_stablePrimePowerMacro
    {s i : ℕ} :
    rootQuotientStablePrimeBase s ≤
      rootQuotientStablePrimePowerMacro s i := by
  let p := Nat.nth Nat.Prime i
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  simpa [rootQuotientStablePrimePowerMacro,
    rootQuotientStableMacroExponent, p] using
    Nat.le_pow_clog hpPrime.one_lt (rootQuotientStablePrimeBase s)

/-- The minimal-power stable family is finite. -/
theorem rootQuotientClogStableMacroSet_finite
    (N s : ℕ) :
    (RootQuotientClogStableMacroSet N s).Finite := by
  classical
  apply Set.Finite.ofFinset (rootQuotientClogStableMacroFinset N s)
  intro g
  rfl

/-- The minimal-power stable family uses at most `s` optional macro types. -/
theorem rootQuotientClogStableMacroSet_ncard_le
    (N s : ℕ) :
    (RootQuotientClogStableMacroSet N s).ncard ≤ s := by
  classical
  have hSubset :
      rootQuotientClogStableMacroFinset N s ⊆
        (Finset.range s).image (rootQuotientStablePrimePowerMacro s) := by
    intro g hg
    simp only [rootQuotientClogStableMacroFinset, Finset.mem_filter] at hg
    exact hg.1
  have hCard : (rootQuotientClogStableMacroFinset N s).card ≤ s := by
    calc
      (rootQuotientClogStableMacroFinset N s).card ≤
          ((Finset.range s).image
            (rootQuotientStablePrimePowerMacro s)).card :=
        Finset.card_le_card hSubset
      _ ≤ (Finset.range s).card := Finset.card_image_le
      _ = s := by simp
  simpa [RootQuotientClogStableMacroSet] using hCard

/-- Uniform residual cap for the minimal-power ladder.  Every small prime
coordinate needs at most `clog_2(q_s)-1` literal residual tokens. -/
def rootQuotientClogStableResidualBudget
    (s : ℕ) : ℕ :=
  s * (Nat.clog 2 (rootQuotientStablePrimeBase s) - 1)

/-- Residual prime-token bound for the minimal-power ladder.

The exact coordinate cap for prime `p` is `clog_p(q_s)-1`.  This theorem first
bounds it by the worst small-prime cap `clog_2(q_s)-1`, then multiplies by the
at-most-`s` possible prime directions. -/
theorem primeFactorCount_le_clogStableResidualBudget_of_no_macro
    {N s b : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hSmallPrime : ∀ p : ℕ, p.Prime → p ∣ b →
      p < rootQuotientStablePrimeBase s)
    (hNoMacro : ∀ g : ℕ,
      g ∈ RootQuotientClogStableMacroSet N s → ¬g ∣ b) :
    rootQuotientPrimeFactorCount b ≤
      rootQuotientClogStableResidualBudget s := by
  classical
  let q := rootQuotientStablePrimeBase s
  have hbZero : b ≠ 0 := by omega
  have hPrimeData : ∀ p : ℕ, p ∈ b.factorization.support →
      p.Prime ∧ p ∣ b ∧ p < q := by
    intro p hpSupport
    have hpNe : b.factorization p ≠ 0 :=
      Finsupp.mem_support_iff.mp hpSupport
    have hpPrime : p.Prime := by
      by_contra hpNot
      exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
    have hpDvd : p ∣ b := by
      by_contra hpNotDvd
      exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
    exact ⟨hpPrime, hpDvd, hSmallPrime p hpPrime hpDvd⟩
  have hExpCap : ∀ p : ℕ, p ∈ b.factorization.support →
      b.factorization p ≤ Nat.clog 2 q - 1 := by
    intro p hpSupport
    have hpData := hPrimeData p hpSupport
    obtain ⟨i, hiLt, hiEq⟩ :=
      exists_primeIndex_lt_budget_of_prime_lt_stableBase
        hpData.1 hpData.2.2
    let e := Nat.clog p q
    have hExpLt : b.factorization p < e := by
      by_contra hNot
      have heLe : e ≤ b.factorization p := by omega
      have hpPowDvd : p ^ e ∣ b :=
        (hpData.1.pow_dvd_iff_le_factorization hbZero).2 heLe
      have hpPowLeB : p ^ e ≤ b :=
        Nat.le_of_dvd (by omega) hpPowDvd
      have hMacroEq : p ^ e = rootQuotientStablePrimePowerMacro s i := by
        rw [hiEq]
        simp [e, q, rootQuotientStablePrimePowerMacro,
          rootQuotientStableMacroExponent]
      have hMacroMem : p ^ e ∈ RootQuotientClogStableMacroSet N s := by
        apply (mem_rootQuotientClogStableMacroSet_iff).2
        exact ⟨hpPowLeB.trans hbN, i, hiLt, hMacroEq⟩
      exact hNoMacro (p ^ e) hMacroMem hpPowDvd
    have hClogLe : Nat.clog p q ≤ Nat.clog 2 q :=
      Nat.clog_anti_left Nat.one_lt_two hpData.1.two_le
    dsimp [e] at hExpLt
    omega
  let primeDirections : Finset ℕ :=
    (Finset.range s).image (Nat.nth Nat.Prime)
  have hSupportSubset : b.factorization.support ⊆ primeDirections := by
    intro p hpSupport
    have hpData := hPrimeData p hpSupport
    obtain ⟨i, hiLt, hiEq⟩ :=
      exists_primeIndex_lt_budget_of_prime_lt_stableBase
        hpData.1 hpData.2.2
    dsimp [primeDirections]
    exact Finset.mem_image.2 ⟨i, by simpa using hiLt, hiEq⟩
  have hSupportCard : b.factorization.support.card ≤ s := by
    calc
      b.factorization.support.card ≤ primeDirections.card :=
        Finset.card_le_card hSupportSubset
      _ ≤ (Finset.range s).card := by
        dsimp [primeDirections]
        exact Finset.card_image_le
      _ = s := by simp
  have hSum :
      (∑ p ∈ b.factorization.support, b.factorization p) ≤
        s * (Nat.clog 2 q - 1) := by
    calc
      (∑ p ∈ b.factorization.support, b.factorization p) ≤
          ∑ _p ∈ b.factorization.support, (Nat.clog 2 q - 1) := by
        exact Finset.sum_le_sum fun p hp => hExpCap p hp
      _ = b.factorization.support.card * (Nat.clog 2 q - 1) := by simp
      _ ≤ s * (Nat.clog 2 q - 1) :=
        Nat.mul_le_mul_right (Nat.clog 2 q - 1) hSupportCard
  rw [rootQuotientPrimeFactorCount_eq_factorization_sum]
  simpa [Finsupp.sum, rootQuotientClogStableResidualBudget, q] using hSum

/-- Minimal-power next-prime stable coding theorem with uniform residual cap. -/
theorem clogStableMacroSet_is_stableMacroCode
    {N s : ℕ} :
    RootQuotientStableMacroCode
      N
      (rootQuotientStablePrimeBase s)
      (rootQuotientClogStableResidualBudget s)
      (RootQuotientClogStableMacroSet N s) := by
  refine ⟨rootQuotientStablePrimeBase_prime s, ?_, ?_⟩
  · intro g hg
    obtain ⟨_hgN, i, _hi, rfl⟩ :=
      (mem_rootQuotientClogStableMacroSet_iff).1 hg
    exact stablePrimeBase_le_stablePrimePowerMacro
  · intro b hbPos hbN hSmallPrime hNoMacro
    exact primeFactorCount_le_clogStableResidualBudget_of_no_macro
      hbPos hbN hSmallPrime hNoMacro

/-- Minimal-power ladder horizon with additive gap
`s*(clog_2(q_s)-1)`. -/
def rootQuotientClogStableMacroHorizon
    (N s : ℕ) : ℕ :=
  rootQuotientClogStableResidualBudget s +
    Nat.log (rootQuotientStablePrimeBase s) N

/-- The minimal-power ladder separates by its uniform-clog stable horizon. -/
theorem clogStableMacroSet_separates_within_horizon
    {r N s : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientClogStableMacroHorizon N s)
      (RootQuotientPrimeBasis N ∪ RootQuotientClogStableMacroSet N s) := by
  simpa [rootQuotientClogStableMacroHorizon] using
    stableMacroCode_separates_within_add_log_stateBound
      (r := r)
      (hCode := clogStableMacroSet_is_stableMacroCode (N := N) (s := s))

/-- In the high-root regime, every stored minimal-power macro is a legitimate
bounded semantic composite instruction. -/
theorem clogStableMacroSet_is_compositeMacroFamily
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    RootQuotientCompositeMacroFamily
      r N (RootQuotientClogStableMacroSet N s) := by
  intro g hg
  obtain ⟨hgN, i, hi, hEq⟩ :=
    (mem_rootQuotientClogStableMacroSet_iff).1 hg
  let p := Nat.nth Nat.Prime i
  let e := rootQuotientStableMacroExponent s i
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  have heTwo : 2 ≤ e := by
    have := one_lt_rootQuotientStableMacroExponent_of_lt_budget hi
    omega
  have hgEq : g = p ^ e := by
    simpa [p, e, rootQuotientStablePrimePowerMacro] using hEq
  have hgTwo : 2 ≤ g := by
    rw [hgEq]
    have hpLePow : p ≤ p ^ e := by
      calc
        p = p ^ 1 := by simp
        _ ≤ p ^ e := Nat.pow_le_pow_right (by omega) (by omega)
    exact hpPrime.two_le.trans hpLePow
  have hgFree : RPowerFree r g :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hgN.trans_lt hBinary)
  have hgNotPrime : ¬g.Prime := by
    intro hgPrime
    have hpDvd : p ∣ g := by
      rw [hgEq]
      exact dvd_pow_self p (by omega)
    rcases hgPrime.eq_one_or_self_of_dvd p hpDvd with hpOne | hpEq
    · exact hpPrime.ne_one hpOne
    · have hpLt : p < g := by
        rw [hgEq]
        have hPowLt : p ^ 1 < p ^ e :=
          pow_lt_pow_right' hpPrime.one_lt (by omega)
        simpa using hPowLt
      omega
  refine ⟨⟨hgTwo, hgN, hgFree⟩, ?_⟩
  intro hgPrimeBasis
  exact hgNotPrime hgPrimeBasis.1

/-- Minimal-power ladder upper bound on the true macro-budget Pareto horizon. -/
theorem minimumHorizonAtCompositeMacroBudget_le_clogStableHorizon
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
      rootQuotientClogStableMacroHorizon N s := by
  let H := rootQuotientClogStableMacroHorizon N s
  let S := RootQuotientClogStableMacroSet N s
  have hPresentation : RootQuotientCompositeMacroPresentation r N H S := by
    refine ⟨
      rootQuotientClogStableMacroSet_finite N s,
      clogStableMacroSet_is_compositeMacroFamily hr hBinary,
      ?_⟩
    dsimp [H, S]
    exact clogStableMacroSet_separates_within_horizon
      (r := r) (N := N) (s := s) (by omega)
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N H ≤ s :=
    (rootQuotientMinimumCompositeMacroCount_le hPresentation).trans
      (rootQuotientClogStableMacroSet_ncard_le N s)
  have hHPos : 1 ≤ H := by
    by_cases hsZero : s = 0
    · subst s
      have hLogPos : 0 < Nat.log 2 N := Nat.log_pos (by omega) hN
      simpa [H, rootQuotientClogStableMacroHorizon,
        rootQuotientClogStableResidualBudget, rootQuotientStablePrimeBase] using hLogPos
    · have hsPos : 1 ≤ s := by omega
      have hqPrime := rootQuotientStablePrimeBase_prime s
      have hClogPos : 1 ≤ Nat.clog 2 (rootQuotientStablePrimeBase s) - 1 := by
        have hQGtTwo : 2 < rootQuotientStablePrimeBase s := by
          have hNth : Nat.nth Nat.Prime 0 < Nat.nth Nat.Prime s :=
            (Nat.nth_lt_nth Nat.infinite_setOfPred_prime).2 (by omega)
          simpa [rootQuotientStablePrimeBase] using hNth
        have hCLog : 1 < Nat.clog 2 (rootQuotientStablePrimeBase s) :=
          (Nat.lt_clog_iff_pow_lt Nat.one_lt_two).2 (by simpa using hQGtTwo)
        omega
      have hResidualPos : 1 ≤ rootQuotientClogStableResidualBudget s := by
        dsimp [rootQuotientClogStableResidualBudget]
        exact Nat.one_le_mul hsPos hClogPos
      dsimp [H, rootQuotientClogStableMacroHorizon]
      omega
  have hStorage :
      rootQuotientMinimumStorageSize r N H ≤
        (RootQuotientPrimeBasis N).ncard + s := by
    rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      hr hHPos]
    exact Nat.add_le_add_left hMuLe _
  have hPrimeBudget :
      (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s := Nat.le_add_right _ _
  have hDepth :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N)
      (s := (RootQuotientPrimeBasis N).ncard + s) (h := H)
      hr hPrimeBudget hHPos).2 hStorage
  simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget, H] using hDepth

/-- Minimal-power next-prime stable sandwich. -/
theorem nextPrime_log_macroBudget_clog_sandwich
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    Nat.log (rootQuotientStablePrimeBase s) N ≤
        rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ∧
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
        rootQuotientClogStableMacroHorizon N s := by
  have hLower := nextPrime_log_macroBudget_sandwich
    (r := r) (N := N) (s := s) hr (by omega) hBinary
  exact ⟨hLower.1,
    minimumHorizonAtCompositeMacroBudget_le_clogStableHorizon
      (r := r) (N := N) (s := s) hr hN hBinary⟩

/-- Uniform-clog additive gap above the information-theoretic next-prime lower
bound. -/
theorem minimumHorizon_sub_nextPrimeLog_le_clogResidualBudget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s -
        Nat.log (rootQuotientStablePrimeBase s) N ≤
      rootQuotientClogStableResidualBudget s := by
  have hSandwich := nextPrime_log_macroBudget_clog_sandwich
    (r := r) (N := N) (s := s) hr hN hBinary
  dsimp [rootQuotientClogStableMacroHorizon] at hSandwich
  omega

end EnterpriseMath.Quotient
