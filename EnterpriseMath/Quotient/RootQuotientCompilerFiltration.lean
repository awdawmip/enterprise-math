import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import EnterpriseMath.Quotient.RootQuotientOmegaFiltration
import EnterpriseMath.Quotient.RootQuotientPrimeShell
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact compiler-depth law from the canonical `Omega`-filtered ISA to the
canonical semantic ISA.

This is the compiler-preorder form of the capacity × execution-depth theorem:
`G_k` implements every required semantic instruction within `h` lower-level
instructions iff `L_r(N) ≤ k*h`. -/
theorem rootQuotientOmegaFilteredBasis_compiles_semanticBasis_iff
    {r N k h : ℕ}
    (hr : 1 ≤ r)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
        h (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientNontrivialPowerFreeBasis r N) ↔
      rootQuotientPrimeHorizon r N ≤ k * h := by
  exact
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := h)
      (G := RootQuotientOmegaFilteredBasis r N k)
      hr rootQuotientOmegaFilteredBasis_positive).symm.trans
      (rootQuotientOmegaFilteredBasis_separates_iff_capacity_mul_horizon
        (r := r) (N := N) (k := k) (h := h) hr hkPos)

/-- The exact rank exposed by the `j`-th `Omega`-filtered presentation on the
bounded semantic domain is `min(j,L_r(N))`. -/
def rootQuotientOmegaFiltrationExposedRank
    (r N j : ℕ) : ℕ :=
  min j (rootQuotientPrimeHorizon r N)

/-- Exact pairwise compiler metric on the canonical `Omega` filtration.

For `r≥2`, a nonempty bounded state domain, and lower-level capacity `k≥1`,
`G_k` can implement every instruction of `G_j` within `h` lower-level steps
iff the largest semantic rank actually exposed by `G_j` fits into the
capacity-depth budget `k*h`:

`G_k ⊢_h G_j  ↔  min(j,L_r(N)) ≤ k*h`.

Thus the whole nested filtration is a one-dimensional compiler geometry, not
merely a family of separately optimal dictionaries. -/
theorem rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
    {r N k j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) ↔
      rootQuotientOmegaFiltrationExposedRank r N j ≤ k * h := by
  let L := rootQuotientPrimeHorizon r N
  let m := rootQuotientOmegaFiltrationExposedRank r N j
  constructor
  · intro hCompile
    by_cases hmZero : m = 0
    · simp [hmZero]
    · have hmPos : 1 ≤ m := by omega
      have hmLeL : m ≤ L := by
        dsimp [m, rootQuotientOmegaFiltrationExposedRank, L]
        exact min_le_right _ _
      have hmLeJ : m ≤ j := by
        dsimp [m, rootQuotientOmegaFiltrationExposedRank]
        exact min_le_left _ _
      let b := rootQuotientPrimeShellMinimum r m
      have hbShell : b ∈ RootQuotientPrimeShell r m := by
        dsimp [b]
        exact rootQuotientPrimeShellMinimum_mem hr
      have hbN : b ≤ N := by
        dsimp [b]
        exact
          (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
            (r := r) (N := N) (k := m) hr hN).2 hmLeL
      have hbTwo : 2 ≤ b := by
        by_contra hNot
        have hbOne : b = 1 := by omega
        have hCountZero : rootQuotientPrimeFactorCount b = 0 := by
          simp [hbOne, rootQuotientPrimeFactorCount]
        have hCountM : rootQuotientPrimeFactorCount b = m := hbShell.2.2
        omega
      have hbGj : b ∈ RootQuotientOmegaFilteredBasis r N j :=
        ⟨hbTwo, hbN, hbShell.2.1, by
          rw [hbShell.2.2]
          exact hmLeJ⟩
      have hReach := hCompile b hbGj
      have hCountLe : rootQuotientPrimeFactorCount b ≤ k * h :=
        (rootQuotientOmegaFilteredBasis_reachableWithin_iff_factorCount_le_mul
          (r := r) (N := N) (k := k) (h := h) (b := b)
          hkPos hbShell.1 hbN hbShell.2.1).1 hReach
      rw [hbShell.2.2] at hCountLe
      simpa [m] using hCountLe
  · intro hBudget g hgGj
    have hCountLeJ : rootQuotientPrimeFactorCount g ≤ j := hgGj.2.2.2
    have hCountLeL :
        rootQuotientPrimeFactorCount g ≤ rootQuotientPrimeHorizon r N := by
      exact
        (rootQuotientPrimeHorizon_le_iff
          (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
          g (by omega) hgGj.2.1 hgGj.2.2.1
    have hCountLeM :
        rootQuotientPrimeFactorCount g ≤
          rootQuotientOmegaFiltrationExposedRank r N j := by
      dsimp [rootQuotientOmegaFiltrationExposedRank]
      exact le_min hCountLeJ hCountLeL
    have hCountBudget : rootQuotientPrimeFactorCount g ≤ k * h :=
      hCountLeM.trans hBudget
    exact
      (rootQuotientOmegaFilteredBasis_reachableWithin_iff_factorCount_le_mul
        (r := r) (N := N) (k := k) (h := h) (b := g)
        hkPos (by omega) hgGj.2.1 hgGj.2.2.1).2 hCountBudget

/-- Below the saturation rank `L_r(N)`, pairwise compiler depth sees the raw
filtration index `j`. -/
theorem rootQuotientOmegaFilteredBasis_compilesWithin_iff_index_le
    {r N k j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hj : j ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) ↔
      j ≤ k * h := by
  rw [rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
    hr hN hkPos]
  simp [rootQuotientOmegaFiltrationExposedRank, hj]

/-- Once the target presentation has saturated the bounded semantic domain,
all larger `Omega` cutoffs have the same compiler cost: only `L_r(N)` remains. -/
theorem rootQuotientOmegaFilteredBasis_compilesWithin_iff_horizon_le_of_saturated
    {r N k j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hkPos : 1 ≤ k)
    (hSat : rootQuotientPrimeHorizon r N ≤ j) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N k)
        (RootQuotientOmegaFilteredBasis r N j) ↔
      rootQuotientPrimeHorizon r N ≤ k * h := by
  rw [rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
    hr hN hkPos]
  simp [rootQuotientOmegaFiltrationExposedRank, hSat]

/-- The prime ISA is the unit-capacity origin of the filtration compiler
geometry. -/
theorem rootQuotientPrimeBasis_relativeCompilerMetric
    {r N j h : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    RootQuotientAlphabetCompilesWithin
        h
        (RootQuotientOmegaFilteredBasis r N 1)
        (RootQuotientOmegaFilteredBasis r N j) ↔
      rootQuotientOmegaFiltrationExposedRank r N j ≤ h := by
  simpa using
    (rootQuotientOmegaFilteredBasis_compilesWithin_iff_exposedRank_le
      (r := r) (N := N) (k := 1) (j := j) (h := h)
      hr hN (by omega))

end EnterpriseMath.Quotient
