import EnterpriseMath.Quotient.RootQuotientMinimumStorage
import EnterpriseMath.Quotient.RootQuotientPrimeHorizonGeometry
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact-state separation restricts monotonically to smaller bounded state
domains. -/
theorem separatesRootQuotientWordsUpTo_mono_stateBound
    {r N M h : ℕ} {G : Set ℕ}
    (hNM : N ≤ M)
    (hSep : SeparatesRootQuotientWordsUpTo r M h G) :
    SeparatesRootQuotientWordsUpTo r N h G := by
  intro x y hxy hyN
  exact hSep hxy (hyN.trans hNM)

/-- Separation for a larger root order implies separation for a smaller root
order, provided the smaller root order is positive.

The reason is semantic rather than pointwise-root monotonicity: every
`r`-power-free required denominator remains `s`-power-free when `r≤s`, so the
reachable-product criterion transfers. -/
theorem separatesRootQuotientWordsUpTo_anti_rootOrder
    {r s N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hrs : r ≤ s)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo s N h G) :
    SeparatesRootQuotientWordsUpTo r N h G := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := h) (G := G) hr hG).2
  intro b hbPos hbN hbFree
  have hbFreeS : RPowerFree s b :=
    rPowerFree_mono_rootOrder hrs hbFree
  exact
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := s) (N := N) (h := h) (G := G)
      (hr.trans hrs) hG).1 hSep
      b hbPos hbN hbFreeS

/-- More execution depth cannot increase minimum primitive-type storage. -/
theorem rootQuotientMinimumStorageSize_anti_horizon
    {r N h j : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h)
    (hhj : h ≤ j) :
    rootQuotientMinimumStorageSize r N j ≤
      rootQuotientMinimumStorageSize r N h := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) hr hh
  have hGSepJ : SeparatesRootQuotientWordsUpTo r N j G :=
    separatesRootQuotientWordsUpTo_mono_horizon hhj hG.2.2.2
  have hGJ : RootQuotientFiniteStorageSeparator r N j G :=
    ⟨hG.1, hG.2.1, hG.2.2.1, hGSepJ⟩
  have hMinLe :=
    rootQuotientMinimumStorageSize_le_normalized hGJ
  simpa [hGCard] using hMinLe

/-- Enlarging the bounded state domain cannot decrease minimum primitive-type
storage. -/
theorem rootQuotientMinimumStorageSize_mono_stateBound
    {r N M h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h)
    (hNM : N ≤ M) :
    rootQuotientMinimumStorageSize r N h ≤
      rootQuotientMinimumStorageSize r M h := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := M) (h := h) hr hh
  have hSepN : SeparatesRootQuotientWordsUpTo r N h G :=
    separatesRootQuotientWordsUpTo_mono_stateBound hNM hG.2.2.2
  obtain ⟨G', hG', hCard⟩ :=
    exists_normalized_storage_separator_le
      (r := r) (N := N) (h := h) hr hG.2.1 hG.2.2.1 hSepN
  have hMinLe := rootQuotientMinimumStorageSize_le_normalized hG'
  rw [hGCard]
  exact hMinLe.trans hCard

/-- Increasing root order enlarges the required semantic denominator family,
so minimum primitive-type storage cannot decrease. -/
theorem rootQuotientMinimumStorageSize_mono_rootOrder
    {r s N h : ℕ}
    (hr : 1 ≤ r)
    (hrs : r ≤ s)
    (hh : 1 ≤ h) :
    rootQuotientMinimumStorageSize r N h ≤
      rootQuotientMinimumStorageSize s N h := by
  have hs : 1 ≤ s := hr.trans hrs
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := s) (N := N) (h := h) hs hh
  have hSepR : SeparatesRootQuotientWordsUpTo r N h G :=
    separatesRootQuotientWordsUpTo_anti_rootOrder
      hr hrs hG.2.2.1 hG.2.2.2
  obtain ⟨G', hG', hCard⟩ :=
    exists_normalized_storage_separator_le
      (r := r) (N := N) (h := h) hr hG.2.1 hG.2.2.1 hSepR
  have hMinLe := rootQuotientMinimumStorageSize_le_normalized hG'
  rw [hGCard]
  exact hMinLe.trans hCard

/-- Joint storage-resource monotonicity: larger semantic domain/root order and
smaller positive execution budget can only make the minimum dictionary at
least as large. -/
theorem rootQuotientMinimumStorageSize_resource_mono
    {r s N M h j : ℕ}
    (hr : 1 ≤ r)
    (hrs : r ≤ s)
    (hh : 1 ≤ h)
    (hj : 1 ≤ j)
    (hjh : j ≤ h)
    (hNM : N ≤ M) :
    rootQuotientMinimumStorageSize r N h ≤
      rootQuotientMinimumStorageSize s M j := by
  calc
    rootQuotientMinimumStorageSize r N h ≤
        rootQuotientMinimumStorageSize r N j :=
      rootQuotientMinimumStorageSize_anti_horizon hr hj hjh
    _ ≤ rootQuotientMinimumStorageSize r M j :=
      rootQuotientMinimumStorageSize_mono_stateBound hr hj hNM
    _ ≤ rootQuotientMinimumStorageSize s M j :=
      rootQuotientMinimumStorageSize_mono_rootOrder hr hrs hj

end EnterpriseMath.Quotient
