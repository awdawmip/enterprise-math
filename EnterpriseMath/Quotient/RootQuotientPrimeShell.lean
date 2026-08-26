import EnterpriseMath.Quotient.RootQuotientFactorGeometry
import EnterpriseMath.Quotient.RootQuotientOmegaFiltration
import EnterpriseMath.Quotient.RootQuotientPrimeHorizonGeometry
import Mathlib.Data.List.Nodup
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Data.Nat.PrimeFin
import Mathlib.Data.Nat.Squarefree
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The first `k` primes, using mathlib's zero-indexed `Nat.nth Nat.Prime`. -/
noncomputable def rootQuotientPrimePrefix (k : ℕ) : List ℕ :=
  (List.range k).map (Nat.nth Nat.Prime)

/-- Squarefree rank-`k` witness obtained by multiplying the first `k` primes. -/
noncomputable def rootQuotientPrimePrefixProduct (k : ℕ) : ℕ :=
  (rootQuotientPrimePrefix k).prod

/-- Every entry of the canonical prime prefix is prime. -/
theorem rootQuotientPrimePrefix_all_prime
    (k : ℕ) :
    ∀ p : ℕ, p ∈ rootQuotientPrimePrefix k → p.Prime := by
  intro p hp
  rcases List.mem_map.1 hp with ⟨i, _hi, rfl⟩
  exact Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i

/-- The canonical prime prefix has no duplicate prime entries. -/
theorem rootQuotientPrimePrefix_nodup
    (k : ℕ) :
    (rootQuotientPrimePrefix k).Nodup := by
  have hInjective : Function.Injective (Nat.nth Nat.Prime) :=
    (Nat.nth_strictMono Nat.infinite_setOfPred_prime).injective
  exact (List.nodup_range k).map hInjective

/-- A finite list of primes has positive product. -/
theorem prime_list_product_positive
    {l : List ℕ}
    (hPrime : ∀ p : ℕ, p ∈ l → p.Prime) :
    1 ≤ l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      have haPrime : a.Prime := hPrime a (by simp)
      have hTail : ∀ p : ℕ, p ∈ l → p.Prime := by
        intro p hp
        exact hPrime p (by simp [hp])
      have hTailPos : 1 ≤ l.prod := ih hTail
      have hNe : a * l.prod ≠ 0 :=
        Nat.mul_ne_zero haPrime.ne_zero (by omega)
      simpa using Nat.one_le_iff_ne_zero.mpr hNe

/-- The first-`k`-prime product has exactly `k` prime-factor tokens. -/
theorem rootQuotientPrimePrefixProduct_factorCount
    (k : ℕ) :
    rootQuotientPrimeFactorCount (rootQuotientPrimePrefixProduct k) = k := by
  let l := rootQuotientPrimePrefix k
  let b := rootQuotientPrimePrefixProduct k
  have hPrime : ∀ p : ℕ, p ∈ l → p.Prime := by
    simpa [l] using rootQuotientPrimePrefix_all_prime k
  have hPerm : l.Perm b.primeFactorsList := by
    apply Nat.primeFactorsList_unique (n := b) (l := l)
    · rfl
    · exact hPrime
  calc
    rootQuotientPrimeFactorCount b = b.primeFactorsList.length := rfl
    _ = l.length := hPerm.length_eq.symm
    _ = k := by simp [l, rootQuotientPrimePrefix]

/-- The first-`k`-prime product is squarefree. -/
theorem rootQuotientPrimePrefixProduct_squarefree
    (k : ℕ) :
    Squarefree (rootQuotientPrimePrefixProduct k) := by
  let l := rootQuotientPrimePrefix k
  let b := rootQuotientPrimePrefixProduct k
  have hPrime : ∀ p : ℕ, p ∈ l → p.Prime := by
    simpa [l] using rootQuotientPrimePrefix_all_prime k
  have hPos : 1 ≤ b := by
    dsimp [b, rootQuotientPrimePrefixProduct]
    exact prime_list_product_positive hPrime
  have hPerm : l.Perm b.primeFactorsList := by
    apply Nat.primeFactorsList_unique (n := b) (l := l)
    · rfl
    · exact hPrime
  have hPrefixNodup : l.Nodup := by
    simpa [l] using rootQuotientPrimePrefix_nodup k
  have hCanonicalNodup : b.primeFactorsList.Nodup :=
    hPerm.nodup_iff.mp hPrefixNodup
  exact (Nat.squarefree_iff_nodup_primeFactorsList (by omega)).2 hCanonicalNodup

/-- The first-`k`-prime product is `r`-power-free for every root order at least two. -/
theorem rootQuotientPrimePrefixProduct_rPowerFree
    {r k : ℕ}
    (hr : 2 ≤ r) :
    RPowerFree r (rootQuotientPrimePrefixProduct k) := by
  have hPrime := rootQuotientPrimePrefix_all_prime k
  have hPos : 1 ≤ rootQuotientPrimePrefixProduct k := by
    exact prime_list_product_positive hPrime
  have hSquarefree := rootQuotientPrimePrefixProduct_squarefree k
  apply (rPowerFree_iff_prime_factorization_lt hPos).2
  intro p _hp
  have hLe : (rootQuotientPrimePrefixProduct k).factorization p ≤ 1 :=
    hSquarefree.natFactorization_le_one p
  omega

/-- Rank-`k` power-free shell in the positive integers. -/
def RootQuotientPrimeShell (r k : ℕ) : Set ℕ :=
  {b : ℕ |
    1 ≤ b ∧ RPowerFree r b ∧ rootQuotientPrimeFactorCount b = k}

/-- Every rank shell is nonempty once `r>=2`. -/
theorem rootQuotientPrimeShell_nonempty
    {r k : ℕ}
    (hr : 2 ≤ r) :
    (RootQuotientPrimeShell r k).Nonempty := by
  refine ⟨rootQuotientPrimePrefixProduct k, ?_⟩
  refine ⟨?_, rootQuotientPrimePrefixProduct_rPowerFree hr,
    rootQuotientPrimePrefixProduct_factorCount k⟩
  exact prime_list_product_positive (rootQuotientPrimePrefix_all_prime k)

/-- Abstract minimum integer on the rank-`k` power-free shell. -/
noncomputable def rootQuotientPrimeShellMinimum (r k : ℕ) : ℕ :=
  sInf (RootQuotientPrimeShell r k)

/-- The abstract shell minimum is itself a member of the shell. -/
theorem rootQuotientPrimeShellMinimum_mem
    {r k : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r k ∈ RootQuotientPrimeShell r k := by
  exact Nat.sInf_mem (rootQuotientPrimeShell_nonempty hr)

/-- The abstract shell minimum is no larger than any shell member. -/
theorem rootQuotientPrimeShellMinimum_le
    {r k b : ℕ}
    (hb : b ∈ RootQuotientPrimeShell r k) :
    rootQuotientPrimeShellMinimum r k ≤ b := by
  exact Nat.sInf_le hb

/-- Rank zero has shell minimum one. -/
theorem rootQuotientPrimeShellMinimum_zero
    {r : ℕ}
    (hr : 2 ≤ r) :
    rootQuotientPrimeShellMinimum r 0 = 1 := by
  have hMem := rootQuotientPrimeShellMinimum_mem (r := r) (k := 0) hr
  have hUpper : rootQuotientPrimeShellMinimum r 0 ≤ 1 := by
    apply rootQuotientPrimeShellMinimum_le
    have hOneFree : RPowerFree r 1 := by
      have hPrefixFree :=
        rootQuotientPrimePrefixProduct_rPowerFree (r := r) (k := 0) hr
      simpa [rootQuotientPrimePrefixProduct, rootQuotientPrimePrefix] using hPrefixFree
    exact ⟨by simp, hOneFree, by simp [rootQuotientPrimeFactorCount]⟩
  omega

/-- A positive power-free denominator with at least `k` prime-factor tokens has
a power-free divisor with exactly `k` tokens. -/
theorem exists_rPowerFree_divisor_with_primeFactorCount
    {r b k : ℕ}
    (hbPos : 1 ≤ b)
    (hbFree : RPowerFree r b)
    (hkPos : 1 ≤ k)
    (hkLe : k ≤ rootQuotientPrimeFactorCount b) :
    ∃ a : ℕ,
      1 ≤ a ∧ a ∣ b ∧ RPowerFree r a ∧
        rootQuotientPrimeFactorCount a = k := by
  by_cases hkEq : k = rootQuotientPrimeFactorCount b
  · exact ⟨b, hbPos, dvd_rfl, hbFree, hkEq.symm⟩
  · have hkLt : k < rootQuotientPrimeFactorCount b := by omega
    obtain ⟨a, _c, haTwo, _hcTwo, haDvd, _hcDvd,
        haFree, _hcFree, _hProd, hCountA, _hCountC⟩ :=
      exists_rPowerFree_factor_split_at_primeFactorCount
        hbPos hbFree hkPos hkLt
    exact ⟨a, by omega, haDvd, haFree, hCountA⟩

/-- Exact abstract shell threshold.

For `r>=2` and a nontrivial bounded domain `N>=1`, rank `k` has appeared by
state bound `N` iff the exact prime-only horizon has reached at least `k`. -/
theorem rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
    {r N k : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    rootQuotientPrimeShellMinimum r k ≤ N ↔
      k ≤ rootQuotientPrimeHorizon r N := by
  constructor
  · intro hMinN
    have hMem := rootQuotientPrimeShellMinimum_mem (r := r) (k := k) hr
    have hBound :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
    have hCount := hBound
      (rootQuotientPrimeShellMinimum r k) hMem.1 hMinN hMem.2.1
    simpa [hMem.2.2] using hCount
  · intro hkHorizon
    by_cases hkZero : k = 0
    · subst k
      rw [rootQuotientPrimeShellMinimum_zero hr]
      exact hN
    · have hkPos : 1 ≤ k := by omega
      have hHorizonPos : 0 < rootQuotientPrimeHorizon r N := by omega
      obtain ⟨b, hbPos, hbN, hbFree, hbCount⟩ :=
        exists_powerFree_boundary_at_rootQuotientPrimeHorizon hHorizonPos
      have hkLeB : k ≤ rootQuotientPrimeFactorCount b := by
        rw [hbCount]
        exact hkHorizon
      obtain ⟨a, haPos, haDvd, haFree, haCount⟩ :=
        exists_rPowerFree_divisor_with_primeFactorCount
          hbPos hbFree hkPos hkLeB
      have haN : a ≤ N :=
        (Nat.le_of_dvd (by omega) haDvd).trans hbN
      have haShell : a ∈ RootQuotientPrimeShell r k :=
        ⟨haPos, haFree, haCount⟩
      exact (rootQuotientPrimeShellMinimum_le haShell).trans haN

/-- Exact interval representation of the prime-horizon staircase by abstract
rank-shell minima. -/
theorem rootQuotientPrimeHorizon_eq_iff_shell_interval
    {r N k : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N) :
    rootQuotientPrimeHorizon r N = k ↔
      rootQuotientPrimeShellMinimum r k ≤ N ∧
      N < rootQuotientPrimeShellMinimum r (k + 1) := by
  constructor
  · intro hEq
    constructor
    · apply (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon hr hN).2
      omega
    · by_contra hNot
      have hNext :
          k + 1 ≤ rootQuotientPrimeHorizon r N :=
        (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
          (r := r) (N := N) (k := k + 1) hr hN).1 (by omega)
      omega
  · rintro ⟨hLower, hUpper⟩
    have hkLe : k ≤ rootQuotientPrimeHorizon r N :=
      (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon hr hN).1 hLower
    have hNotNext : ¬k + 1 ≤ rootQuotientPrimeHorizon r N := by
      intro hNext
      have hMinNext : rootQuotientPrimeShellMinimum r (k + 1) ≤ N :=
        (rootQuotientPrimeShellMinimum_le_iff_rank_le_horizon
          (r := r) (N := N) (k := k + 1) hr hN).2 hNext
      omega
    omega

end EnterpriseMath.Quotient
