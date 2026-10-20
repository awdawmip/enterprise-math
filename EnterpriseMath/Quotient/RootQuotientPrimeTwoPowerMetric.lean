import EnterpriseMath.Quotient.RootQuotientPrimeFourMetric
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with one `2^m` macro instruction. -/
def RootQuotientPrimeTwoPowerBasis (N m : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({2 ^ m} : Set ℕ)

/-- The generalized one-two-power-macro ISA is positive. -/
theorem rootQuotientPrimeTwoPowerBasis_positive
    {N m : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeTwoPowerBasis N m) := by
  intro g hg
  rcases hg with hgPrime | hgMacro
  · exact hgPrime.1.one_le
  · have hEq : g = 2 ^ m := by simpa using hgMacro
    subst g
    positivity

/-- Exact weighted cost induced by the single macro `2^m`.

Each macro occurrence replaces `m` literal prime-2 instructions by one, saving
`m-1` steps. -/
def rootQuotientPrimeTwoPowerCost (m b : ℕ) : ℕ :=
  rootQuotientPrimeFactorCount b -
    (m - 1) * (b.factorization 2 / m)

/-- Prime-factor count of a word over bounded primes plus `2^m`.

For `m>=2`, every prime instruction contributes one prime token while every
macro contributes `m`, so the total is

`word_length + (m-1) * macro_count`. -/
theorem rootQuotientPrimeFactorCount_wordProduct_primeTwoPower
    {N m : ℕ} {w : List ℕ}
    (hm : 2 ≤ m)
    (hw : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) =
      w.length + (m - 1) * w.count (2 ^ m) := by
  induction w with
  | nil => simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haBasis : a ∈ RootQuotientPrimeTwoPowerBasis N m := hw a (by simp)
      have hwTail : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) w := by
        intro g hg
        exact hw g (by simp [hg])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_one_le_of_positiveGenerators
          rootQuotientPrimeTwoPowerBasis_positive hwTail
      have haPos : 1 ≤ a := rootQuotientPrimeTwoPowerBasis_positive a haBasis
      rw [rootQuotientWordProduct]
      rw [rootQuotientPrimeFactorCount_mul haPos hTailPos]
      rw [ih hwTail]
      rcases haBasis with haPrime | haMacro
      · have haCount : rootQuotientPrimeFactorCount a = 1 := by
          rw [rootQuotientPrimeFactorCount,
            Nat.primeFactorsList_prime haPrime.1]
          simp
        have haNeMacro : a ≠ 2 ^ m := by
          intro hEq
          have hMacroCount : rootQuotientPrimeFactorCount (2 ^ m) = m :=
            rootQuotientPrimeFactorCount_two_pow m
          rw [hEq] at haCount
          rw [hMacroCount] at haCount
          omega
        rw [haCount, List.count_cons]
        simp [haNeMacro]
        omega
      · have haEq : a = 2 ^ m := by simpa using haMacro
        subst a
        have hMacroCount : rootQuotientPrimeFactorCount (2 ^ m) = m :=
          rootQuotientPrimeFactorCount_two_pow m
        rw [hMacroCount, List.count_cons]
        simp
        ring_nf
        omega

/-- Every occurrence of macro `2^m` contributes a corresponding factor to the
compiled product. -/
theorem pow_twoPower_count_dvd_rootQuotientWordProduct
    (m : ℕ) (w : List ℕ) :
    (2 ^ m) ^ w.count (2 ^ m) ∣ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      by_cases haMacro : a = 2 ^ m
      · subst a
        have hMul := Nat.mul_dvd_mul_left (2 ^ m) ih
        simpa [rootQuotientWordProduct, List.count_cons, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hMul
      · have hDvd : (2 ^ m) ^ w.count (2 ^ m) ∣
            a * rootQuotientWordProduct w :=
          dvd_mul_of_dvd_right ih a
        simpa [rootQuotientWordProduct, List.count_cons, haMacro] using hDvd

/-- Universal lower bound for the generalized weighted cost. -/
theorem rootQuotientPrimeTwoPowerCost_le_word_length
    {N m b : ℕ} {w : List ℕ}
    (hm : 2 ≤ m)
    (hbPos : 1 ≤ b)
    (hw : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) w)
    (hProd : b = rootQuotientWordProduct w) :
    rootQuotientPrimeTwoPowerCost m b ≤ w.length := by
  have hbZero : b ≠ 0 := by omega
  let c := w.count (2 ^ m)
  let q := b.factorization 2 / m
  have hCount : rootQuotientPrimeFactorCount b =
      w.length + (m - 1) * c := by
    rw [hProd]
    simpa [c] using
      rootQuotientPrimeFactorCount_wordProduct_primeTwoPower hm hw
  have hMacroDvd : (2 ^ m) ^ c ∣ b := by
    rw [hProd]
    simpa [c] using pow_twoPower_count_dvd_rootQuotientWordProduct m w
  have hTwoPowDvd : 2 ^ (m * c) ∣ b := by
    simpa [← pow_mul] using hMacroDvd
  have hValuation : m * c ≤ b.factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization hbZero).1 hTwoPowDvd
  have hcLeQ : c ≤ q := by
    dsimp [q]
    apply (Nat.le_div_iff_mul_le (by omega)).2
    simpa [Nat.mul_comm] using hValuation
  have hSavedLe : (m - 1) * c ≤ (m - 1) * q :=
    Nat.mul_le_mul_left (m - 1) hcLeQ
  have hSub :
      rootQuotientPrimeFactorCount b - (m - 1) * q ≤
        rootQuotientPrimeFactorCount b - (m - 1) * c :=
    Nat.sub_le_sub_left hSavedLe _
  have hRight :
      rootQuotientPrimeFactorCount b - (m - 1) * c = w.length := by
    rw [hCount]
    simp
  dsimp [rootQuotientPrimeTwoPowerCost, q]
  exact hSub.trans_eq hRight

/-- Exact algebraic pairing identity for the `2`-adic exponent. -/
theorem twoPower_pow_div_mul_two_pow_mod
    {m e : ℕ}
    (hm : 1 ≤ m) :
    (2 ^ m) ^ (e / m) * 2 ^ (e % m) = 2 ^ e := by
  have hDecomp : e % m + (e / m) * m = e :=
    Nat.mod_add_div' e m
  rw [← pow_mul, ← pow_add]
  congr 1
  calc
    m * (e / m) + e % m = e % m + (e / m) * m := by ring
    _ = e := hDecomp

/-- Canonical shortest candidate: group all prime-2 tokens into `m`-blocks,
leave fewer than `m` literal twos, and retain all non-two prime factors. -/
def rootQuotientPrimeTwoPowerCanonicalWord (m b : ℕ) : List ℕ :=
  List.replicate (b.factorization 2 / m) (2 ^ m) ++
    List.replicate (b.factorization 2 % m) 2 ++
      b.primeFactorsList.filter (fun p : ℕ => p != 2)

/-- Exact length of the generalized canonical word. -/
theorem rootQuotientPrimeTwoPowerCanonicalWord_length
    {m b : ℕ}
    (hm : 2 ≤ m) :
    (rootQuotientPrimeTwoPowerCanonicalWord m b).length =
      rootQuotientPrimeTwoPowerCost m b := by
  let e := b.factorization 2
  let q := e / m
  let s := e % m
  let odd := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  have hCount : b.primeFactorsList.count 2 = e := by
    dsimp [e]
    exact Nat.primeFactorsList_count_eq
  have hSplit := length_filter_ne_two_add_count_two b.primeFactorsList
  rw [hCount] at hSplit
  have hDecomp : s + q * m = e := by
    dsimp [q, s]
    exact Nat.mod_add_div' e m
  have hmDecomp : m = (m - 1) + 1 := by omega
  have hOmega : odd.length + e = rootQuotientPrimeFactorCount b := by
    dsimp [odd, rootQuotientPrimeFactorCount]
    exact hSplit
  have hAdd :
      (q + s + odd.length) + (m - 1) * q =
        rootQuotientPrimeFactorCount b := by
    calc
      (q + s + odd.length) + (m - 1) * q =
          odd.length + (s + q * m) := by
        rw [hmDecomp]
        ring
      _ = odd.length + e := by rw [hDecomp]
      _ = rootQuotientPrimeFactorCount b := hOmega
  change q + s + odd.length =
    rootQuotientPrimeFactorCount b - (m - 1) * q
  rw [← hAdd]
  simp

/-- Product of the generalized canonical word is the original positive target. -/
theorem rootQuotientPrimeTwoPowerCanonicalWord_product
    {m b : ℕ}
    (hm : 2 ≤ m)
    (hbPos : 1 ≤ b) :
    b = rootQuotientWordProduct (rootQuotientPrimeTwoPowerCanonicalWord m b) := by
  have hbZero : b ≠ 0 := by omega
  let e := b.factorization 2
  let q := e / m
  let s := e % m
  let odd := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  have hCount : b.primeFactorsList.count 2 = e := by
    dsimp [e]
    exact Nat.primeFactorsList_count_eq
  have hSplit := pow_count_two_mul_filter_ne_two_prod b.primeFactorsList
  rw [hCount, Nat.prod_primeFactorsList hbZero] at hSplit
  have hPair := twoPower_pow_div_mul_two_pow_mod (e := e) (by omega : 1 ≤ m)
  rw [rootQuotientWordProduct_eq_prod]
  dsimp [rootQuotientPrimeTwoPowerCanonicalWord, q, s, odd]
  simp only [List.prod_append, List.prod_replicate]
  calc
    b = 2 ^ e * odd.prod := by simpa [odd] using hSplit.symm
    _ = ((2 ^ m) ^ q * 2 ^ s) * odd.prod := by rw [hPair]
    _ = (2 ^ m) ^ q * (2 ^ s * odd.prod) := by rw [Nat.mul_assoc]

/-- The generalized canonical word uses only bounded primes and the single
`2^m` macro. -/
theorem rootQuotientPrimeTwoPowerCanonicalWord_over_basis
    {N m b : ℕ}
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hbN : b ≤ N) :
    RootQuotientWordOver
      (RootQuotientPrimeTwoPowerBasis N m)
      (rootQuotientPrimeTwoPowerCanonicalWord m b) := by
  let wm := List.replicate (b.factorization 2 / m) (2 ^ m)
  let w2 := List.replicate (b.factorization 2 % m) 2
  let wo := b.primeFactorsList.filter (fun p : ℕ => p != 2)
  have hwm : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) wm := by
    intro g hg
    have hEq : g = 2 ^ m := List.eq_of_mem_replicate hg
    subst g
    exact Or.inr (by simp)
  have hw2 : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) w2 := by
    intro g hg
    have hEq : g = 2 := List.eq_of_mem_replicate hg
    subst g
    exact Or.inl ⟨Nat.prime_two, hN⟩
  have hwo : RootQuotientWordOver (RootQuotientPrimeTwoPowerBasis N m) wo := by
    intro p hp
    have hpFactors : p ∈ b.primeFactorsList := (List.mem_filter.1 hp).1
    have hpPrime : p.Prime := Nat.prime_of_mem_primeFactorsList hpFactors
    have hpLeB : p ≤ b := Nat.le_of_mem_primeFactorsList hpFactors
    exact Or.inl ⟨hpPrime, hpLeB.trans hbN⟩
  simpa [rootQuotientPrimeTwoPowerCanonicalWord, wm, w2, wo] using
    rootQuotientWordOver_append hwm (rootQuotientWordOver_append hw2 hwo)

/-- Exact pointwise reachability law for bounded primes plus one `2^m` macro. -/
theorem rootQuotientPrimeTwoPowerBasis_reachableWithin_iff_cost_le
    {N m b h : ℕ}
    (hm : 2 ≤ m)
    (hN : 2 ≤ N)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin
        h (RootQuotientPrimeTwoPowerBasis N m) b ↔
      rootQuotientPrimeTwoPowerCost m b ≤ h := by
  constructor
  · rintro ⟨w, hwLen, hwBasis, hProd⟩
    exact (rootQuotientPrimeTwoPowerCost_le_word_length
      hm hbPos hwBasis hProd).trans hwLen
  · intro hCost
    refine ⟨rootQuotientPrimeTwoPowerCanonicalWord m b, ?_, ?_, ?_⟩
    · rw [rootQuotientPrimeTwoPowerCanonicalWord_length hm]
      exact hCost
    · exact rootQuotientPrimeTwoPowerCanonicalWord_over_basis hm hN hbN
    · exact rootQuotientPrimeTwoPowerCanonicalWord_product hm hbPos

/-- The earlier prime-plus-four weighted metric is exactly the `m=2`
specialization. -/
theorem rootQuotientPrimeTwoPowerCost_two_eq_primeFourCost
    (b : ℕ) :
    rootQuotientPrimeTwoPowerCost 2 b = rootQuotientPrimeFourCost b := by
  simp [rootQuotientPrimeTwoPowerCost, rootQuotientPrimeFourCost]

end EnterpriseMath.Quotient
