import EnterpriseMath.Quotient.RootQuotientPrimeTwoPowerMetric
import EnterpriseMath.Quotient.RootQuotientBinaryPenultimate
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Mixed `2`/`3` product decreases as more of a fixed number of cost slots are
allowed to use the cheaper factor `2` instead of `3`. -/
theorem two_pow_mul_three_pow_mono_cheapSlots
    {k c a : ℕ}
    (hca : c ≤ a)
    (hak : a ≤ k) :
    2 ^ a * 3 ^ (k - a) ≤
      2 ^ c * 3 ^ (k - c) := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hca
  obtain ⟨t, hkt⟩ := Nat.exists_eq_add_of_le hak
  subst k
  have hPow : 2 ^ d ≤ 3 ^ d :=
    Nat.pow_le_pow_left (by omega) d
  have hMid : 2 ^ d * 3 ^ t ≤ 3 ^ d * 3 ^ t :=
    Nat.mul_le_mul_right (3 ^ t) hPow
  have hAll : 2 ^ c * (2 ^ d * 3 ^ t) ≤
      2 ^ c * (3 ^ d * 3 ^ t) :=
    Nat.mul_le_mul_left (2 ^ c) hMid
  simpa [pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hAll

/-- Exact hard-shell candidate for primes plus one `2^m` macro. -/
def rootQuotientPrimeTwoPowerShellMinimumCandidate
    (m k : ℕ) : ℕ :=
  let a := min k (m - 1)
  2 ^ a * 3 ^ (k - a)

/-- The shell candidate has exactly weighted cost `k`. -/
theorem primeTwoPowerCost_shellCandidate
    {m k : ℕ}
    (hm : 2 ≤ m) :
    rootQuotientPrimeTwoPowerCost m
      (rootQuotientPrimeTwoPowerShellMinimumCandidate m k) = k := by
  let a := min k (m - 1)
  have haK : a ≤ k := min_le_left _ _
  have haM : a ≤ m - 1 := min_le_right _ _
  have haLtM : a < m := by omega
  let b := 2 ^ a * 3 ^ (k - a)
  have hTwoPos : 1 ≤ 2 ^ a := by positivity
  have hThreePos : 1 ≤ 3 ^ (k - a) := by positivity
  have hCountTwo : rootQuotientPrimeFactorCount 2 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_two]
    simp
  have hCountThree : rootQuotientPrimeFactorCount 3 = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime Nat.prime_three]
    simp
  have hOmega : rootQuotientPrimeFactorCount b = k := by
    dsimp [b]
    calc
      rootQuotientPrimeFactorCount (2 ^ a * 3 ^ (k - a)) =
          rootQuotientPrimeFactorCount (2 ^ a) +
            rootQuotientPrimeFactorCount (3 ^ (k - a)) :=
        rootQuotientPrimeFactorCount_mul hTwoPos hThreePos
      _ = a * 1 + (k - a) * 1 := by
        rw [rootQuotientPrimeFactorCount_pow (by omega),
          rootQuotientPrimeFactorCount_pow (by omega),
          hCountTwo, hCountThree]
      _ = k := by omega
  have hValuation : b.factorization 2 = a := by
    dsimp [b]
    rw [Nat.factorization_mul (by positivity) (by positivity)]
    simp [Nat.prime_two, Nat.prime_three]
  have hDivZero : a / m = 0 := Nat.div_eq_of_lt haLtM
  dsimp [rootQuotientPrimeTwoPowerShellMinimumCandidate,
    rootQuotientPrimeTwoPowerCost, a, b]
  rw [hOmega, hValuation, hDivZero]
  simp

/-- Exact generalized hard-shell lower bound.

At weighted cost `k`, at most `m-1` cost slots can be literal twos.  Every
remaining canonical slot contributes multiplicative value at least three.
Hence the smallest possible target is

`2^min(k,m-1) * 3^(k-min(k,m-1))`. -/
theorem primeTwoPowerShellCandidate_le_of_cost_eq
    {m b k : ℕ}
    (hm : 2 ≤ m)
    (hbPos : 1 ≤ b)
    (hCost : rootQuotientPrimeTwoPowerCost m b = k) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate m k ≤ b := by
  let e := b.factorization 2
  let q := e / m
  let s := e % m
  let odd := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  let a := min k (m - 1)
  have hsLtM : s < m := by
    dsimp [s]
    exact Nat.mod_lt e (by omega)
  have hsLeM : s ≤ m - 1 := by omega
  have hCanonicalLen := rootQuotientPrimeTwoPowerCanonicalWord_length
    (m := m) (b := b) hm
  rw [hCost] at hCanonicalLen
  have hCostSlots : q + s + odd.length = k := by
    simpa [rootQuotientPrimeTwoPowerCanonicalWord, q, s, odd,
      List.length_append] using hCanonicalLen
  have hsLeK : s ≤ k := by omega
  have hsLeA : s ≤ a := by
    dsimp [a]
    exact le_min hsLeK hsLeM
  have haLeK : a ≤ k := by
    dsimp [a]
    exact min_le_left _ _
  have hCheapSlots :
      2 ^ a * 3 ^ (k - a) ≤ 2 ^ s * 3 ^ (k - s) :=
    two_pow_mul_three_pow_mono_cheapSlots hsLeA haLeK
  have hMacroBase : 3 ≤ 2 ^ m := by
    have hFour : 2 ^ 2 ≤ 2 ^ m :=
      Nat.pow_le_pow_right (by omega) hm
    norm_num at hFour ⊢
    omega
  have hMacroLower : 3 ^ q ≤ (2 ^ m) ^ q :=
    Nat.pow_le_pow_left hMacroBase q
  have hOddLower : 3 ^ odd.length ≤ odd.prod := by
    apply pow_three_length_le_list_prod
    intro p hp
    exact three_le_of_mem_primeFactorsList_filter_ne_two hp
  have hQOdd : 3 ^ q * 3 ^ odd.length ≤
      (2 ^ m) ^ q * odd.prod :=
    Nat.mul_le_mul hMacroLower hOddLower
  have hScaled : 2 ^ s * (3 ^ q * 3 ^ odd.length) ≤
      2 ^ s * ((2 ^ m) ^ q * odd.prod) :=
    Nat.mul_le_mul_left (2 ^ s) hQOdd
  have hExp : q + odd.length = k - s := by omega
  have hIntermediate : 2 ^ s * 3 ^ (k - s) ≤
      (2 ^ m) ^ q * (2 ^ s * odd.prod) := by
    rw [← hExp, pow_add]
    simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hScaled
  have hProd := rootQuotientPrimeTwoPowerCanonicalWord_product
    (m := m) (b := b) hm hbPos
  rw [rootQuotientWordProduct_eq_prod] at hProd
  have hProdForm : b = (2 ^ m) ^ q * (2 ^ s * odd.prod) := by
    simpa [rootQuotientPrimeTwoPowerCanonicalWord, q, s, odd,
      List.prod_append, List.prod_replicate, Nat.mul_assoc] using hProd
  dsimp [rootQuotientPrimeTwoPowerShellMinimumCandidate, a]
  rw [hProdForm]
  exact hCheapSlots.trans hIntermediate

/-- Exact hard-shell theorem for the whole `2^m` single-macro family. -/
theorem primeTwoPowerShellMinimum_exact
    {m k : ℕ}
    (hm : 2 ≤ m) :
    rootQuotientPrimeTwoPowerCost m
        (rootQuotientPrimeTwoPowerShellMinimumCandidate m k) = k ∧
      (∀ b : ℕ,
        1 ≤ b →
        rootQuotientPrimeTwoPowerCost m b = k →
        rootQuotientPrimeTwoPowerShellMinimumCandidate m k ≤ b) :=
  ⟨primeTwoPowerCost_shellCandidate hm,
    fun b hb hCost => primeTwoPowerShellCandidate_le_of_cost_eq hm hb hCost⟩

/-- Macro `4` (`m=2`) has the largest hard-shell threshold among all single
`2^m` macros, pointwise at every positive weighted cost.

This is the structural reason `4` is the depth-optimal member of the whole
power-of-two macro family. -/
theorem primeTwoPowerShellCandidate_le_primeFourShell
    {m k : ℕ}
    (hm : 2 ≤ m)
    (hk : 1 ≤ k) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate m k ≤
      2 * 3 ^ (k - 1) := by
  let a := min k (m - 1)
  have hOneLeA : 1 ≤ a := by
    dsimp [a]
    exact le_min hk (by omega)
  have haLeK : a ≤ k := by
    dsimp [a]
    exact min_le_left _ _
  have hMono := two_pow_mul_three_pow_mono_cheapSlots
    (k := k) (c := 1) (a := a) hOneLeA haLeK
  dsimp [rootQuotientPrimeTwoPowerShellMinimumCandidate, a]
  simpa using hMono

/-- Equality case at `m=2`: the generalized shell recovers exactly
`2*3^(k-1)` for positive `k`. -/
theorem primeTwoPowerShellCandidate_two_eq_primeFourShell
    {k : ℕ}
    (hk : 1 ≤ k) :
    rootQuotientPrimeTwoPowerShellMinimumCandidate 2 k =
      2 * 3 ^ (k - 1) := by
  simp [rootQuotientPrimeTwoPowerShellMinimumCandidate, min_eq_right hk]

end EnterpriseMath.Quotient
