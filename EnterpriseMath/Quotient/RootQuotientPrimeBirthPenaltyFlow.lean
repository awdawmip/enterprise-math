import EnterpriseMath.Quotient.RootQuotientPrimeBirthPreinvestmentPenalty
import EnterpriseMath.Quotient.RootQuotientResourceFlow
import EnterpriseMath.Quotient.RootQuotientMixedOverheadFlow
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Prime-birth mixed-cover flow from the cover preinvestment price.**

At `N+1=p^(h+1)`, the direction coordinate always rises by one, while the cover
coordinate rises by the cover preinvestment penalty.  Hence the signed
cover-over-direction gap changes by `penalty-1`. -/
theorem mixedCoverGapFlow_at_prime_birth_eq_coverPenalty_sub_one
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientMixedCoverGapInt r (N + 1) h -
        rootQuotientMixedCoverGapInt r N h =
      (rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p : ℤ) - 1 := by
  rw [mixedCoverGapInt_succ_sub_eq_event_difference]
  have hEvent := resourceEvent_at_prime_birth_eq_preinvestmentPenalties
    hr hh hp hBirth hBinaryNext
  have hSigned := signedResourceEvent_eq_cast_resourceEvent
    (r := r) (N := N) (h := h) hr hh
  rw [hSigned.1, hSigned.2.1, hEvent]
  rfl

/-- **Prime-birth residual-depth flow from the penalty difference.**

The exact-over-cover gap changes by

`exact preinvestment penalty - cover preinvestment penalty`.

Thus exact-only preinvestment is precisely a one-unit absorption of old
residual-depth overhead. -/
theorem residualDepthGapFlow_at_prime_birth_eq_exactPenalty_sub_coverPenalty
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResidualDepthGapInt r (N + 1) h -
        rootQuotientResidualDepthGapInt r N h =
      (rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p : ℤ) -
        (rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p : ℤ) := by
  rw [residualDepthGapInt_succ_sub_eq_event_difference]
  have hEvent := resourceEvent_at_prime_birth_eq_preinvestmentPenalties
    hr hh hp hBirth hBinaryNext
  have hSigned := signedResourceEvent_eq_cast_resourceEvent
    (r := r) (N := N) (h := h) hr hh
  rw [hSigned.2.1, hSigned.2.2, hEvent]
  rfl

/-- **Prime-birth total mixed-overhead flow.**

The intermediate cover layer cancels: total mixed overhead changes by

`exact preinvestment penalty - 1`.

Hence it decreases exactly when the exact layer had preinvested in the future
prime direction. -/
theorem totalMixedGapFlow_at_prime_birth_eq_exactPenalty_sub_one
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientTotalMixedGapInt r (N + 1) h -
        rootQuotientTotalMixedGapInt r N h =
      (rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p : ℤ) - 1 := by
  rw [totalMixedGapInt_succ_sub_eq_cast_event_difference hr hh]
  have hEvent := resourceEvent_at_prime_birth_eq_preinvestmentPenalties
    hr hh hp hBirth hBinaryNext
  rw [hEvent]
  rfl

/-- Exact preinvestment at a prime birth is equivalent to losing one unit of
total mixed overhead. -/
theorem exactPrimeDirectionPreinvestment_iff_totalMixedGap_drops_one
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    RootQuotientExactPrimeDirectionPreinvestment r N h p ↔
      rootQuotientTotalMixedGapInt r (N + 1) h -
        rootQuotientTotalMixedGapInt r N h = -1 := by
  have hFlow := totalMixedGapFlow_at_prime_birth_eq_exactPenalty_sub_one
    hr hh hp hBirth hBinaryNext
  constructor
  · intro hPre
    have hPenalty :
        rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p = 0 :=
      (exactPrimeDirectionPreinvestmentPenalty_eq_zero_iff).2 hPre
    rw [hFlow, hPenalty]
    norm_num
  · intro hDrop
    have hBits := primeDirectionPreinvestmentPenalties_zero_or_one r N h p |>.2
    rcases hBits with hZero | hOne
    · exact (exactPrimeDirectionPreinvestmentPenalty_eq_zero_iff).1 hZero
    · rw [hFlow, hOne] at hDrop
      norm_num at hDrop

end EnterpriseMath.Quotient
