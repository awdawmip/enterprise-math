import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import EnterpriseMath.Quotient.RootQuotientPrimeTwoPowerShell
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Successor recurrence of the generalized hard shell: while cheap literal-2
slots remain, the next shell multiplies by `2`; after all `m-1` cheap slots are
used, every further cost level multiplies by `3`. -/
theorem rootQuotientPrimeTwoPowerShellMinimumCandidate_succ
    {m k : ℕ}
    (hm : 2 ≤ m) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate m (k + 1) =
      rootQuotientPrimeTwoPowerShellMinimumCandidate m k *
        (if k < m - 1 then 2 else 3) := by
  by_cases hk : k < m - 1
  · have hkLe : k ≤ m - 1 := by omega
    have hSuccLe : k + 1 ≤ m - 1 := by omega
    rw [rootQuotientPrimeTwoPowerShellMinimumCandidate]
    simp [min_eq_left hkLe, min_eq_left hSuccLe, hk, pow_succ,
      Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  · have hmk : m - 1 ≤ k := by omega
    have hmkSucc : m - 1 ≤ k + 1 := by omega
    have hSub : k + 1 - (m - 1) = (k - (m - 1)) + 1 := by omega
    rw [rootQuotientPrimeTwoPowerShellMinimumCandidate]
    simp [min_eq_right hmk, min_eq_right hmkSucc, hk, hSub, pow_succ,
      Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Generalized hard-shell thresholds are strictly increasing in weighted
instruction cost. -/
theorem rootQuotientPrimeTwoPowerShellMinimumCandidate_strictMono
    {m : ℕ}
    (hm : 2 ≤ m) :
    StrictMono (rootQuotientPrimeTwoPowerShellMinimumCandidate m) := by
  apply strictMono_nat_of_lt_succ
  intro k
  rw [rootQuotientPrimeTwoPowerShellMinimumCandidate_succ hm]
  split_ifs
  · exact Nat.lt_mul_of_one_lt_right (by positivity) (by omega)
  · exact Nat.lt_mul_of_one_lt_right (by positivity) (by omega)

/-- Monotone form of the generalized hard-shell thresholds. -/
theorem rootQuotientPrimeTwoPowerShellMinimumCandidate_monotone
    {m : ℕ}
    (hm : 2 ≤ m) :
    Monotone (rootQuotientPrimeTwoPowerShellMinimumCandidate m) :=
  (rootQuotientPrimeTwoPowerShellMinimumCandidate_strictMono hm).monotone

/-- Exact high-root state-bound threshold for bounded primes plus a single
`2^m` macro.

The first target whose weighted cost exceeds `h` is exactly the hard shell at
cost `h+1`; therefore separation within `h` holds iff the bounded state domain
stops before that integer. -/
theorem primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeTwoPowerBasis N m) ↔
      N < rootQuotientPrimeTwoPowerShellMinimumCandidate m (h + 1) := by
  constructor
  · intro hSep
    by_contra hNot
    let b := rootQuotientPrimeTwoPowerShellMinimumCandidate m (h + 1)
    have hbN : b ≤ N := by dsimp [b]; omega
    have hbPos : 1 ≤ b := by
      dsimp [b, rootQuotientPrimeTwoPowerShellMinimumCandidate]
      positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeTwoPowerBasis N m)
        (by omega) rootQuotientPrimeTwoPowerBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeTwoPowerBasis_reachableWithin_iff_cost_le
        (N := N) (m := m) (b := b) (h := h)
        hm hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeTwoPowerCost m b = h + 1 := by
      dsimp [b]
      exact primeTwoPowerCost_shellCandidate hm
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeTwoPowerBasis N m)
      (by omega) rootQuotientPrimeTwoPowerBasis_positive).2
    intro b hbPos hbN hbFree
    apply (rootQuotientPrimeTwoPowerBasis_reachableWithin_iff_cost_le
      (N := N) (m := m) (b := b) (h := h)
      hm hN hbPos hbN).2
    by_contra hNot
    let k := rootQuotientPrimeTwoPowerCost m b
    have hk : h + 1 ≤ k := by dsimp [k]; omega
    have hShellB : rootQuotientPrimeTwoPowerShellMinimumCandidate m k ≤ b := by
      apply primeTwoPowerShellCandidate_le_of_cost_eq hm hbPos
      rfl
    have hShellMono :
        rootQuotientPrimeTwoPowerShellMinimumCandidate m (h + 1) ≤
          rootQuotientPrimeTwoPowerShellMinimumCandidate m k :=
      rootQuotientPrimeTwoPowerShellMinimumCandidate_monotone hm hk
    have hContr : rootQuotientPrimeTwoPowerShellMinimumCandidate m (h + 1) ≤ N :=
      hShellMono.trans (hShellB.trans hbN)
    omega

/-- Macro `4` pointwise horizon-dominates every larger single `2^m` macro in
the high-root regime.

If primes plus `2^m` can separate the task within `h`, then primes plus `4` can
separate it within the same `h`.  This is stronger than merely comparing their
minimum worst-case horizons. -/
theorem primeFourBasis_separates_of_primeTwoPowerBasis_separates
    {r N m h : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hSepM : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeTwoPowerBasis N m)) :
    SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeFourBasis N) := by
  have hStateM :=
    (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
      (r := r) (N := N) (m := m) (h := h)
      hr hm hN hBinary).1 hSepM
  have hShellDom :
      rootQuotientPrimeTwoPowerShellMinimumCandidate m (h + 1) ≤
        2 * 3 ^ h := by
    have h := primeTwoPowerShellCandidate_le_primeFourShell
      (m := m) (k := h + 1) hm (by omega)
    simpa using h
  have hStateFour : N < 2 * 3 ^ h := hStateM.trans_le hShellDom
  exact
    (primeFourBasis_separates_iff_stateBound_lt_two_mul_three_pow
      (r := r) (N := N) (h := h) hr hN hBinary).2 hStateFour

/-- `m=2` recovers exactly the prime-plus-four next-shell threshold. -/
theorem primeTwoPower_nextShell_two_eq_primeFour_threshold
    {h : ℕ} :
    rootQuotientPrimeTwoPowerShellMinimumCandidate 2 (h + 1) =
      2 * 3 ^ h := by
  simpa using
    primeTwoPowerShellCandidate_two_eq_primeFourShell (k := h + 1) (by omega)

end EnterpriseMath.Quotient
