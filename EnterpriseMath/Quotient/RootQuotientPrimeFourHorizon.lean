import EnterpriseMath.Quotient.RootQuotientPrimeFourShell
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every positive integer below `2^r` is `r`-power-free. -/
theorem rPowerFree_of_lt_two_pow_rootOrder
    {r b : ℕ}
    (hbPos : 1 ≤ b)
    (hbLt : b < 2 ^ r) :
    RPowerFree r b := by
  intro t ht hDvd
  have hDvdLe : t ^ r ≤ b :=
    Nat.le_of_dvd (by omega) hDvd
  have hTwoPowLe : 2 ^ r ≤ t ^ r :=
    Nat.pow_le_pow_left ht r
  omega

/-- Exact high-root separation threshold for bounded primes plus the single
macro `4`.

When `N<2^r`, every positive denominator up to `N` is semantically required.
The weighted-shell minimum `2*3^h` is therefore exactly the first boundary that
cannot be reached in `h` prime-plus-four instructions. -/
theorem primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourBasis N) ↔
      N < 2 * 3 ^ h := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 2 * 3 ^ h ≤ N := by omega
    let b := 2 * 3 ^ h
    have hbPos : 1 ≤ b := by
      dsimp [b]
      positivity
    have hbLt : b < 2 ^ r := hbN.trans_lt hBinary
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos hbLt
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeFourBasis N)
        (by omega) rootQuotientPrimeFourBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeFourBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeFourCost b = h + 1 := by
      dsimp [b]
      simpa using primeFourCost_two_mul_three_pow_pred (k := h + 1) (by omega)
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeFourBasis N)
      (by omega) rootQuotientPrimeFourBasis_positive).2
    intro b hbPos hbN hbFree
    apply (rootQuotientPrimeFourBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hNext : h + 1 ≤ rootQuotientPrimeFourCost b := by omega
    have hCostPos : 1 ≤ rootQuotientPrimeFourCost b := by omega
    have hShell :=
      two_mul_three_pow_pred_le_of_primeFourCost_eq
        hbPos hCostPos rfl
    have hExp : h ≤ rootQuotientPrimeFourCost b - 1 := by omega
    have hPow : 3 ^ h ≤
        3 ^ (rootQuotientPrimeFourCost b - 1) :=
      Nat.pow_le_pow_right (by omega) hExp
    have hScaled : 2 * 3 ^ h ≤
        2 * 3 ^ (rootQuotientPrimeFourCost b - 1) :=
      Nat.mul_le_mul_left 2 hPow
    have hContr : 2 * 3 ^ h ≤ N :=
      hScaled.trans (hShell.trans hbN)
    omega

/-- Arithmetic bridge between the weighted shell threshold and base-three
natural logarithm. -/
theorem one_add_log_three_div_two_le_iff_stateBound_lt_two_mul_three_pow
    {N h : ℕ}
    (hN : 2 ≤ N) :
    1 + Nat.log 3 (N / 2) ≤ h ↔
      N < 2 * 3 ^ h := by
  have hDivPos : N / 2 ≠ 0 := by omega
  calc
    1 + Nat.log 3 (N / 2) ≤ h ↔ Nat.log 3 (N / 2) < h := by omega
    _ ↔ N / 2 < 3 ^ h :=
      Nat.log_lt_iff_lt_pow (by omega) hDivPos
    _ ↔ N < 3 ^ h * 2 := by
      rw [Nat.div_lt_iff_lt_mul]
    _ ↔ N < 2 * 3 ^ h := by rw [Nat.mul_comm]

/-- Closed-form exact high-root horizon for bounded primes plus macro `4`.

A single extra primitive macro changes the worst-case depth scale from the
prime-only `Nat.log 2 N` to

`1 + Nat.log 3 (N/2)`.

Equivalently, for every candidate horizon `h`, separation holds iff this exact
minimum depth is at most `h`. -/
theorem primeFourBasis_separates_iff_log_three_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourBasis N) ↔
      1 + Nat.log 3 (N / 2) ≤ h := by
  rw [primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
    hr hN hBinary]
  exact
    (one_add_log_three_div_two_le_iff_stateBound_lt_two_mul_three_pow hN).symm

/-- The exact prime-plus-four high-root compiler horizon as a named object. -/
def rootQuotientPrimeFourHorizon (N : ℕ) : ℕ :=
  if N < 2 then 0 else 1 + Nat.log 3 (N / 2)

/-- For nontrivial high-root domains, the named prime-plus-four horizon has the
expected closed form. -/
theorem rootQuotientPrimeFourHorizon_eq
    {N : ℕ}
    (hN : 2 ≤ N) :
    rootQuotientPrimeFourHorizon N = 1 + Nat.log 3 (N / 2) := by
  simp [rootQuotientPrimeFourHorizon, not_lt_of_ge hN]

/-- Exact separation law in terms of the named prime-plus-four horizon. -/
theorem primeFourBasis_separates_iff_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourBasis N) ↔
      rootQuotientPrimeFourHorizon N ≤ h := by
  rw [rootQuotientPrimeFourHorizon_eq hN]
  exact primeFourBasis_separates_iff_log_three_horizon_le
    hr hN hBinary

/-- The exact prime-plus-four horizon is attained. -/
theorem primeFourBasis_separates_at_exact_horizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeFourHorizon N)
      (RootQuotientPrimeFourBasis N) := by
  exact (primeFourBasis_separates_iff_horizon_le hr hN hBinary).2 le_rfl

/-- No smaller horizon separates with the prime-plus-four ISA. -/
theorem rootQuotientPrimeFourHorizon_minimal
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeFourBasis N)) :
    rootQuotientPrimeFourHorizon N ≤ h :=
  (primeFourBasis_separates_iff_horizon_le hr hN hBinary).1 hSep

/-- Direct comparison with the prime-only high-root horizon. -/
theorem primeFourHorizon_le_primeHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeFourHorizon N ≤ rootQuotientPrimeHorizon r N := by
  have hPrimeSep : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N)
      (RootQuotientPrimeBasis N) :=
    rootQuotientPrimeBasis_separates_at_exact_horizon (by omega)
  have hPrimeSub : RootQuotientPrimeBasis N ⊆ RootQuotientPrimeFourBasis N :=
    Set.subset_union_left
  have hSepFour : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N)
      (RootQuotientPrimeFourBasis N) := by
    apply (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)
      (G := RootQuotientPrimeFourBasis N)
      (by omega) rootQuotientPrimeFourBasis_positive).2
    have hPrimeCompile :=
      (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
        (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)
        (G := RootQuotientPrimeBasis N)
        (by omega) rootQuotientPrimeBasis_positive).1 hPrimeSep
    exact rootQuotientAlphabetCompilesWithin_mono_implementation
      hPrimeSub hPrimeCompile
  exact rootQuotientPrimeFourHorizon_minimal hr hN hBinary hSepFour

end EnterpriseMath.Quotient
