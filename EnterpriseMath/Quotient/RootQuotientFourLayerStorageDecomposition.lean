import EnterpriseMath.Quotient.RootQuotientRepairPacking
import EnterpriseMath.Quotient.RootQuotientMixedOverheadDecomposition
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Mixed hard-target pressure already visible as pairwise divisor
incompatibility beyond the pure-prime-direction floor. -/
noncomputable def rootQuotientMixedPackingOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientGlobalRepairDivisorPackingNumber r N h -
    rootQuotientPrimeDirectionDemand N h

/-- Additional first-order cover coordination beyond pairwise
incompatibility.  This measures the part of divisor-cover storage not certified
by a simple divisor-incompatible target packing. -/
noncomputable def rootQuotientPackingToCoverOverhead
    (r N h : ℕ) : ℕ :=
  rootQuotientGlobalRepairDivisorCoverNumber r N h -
    rootQuotientGlobalRepairDivisorPackingNumber r N h

/-- Packing size decomposes into pure directions plus extra mixed packing
pressure. -/
theorem globalRepairPackingNumber_eq_directionDemand_add_mixedPackingOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientGlobalRepairDivisorPackingNumber r N h =
      rootQuotientPrimeDirectionDemand N h +
        rootQuotientMixedPackingOverhead r N h := by
  have hLe := primeDirectionDemand_le_globalRepairDivisorPackingNumber
    hr hh hBinary
  dsimp [rootQuotientMixedPackingOverhead]
  omega

/-- Divisor-cover size decomposes into packing size plus the additional cover
coordination overhead. -/
theorem globalRepairCoverNumber_eq_packing_add_packingToCoverOverhead
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h =
      rootQuotientGlobalRepairDivisorPackingNumber r N h +
        rootQuotientPackingToCoverOverhead r N h := by
  have hHierarchy := canonicalRepairFourLayerHierarchy hr hh hBinary
  dsimp [rootQuotientPackingToCoverOverhead]
  omega

/-- Existing mixed divisor-cover overhead itself splits into two distinct
first-order resources: mixed incompatibility visible to packing, and extra
set-cover coordination invisible to pairwise packing. -/
theorem mixedDivisorCoverOverhead_eq_mixedPacking_add_packingToCover
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMixedDivisorCoverOverhead r N h =
      rootQuotientMixedPackingOverhead r N h +
        rootQuotientPackingToCoverOverhead r N h := by
  have hPack :=
    globalRepairPackingNumber_eq_directionDemand_add_mixedPackingOverhead
      hr hh hBinary
  have hCover :=
    globalRepairCoverNumber_eq_packing_add_packingToCoverOverhead
      hr hh hBinary
  have hOld := globalRepairDivisorCoverNumber_eq_directionDemand_add_mixedDivisorOverhead
    hr hh hBinary
  omega

/-- **Four-source optional-macro storage decomposition.**

Exact optional storage has four nested sources:

1. mandatory pure-prime directions;
2. extra mixed divisor-incompatibility packing pressure;
3. set-cover coordination beyond pairwise packing;
4. residual bounded-depth execution pressure beyond divisor hitting.
-/
theorem minimumCompositeMacroCount_eq_fourLayerResources
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientPrimeDirectionDemand N h +
      rootQuotientMixedPackingOverhead r N h +
      rootQuotientPackingToCoverOverhead r N h +
      rootQuotientResidualDepthStorageOverhead r N h := by
  have hMixed := mixedDirectionMacroOverhead_eq_mixedDivisor_add_residualDepth
    hr hh hBinary
  have hDiv := mixedDivisorCoverOverhead_eq_mixedPacking_add_packingToCover
    hr hh hBinary
  have hMu := minimumCompositeMacroCount_eq_directionDemand_add_mixedOverhead
    hr hh hBinary
  omega

/-- Total primitive storage adds the forced prime core to the same four-source
optional-macro decomposition. -/
theorem minimumStorage_eq_primeBasis_add_fourLayerResources
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard +
      rootQuotientPrimeDirectionDemand N h +
      rootQuotientMixedPackingOverhead r N h +
      rootQuotientPackingToCoverOverhead r N h +
      rootQuotientResidualDepthStorageOverhead r N h := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  rw [minimumCompositeMacroCount_eq_fourLayerResources hr hh hBinary]

end EnterpriseMath.Quotient
