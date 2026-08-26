import EnterpriseMath.Quotient.RootQuotientPrimeFourSixShell
import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact high-root separation threshold for bounded primes plus macros `4,6`.

From horizon two onward, the first unreachable hard shell is exactly
`3^(h+1)`.  Hence this two-macro ISA separates the full bounded semantic domain
iff the state bound lies strictly below that shell. -/
theorem primeFourSixBasis_separates_iff_stateBound_lt_three_pow_succ
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 3 ≤ N)
    (hh : 2 ≤ h)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeFourSixBasis N) ↔
      N < 3 ^ (h + 1) := by
  constructor
  · intro hSep
    by_contra hNot
    have hbN : 3 ^ (h + 1) ≤ N := by omega
    let b := 3 ^ (h + 1)
    have hbPos : 1 ≤ b := by
      dsimp [b]
      positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos
        (hbN.trans_lt hBinary)
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeFourSixBasis N)
        (by omega) rootQuotientPrimeFourSixBasis_positive).1 hSep
        b hbPos hbN hbFree
    have hCostLe :=
      (rootQuotientPrimeFourSixBasis_reachableWithin_iff_cost_le
        (N := N) (b := b) (h := h) hN hbPos hbN).1 hReach
    have hCostExact : rootQuotientPrimeFourSixCost b = h + 1 := by
      dsimp [b]
      exact rootQuotientPrimeFourSixCost_three_pow (h + 1)
    rw [hCostExact] at hCostLe
    omega
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeFourSixBasis N)
      (by omega) rootQuotientPrimeFourSixBasis_positive).2
    intro b hbPos hbN _hbFree
    apply (rootQuotientPrimeFourSixBasis_reachableWithin_iff_cost_le
      (N := N) (b := b) (h := h) hN hbPos hbN).2
    by_contra hNot
    have hCostGt : h < rootQuotientPrimeFourSixCost b := by omega
    have hCostThree : 3 ≤ rootQuotientPrimeFourSixCost b := by omega
    have hShell : 3 ^ rootQuotientPrimeFourSixCost b ≤ b :=
      three_pow_primeFourSixCost_le hbPos hCostThree
    have hExp : h + 1 ≤ rootQuotientPrimeFourSixCost b := by omega
    have hPow : 3 ^ (h + 1) ≤
        3 ^ rootQuotientPrimeFourSixCost b :=
      Nat.pow_le_pow_right (by omega) hExp
    have hContr : 3 ^ (h + 1) ≤ N :=
      hPow.trans (hShell.trans hbN)
    omega

/-- At every `h>=2`, the exact state threshold of `{4,6}` is strictly above
that of the one-macro optimum `{4}`:

`2*3^h < 3^(h+1)`.

This arithmetic gap is exactly where the mixed-direction storage overhead can
be positive. -/
theorem two_mul_three_pow_lt_three_pow_succ
    {h : ℕ} :
    2 * 3 ^ h < 3 ^ (h + 1) := by
  rw [pow_succ]
  nlinarith [show 0 < 3 ^ h by positivity]

end EnterpriseMath.Quotient
