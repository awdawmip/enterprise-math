import EnterpriseMath.Quotient.RootQuotientInstructionMetric
import EnterpriseMath.Quotient.RootQuotientOmegaFiltration
import EnterpriseMath.Quotient.RootQuotientPrimeFourMetric
import Mathlib.Algebra.Order.Floor.Div
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Generic identification principle: if bounded reachability of one target is
exactly characterized by a natural threshold `c<=h`, then the infinite-valued
shortest instruction length is precisely the natural cast of `c`. -/
theorem rootQuotientInstructionLength_eq_natCast_of_exact_threshold
    {G : Set ℕ} {b c : ℕ}
    (hCriterion : ∀ h : ℕ,
      RootQuotientProductReachableWithin h G b ↔ c ≤ h) :
    rootQuotientInstructionLength G b = (c : ℕ∞) := by
  classical
  have hReachC : RootQuotientProductReachableWithin c G b :=
    (hCriterion c).2 le_rfl
  let hExists : ∃ h : ℕ, RootQuotientProductReachableWithin h G b :=
    ⟨c, hReachC⟩
  have hFindLe : Nat.find hExists ≤ c :=
    Nat.find_min' hExists hReachC
  have hFindReach :
      RootQuotientProductReachableWithin (Nat.find hExists) G b :=
    Nat.find_spec hExists
  have hCLeFind : c ≤ Nat.find hExists :=
    (hCriterion (Nat.find hExists)).1 hFindReach
  have hFindEq : Nat.find hExists = c :=
    Nat.le_antisymm hFindLe hCLeFind
  unfold rootQuotientInstructionLength
  rw [dif_pos hExists]
  rw [hFindEq]

/-- The bounded-prime ISA induces exactly the classical total prime-factor
count `Omega` as its instruction word metric. -/
theorem rootQuotientInstructionLength_primeBasis_eq_primeFactorCount
    {N b : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    rootQuotientInstructionLength (RootQuotientPrimeBasis N) b =
      (rootQuotientPrimeFactorCount b : ℕ∞) := by
  apply rootQuotientInstructionLength_eq_natCast_of_exact_threshold
  intro h
  exact rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
    hbPos hbN

/-- The canonical capacity-`k` `Omega` filtration induces the exact block
metric `ceil(Omega/k)` on every required semantic target. -/
theorem rootQuotientInstructionLength_omegaFiltered_eq_ceilDiv
    {r N k b : ℕ}
    (hkPos : 1 ≤ k)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b) :
    rootQuotientInstructionLength
        (RootQuotientOmegaFilteredBasis r N k) b =
      ((rootQuotientPrimeFactorCount b ⌈/⌉ k : ℕ) : ℕ∞) := by
  apply rootQuotientInstructionLength_eq_natCast_of_exact_threshold
  intro h
  calc
    RootQuotientProductReachableWithin
        h (RootQuotientOmegaFilteredBasis r N k) b ↔
        rootQuotientPrimeFactorCount b ≤ k * h :=
      rootQuotientOmegaFilteredBasis_reachableWithin_iff_factorCount_le_mul
        hkPos hbPos hbN hbFree
    _ ↔ rootQuotientPrimeFactorCount b ⌈/⌉ k ≤ h :=
      (ceilDiv_le_iff_le_mul (by omega)).symm

/-- Bounded primes plus the single macro `4` induce exactly the weighted
factor-lattice cost

`Omega(b) - floor(v_2(b)/2)`.

This identifies the prime-plus-four formula as another closed form of the same
arbitrary-ISA word metric, not a separate notion of depth. -/
theorem rootQuotientInstructionLength_primeFour_eq_weightedCost
    {N b : ℕ}
    (hN : 2 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    rootQuotientInstructionLength (RootQuotientPrimeFourBasis N) b =
      (rootQuotientPrimeFourCost b : ℕ∞) := by
  apply rootQuotientInstructionLength_eq_natCast_of_exact_threshold
  intro h
  exact rootQuotientPrimeFourBasis_reachableWithin_iff_cost_le
    hN hbPos hbN

/-- The three exact metric forms side-by-side: atomic primes, capacity blocks,
and a sparse anisotropic macro extension. -/
theorem rootQuotientInstructionMetric_three_closedForms
    {r N k b : ℕ}
    (hkPos : 1 ≤ k)
    (hN : 2 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b) :
    rootQuotientInstructionLength (RootQuotientPrimeBasis N) b =
        (rootQuotientPrimeFactorCount b : ℕ∞) ∧
      rootQuotientInstructionLength
          (RootQuotientOmegaFilteredBasis r N k) b =
        ((rootQuotientPrimeFactorCount b ⌈/⌉ k : ℕ) : ℕ∞) ∧
      rootQuotientInstructionLength (RootQuotientPrimeFourBasis N) b =
        (rootQuotientPrimeFourCost b : ℕ∞) :=
  ⟨rootQuotientInstructionLength_primeBasis_eq_primeFactorCount hbPos hbN,
    rootQuotientInstructionLength_omegaFiltered_eq_ceilDiv
      hkPos hbPos hbN hbFree,
    rootQuotientInstructionLength_primeFour_eq_weightedCost
      hN hbPos hbN⟩

end EnterpriseMath.Quotient
