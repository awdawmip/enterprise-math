import EnterpriseMath.Quotient.RootQuotientPrimeSkeleton
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Data.Finset.Range
import Mathlib.Data.Nat.Factors
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primitive prime generator alphabet. -/
def RootQuotientPrimeBasis (N : ℕ) : Set ℕ :=
  {p : ℕ | p.Prime ∧ p ≤ N}

/-- Every bounded prime generator is a positive quotient denominator. -/
theorem rootQuotientPrimeBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeBasis N) := by
  intro p hp
  exact hp.1.one_le

/-- Project quotient-word products are ordinary list products. -/
theorem rootQuotientWordProduct_eq_prod
    (w : List ℕ) :
    rootQuotientWordProduct w = w.prod := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih => simp [rootQuotientWordProduct, ih]

/-- Canonical multiplicative instruction count of a positive denominator. -/
def rootQuotientPrimeFactorCount (b : ℕ) : ℕ :=
  b.primeFactorsList.length

/-- Every literal word over the bounded prime alphabet that compiles to `b`
has exactly the canonical prime-factor count of `b`.

This is the finite quotient-word form of uniqueness of prime factorization. -/
theorem prime_word_length_eq_primeFactorCount
    {N b : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeBasis N) w)
    (hProd : rootQuotientWordProduct w = b) :
    w.length = rootQuotientPrimeFactorCount b := by
  have hListProd : w.prod = b := by
    rw [← rootQuotientWordProduct_eq_prod]
    exact hProd
  have hPrime : ∀ p : ℕ, p ∈ w → p.Prime := by
    intro p hp
    exact (hw p hp).1
  have hPerm : w.Perm b.primeFactorsList :=
    Nat.primeFactorsList_unique hListProd hPrime
  simpa [rootQuotientPrimeFactorCount] using hPerm.length_eq

/-- Exact reachability metric for the bounded prime instruction alphabet.

For a positive target denominator `b ≤ N`, reachability within `h` primitive
prime instructions is equivalent to the canonical prime-factor count being at
most `h`. -/
theorem rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
    {N h b : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) b ↔
      rootQuotientPrimeFactorCount b ≤ h := by
  constructor
  · intro hReach
    obtain ⟨w, hwLen, hwPrime, hProd⟩ := hReach
    have hExact :
        w.length = rootQuotientPrimeFactorCount b :=
      prime_word_length_eq_primeFactorCount hwPrime hProd.symm
    calc
      rootQuotientPrimeFactorCount b = w.length := hExact.symm
      _ ≤ h := hwLen
  · intro hCount
    have hbZero : b ≠ 0 := by omega
    have hwLen : b.primeFactorsList.length ≤ h := by
      simpa [rootQuotientPrimeFactorCount] using hCount
    have hwPrime :
        RootQuotientWordOver
          (RootQuotientPrimeBasis N) b.primeFactorsList := by
      intro p hp
      exact ⟨Nat.prime_of_mem_primeFactorsList hp,
        (Nat.le_of_mem_primeFactorsList hp).trans hbN⟩
    refine ⟨b.primeFactorsList, hwLen, hwPrime, ?_⟩
    rw [rootQuotientWordProduct_eq_prod]
    exact (Nat.prod_primeFactorsList hbZero).symm

/-- Exact finite-horizon criterion for the bounded prime instruction alphabet.

The semantic boundary set remains the canonical bounded `r`-power-free set
from the one-step theorem. Composition changes only the execution resource:
the prime alphabet separates exactly when every required semantic denominator
has prime-factor count at most the available word horizon. -/
theorem rootQuotientPrimeBasis_separates_iff_factorCount_bound
    {r N h : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) ↔
      ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b →
        rootQuotientPrimeFactorCount b ≤ h := by
  constructor
  · intro hSep b hbPos hbN hbFree
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h) (G := RootQuotientPrimeBasis N)
        hr rootQuotientPrimeBasis_positive).1 hSep
        b hbPos hbN hbFree
    exact
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
        (N := N) (h := h) (b := b) hbPos hbN).1 hReach
  · intro hBound
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h) (G := RootQuotientPrimeBasis N)
      hr rootQuotientPrimeBasis_positive).2
    intro b hbPos hbN hbFree
    exact
      (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
        (N := N) (h := h) (b := b) hbPos hbN).2
        (hBound b hbPos hbN hbFree)

/-- Exact worst-case prime-only execution horizon on the canonical bounded
`r`-power-free semantic action set.  This is the project object corresponding
to `L_r(N)=max Omega(b)` over required boundaries `1 ≤ b ≤ N`. -/
noncomputable def rootQuotientPrimeHorizon (r N : ℕ) : ℕ := by
  classical
  exact (Finset.range (N + 1)).sup fun b =>
    if 1 ≤ b ∧ RPowerFree r b then
      rootQuotientPrimeFactorCount b
    else
      0

/-- The exact prime horizon is below `h` iff every required bounded semantic
denominator has prime-factor count at most `h`. -/
theorem rootQuotientPrimeHorizon_le_iff
    {r N h : ℕ} :
    rootQuotientPrimeHorizon r N ≤ h ↔
      ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b →
        rootQuotientPrimeFactorCount b ≤ h := by
  classical
  constructor
  · intro hHorizon b hbPos hbN hbFree
    have hSup :
        (Finset.range (N + 1)).sup (fun q =>
          if 1 ≤ q ∧ RPowerFree r q then
            rootQuotientPrimeFactorCount q
          else
            0) ≤ h := by
      simpa [rootQuotientPrimeHorizon] using hHorizon
    have hbMem : b ∈ Finset.range (N + 1) := by
      simp
      omega
    have hTerm := (Finset.sup_le_iff).1 hSup b hbMem
    simpa [hbPos, hbFree] using hTerm
  · intro hBound
    have hSup :
        (Finset.range (N + 1)).sup (fun q =>
          if 1 ≤ q ∧ RPowerFree r q then
            rootQuotientPrimeFactorCount q
          else
            0) ≤ h := by
      apply (Finset.sup_le_iff).2
      intro b hbMem
      have hbN : b ≤ N := by
        simp at hbMem
        omega
      by_cases hRequired : 1 ≤ b ∧ RPowerFree r b
      · simpa [hRequired] using
          hBound b hRequired.1 hbN hRequired.2
      · simp [hRequired]
    simpa [rootQuotientPrimeHorizon] using hSup

/-- Exact prime-only finite-horizon law. -/
theorem rootQuotientPrimeBasis_separates_iff_horizon_le
    {r N h : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N h (RootQuotientPrimeBasis N) ↔
      rootQuotientPrimeHorizon r N ≤ h := by
  constructor
  · intro hSep
    apply (rootQuotientPrimeHorizon_le_iff (r := r) (N := N) (h := h)).2
    exact
      (rootQuotientPrimeBasis_separates_iff_factorCount_bound
        (r := r) (N := N) (h := h) hr).1 hSep
  · intro hHorizon
    apply (rootQuotientPrimeBasis_separates_iff_factorCount_bound
      (r := r) (N := N) (h := h) hr).2
    exact
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := h)).1 hHorizon

/-- The bounded prime alphabet separates at its exact worst-case horizon. -/
theorem rootQuotientPrimeBasis_separates_at_exact_horizon
    {r N : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N) (RootQuotientPrimeBasis N) := by
  exact
    (rootQuotientPrimeBasis_separates_iff_horizon_le
      (r := r) (N := N) (h := rootQuotientPrimeHorizon r N) hr).2 le_rfl

/-- Any horizon at which the bounded prime alphabet separates is at least the
exact prime-only horizon. -/
theorem rootQuotientPrimeHorizon_minimal_of_separates
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N)) :
    rootQuotientPrimeHorizon r N ≤ h := by
  exact
    (rootQuotientPrimeBasis_separates_iff_horizon_le
      (r := r) (N := N) (h := h) hr).1 hSep

/-- Every positive integer `b` admits a literal prime word of length at most `b`
whose compiled quotient denominator is exactly `b`.

The proof is finite strong descent and does not use uniqueness of factorization. -/
theorem exists_prime_word_product
    {b : ℕ}
    (hb : 1 ≤ b) :
    ∃ w : List ℕ,
      w.length ≤ b ∧
      RootQuotientWordOver (RootQuotientPrimeBasis b) w ∧
      b = rootQuotientWordProduct w := by
  induction b using Nat.strong_induction_on with
  | h b ih =>
      by_cases hbOne : b = 1
      · subst b
        exact ⟨[], by simp, by simp [RootQuotientWordOver], by simp [rootQuotientWordProduct]⟩
      · obtain ⟨p, hpPrime, hpDvd⟩ := Nat.exists_prime_and_dvd hbOne
        rcases hpDvd with ⟨c, hbc⟩
        have hcPos : 1 ≤ c := by
          by_contra hnot
          have hcZero : c = 0 := by omega
          subst c
          simp at hbc
          omega
        have hpTwo : 2 ≤ p := hpPrime.two_le
        have hcLt : c < b := by
          nlinarith [hbc, hpTwo, hcPos]
        obtain ⟨w, hwLen, hwPrime, hcProd⟩ := ih c hcLt hcPos
        have hpLeB : p ≤ b := by
          exact Nat.le_of_dvd (by omega) ⟨c, hbc⟩
        have hcLeB : c ≤ b := Nat.le_of_lt hcLt
        have hTail : RootQuotientWordOver (RootQuotientPrimeBasis b) w := by
          intro q hq
          have hqc := hwPrime q hq
          exact ⟨hqc.1, hqc.2.trans hcLeB⟩
        have hWord : RootQuotientWordOver (RootQuotientPrimeBasis b) (p :: w) := by
          intro q hq
          simp at hq
          rcases hq with rfl | hqTail
          · exact ⟨hpPrime, hpLeB⟩
          · exact hTail q hqTail
        have hLen : (p :: w).length ≤ b := by
          have hStep : w.length + 1 ≤ c + 1 := Nat.succ_le_succ hwLen
          have hcOneLeB : c + 1 ≤ b := by
            nlinarith [hbc, hpTwo, hcPos]
          simpa using hStep.trans hcOneLeB
        refine ⟨p :: w, hLen, hWord, ?_⟩
        calc
          b = p * c := hbc
          _ = p * rootQuotientWordProduct w := by rw [hcProd]
          _ = rootQuotientWordProduct (p :: w) := by
            simp [rootQuotientWordProduct]

/-- The bounded prime alphabet is sufficient with the explicit finite horizon
`N`: every required power-free boundary at most `N` has a prime word of length
at most its own value, hence at most `N`. -/
theorem rootQuotientPrimeBasis_separates_at_self_horizon
    {r N : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N N (RootQuotientPrimeBasis N) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := N) (G := RootQuotientPrimeBasis N)
    hr rootQuotientPrimeBasis_positive).2
  intro b hbPos hbN _hbFree
  obtain ⟨w, hwLen, hwPrimeB, hProd⟩ := exists_prime_word_product hbPos
  have hWordN : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro p hpw
    have hpB := hwPrimeB p hpw
    exact ⟨hpB.1, hpB.2.trans hbN⟩
  exact ⟨w, hwLen.trans hbN, hWordN, hProd⟩

/-- The exact prime-only horizon is always bounded by the coarse self horizon
`N` already supplied by the strong-descent construction. -/
theorem rootQuotientPrimeHorizon_le_self
    {r N : ℕ}
    (hr : 1 ≤ r) :
    rootQuotientPrimeHorizon r N ≤ N := by
  exact
    rootQuotientPrimeHorizon_minimal_of_separates hr
      (rootQuotientPrimeBasis_separates_at_self_horizon hr)

/-- For `r>=2`, the bounded prime alphabet is contained in every primitive
generator set that separates the bounded exact state domain at any finite word
horizon. -/
theorem rootQuotientPrimeBasis_subset_of_word_separates
    {r N h : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    RootQuotientPrimeBasis N ⊆ G := by
  intro p hp
  exact prime_generator_forced_of_word_separates
    hr hp.1 hp.2 hG hSep

/-- Exact primitive-alphabet theorem.

For `r>=2`, primes up to `N` form the unique least primitive quotient-generator
alphabet (under inclusion) among all finite-horizon languages capable of exact
state separation on `0,...,N`. Horizon `N` is an explicit sufficient bound;
the independent depth problem asks how far that horizon can be reduced. -/
theorem rootQuotientPrimeBasis_is_least_finite_horizon_alphabet
    {r N : ℕ}
    (hr : 2 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N N (RootQuotientPrimeBasis N) ∧
    ∀ {h : ℕ} {G : Set ℕ},
      PositiveRootQuotientGenerators G →
      SeparatesRootQuotientWordsUpTo r N h G →
      RootQuotientPrimeBasis N ⊆ G := by
  constructor
  · exact rootQuotientPrimeBasis_separates_at_self_horizon (by omega)
  · intro h G hG hSep
    exact rootQuotientPrimeBasis_subset_of_word_separates hr hG hSep

end EnterpriseMath.Quotient
