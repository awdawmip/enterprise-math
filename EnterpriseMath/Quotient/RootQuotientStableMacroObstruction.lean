import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A primitive macro serves prime direction `p` when it is a positive power of
that prime.  Only such macros can divide pure powers of `p`. -/
def RootQuotientMacroServesPrimeDirection
    (g p : ℕ) : Prop :=
  ∃ e : ℕ, 1 ≤ e ∧ g = p ^ e

/-- One positive integer cannot be a positive power of two different primes. -/
theorem primeDirection_eq_of_macro_serves_both
    {g p q : ℕ}
    (hp : p.Prime)
    (hq : q.Prime)
    (hgp : RootQuotientMacroServesPrimeDirection g p)
    (hgq : RootQuotientMacroServesPrimeDirection g q) :
    p = q := by
  obtain ⟨a, ha, hga⟩ := hgp
  obtain ⟨b, hb, hgb⟩ := hgq
  have hpDvd : p ∣ q ^ b := by
    rw [← hgb, hga]
    exact dvd_pow_self p (by omega)
  have hpDvdQ : p ∣ q := hp.dvd_of_dvd_pow hpDvd
  exact (Nat.prime_dvd_prime_iff_eq hp hq).1 hpDvdQ

/-- Every positive divisor at least two of a prime power serves that prime
direction. -/
theorem macroServesPrimeDirection_of_dvd_primePow
    {g p n : ℕ}
    (hp : p.Prime)
    (hgTwo : 2 ≤ g)
    (hgDvd : g ∣ p ^ n) :
    RootQuotientMacroServesPrimeDirection g p := by
  have hgZero : g ≠ 0 := by omega
  have hPowZero : p ^ n ≠ 0 := by positivity
  have hEq : g = p ^ g.factorization p := by
    apply Nat.eq_pow_of_factorization_eq_single hgZero
    ext q
    by_cases hqp : q = p
    · subst q
      simp
    · have hLe : g.factorization q ≤ (p ^ n).factorization q :=
        ((Nat.factorization_le_iff_dvd hgZero hPowZero).2 hgDvd) q
      have hPowQ : (p ^ n).factorization q = 0 := by
        rw [Nat.Prime.factorization_pow hp]
        simp [hqp]
      have hgQ : g.factorization q = 0 := by omega
      rw [hgQ]
      simp [hqp]
  have hExpPos : 1 ≤ g.factorization p := by
    by_contra hNot
    have hExpZero : g.factorization p = 0 := by omega
    rw [hEq, hExpZero, pow_zero] at hgTwo
    omega
  exact ⟨g.factorization p, hExpPos, hEq⟩

/-- Among the first `s+1` prime directions, a finite family of at most `s`
optional macros leaves at least one direction unserved.

The proof is a finite pigeonhole argument: if every prime direction had a
serving macro, choosing one macro per direction would inject `s+1` indices into
an `s`-element family because one macro cannot serve two different primes. -/
theorem exists_unserved_firstPrimeDirection
    {r N s : ℕ} {S : Set ℕ}
    (hSFinite : S.Finite)
    (_hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSCard : S.ncard ≤ s) :
    ∃ i : ℕ,
      i < s + 1 ∧
      ∀ g : ℕ, g ∈ S →
        ¬RootQuotientMacroServesPrimeDirection
          g (Nat.nth Nat.Prime i) := by
  classical
  by_contra hNo
  push_neg at hNo
  have hAll : ∀ i : ℕ, i < s + 1 →
      ∃ g : ℕ, g ∈ S ∧
        RootQuotientMacroServesPrimeDirection
          g (Nat.nth Nat.Prime i) := by
    exact hNo
  let f : ℕ → ℕ := fun i =>
    if hi : i < s + 1 then
      Classical.choose (hAll i hi)
    else
      1
  have hfSpec : ∀ i : ℕ, (hi : i < s + 1) →
      f i ∈ S ∧
        RootQuotientMacroServesPrimeDirection
          (f i) (Nat.nth Nat.Prime i) := by
    intro i hi
    dsimp [f]
    rw [dif_pos hi]
    exact Classical.choose_spec (hAll i hi)
  have hLower : s + 1 ≤ S.ncard := by
    apply Set.le_ncard_of_inj_on_range f
    · intro i hi
      exact (hfSpec i hi).1
    · intro i hi j hj hEq
      have hiServe := (hfSpec i hi).2
      have hjServe := (hfSpec j hj).2
      have hiPrime : (Nat.nth Nat.Prime i).Prime :=
        Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
      have hjPrime : (Nat.nth Nat.Prime j).Prime :=
        Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime j
      have hPrimeEq : Nat.nth Nat.Prime i = Nat.nth Nat.Prime j :=
        primeDirection_eq_of_macro_serves_both
          hiPrime hjPrime hiServe (hEq ▸ hjServe)
      exact Nat.nth_injective Nat.infinite_setOfPred_prime hPrimeEq
    · exact hSFinite
  omega

/-- Universal finite-horizon next-prime obstruction.

Let `q_s` be the zero-indexed `s`-th prime, i.e. the `(s+1)`-st prime.  In the
high-root regime, any normalized presentation with at most `s` optional
composite macro types that separates within `h` must satisfy

`N < q_s^(h+1)`.

Indeed, one of the first `s+1` prime directions has no dedicated pure-power
macro.  Its target `p^(h+1)` therefore still requires `h+1` literal prime
instructions. -/
theorem stateBound_lt_nthPrime_pow_succ_of_macroBudget_separator
    {r N s h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSCard : S.ncard ≤ s)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S)) :
    N < (Nat.nth Nat.Prime s) ^ (h + 1) := by
  by_contra hNot
  have hQPowLeN : (Nat.nth Nat.Prime s) ^ (h + 1) ≤ N := by omega
  obtain ⟨i, hi, hiUnserved⟩ :=
    exists_unserved_firstPrimeDirection hSFinite hSFamily hSCard
  let p := Nat.nth Nat.Prime i
  let q := Nat.nth Nat.Prime s
  have hpPrime : p.Prime :=
    Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i
  have hiLeS : i ≤ s := by omega
  have hpLeQ : p ≤ q := by
    dsimp [p, q]
    exact Nat.nth_monotone Nat.infinite_setOfPred_prime hiLeS
  have hpPowLeQPow : p ^ (h + 1) ≤ q ^ (h + 1) :=
    Nat.pow_le_pow_left hpLeQ (h + 1)
  have hpPowLeN : p ^ (h + 1) ≤ N :=
    hpPowLeQPow.trans hQPowLeN
  have hpPowPos : 1 ≤ p ^ (h + 1) := by positivity
  have hpPowFree : RPowerFree r (p ^ (h + 1)) :=
    rPowerFree_of_lt_two_pow_rootOrder hpPowPos
      (hpPowLeN.trans_lt hBinary)
  have hUnionPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hSFamily hgS).1
      omega
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hUnionPos).1 hSep
      (p ^ (h + 1)) hpPowPos hpPowLeN hpPowFree
  obtain ⟨w, hwLen, hwUnion, hProd⟩ := hReach
  have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro g hgWord
    have hgUnion := hwUnion g hgWord
    rcases hgUnion with hgPrime | hgS
    · exact hgPrime
    · have hgSemantic := (hSFamily hgS).1
      have hgDvd : g ∣ p ^ (h + 1) :=
        word_member_dvd_compiled_product hgWord hProd
      have hgServes : RootQuotientMacroServesPrimeDirection g p :=
        macroServesPrimeDirection_of_dvd_primePow
          hpPrime hgSemantic.1 hgDvd
      exact (hiUnserved g hgS hgServes).elim
  have hExact : w.length =
      rootQuotientPrimeFactorCount (p ^ (h + 1)) :=
    prime_word_length_eq_primeFactorCount hwPrime hProd.symm
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hpPrime]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ (h + 1)) = h + 1 := by
    rw [rootQuotientPrimeFactorCount_pow hpPrime.one_le, hpCount]
    simp
  rw [hPowCount] at hExact
  omega

/-- Macro-budget form: every high-root separator using at most `s` optional
composite types has semantic radius at least the next-prime obstruction. -/
theorem nthPrime_pow_succ_le_stateBound_obstructs_macroBudget
    {r N s h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSCard : S.ncard ≤ s)
    (hState : (Nat.nth Nat.Prime s) ^ (h + 1) ≤ N) :
    ¬SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S) := by
  intro hSep
  have hBound := stateBound_lt_nthPrime_pow_succ_of_macroBudget_separator
    hr hBinary hSFinite hSFamily hSCard hSep
  omega

end EnterpriseMath.Quotient
