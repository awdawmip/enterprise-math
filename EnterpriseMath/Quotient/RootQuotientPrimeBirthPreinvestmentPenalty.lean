import EnterpriseMath.Quotient.RootQuotientPrimeBirthEventClassification
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Zero/one cover-layer cost of not having preinvested in a future hard prime
direction.  It is zero exactly when some old cover optimum already stores a
useful `p^e`, `2≤e≤h`. -/
noncomputable def rootQuotientCoverPrimeDirectionPreinvestmentPenalty
    (r N h p : ℕ) : ℕ :=
  if RootQuotientCoverPrimeDirectionPreinvestment r N h p then 0 else 1

/-- Zero/one exact-layer cost of not having preinvested in a future hard prime
direction. -/
noncomputable def rootQuotientExactPrimeDirectionPreinvestmentPenalty
    (r N h p : ℕ) : ℕ :=
  if RootQuotientExactPrimeDirectionPreinvestment r N h p then 0 else 1

@[simp]
theorem coverPrimeDirectionPreinvestmentPenalty_eq_zero_iff
    {r N h p : ℕ} :
    rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p = 0 ↔
      RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  classical
  unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
  by_cases hPre : RootQuotientCoverPrimeDirectionPreinvestment r N h p <;>
    simp [hPre]

@[simp]
theorem exactPrimeDirectionPreinvestmentPenalty_eq_zero_iff
    {r N h p : ℕ} :
    rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p = 0 ↔
      RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  classical
  unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
  by_cases hPre : RootQuotientExactPrimeDirectionPreinvestment r N h p <;>
    simp [hPre]

/-- Both preinvestment penalties are binary. -/
theorem primeDirectionPreinvestmentPenalties_zero_or_one
    (r N h p : ℕ) :
    (rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p = 0 ∨
      rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p = 1) ∧
    (rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p = 0 ∨
      rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p = 1) := by
  classical
  unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
  unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
  split <;> split <;> simp_all

/-- **Hard-prime-birth event = preinvestment price vector.**

At the entering state `N+1=p^(h+1)`, the direction coordinate always costs one
new unit.  The cover and exact coordinates are exactly their old-domain
preinvestment penalties. -/
theorem resourceEvent_at_prime_birth_eq_preinvestmentPenalties
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResourceEvent r N h =
      { direction := 1
        divisorCover :=
          rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p
        exactStorage :=
          rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p } := by
  have hDir := directionEvent_eq_one_at_prime_birth
    (r := r) hp hBirth
  have hCoverBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.1
  have hExactBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.2
  apply RootQuotientResourceEvent.ext
  · exact hDir
  · classical
    unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
    by_cases hPre : RootQuotientCoverPrimeDirectionPreinvestment r N h p
    · simp [hPre]
      exact (coverEvent_zero_iff_coverPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).2 hPre
    · simp [hPre]
      have hNotZero : (rootQuotientResourceEvent r N h).divisorCover ≠ 0 := by
        intro hZero
        exact hPre ((coverEvent_zero_iff_coverPrimeDirectionPreinvestment
          hr hh hp hBirth hBinaryNext).1 hZero)
      omega
  · classical
    unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
    by_cases hPre : RootQuotientExactPrimeDirectionPreinvestment r N h p
    · simp [hPre]
      exact (exactEvent_zero_iff_exactPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).2 hPre
    · simp [hPre]
      have hNotZero : (rootQuotientResourceEvent r N h).exactStorage ≠ 0 := by
        intro hZero
        exact hPre ((exactEvent_zero_iff_exactPrimeDirectionPreinvestment
          hr hh hp hBirth hBinaryNext).1 hZero)
      omega

/-- The unresolved dual-catchup event is exactly the penalty pair `(1,0)`: the
cover layer pays one type at birth while the exact layer pays zero because it
had already preinvested. -/
theorem dualCatchupEvent_at_prime_birth_iff_penalties_one_zero
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent ↔
      rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p = 1 ∧
      rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p = 0 := by
  classical
  rw [dualCatchupEvent_at_prime_birth_iff_exactOnlyPreinvestment
    hr hh hp hBirth hBinaryNext]
  unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
  unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
  by_cases hCover : RootQuotientCoverPrimeDirectionPreinvestment r N h p <;>
    by_cases hExact : RootQuotientExactPrimeDirectionPreinvestment r N h p <;>
      simp [hCover, hExact]

/-- When the old divisor relaxation is exact, the exact preinvestment penalty
can never be smaller than the cover preinvestment penalty. -/
theorem coverPenalty_le_exactPenalty_of_globalRepairGap_zero
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hGapZero : rootQuotientGlobalRepairRelaxationGap r N h = 0) :
    rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p ≤
      rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p := by
  classical
  unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
  unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
  by_cases hExact : RootQuotientExactPrimeDirectionPreinvestment r N h p
  · have hCover := coverPrimeDirectionPreinvestment_of_exact_of_globalRepairGap_zero
      hr hGapZero hExact
    simp [hExact, hCover]
  · simp [hExact]

end EnterpriseMath.Quotient
