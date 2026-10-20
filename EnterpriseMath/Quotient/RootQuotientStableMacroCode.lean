import EnterpriseMath.Quotient.RootQuotientInstructionMetric
import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Abstract stable macro code with base `q` and residual literal-prime budget
`T` on bounded targets `<=N`.

Every stored macro has multiplicative value at least `q`.  Any positive bounded
target with no prime factor at least `q` and no stored macro divisor has at most
`T` prime-factor tokens left.  These two conditions are exactly what the
recursive stable coding argument needs. -/
def RootQuotientStableMacroCode
    (N q T : ℕ) (S : Set ℕ) : Prop :=
  q.Prime ∧
  (∀ g : ℕ, g ∈ S → q ≤ g) ∧
  (∀ b : ℕ,
    1 ≤ b →
    b ≤ N →
    (∀ p : ℕ, p.Prime → p ∣ b → p < q) →
    (∀ g : ℕ, g ∈ S → ¬g ∣ b) →
    rootQuotientPrimeFactorCount b ≤ T)

/-- Consuming one factor of multiplicative value at least the log base raises
`Nat.log` by at least one. -/
theorem add_one_log_le_log_mul_of_base_le_factor
    {q g c : ℕ}
    (hq : 1 < q)
    (hc : 1 ≤ c)
    (hqg : q ≤ g) :
    Nat.log q c + 1 ≤ Nat.log q (g * c) := by
  have hcZero : c ≠ 0 := by omega
  have hPow : q ^ Nat.log q c ≤ c :=
    Nat.pow_log_le_self q hcZero
  have hMul : q ^ Nat.log q c * q ≤ c * g :=
    Nat.mul_le_mul hPow hqg
  have hBound : q ^ (Nat.log q c + 1) ≤ g * c := by
    rw [pow_succ]
    simpa [Nat.mul_comm] using hMul
  exact Nat.le_log_of_pow_le hq hBound

/-- A prime literal or stable macro factor `g>=q` strictly reduces any positive
multiple when divided out. -/
theorem quotient_lt_of_factor_two_le
    {g b c : ℕ}
    (hg : 2 ≤ g)
    (hc : 1 ≤ c)
    (hbc : b = g * c) :
    c < b := by
  rw [hbc]
  have hlt : c < c * g :=
    Nat.lt_mul_of_one_lt_right (by omega) (by omega)
  simpa [Nat.mul_comm] using hlt

/-- Core recursive coding theorem.

A stable macro code compiles every positive target `b<=N` in at most

`T + log_q b`

instructions over bounded primes together with the stored macro family.  Each
recursive expensive step consumes either a prime factor `>=q` or a macro factor
`>=q`; if neither exists, the residual target has at most `T` prime tokens and
is finished literally by the bounded prime ISA. -/
theorem stableMacroCode_reachableWithin_add_log
    {N q T b : ℕ} {S : Set ℕ}
    (hCode : RootQuotientStableMacroCode N q T S)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RootQuotientProductReachableWithin
      (T + Nat.log q b)
      (RootQuotientPrimeBasis N ∪ S)
      b := by
  classical
  induction b using Nat.strong_induction_on with
  | h b ih =>
      have hqPrime : q.Prime := hCode.1
      have hqTwo : 2 ≤ q := hqPrime.two_le
      by_cases hBig : ∃ p : ℕ, p.Prime ∧ p ∣ b ∧ q ≤ p
      · obtain ⟨p, hpPrime, hpDvd, hqP⟩ := hBig
        obtain ⟨c, hbc⟩ := hpDvd
        have hcPos : 1 ≤ c := by
          by_contra hNot
          have hcZero : c = 0 := by omega
          subst c
          simp at hbc
          omega
        have hcLt : c < b :=
          quotient_lt_of_factor_two_le hpPrime.two_le hcPos hbc
        have hcDvd : c ∣ b := by
          refine ⟨p, ?_⟩
          simpa [Nat.mul_comm] using hbc
        have hcN : c ≤ N :=
          (Nat.le_of_dvd (by omega) hcDvd).trans hbN
        have hRec := ih c hcLt hcPos hcN
        obtain ⟨w, hwLen, hwBasis, hProd⟩ := hRec
        have hpN : p ≤ N :=
          (Nat.le_of_dvd (by omega) hpDvd).trans hbN
        have hLogStep : Nat.log q c + 1 ≤ Nat.log q b := by
          rw [hbc]
          exact add_one_log_le_log_mul_of_base_le_factor
            hqPrime.one_lt hcPos hqP
        refine ⟨p :: w, ?_, ?_, ?_⟩
        · simp only [List.length_cons]
          omega
        · intro g hg
          simp at hg
          rcases hg with rfl | hgTail
          · exact Or.inl ⟨hpPrime, hpN⟩
          · exact hwBasis g hgTail
        · calc
            b = p * c := hbc
            _ = p * rootQuotientWordProduct w := by rw [← hProd]
            _ = rootQuotientWordProduct (p :: w) := by rfl
      · by_cases hMacro : ∃ g : ℕ, g ∈ S ∧ g ∣ b
        · obtain ⟨g, hgS, hgDvd⟩ := hMacro
          have hqG : q ≤ g := hCode.2.1 g hgS
          have hgTwo : 2 ≤ g := hqTwo.trans hqG
          obtain ⟨c, hbc⟩ := hgDvd
          have hcPos : 1 ≤ c := by
            by_contra hNot
            have hcZero : c = 0 := by omega
            subst c
            simp at hbc
            omega
          have hcLt : c < b :=
            quotient_lt_of_factor_two_le hgTwo hcPos hbc
          have hcDvd : c ∣ b := by
            refine ⟨g, ?_⟩
            simpa [Nat.mul_comm] using hbc
          have hcN : c ≤ N :=
            (Nat.le_of_dvd (by omega) hcDvd).trans hbN
          have hRec := ih c hcLt hcPos hcN
          obtain ⟨w, hwLen, hwBasis, hProd⟩ := hRec
          have hLogStep : Nat.log q c + 1 ≤ Nat.log q b := by
            rw [hbc]
            exact add_one_log_le_log_mul_of_base_le_factor
              hqPrime.one_lt hcPos hqG
          refine ⟨g :: w, ?_, ?_, ?_⟩
          · simp only [List.length_cons]
            omega
          · intro a ha
            simp at ha
            rcases ha with rfl | haTail
            · exact Or.inr hgS
            · exact hwBasis a haTail
          · calc
              b = g * c := hbc
              _ = g * rootQuotientWordProduct w := by rw [← hProd]
              _ = rootQuotientWordProduct (g :: w) := by rfl
        · have hSmallPrime : ∀ p : ℕ, p.Prime → p ∣ b → p < q := by
            intro p hp hpDvd
            by_contra hNot
            have hqP : q ≤ p := by omega
            exact hBig ⟨p, hp, hpDvd, hqP⟩
          have hNoMacro : ∀ g : ℕ, g ∈ S → ¬g ∣ b := by
            intro g hgS hgDvd
            exact hMacro ⟨g, hgS, hgDvd⟩
          have hOmega : rootQuotientPrimeFactorCount b ≤ T :=
            hCode.2.2 b hbPos hbN hSmallPrime hNoMacro
          have hPrimeReach : RootQuotientProductReachableWithin
              T (RootQuotientPrimeBasis N) b :=
            (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
              hbPos hbN).2 hOmega
          obtain ⟨w, hwLen, hwPrime, hProd⟩ := hPrimeReach
          refine ⟨w, hwLen.trans (Nat.le_add_right _ _), ?_, hProd⟩
          intro p hp
          exact Or.inl (hwPrime p hp)

/-- Stable macro code gives a bounded-domain task horizon `T+log_q N`. -/
theorem stableMacroCode_separates_within_add_log_stateBound
    {r N q T : ℕ} {S : Set ℕ}
    (hr : 1 ≤ r)
    (hCode : RootQuotientStableMacroCode N q T S) :
    SeparatesRootQuotientWordsUpTo
      r N (T + Nat.log q N)
      (RootQuotientPrimeBasis N ∪ S) := by
  have hUnionPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hqPrime := hCode.1
      exact hqPrime.one_le.trans (hCode.2.1 g hgS)
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N)
    (h := T + Nat.log q N)
    (G := RootQuotientPrimeBasis N ∪ S)
    hr hUnionPos).2
  intro b hbPos hbN hbFree
  have hReach := stableMacroCode_reachableWithin_add_log
    hCode hbPos hbN
  obtain ⟨w, hwLen, hwBasis, hProd⟩ := hReach
  have hLogMono : Nat.log q b ≤ Nat.log q N :=
    Nat.log_mono_right hbN
  refine ⟨w, ?_, hwBasis, hProd⟩
  omega

/-- Word-metric form of the same stable coding upper bound. -/
theorem instructionLength_stableMacroCode_le_add_log
    {N q T b : ℕ} {S : Set ℕ}
    (hCode : RootQuotientStableMacroCode N q T S)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    rootQuotientInstructionLength
        (RootQuotientPrimeBasis N ∪ S) b ≤
      ((T + Nat.log q b : ℕ) : ℕ∞) :=
  (rootQuotientInstructionLength_le_natCast_iff).2
    (stableMacroCode_reachableWithin_add_log hCode hbPos hbN)

end EnterpriseMath.Quotient
