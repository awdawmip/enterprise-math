import EnterpriseMath.Quotient.RootQuotientCompilerRefinement
import EnterpriseMath.Quotient.RootQuotientPrimeShellBinary
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with the single composite macro instruction `4`. -/
def RootQuotientPrimeFourBasis (N : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({4} : Set ℕ)

/-- Prime-plus-four generators are positive. -/
theorem rootQuotientPrimeFourBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeFourBasis N) := by
  intro g hg
  rcases hg with hgPrime | hgFour
  · exact hgPrime.1.one_le
  · have hEq : g = 4 := by simpa using hgFour
    subst g
    omega

/-- A word over positive quotient generators has positive compiled product. -/
theorem rootQuotientWordProduct_one_le_of_positiveGenerators
    {G : Set ℕ} {w : List ℕ}
    (hGPos : PositiveRootQuotientGenerators G)
    (hw : RootQuotientWordOver G w) :
    1 ≤ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      have haG : a ∈ G := hw a (by simp)
      have haPos : 1 ≤ a := hGPos a haG
      have hwTail : RootQuotientWordOver G w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTail := ih hwTail
      simp only [rootQuotientWordProduct]
      exact Nat.one_le_mul haPos hTail

/-- The prime-factor count of a prime-plus-four word product is literal word
length plus the number of uses of macro `4`.

Each prime instruction carries one prime token; each `4` instruction carries
two. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeFour
    {N : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeFourBasis N) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + w.count 4 := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeFourBasis N := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeFourBasis N) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeFourBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeFourBasis_positive a haBasis
      rw [rootQuotientWordProduct]
      rw [rootQuotientPrimeFactorCount_mul haPos hTailPos]
      rw [ih hwTail]
      rcases haBasis with haPrime | haFour
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have haNeFour : a ≠ 4 := by
          intro hEq
          subst a
          norm_num at haPrime
        rw [haCount, List.count_cons]
        simp [haNeFour]
        omega
      · have haEq : a = 4 := by simpa using haFour
        subst a
        have hFourCount : rootQuotientPrimeFactorCount 4 = 2 := by
          simpa using rootQuotientPrimeFactorCount_two_pow 2
        rw [hFourCount, List.count_cons]
        simp
        omega

/-- Every occurrence of `4` contributes a factor `4` to the compiled product. -/
theorem pow_four_count_dvd_rootQuotientWordProduct
    (w : List ℕ) :
    4 ^ w.count 4 ∣ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases haFour : a = 4
      · subst a
        have hMul := Nat.mul_dvd_mul_left 4 ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · have hDvd : 4 ^ w.count 4 ∣ a * rootQuotientWordProduct w :=
          dvd_mul_of_dvd_right ih a
        simpa [rootQuotientWordProduct, List.count_cons, haFour] using hDvd

/-- Exact weighted cost induced by adding macro `4` to the bounded prime ISA. -/
def rootQuotientPrimeFourCost (b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b - b.factorization 2 / 2

/-- Universal lower bound: no prime-plus-four word for `b` can be shorter than
the weighted cost `Omega(b)-floor(v_2(b)/2)`. -/
theorem rootQuotientPrimeFourCost_le_word_length
    {N b : ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeFourBasis N) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeFourCost b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let m := w.count 4
  have hCount : rootQuotientPrimeFactorCount b = w.length + m := by
    rw [hProd]
    simpa [m] using rootQuotientPrimeFactorCount_wordProduct_primeFour hw
  have hFourDvd : 4 ^ m ∣ b := by
    rw [hProd]
    simpa [m] using pow_four_count_dvd_rootQuotientWordProduct w
  have hTwoPowDvd : 2 ^ (2 * m) ∣ b := by
    have hFourEq : (4 : ℕ) = 2 ^ 2 := by norm_num
    rw [hFourEq] at hFourDvd
    simpa [← pow_mul] using hFourDvd
  have hValuation : 2 * m ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hmLe : m ≤ b.factorization 2 / 2 := by omega
  dsimp [rootQuotientPrimeFourCost]
  omega

/-- Filtering away all `2` entries partitions list length into odd/non-two
entries plus the count of `2`. -/
theorem length_filter_ne_two_add_count_two
    (l : List ℕ) :
    (l.filter (fun n : ℕ => n != 2)).length + l.count 2 = l.length := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases ha : a = 2
      · subst a
        simp [List.count_cons, ih]
      · simp [List.count_cons, ha, ih]

/-- Multiplicative counterpart of the same filter partition. -/
theorem pow_count_two_mul_filter_ne_two_prod
    (l : List ℕ) :
    2 ^ l.count 2 * (l.filter (fun n : ℕ => n != 2)).prod = l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases ha : a = 2
      · subst a
        simp [List.count_cons, ih, pow_succ, Nat.mul_assoc,
          Nat.mul_comm, Nat.mul_left_comm]
      · simp [List.count_cons, ha, ih, Nat.mul_assoc,
          Nat.mul_comm, Nat.mul_left_comm]

/-- Pairing the exponent of `2` into blocks of two is exactly the algebraic
identity behind macro `4`. -/
theorem four_pow_div_two_mul_two_pow_mod_two
    (e : ℕ) :
    4 ^ (e / 2) * 2 ^ (e % 2) = 2 ^ e := by
  have hDecomp : e % 2 + (e / 2) * 2 = e :=
    Nat.mod_add_div' e 2
  rw [show (4 : ℕ) = 2 ^ 2 by norm_num]
  rw [← pow_mul, ← pow_add]
  congr 1
  omega

/-- Canonical shortest candidate: pair all prime-factor tokens `2,2` into
macro `4`, leave at most one literal `2`, and retain every non-two prime factor
literally. -/
def rootQuotientPrimeFourCanonicalWord (b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / 2) 4 ++
    List.replicate (b.factorization 2 % 2) 2 ++
      b.primeFactorsList.filter (fun p : ℕ => p != 2)

/-- Exact length of the canonical prime-plus-four word. -/
theorem rootQuotientPrimeFourCanonicalWord_length
    (b : ℕ) :
    (rootQuotientPrimeFourCanonicalWord b).length =
      rootQuotientPrimeFourCost b := by
  have hCount : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_add_count_two b.primeFactorsList
  rw [hCount] at hSplit
  have hDiv : b.factorization 2 % 2 +
      (b.factorization 2 / 2) * 2 = b.factorization 2 :=
    Nat.mod_add_div' (b.factorization 2) 2
  dsimp [rootQuotientPrimeFourCanonicalWord, rootQuotientPrimeFourCost,
    rootQuotientPrimeFactorCount]
  simp only [List.length_append, List.length_replicate]
  omega

/-- Product of the canonical prime-plus-four word is the original positive
integer. -/
theorem rootQuotientPrimeFourCanonicalWord_product
    {b : ℕ}
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeFourCanonicalWord b) := by
  have hbZero : b ≠ 0 := by omega
  have hCount : b.primeFactorsList.count 2 = b.factorization 2 :=
    Nat.primeFactorsList_count_eq
  have hSplit := pow_count_two_mul_filter_ne_two_prod b.primeFactorsList
  rw [hCount, Nat.prod_primeFactorsList hbZero] at hSplit
  have hPair := four_pow_div_two_mul_two_pow_mod_two (b.factorization 2)
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeFourCanonicalWord]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = 2 ^ b.factorization 2 *
        (b.primeFactorsList.filter (fun p : ℕ => p != 2)).prod := hSplit.symm
    _ = (4 ^ (b.factorization 2 / 2) * 2 ^ (b.factorization 2 % 2)) *
        (b.primeFactorsList.filter (fun p : ℕ => p != 2)).prod := by rw [hPair]
    _ = 4 ^ (b.factorization 2 / 2) *
        (2 ^ (b.factorization 2 % 2) *
          (b.primeFactorsList.filter (fun p : ℕ => p != 2)).prod) := by
      rw [Nat.mul_assoc]

/-- The canonical word uses only bounded primes and macro `4`, provided the
state bound includes the prime `2`. -/
theorem rootQuotientPrimeFourCanonicalWord_over_basis
    {N b : ℕ}
    (hN : 2 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeFourBasis N)
      (rootQuotientPrimeFourCanonicalWord b) := by
  let w4 := List.replicate (b.factorization 2 / 2) 4
  let w2 := List.replicate (b.factorization 2 % 2) 2
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  have hw4 : RootQuotientWordOver (RootQuotientPrimeFourBasis N) w4 := by
    intro g hg
    have hEq : g = 4 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inr (by simp)
  have hw2 : RootQuotientWordOver (RootQuotientPrimeFourBasis N) w2 := by
    intro g hg
    have hEq : g = 2 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inl ⟨Nat.prime_two, hN⟩
  have hwo : RootQuotientWordOver (RootQuotientPrimeFourBasis N) wo := by
    intro p hp
    have hpFactors : p ∈ b.primeFactorsList := by
      simpa [wo] using (List.mem_filter.1 hp).1
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpFactors
    have hpLeB : p ≤ b := Nat.le_of_mem_primeFactorsList hpFactors
    exact Or.inl ⟨hpPrime, hpLeB.trans hbN⟩
  simpa [rootQuotientPrimeFourCanonicalWord, w4, w2, wo] using
    rootQuotientWordOver_append hw4 (rootQuotientWordOver_append hw2 hwo)

/-- Exact pointwise reachability law for bounded primes plus macro `4`. -/
theorem rootQuotientPrimeFourBasis_reachableWithin_iff_cost_le
    {N b h : ℕ}
    (hN : 2 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin
        h (RootQuotientPrimeFourBasis N) b ↔
      rootQuotientPrimeFourCost b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeFourCost_le_word_length
      hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeFourCanonicalWord b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeFourCanonicalWord_length]
      exact hCost
    · exact rootQuotientPrimeFourCanonicalWord_over_basis hN hbN
    · exact rootQuotientPrimeFourCanonicalWord_product hbPos

end EnterpriseMath.Quotient
