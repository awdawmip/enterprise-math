import EnterpriseMath.Quotient.RootQuotientCapacity
import EnterpriseMath.Quotient.RootQuotientLeastPhase
import Mathlib.Data.List.TakeDrop
import Mathlib.Data.Nat.Factors
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Canonical `Omega`-filtered primitive quotient alphabet.

It contains exactly the nontrivial bounded `r`-power-free semantic
denominators whose prime-factor count is at most the per-instruction capacity
`k`. -/
def RootQuotientOmegaFilteredBasis (r N k : ℕ) : Set ℕ :=
  {g : ℕ |
    2 ≤ g ∧ g ≤ N ∧ RPowerFree r g ∧
      rootQuotientPrimeFactorCount g ≤ k}

/-- Every `Omega`-filtered primitive denominator is positive. -/
theorem rootQuotientOmegaFilteredBasis_positive
    {r N k : ℕ} :
    PositiveRootQuotientGenerators
      (RootQuotientOmegaFilteredBasis r N k) := by
  intro g hg
  omega

/-- The canonical `Omega`-filtered alphabet has factor capacity at most `k`. -/
theorem rootQuotientOmegaFilteredBasis_factorCapacity
    {r N k : ℕ} :
    RootQuotientFactorCapacity k
      (RootQuotientOmegaFilteredBasis r N k) := by
  intro g hg
  exact hg.2.2.2

/-- Split a positive power-free denominator after the first `k` prime-factor
tokens.

When `1 ≤ k < Omega(b)`, the first `k` factors compile to a proper nontrivial
factor `a`, the remaining factors compile to a nontrivial factor `c`, and

`b = a*c`, `Omega(a)=k`, `Omega(c)=Omega(b)-k`.

Both factors remain `r`-power-free because the semantic set is divisor-closed. -/
theorem exists_rPowerFree_factor_split_at_primeFactorCount
    {r b k : ℕ}
    (hbPos : 1 ≤ b)
    (hbFree : RPowerFree r b)
    (hkPos : 1 ≤ k)
    (hkLt : k < rootQuotientPrimeFactorCount b) :
    ∃ a c : ℕ,
      2 ≤ a ∧ 2 ≤ c ∧
      a ∣ b ∧ c ∣ b ∧
      RPowerFree r a ∧ RPowerFree r c ∧
      b = a * c ∧
      rootQuotientPrimeFactorCount a = k ∧
      rootQuotientPrimeFactorCount c =
        rootQuotientPrimeFactorCount b - k := by
  let l := b.primeFactorsList
  let a := (l.take k).prod
  let c := (l.drop k).prod
  have hbZero : b ≠ 0 := by omega
  have hkLe : k ≤ l.length := by
    simpa [l, rootQuotientPrimeFactorCount] using Nat.le_of_lt hkLt
  have hSplit : a * c = b := by
    dsimp [a, c]
    rw [← List.prod_append, List.take_append_drop]
    simpa [l] using Nat.prod_primeFactorsList hbZero
  have hTakePrime : ∀ p : ℕ, p ∈ l.take k → p.Prime := by
    intro p hp
    apply Nat.prime_of_mem_primeFactorsList
    have hpOrig : p ∈ l := by
      rw [← List.take_append_drop k l]
      exact List.mem_append.mpr (Or.inl hp)
    simpa [l] using hpOrig
  have hDropPrime : ∀ p : ℕ, p ∈ l.drop k → p.Prime := by
    intro p hp
    apply Nat.prime_of_mem_primeFactorsList
    have hpOrig : p ∈ l := by
      rw [← List.take_append_drop k l]
      exact List.mem_append.mpr (Or.inr hp)
    simpa [l] using hpOrig
  have hPermA : (l.take k).Perm a.primeFactorsList := by
    apply Nat.primeFactorsList_unique (n := a) (l := l.take k)
    · rfl
    · exact hTakePrime
  have hPermC : (l.drop k).Perm c.primeFactorsList := by
    apply Nat.primeFactorsList_unique (n := c) (l := l.drop k)
    · rfl
    · exact hDropPrime
  have hTakeLen : (l.take k).length = k := by
    simp [List.length_take, hkLe]
  have hCountA : rootQuotientPrimeFactorCount a = k := by
    calc
      rootQuotientPrimeFactorCount a = a.primeFactorsList.length := rfl
      _ = (l.take k).length := hPermA.length_eq.symm
      _ = k := hTakeLen
  have hCountC :
      rootQuotientPrimeFactorCount c =
        rootQuotientPrimeFactorCount b - k := by
    calc
      rootQuotientPrimeFactorCount c = c.primeFactorsList.length := rfl
      _ = (l.drop k).length := hPermC.length_eq.symm
      _ = l.length - k := by simp
      _ = rootQuotientPrimeFactorCount b - k := by
        simp [l, rootQuotientPrimeFactorCount]
  have hMulNe : a * c ≠ 0 := by
    rw [hSplit]
    exact hbZero
  have haNe : a ≠ 0 := by
    intro ha
    apply hMulNe
    simp [ha]
  have hcNe : c ≠ 0 := by
    intro hc
    apply hMulNe
    simp [hc]
  have haPos : 1 ≤ a := Nat.one_le_iff_ne_zero.mpr haNe
  have hcPos : 1 ≤ c := Nat.one_le_iff_ne_zero.mpr hcNe
  have haNeOne : a ≠ 1 := by
    intro haOne
    have hZero : rootQuotientPrimeFactorCount a = 0 := by
      simp [haOne, rootQuotientPrimeFactorCount]
    omega
  have hcCountPos : 0 < rootQuotientPrimeFactorCount c := by
    rw [hCountC]
    omega
  have hcNeOne : c ≠ 1 := by
    intro hcOne
    have hZero : rootQuotientPrimeFactorCount c = 0 := by
      simp [hcOne, rootQuotientPrimeFactorCount]
    omega
  have haTwo : 2 ≤ a := by omega
  have hcTwo : 2 ≤ c := by omega
  have haDvd : a ∣ b := ⟨c, hSplit.symm⟩
  have hcDvd : c ∣ b := by
    refine ⟨a, ?_⟩
    simpa [Nat.mul_comm] using hSplit.symm
  have haFree : RPowerFree r a :=
    rPowerFree_of_dvd_of_rPowerFree haDvd hbFree
  have hcFree : RPowerFree r c :=
    rPowerFree_of_dvd_of_rPowerFree hcDvd hbFree
  exact ⟨a, c, haTwo, hcTwo, haDvd, hcDvd, haFree, hcFree,
    hSplit.symm, hCountA, hCountC⟩

/-- Constructive upper bound for the canonical `Omega` filtration.

A required semantic denominator with `Omega(b) ≤ k*h` can be compiled in at
most `h` instructions by repeatedly taking the first `k` prime-factor tokens as
one macro instruction. -/
theorem rootQuotientOmegaFilteredBasis_reachable_of_factorCount_le_mul
    {r N k h b : ℕ}
    (hkPos : 1 ≤ k)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b)
    (hCount : rootQuotientPrimeFactorCount b ≤ k * h) :
    RootQuotientProductReachableWithin h
      (RootQuotientOmegaFilteredBasis r N k) b := by
  induction h generalizing b with
  | zero =>
      have hCountZero : rootQuotientPrimeFactorCount b = 0 := by
        simpa using hCount
      have hLenZero : b.primeFactorsList.length = 0 := by
        simpa [rootQuotientPrimeFactorCount] using hCountZero
      have hNil : b.primeFactorsList = [] :=
        List.length_eq_zero_iff.mp hLenZero
      have hbOne : b = 1 := by
        rcases (Nat.primeFactorsList_eq_nil b).1 hNil with hbZero | hbOne
        · omega
        · exact hbOne
      subst b
      exact ⟨[], by simp, by simp [RootQuotientWordOver],
        by simp [rootQuotientWordProduct]⟩
  | succ h ih =>
      by_cases hbOne : b = 1
      · subst b
        exact ⟨[], by simp, by simp [RootQuotientWordOver],
          by simp [rootQuotientWordProduct]⟩
      · have hbTwo : 2 ≤ b := by omega
        by_cases hSmall : rootQuotientPrimeFactorCount b ≤ k
        · have hbMem : b ∈ RootQuotientOmegaFilteredBasis r N k :=
            ⟨hbTwo, hbN, hbFree, hSmall⟩
          refine ⟨[b], by simp, ?_, by simp [rootQuotientWordProduct]⟩
          intro g hg
          simp at hg
          subst g
          exact hbMem
        · have hkLt : k < rootQuotientPrimeFactorCount b := by omega
          obtain ⟨a, c, haTwo, hcTwo, haDvd, hcDvd, haFree, hcFree,
              hbc, hCountA, hCountC⟩ :=
            exists_rPowerFree_factor_split_at_primeFactorCount
              hbPos hbFree hkPos hkLt
          have haN : a ≤ N :=
            (Nat.le_of_dvd (by omega) haDvd).trans hbN
          have hcN : c ≤ N :=
            (Nat.le_of_dvd (by omega) hcDvd).trans hbN
          have haMem : a ∈ RootQuotientOmegaFilteredBasis r N k :=
            ⟨haTwo, haN, haFree, by omega⟩
          have hcCountBound :
              rootQuotientPrimeFactorCount c ≤ k * h := by
            rw [hCountC]
            rw [Nat.mul_succ] at hCount
            omega
          obtain ⟨w, hwLen, hwG, hProd⟩ :=
            ih (by omega) hcN hcFree hcCountBound
          refine ⟨a :: w, ?_, ?_, ?_⟩
          · simp
            exact hwLen
          · intro g hg
            simp at hg
            rcases hg with rfl | hgTail
            · exact haMem
            · exact hwG g hgTail
          · calc
              b = a * c := hbc
              _ = a * rootQuotientWordProduct w := by rw [← hProd]
              _ = rootQuotientWordProduct (a :: w) := by
                rfl

/-- Exact pointwise reachability law for the canonical `Omega` filtration. -/
theorem rootQuotientOmegaFilteredBasis_reachableWithin_iff_factorCount_le_mul
    {r N k h b : ℕ}
    (hkPos : 1 ≤ k)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b) :
    RootQuotientProductReachableWithin h
      (RootQuotientOmegaFilteredBasis r N k) b ↔
      rootQuotientPrimeFactorCount b ≤ k * h := by
  constructor
  · intro hReach
    exact
      rootQuotientPrimeFactorCount_le_capacity_mul_horizon_of_reachable
        rootQuotientOmegaFilteredBasis_positive
        rootQuotientOmegaFilteredBasis_factorCapacity hReach
  · exact rootQuotientOmegaFilteredBasis_reachable_of_factorCount_le_mul
      hkPos hbPos hbN hbFree

/-- Exact instruction-capacity × execution-depth law for the canonical
`Omega`-filtered compiler family. -/
theorem rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
    {r N k h : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis r N k) ↔
      rootQuotientPrimeHorizon r N ≤ k * h := by
  constructor
  · intro hSep
    exact rootQuotientPrimeHorizon_le_capacity_mul_horizon
      hr rootQuotientOmegaFilteredBasis_positive
      rootQuotientOmegaFilteredBasis_factorCapacity hSep
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientOmegaFilteredBasis r N k)
      hr rootQuotientOmegaFilteredBasis_positive).2
    intro b hbPos hbN hbFree
    have hCount :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := k * h)).1 hBound
        b hbPos hbN hbFree
    exact rootQuotientOmegaFilteredBasis_reachable_of_factorCount_le_mul
      hkPos hbPos hbN hbFree hCount

end EnterpriseMath.Quotient
