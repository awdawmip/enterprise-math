import EnterpriseMath.Quotient.RootQuotientStableMacroCode
import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import EnterpriseMath.Quotient.RootQuotientFactorGeometry
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Stable-base candidate selected by an optional macro budget `s`: the
zero-indexed `s`-th prime, i.e. the `(s+1)`-st prime. -/
noncomputable def rootQuotientStablePrimeBase (s : ℕ) : ℕ :=
  Nat.nth Nat.Prime s

/-- Coarse canonical stable macro family at budget `s`.

For each of the first `s` prime directions `p_i<q_s`, store the pure-power
macro `p_i^q_s`, retaining only macros that lie in the bounded state domain.
The exponent `q_s` is deliberately coarse: it is chosen to make the first
stable-base theorem easy to formalize.  Later refinements can replace it by
the least exponent `e_i` with `p_i^e_i>=q_s` to optimize the additive constant. -/
noncomputable def rootQuotientCoarseStableMacroFinset
    (N s : ℕ) : Finset ℕ := by
  classical
  exact (((Finset.range s).image fun i =>
      (Nat.nth Nat.Prime i) ^ rootQuotientStablePrimeBase s).filter
        fun g => g ≤ N)

/-- Set-valued form of the coarse canonical stable macro family. -/
noncomputable def RootQuotientCoarseStableMacroSet
    (N s : ℕ) : Set ℕ :=
  ↑(rootQuotientCoarseStableMacroFinset N s)

/-- Membership in the coarse family is exactly bounded membership of one of the
first `s` prime-power macros. -/
theorem mem_rootQuotientCoarseStableMacroSet_iff
    {N s g : ℕ} :
    g ∈ RootQuotientCoarseStableMacroSet N s ↔
      g ≤ N ∧
      ∃ i : ℕ, i < s ∧
        g = (Nat.nth Nat.Prime i) ^ rootQuotientStablePrimeBase s := by
  classical
  constructor
  · intro hg
    change g ∈ rootQuotientCoarseStableMacroFinset N s at hg
    simp only [rootQuotientCoarseStableMacroFinset, Finset.mem_filter,
      Finset.mem_image, Finset.mem_range] at hg
    rcases hg with ⟨⟨i, hi, hEq⟩, hgN⟩
    exact ⟨hgN, i, hi, hEq.symm⟩
  · rintro ⟨hgN, i, hi, rfl⟩
    change (Nat.nth Nat.Prime i) ^ rootQuotientStablePrimeBase s ∈
      rootQuotientCoarseStableMacroFinset N s
    simp [rootQuotientCoarseStableMacroFinset, hi, hgN]

/-- Elementary growth bound used to show every coarse macro has value at least
the stable base. -/
theorem self_le_two_pow (n : ℕ) :
    n ≤ 2 ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ]
      have hPos : 1 ≤ 2 ^ n := by positivity
      omega

/-- The stable base `q_s` is prime. -/
theorem rootQuotientStablePrimeBase_prime
    (s : ℕ) :
    (rootQuotientStablePrimeBase s).Prime := by
  exact Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime s

/-- Every stored coarse macro has multiplicative value at least the stable
base. -/
theorem stablePrimeBase_le_of_mem_coarseStableMacroSet
    {N s g : ℕ}
    (hg : g ∈ RootQuotientCoarseStableMacroSet N s) :
    rootQuotientStablePrimeBase s ≤ g := by
  obtain ⟨_hgN, i, _hi, rfl⟩ :=
    (mem_rootQuotientCoarseStableMacroSet_iff).1 hg
  let q := rootQuotientStablePrimeBase s
  let p := Nat.nth Nat.Prime i
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  have hQTwoPow : q ≤ 2 ^ q := self_le_two_pow q
  have hTwoPowLe : 2 ^ q ≤ p ^ q :=
    Nat.pow_le_pow_left hpPrime.two_le q
  simpa [q, p] using hQTwoPow.trans hTwoPowLe

/-- The coarse family is finite. -/
theorem rootQuotientCoarseStableMacroSet_finite
    (N s : ℕ) :
    (RootQuotientCoarseStableMacroSet N s).Finite := by
  classical
  apply Set.Finite.ofFinset (rootQuotientCoarseStableMacroFinset N s)
  intro g
  rfl

/-- The coarse family uses at most `s` optional macro types. -/
theorem rootQuotientCoarseStableMacroSet_ncard_le
    (N s : ℕ) :
    (RootQuotientCoarseStableMacroSet N s).ncard ≤ s := by
  classical
  have hSubset :
      rootQuotientCoarseStableMacroFinset N s ⊆
        ((Finset.range s).image fun i =>
          (Nat.nth Nat.Prime i) ^ rootQuotientStablePrimeBase s) := by
    intro g hg
    simpa [rootQuotientCoarseStableMacroFinset] using hg.1
  have hCard : (rootQuotientCoarseStableMacroFinset N s).card ≤ s := by
    calc
      (rootQuotientCoarseStableMacroFinset N s).card ≤
          (((Finset.range s).image fun i =>
            (Nat.nth Nat.Prime i) ^ rootQuotientStablePrimeBase s)).card :=
        Finset.card_le_card hSubset
      _ ≤ (Finset.range s).card := Finset.card_image_le
      _ = s := by simp
  simpa [RootQuotientCoarseStableMacroSet] using hCard

/-- Coarse next-prime stable coding law.

With `q=q_s`, the canonical family of at most `s` pure-prime-power macros is a
stable macro code with the deliberately loose residual constant `T=q^2`.

The key residual argument is finite factorization bookkeeping.  If a bounded
target has only prime divisors below `q` and no stored macro divisor, then every
prime exponent is below `q`; otherwise `p^q` would be a bounded stored macro
dividing the target.  Its factorization support is also contained in
`{0,...,q-1}`, so the total prime-token count is at most `q*q`. -/
theorem coarseStableMacroSet_is_stableMacroCode
    {N s : ℕ} :
    RootQuotientStableMacroCode
      N
      (rootQuotientStablePrimeBase s)
      (rootQuotientStablePrimeBase s * rootQuotientStablePrimeBase s)
      (RootQuotientCoarseStableMacroSet N s) := by
  classical
  let q := rootQuotientStablePrimeBase s
  have hqPrime : q.Prime := rootQuotientStablePrimeBase_prime s
  refine ⟨hqPrime, ?_, ?_⟩
  · intro g hg
    exact stablePrimeBase_le_of_mem_coarseStableMacroSet hg
  · intro b hbPos hbN hSmallPrime hNoMacro
    have hbZero : b ≠ 0 := by omega
    have hPrimeLt : ∀ p : ℕ, p ∈ b.factorization.support → p < q := by
      intro p hpSupport
      have hpNe : b.factorization p ≠ 0 :=
        Finsupp.mem_support_iff.mp hpSupport
      have hpPrime : p.Prime := by
        by_contra hpNot
        exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
      have hpDvd : p ∣ b := by
        by_contra hpNotDvd
        exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
      exact hSmallPrime p hpPrime hpDvd
    have hExpLt : ∀ p : ℕ, p ∈ b.factorization.support → b.factorization p < q := by
      intro p hpSupport
      have hpNe : b.factorization p ≠ 0 :=
        Finsupp.mem_support_iff.mp hpSupport
      have hpPrime : p.Prime := by
        by_contra hpNot
        exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
      have hpDvd : p ∣ b := by
        by_contra hpNotDvd
        exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
      have hpLtQ : p < q := hSmallPrime p hpPrime hpDvd
      by_contra hNot
      have hqLeExp : q ≤ b.factorization p := by omega
      have hpPowDvd : p ^ q ∣ b :=
        (hpPrime.pow_dvd_iff_le_factorization hbZero).2 hqLeExp
      have hpPowLeB : p ^ q ≤ b :=
        Nat.le_of_dvd (by omega) hpPowDvd
      have hpRange : p ∈ Set.range (Nat.nth Nat.Prime) :=
        Nat.subset_range_nth hpPrime
      obtain ⟨i, hiEq⟩ := hpRange
      have hNthLt : Nat.nth Nat.Prime i < Nat.nth Nat.Prime s := by
        rw [hiEq]
        simpa [q, rootQuotientStablePrimeBase] using hpLtQ
      have hiLtS : i < s :=
        (Nat.nth_lt_nth Nat.infinite_setOfPred_prime).1 hNthLt
      have hMacroMem : p ^ q ∈ RootQuotientCoarseStableMacroSet N s := by
        apply (mem_rootQuotientCoarseStableMacroSet_iff).2
        refine ⟨hpPowLeB.trans hbN, i, hiLtS, ?_⟩
        rw [hiEq]
        simp [q]
      exact hNoMacro (p ^ q) hMacroMem hpPowDvd
    have hSupportSubset : b.factorization.support ⊆ Finset.range q := by
      intro p hpSupport
      simpa using hPrimeLt p hpSupport
    have hSupportCard : b.factorization.support.card ≤ q := by
      have hCard := Finset.card_le_card hSupportSubset
      simpa using hCard
    have hSum :
        (∑ p ∈ b.factorization.support, b.factorization p) ≤ q * q := by
      calc
        (∑ p ∈ b.factorization.support, b.factorization p) ≤
            ∑ _p ∈ b.factorization.support, q := by
          exact Finset.sum_le_sum fun p hp => (hExpLt p hp).le
        _ = b.factorization.support.card * q := by simp
        _ ≤ q * q := Nat.mul_le_mul_right q hSupportCard
    rw [rootQuotientPrimeFactorCount_eq_factorization_sum]
    simpa [Finsupp.sum, q] using hSum

/-- Bounded-domain execution upper bound supplied by the coarse `s`-macro
ladder. -/
theorem coarseStableMacroSet_separates_within_square_add_log
    {r N s : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N
      (rootQuotientStablePrimeBase s * rootQuotientStablePrimeBase s +
        Nat.log (rootQuotientStablePrimeBase s) N)
      (RootQuotientPrimeBasis N ∪ RootQuotientCoarseStableMacroSet N s) := by
  simpa [Nat.add_comm] using
    stableMacroCode_separates_within_add_log_stateBound
      (r := r)
      (hCode := coarseStableMacroSet_is_stableMacroCode (N := N) (s := s))

/-- In the high-root regime, the coarse canonical macro set is a legitimate
bounded semantic composite-macro family. -/
theorem coarseStableMacroSet_is_compositeMacroFamily
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    RootQuotientCompositeMacroFamily
      r N (RootQuotientCoarseStableMacroSet N s) := by
  intro g hg
  obtain ⟨hgN, i, _hi, hEq⟩ :=
    (mem_rootQuotientCoarseStableMacroSet_iff).1 hg
  let q := rootQuotientStablePrimeBase s
  let p := Nat.nth Nat.Prime i
  have hqPrime : q.Prime := rootQuotientStablePrimeBase_prime s
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  have hqTwo : 2 ≤ q := hqPrime.two_le
  have hpTwo : 2 ≤ p := hpPrime.two_le
  have hgEq : g = p ^ q := by
    simpa [q, p] using hEq
  have hgTwo : 2 ≤ g := by
    rw [hgEq]
    have hpLePow : p ≤ p ^ q := by
      calc
        p = p ^ 1 := by simp
        _ ≤ p ^ q := Nat.pow_le_pow_right (by omega) (by omega)
    exact hpTwo.trans hpLePow
  have hgFree : RPowerFree r g :=
    rPowerFree_of_lt_two_pow_rootOrder (by omega) (hgN.trans_lt hBinary)
  have hgNotPrime : ¬g.Prime := by
    intro hgPrime
    have hpDvd : p ∣ g := by
      rw [hgEq]
      exact dvd_pow_self p (by omega)
    rcases hgPrime.eq_one_or_self_of_dvd p hpDvd with hpOne | hpEq
    · exact hpPrime.ne_one hpOne
    · have hpLt : p < g := by
        rw [hgEq]
        have hPowLt : p ^ 1 < p ^ q :=
          pow_lt_pow_right' hpPrime.one_lt (by omega)
        simpa using hPowLt
      omega
  refine ⟨⟨hgTwo, hgN, hgFree⟩, ?_⟩
  intro hgPrimeBasis
  exact hgNotPrime hgPrimeBasis.1

end EnterpriseMath.Quotient
