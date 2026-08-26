import EnterpriseMath.Quotient.RootQuotientOmegaFiltration
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Existence of a positive separating primitive quotient alphabet whose every
instruction carries at most `k` prime-factor tokens. -/
def ExistsRootQuotientSeparatorWithFactorCapacity
    (r N h k : ℕ) : Prop :=
  ∃ G : Set ℕ,
    PositiveRootQuotientGenerators G ∧
    RootQuotientFactorCapacity k G ∧
    SeparatesRootQuotientWordsUpTo r N h G

/-- Pointwise dominance of the canonical `Omega`-filtered dictionary.

For a required bounded semantic denominator, every target reachable within `h`
steps by any positive capacity-`k` primitive alphabet is also reachable within
the same horizon by the canonical `Omega`-filtered alphabet. -/
theorem rootQuotientOmegaFilteredBasis_reaches_of_capacity_reaches
    {r N k h b : ℕ} {G : Set ℕ}
    (hkPos : 1 ≤ k)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b)
    (hGPos : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G)
    (hReach : RootQuotientProductReachableWithin h G b) :
    RootQuotientProductReachableWithin h
      (RootQuotientOmegaFilteredBasis r N k) b := by
  have hCount : rootQuotientPrimeFactorCount b ≤ k * h :=
    rootQuotientPrimeFactorCount_le_capacity_mul_horizon_of_reachable
      hGPos hCap hReach
  exact rootQuotientOmegaFilteredBasis_reachable_of_factorCount_le_mul
    hkPos hbPos hbN hbFree hCount

/-- Horizon-preserving dominance at the full separation level.

If any positive capacity-`k` primitive alphabet separates the bounded exact
state domain at horizon `h`, then the canonical `Omega`-filtered alphabet does
so at the same horizon. -/
theorem rootQuotientOmegaFilteredBasis_separates_of_capacity_separator
    {r N k h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k)
    (hGPos : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    SeparatesRootQuotientWordsUpTo r N h
      (RootQuotientOmegaFilteredBasis r N k) := by
  have hBound : rootQuotientPrimeHorizon r N ≤ k * h :=
    rootQuotientPrimeHorizon_le_capacity_mul_horizon
      hr hGPos hCap hSep
  exact
    (rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
      (r := r) (N := N) (k := k) (h := h) hr hkPos).2 hBound

/-- Exact feasibility region for capacity-bounded primitive quotient compilers.

There exists some positive primitive alphabet of factor capacity at most `k`
separating within horizon `h` iff the universal resource inequality

`L_r(N) ≤ k*h`

holds.  The canonical `Omega`-filtered alphabet realizes every feasible point. -/
theorem exists_rootQuotientSeparatorWithFactorCapacity_iff
    {r N k h : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    ExistsRootQuotientSeparatorWithFactorCapacity r N h k ↔
      rootQuotientPrimeHorizon r N ≤ k * h := by
  constructor
  · rintro ⟨G, hGPos, hCap, hSep⟩
    exact rootQuotientPrimeHorizon_le_capacity_mul_horizon
      hr hGPos hCap hSep
  · intro hBound
    refine ⟨RootQuotientOmegaFilteredBasis r N k,
      rootQuotientOmegaFilteredBasis_positive,
      rootQuotientOmegaFilteredBasis_factorCapacity, ?_⟩
    exact
      (rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
        (r := r) (N := N) (k := k) (h := h) hr hkPos).2 hBound

/-- The canonical `Omega` filtration is Pareto-optimal in the following strong
sense: within a fixed factor-capacity class it never requires a larger horizon
than another positive primitive alphabet for any required semantic target. -/
theorem rootQuotientOmegaFilteredBasis_horizon_dominates
    {r N k b : ℕ} {G : Set ℕ}
    (hkPos : 1 ≤ k)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hbFree : RPowerFree r b)
    (hGPos : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G) :
    ∀ h : ℕ,
      RootQuotientProductReachableWithin h G b →
      RootQuotientProductReachableWithin h
        (RootQuotientOmegaFilteredBasis r N k) b := by
  intro h hReach
  exact rootQuotientOmegaFilteredBasis_reaches_of_capacity_reaches
    hkPos hbPos hbN hbFree hGPos hCap hReach

end EnterpriseMath.Quotient
