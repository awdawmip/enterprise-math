import EnterpriseMath.Quotient.RootQuotientPrimeTwoPowerHorizon
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Before the cheap-literal-2 budget `m-1` is exhausted, the generalized hard
shell is just the ordinary power-of-two shell. -/
theorem primeTwoPowerShellCandidate_eq_two_pow_of_le
    {m k : ℕ}
    (hk : k ≤ m - 1) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate m k = 2 ^ k := by
  simp [rootQuotientPrimeTwoPowerShellMinimumCandidate, min_eq_left hk]

/-- After `m-1` cheap literal twos are exhausted, every further hard-shell level
multiplies by three. -/
theorem primeTwoPowerShellCandidate_eq_twoPow_mul_threePow_of_le
    {m k : ℕ}
    (hmk : m - 1 ≤ k) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate m k =
      2 ^ (m - 1) * 3 ^ (k - (m - 1)) := by
  simp [rootQuotientPrimeTwoPowerShellMinimumCandidate, min_eq_right hmk]

/-- Exact arithmetic horizon for bounded primes plus one `2^m` macro.

Let `t=m-1`.  If the prime-only dyadic depth has not yet reached `t`, the macro
is too large to help and the exact depth remains `log_2 N`.  Once the state
domain crosses `2^t`, the remaining depth grows on a base-three scale. -/
def rootQuotientPrimeTwoPowerHorizon (m N : ℕ) : ℕ :=
  let t := m - 1
  let L := Nat.log 2 N
  if L < t then
    L
  else
    t + Nat.log 3 (N / 2 ^ t)

/-- Low-state branch of the closed-form horizon. -/
theorem rootQuotientPrimeTwoPowerHorizon_eq_log_two_of_log_lt
    {m N : ℕ}
    (hLow : Nat.log 2 N < m - 1) :
    rootQuotientPrimeTwoPowerHorizon m N = Nat.log 2 N := by
  simp [rootQuotientPrimeTwoPowerHorizon, hLow]

/-- High-state branch of the closed-form horizon. -/
theorem rootQuotientPrimeTwoPowerHorizon_eq_block_add_log_three_of_le_log
    {m N : ℕ}
    (hHigh : m - 1 ≤ Nat.log 2 N) :
    rootQuotientPrimeTwoPowerHorizon m N =
      (m - 1) + Nat.log 3 (N / 2 ^ (m - 1)) := by
  simp [rootQuotientPrimeTwoPowerHorizon, not_lt_of_ge hHigh]

/-- The generalized one-two-power-macro ISA separates at its closed-form exact
horizon in the high-root semantic regime. -/
theorem primeTwoPowerBasis_separates_at_exact_closedHorizon
    {r N m : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeTwoPowerHorizon m N)
      (RootQuotientPrimeTwoPowerBasis N m) := by
  let t := m - 1
  let L := Nat.log 2 N
  by_cases hLow : L < t
  · have hH : rootQuotientPrimeTwoPowerHorizon m N = L := by
      dsimp [L, t] at hLow ⊢
      exact rootQuotientPrimeTwoPowerHorizon_eq_log_two_of_log_lt hLow
    apply (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
      (r := r) (N := N) (m := m) (h := rootQuotientPrimeTwoPowerHorizon m N)
      hr hm hN hBinary).2
    rw [hH]
    have hSuccLe : L + 1 ≤ t := by omega
    rw [primeTwoPowerShellCandidate_eq_two_pow_of_le hSuccLe]
    dsimp [L]
    exact Nat.lt_pow_succ_log_self (by omega) N
  · have hHigh : t ≤ L := by omega
    have hH : rootQuotientPrimeTwoPowerHorizon m N =
        t + Nat.log 3 (N / 2 ^ t) := by
      dsimp [L, t] at hHigh ⊢
      exact
        rootQuotientPrimeTwoPowerHorizon_eq_block_add_log_three_of_le_log
          hHigh
    have hNZero : N ≠ 0 := by omega
    have hBlockLeN : 2 ^ t ≤ N := by
      dsimp [L] at hHigh
      exact Nat.pow_le_of_le_log hNZero hHigh
    have hDivPos : N / 2 ^ t ≠ 0 := by
      have hPos := Nat.div_pos hBlockLeN (by positivity : 0 < 2 ^ t)
      omega
    apply (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
      (r := r) (N := N) (m := m) (h := rootQuotientPrimeTwoPowerHorizon m N)
      hr hm hN hBinary).2
    rw [hH]
    have hShellHigh : t ≤ t + Nat.log 3 (N / 2 ^ t) + 1 := by omega
    rw [primeTwoPowerShellCandidate_eq_twoPow_mul_threePow_of_le hShellHigh]
    have hExp :
        t + Nat.log 3 (N / 2 ^ t) + 1 - t =
          Nat.log 3 (N / 2 ^ t) + 1 := by omega
    rw [hExp]
    have hDivLt : N / 2 ^ t <
        3 ^ (Nat.log 3 (N / 2 ^ t) + 1) :=
      Nat.lt_pow_succ_log_self (by omega) (N / 2 ^ t)
    have hMulLt : N <
        3 ^ (Nat.log 3 (N / 2 ^ t) + 1) * 2 ^ t := by
      exact (Nat.div_lt_iff_lt_mul (by positivity : 0 < 2 ^ t)).1 hDivLt
    simpa [Nat.mul_comm] using hMulLt

/-- The closed-form generalized horizon is minimal. -/
theorem rootQuotientPrimeTwoPowerHorizon_minimal
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeTwoPowerBasis N m)) :
    rootQuotientPrimeTwoPowerHorizon m N ≤ h := by
  let t := m - 1
  let L := Nat.log 2 N
  have hState :=
    (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
      (r := r) (N := N) (m := m) (h := h)
      hr hm hN hBinary).1 hSep
  by_cases hLow : L < t
  · have hH : rootQuotientPrimeTwoPowerHorizon m N = L := by
      dsimp [L, t] at hLow ⊢
      exact rootQuotientPrimeTwoPowerHorizon_eq_log_two_of_log_lt hLow
    rw [hH]
    by_contra hNot
    have hHLt : h < L := by omega
    have hSuccLe : h + 1 ≤ t := by omega
    rw [primeTwoPowerShellCandidate_eq_two_pow_of_le hSuccLe] at hState
    have hNZero : N ≠ 0 := by omega
    have hPowL : 2 ^ L ≤ N := by
      dsimp [L]
      exact Nat.pow_log_le_self 2 hNZero
    have hPowMono : 2 ^ (h + 1) ≤ 2 ^ L :=
      Nat.pow_le_pow_right (by omega) (by omega)
    exact (not_le_of_gt hState) (hPowMono.trans hPowL)
  · have hHigh : t ≤ L := by omega
    have hH : rootQuotientPrimeTwoPowerHorizon m N =
        t + Nat.log 3 (N / 2 ^ t) := by
      dsimp [L, t] at hHigh ⊢
      exact
        rootQuotientPrimeTwoPowerHorizon_eq_block_add_log_three_of_le_log
          hHigh
    rw [hH]
    by_contra hNot
    have hHLt : h < t + Nat.log 3 (N / 2 ^ t) := by omega
    have hNZero : N ≠ 0 := by omega
    have hBlockLeN : 2 ^ t ≤ N := by
      dsimp [L] at hHigh
      exact Nat.pow_le_of_le_log hNZero hHigh
    by_cases hBeforeBlock : h < t
    · have hSuccLe : h + 1 ≤ t := by omega
      rw [primeTwoPowerShellCandidate_eq_two_pow_of_le hSuccLe] at hState
      have hPowMono : 2 ^ (h + 1) ≤ 2 ^ t :=
        Nat.pow_le_pow_right (by omega) hSuccLe
      exact (not_le_of_gt hState) (hPowMono.trans hBlockLeN)
    · have htLeH : t ≤ h := by omega
      have hShellHigh : t ≤ h + 1 := by omega
      rw [primeTwoPowerShellCandidate_eq_twoPow_mul_threePow_of_le hShellHigh] at hState
      have hExpLe : h + 1 - t ≤ Nat.log 3 (N / 2 ^ t) := by omega
      have hPowLe : 3 ^ (h + 1 - t) ≤
          3 ^ Nat.log 3 (N / 2 ^ t) :=
        Nat.pow_le_pow_right (by omega) hExpLe
      have hDivLe : 3 ^ Nat.log 3 (N / 2 ^ t) ≤ N / 2 ^ t :=
        Nat.pow_log_le_self 3 (by
          have hPos := Nat.div_pos hBlockLeN (by positivity : 0 < 2 ^ t)
          omega)
      have hScaled : 2 ^ t * 3 ^ (h + 1 - t) ≤
          2 ^ t * (N / 2 ^ t) :=
        Nat.mul_le_mul_left (2 ^ t) (hPowLe.trans hDivLe)
      have hDivMul : 2 ^ t * (N / 2 ^ t) ≤ N := by
        simpa [Nat.mul_comm] using Nat.div_mul_le_self N (2 ^ t)
      exact (not_le_of_gt hState) (hScaled.trans hDivMul)

/-- Exact separation law in terms of the generalized closed-form horizon. -/
theorem primeTwoPowerBasis_separates_iff_closedHorizon_le
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeTwoPowerBasis N m) ↔
      rootQuotientPrimeTwoPowerHorizon m N ≤ h := by
  constructor
  · exact rootQuotientPrimeTwoPowerHorizon_minimal hr hm hN hBinary
  · intro hHLe
    exact separatesRootQuotientWordsUpTo_mono_horizon hHLe
      (primeTwoPowerBasis_separates_at_exact_closedHorizon
        hr hm hN hBinary)

/-- `m=2` specialization recovers the exact prime-plus-four horizon. -/
theorem rootQuotientPrimeTwoPowerHorizon_two_eq_primeFourHorizon
    {N : ℕ}
    (hN : 2 ≤ N) :
    rootQuotientPrimeTwoPowerHorizon 2 N =
      rootQuotientPrimeFourHorizon N := by
  have hLogPos : 1 ≤ Nat.log 2 N := by
    apply Nat.le_log_of_pow_le (by omega)
    simpa using hN
  rw [rootQuotientPrimeTwoPowerHorizon_eq_block_add_log_three_of_le_log
    (m := 2) (N := N) (by simpa using hLogPos)]
  rw [rootQuotientPrimeFourHorizon_eq hN]
  norm_num

/-- Closed-form family dominance: macro `4` has no larger exact horizon than
any single `2^m` macro. -/
theorem rootQuotientPrimeFourHorizon_le_primeTwoPowerHorizon
    {r N m : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeFourHorizon N ≤
      rootQuotientPrimeTwoPowerHorizon m N := by
  have hSepM := primeTwoPowerBasis_separates_at_exact_closedHorizon
    hr hm hN hBinary
  have hSepFour := primeFourBasis_separates_of_primeTwoPowerBasis_separates
    hr hm hN hBinary hSepM
  exact rootQuotientPrimeFourHorizon_minimal hr hN hBinary hSepFour

end EnterpriseMath.Quotient
