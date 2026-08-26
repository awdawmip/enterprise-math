import EnterpriseMath.Quotient.RootQuotientPrimeBirthPreinvestmentPenalty
import EnterpriseMath.Quotient.RootQuotientPrimeBirthPreinvestmentGap
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Canonical prime-birth preinvestment dominance.**

For one specified future hard prime direction, every exact-layer preinvestment
can also be realized by some divisor-cover optimum.  This is the precise local
property whose validity would exclude the remaining algebraic event `(1,1,0)`.
-/
def RootQuotientPrimeBirthPreinvestmentDominance
    (r N h p : ℕ) : Prop :=
  RootQuotientExactPrimeDirectionPreinvestment r N h p →
    RootQuotientCoverPrimeDirectionPreinvestment r N h p

/-- Dominance is equivalently the zero/one penalty inequality: the cover layer
never charges more for future-direction preinvestment than the exact layer. -/
theorem primeBirthPreinvestmentDominance_iff_coverPenalty_le_exactPenalty
    {r N h p : ℕ} :
    RootQuotientPrimeBirthPreinvestmentDominance r N h p ↔
      rootQuotientCoverPrimeDirectionPreinvestmentPenalty r N h p ≤
        rootQuotientExactPrimeDirectionPreinvestmentPenalty r N h p := by
  classical
  unfold RootQuotientPrimeBirthPreinvestmentDominance
  unfold rootQuotientCoverPrimeDirectionPreinvestmentPenalty
  unfold rootQuotientExactPrimeDirectionPreinvestmentPenalty
  by_cases hCover : RootQuotientCoverPrimeDirectionPreinvestment r N h p <;>
    by_cases hExact : RootQuotientExactPrimeDirectionPreinvestment r N h p <;>
      simp [hCover, hExact]

/-- At a hard-prime birth, canonical dominance is exactly exclusion of the
remaining dual-catchup event `(1,1,0)`. -/
theorem primeBirthPreinvestmentDominance_iff_not_dualCatchupEvent
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    RootQuotientPrimeBirthPreinvestmentDominance r N h p ↔
      rootQuotientResourceEvent r N h ≠ rootQuotientDualCatchupEvent := by
  rw [dualCatchupEvent_at_prime_birth_iff_exactOnlyPreinvestment
    hr hh hp hBirth hBinaryNext]
  unfold RootQuotientPrimeBirthPreinvestmentDominance
  tauto

/-- The canonical dominance property is already proved throughout every old
state where the global divisor relaxation is exact. -/
theorem primeBirthPreinvestmentDominance_of_globalRepairGap_zero
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hGapZero : rootQuotientGlobalRepairRelaxationGap r N h = 0) :
    RootQuotientPrimeBirthPreinvestmentDominance r N h p := by
  intro hExact
  exact coverPrimeDirectionPreinvestment_of_exact_of_globalRepairGap_zero
    hr hGapZero hExact

/-- Consequently, any genuine counterexample to canonical dominance must live
inside a positive residual-depth phase. -/
theorem globalRepairGap_pos_of_not_primeBirthPreinvestmentDominance
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hFail : ¬RootQuotientPrimeBirthPreinvestmentDominance r N h p) :
    1 ≤ rootQuotientGlobalRepairRelaxationGap r N h := by
  by_contra hNot
  have hZero : rootQuotientGlobalRepairRelaxationGap r N h = 0 := by omega
  exact hFail (primeBirthPreinvestmentDominance_of_globalRepairGap_zero hr hZero)

end EnterpriseMath.Quotient
