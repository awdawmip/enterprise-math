import EnterpriseMath.Quotient.RootQuotientPrimeBirthCoverPreinvestment
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Hard-prime-direction cardinality is exactly the prime-direction demand. -/
theorem hardPrimeDirections_ncard_eq_primeDirectionDemand
    (N h : ℕ) :
    (RootQuotientHardPrimeDirections N h).ncard =
      rootQuotientPrimeDirectionDemand N h := by
  rw [rootQuotientHardPrimeDirections_ncard_eq_primeCounting_cutoff]
  rfl

/-- **A hard-prime birth always contributes direction event one.**

If the newly exposed state is exactly `p^(h+1)` for a prime `p`, then `p` is
absent from the old hard-direction set and present in the new one.  Since the
direction-demand staircase can rise by at most one, it rises by exactly one. -/
theorem directionEvent_eq_one_at_prime_birth
    {r N h p : ℕ}
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1)) :
    (rootQuotientResourceEvent r N h).direction = 1 := by
  let H₀ := RootQuotientHardPrimeDirections N h
  let H₁ := RootQuotientHardPrimeDirections (N + 1) h
  have hSub : H₀ ⊆ H₁ := by
    intro q hq
    exact ⟨hq.1, hq.2.trans (Nat.le_succ N)⟩
  have hpNew : p ∈ H₁ := by
    refine ⟨hp, ?_⟩
    rw [← hBirth]
  have hpNotOld : p ∉ H₀ := by
    intro hpOld
    have hpLeN : p ^ (h + 1) ≤ N := hpOld.2
    rw [← hBirth] at hpLeN
    omega
  have hSetsNe : H₀ ≠ H₁ := by
    intro hEq
    apply hpNotOld
    rw [hEq]
    exact hpNew
  have hCardNe : H₀.ncard ≠ H₁.ncard := by
    intro hCard
    have hCardLe : H₁.ncard ≤ H₀.ncard := hCard.symm.le
    have hEq : H₀ = H₁ :=
      Set.eq_of_subset_of_ncard_le hSub hCardLe
        (rootQuotientHardPrimeDirections_finite (N + 1) h)
    exact hSetsNe hEq
  have hDemandNe :
      rootQuotientPrimeDirectionDemand N h ≠
        rootQuotientPrimeDirectionDemand (N + 1) h := by
    intro hEq
    apply hCardNe
    simpa [hardPrimeDirections_ncard_eq_primeDirectionDemand] using hEq
  have hStep := primeDirectionDemand_succ_staircase N h
  dsimp [rootQuotientResourceEvent]
  omega

/-- Cover-event bit one is exactly absence of cover preinvestment at a hard
prime birth. -/
theorem coverEvent_one_iff_not_coverPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    (rootQuotientResourceEvent r N h).divisorCover = 1 ↔
      ¬RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  have hBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.1
  have hZeroIff := coverEvent_zero_iff_coverPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  constructor
  · intro hOne hPre
    have hZero := hZeroIff.2 hPre
    omega
  · intro hNoPre
    rcases hBits with hZero | hOne
    · exact (hNoPre (hZeroIff.1 hZero)).elim
    · exact hOne

/-- Exact-storage event bit one is exactly absence of exact preinvestment at a
hard prime birth. -/
theorem exactEvent_one_iff_not_exactPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    (rootQuotientResourceEvent r N h).exactStorage = 1 ↔
      ¬RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  have hBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.2
  have hZeroIff := exactEvent_zero_iff_exactPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  constructor
  · intro hOne hPre
    have hZero := hZeroIff.2 hPre
    omega
  · intro hNoPre
    rcases hBits with hZero | hOne
    · exact (hNoPre (hZeroIff.1 hZero)).elim
    · exact hOne

/-- **Complete hard-prime-birth event state machine.**

At `N+1 = p^(h+1)`, the event is determined by two old-domain preinvestment
flags.  The direction component is always one; cover/exact components are zero
exactly when their corresponding optimization layer had already stored a useful
pure `p`-power.

Truth table:

* no cover preinvestment, no exact preinvestment  -> `(1,1,1)`;
* cover preinvestment, no exact preinvestment     -> `(1,0,1)`;
* cover preinvestment, exact preinvestment        -> `(1,0,0)`;
* no cover preinvestment, exact preinvestment     -> `(1,1,0)`.
-/
theorem resourceEvent_at_prime_birth_eq_by_preinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResourceEvent r N h =
      if RootQuotientCoverPrimeDirectionPreinvestment r N h p then
        if RootQuotientExactPrimeDirectionPreinvestment r N h p then
          rootQuotientDirectionCatchupEvent
        else
          rootQuotientDirectionDepthTransferEvent
      else
        if RootQuotientExactPrimeDirectionPreinvestment r N h p then
          rootQuotientDualCatchupEvent
        else
          rootQuotientDirectionBirthEvent := by
  have hDir := directionEvent_eq_one_at_prime_birth
    (r := r) hp hBirth
  have hCoverZero := coverEvent_zero_iff_coverPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  have hCoverOne := coverEvent_one_iff_not_coverPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  have hExactZero := exactEvent_zero_iff_exactPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  have hExactOne := exactEvent_one_iff_not_exactPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
  by_cases hCoverPre : RootQuotientCoverPrimeDirectionPreinvestment r N h p <;>
    by_cases hExactPre : RootQuotientExactPrimeDirectionPreinvestment r N h p
  · simp [hCoverPre, hExactPre]
    apply RootQuotientResourceEvent.ext
    · simpa [rootQuotientDirectionCatchupEvent] using hDir
    · simpa [rootQuotientDirectionCatchupEvent] using hCoverZero.2 hCoverPre
    · simpa [rootQuotientDirectionCatchupEvent] using hExactZero.2 hExactPre
  · simp [hCoverPre, hExactPre]
    apply RootQuotientResourceEvent.ext
    · simpa [rootQuotientDirectionDepthTransferEvent] using hDir
    · simpa [rootQuotientDirectionDepthTransferEvent] using hCoverZero.2 hCoverPre
    · simpa [rootQuotientDirectionDepthTransferEvent] using hExactOne.2 hExactPre
  · simp [hCoverPre, hExactPre]
    apply RootQuotientResourceEvent.ext
    · simpa [rootQuotientDualCatchupEvent] using hDir
    · simpa [rootQuotientDualCatchupEvent] using hCoverOne.2 hCoverPre
    · simpa [rootQuotientDualCatchupEvent] using hExactZero.2 hExactPre
  · simp [hCoverPre, hExactPre]
    apply RootQuotientResourceEvent.ext
    · simpa [rootQuotientDirectionBirthEvent] using hDir
    · simpa [rootQuotientDirectionBirthEvent] using hCoverOne.2 hCoverPre
    · simpa [rootQuotientDirectionBirthEvent] using hExactOne.2 hExactPre

/-- The previously unresolved dual-catchup event has a clean intrinsic
characterization at every hard-prime birth. -/
theorem dualCatchupEvent_at_prime_birth_iff_exactOnlyPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent ↔
      ¬RootQuotientCoverPrimeDirectionPreinvestment r N h p ∧
      RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  exact dualCatchupEvent_iff_exactOnlyPrimeDirectionPreinvestment
    hr hh hp hBirth hBinaryNext
      (directionEvent_eq_one_at_prime_birth (r := r) hp hBirth)

end EnterpriseMath.Quotient
