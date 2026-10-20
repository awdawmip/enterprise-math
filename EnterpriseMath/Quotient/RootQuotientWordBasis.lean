import EnterpriseMath.Quotient.PowerFreeActionBasis
import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

open EnterpriseMath.IntegerRoot

/-- Execute a literal word of floor-quotient actions from left to right. -/
def rootQuotientWordState : ℕ → List ℕ → ℕ
  | q, [] => q
  | q, a :: w => rootQuotientWordState (q / a) w

/-- Product denominator compiled from one literal quotient-action word. -/
def rootQuotientWordProduct : List ℕ → ℕ
  | [] => 1
  | a :: w => a * rootQuotientWordProduct w

/-- Literal quotient words are exactly flat quotient actions by the product
of their action denominators. -/
theorem rootQuotientWordState_eq_div_product
    (q : ℕ) (w : List ℕ) :
    rootQuotientWordState q w = q / rootQuotientWordProduct w := by
  induction w generalizing q with
  | nil => simp [rootQuotientWordState, rootQuotientWordProduct]
  | cons a w ih =>
      simp [rootQuotientWordState, rootQuotientWordProduct, ih,
        Nat.div_div_eq_div_mul]

/-- Every literal action in a word belongs to the declared generator set. -/
def RootQuotientWordOver (G : Set ℕ) (w : List ℕ) : Prop :=
  ∀ a : ℕ, a ∈ w → a ∈ G

/-- Declared quotient generators are positive action denominators. -/
def PositiveRootQuotientGenerators (G : Set ℕ) : Prop :=
  ∀ a : ℕ, a ∈ G → 1 ≤ a

/-- Products obtainable by at most `h` declared primitive quotient actions. -/
def RootQuotientProductReachableWithin
    (h : ℕ) (G : Set ℕ) (d : ℕ) : Prop :=
  ∃ w : List ℕ,
    w.length ≤ h ∧ RootQuotientWordOver G w ∧
      d = rootQuotientWordProduct w

/-- A bounded quotient-word language separates all exact states through the
terminal `r`-th-root observation. -/
def SeparatesRootQuotientWordsUpTo
    (r N h : ℕ) (G : Set ℕ) : Prop :=
  ∀ ⦃x y : ℕ⦄, x < y → y ≤ N →
    ∃ w : List ℕ,
      w.length ≤ h ∧ RootQuotientWordOver G w ∧
        root r (rootQuotientWordState x w) ≠
          root r (rootQuotientWordState y w)

/-- A word over positive quotient generators has a positive compiled product. -/
theorem rootQuotientWordProduct_pos
    {G : Set ℕ} {w : List ℕ}
    (hG : PositiveRootQuotientGenerators G)
    (hw : RootQuotientWordOver G w) :
    1 ≤ rootQuotientWordProduct w := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      have haG : a ∈ G := hw a (by simp)
      have haPos : 1 ≤ a := hG a haG
      have hTail : RootQuotientWordOver G w := by
        intro b hb
        exact hw b (by simp [hb])
      have hProdPos : 1 ≤ rootQuotientWordProduct w := ih hTail
      have haNe : a ≠ 0 := by omega
      have hProdNe : rootQuotientWordProduct w ≠ 0 := by omega
      have hMulNe : a * rootQuotientWordProduct w ≠ 0 :=
        Nat.mul_ne_zero haNe hProdNe
      have hMulOne : 1 ≤ a * rootQuotientWordProduct w :=
        Nat.one_le_iff_ne_zero.mpr hMulNe
      simpa [rootQuotientWordProduct] using hMulOne

/-- Exact finite-horizon future-language reduction.

For positive quotient generators, literal quotient words of length at most `h`
separate every exact state in `0,...,N` through `r`-th-root terminal
observations iff their reachable denominator products contain every positive
`r`-power-free boundary up to `N`.

The theorem is a structured quotient-root specialization of classical
multiplicative-basis/test-family ideas. -/
theorem separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hG : PositiveRootQuotientGenerators G) :
    SeparatesRootQuotientWordsUpTo r N h G ↔
      ∀ b : ℕ, 1 ≤ b → b ≤ N → RPowerFree r b →
        RootQuotientProductReachableWithin h G b := by
  constructor
  · intro hSep b hbPos hbN hbFree
    have hPred : b - 1 < b := by omega
    obtain ⟨w, hwLen, hwG, hJump⟩ := hSep hPred hbN
    let a := rootQuotientWordProduct w
    have haPos : 1 ≤ a := rootQuotientWordProduct_pos hG hwG
    have hJumpA : root r ((b - 1) / a) ≠ root r (b / a) := by
      rw [rootQuotientWordState_eq_div_product,
        rootQuotientWordState_eq_div_product] at hJump
      exact hJump
    have haEq : a = b :=
      rPowerFree_boundary_forces_action hr hbPos haPos hbFree hJumpA
    refine ⟨w, hwLen, hwG, ?_⟩
    simpa [a] using haEq.symm
  · intro hReach
    let A : Set ℕ := {d : ℕ | RootQuotientProductReachableWithin h G d}
    have hEffective : SeparatesRootQuotientUpTo r N A := by
      apply powerFree_actions_separate_up_to hr
      intro b hbPos hbN hbFree
      change RootQuotientProductReachableWithin h G b
      exact hReach b hbPos hbN hbFree
    intro x y hxy hyN
    obtain ⟨a, haA, _haPos, hDist⟩ := hEffective hxy hyN
    change RootQuotientProductReachableWithin h G a at haA
    obtain ⟨w, hwLen, hwG, haEq⟩ := haA
    refine ⟨w, hwLen, hwG, ?_⟩
    rw [rootQuotientWordState_eq_div_product,
      rootQuotientWordState_eq_div_product]
    simpa [haEq] using hDist

/-- Below the first nontrivial `r`-th power, every positive boundary is
`r`-power-free. -/
theorem rPowerFree_of_le_of_lt_two_pow
    {r N b : ℕ}
    (_hr : 1 ≤ r)
    (hN : N < 2 ^ r)
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N) :
    RPowerFree r b := by
  intro t ht hDvd
  have hPowLeB : t ^ r ≤ b := Nat.le_of_dvd (by omega) hDvd
  have hTwoPowLe : 2 ^ r ≤ t ^ r := Nat.pow_le_pow_left ht r
  omega

/-- In the same finite regime, every positive current state has root exactly
one.  Thus the current observation has only the classes `0` and `1`. -/
theorem root_eq_one_of_pos_le_of_lt_two_pow
    {r N q : ℕ}
    (hr : 1 ≤ r)
    (hN : N < 2 ^ r)
    (hqPos : 1 ≤ q)
    (hqN : q ≤ N) :
    root r q = 1 := by
  have hr0 : r ≠ 0 := by omega
  apply (EnterpriseMath.IntegerRoot.root_eq_iff
    (p := r) (n := q) (k := 1) hr0).2
  constructor
  · simpa using hqPos
  · have hqLt : q < 2 ^ r := hqN.trans_lt hN
    simpa using hqLt

/-- Extreme finite separation law.

If `N < 2^r`, the present root observation has only two classes, but a
one-step primitive quotient language that separates all exact states is forced
to contain every nontrivial denominator `2,...,N`.  Denominator `1` is supplied
for free by the empty word/current observation. -/
theorem one_step_generators_contain_all_nontrivial_of_lt_two_pow
    {r N : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hN : N < 2 ^ r)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N 1 G) :
    ∀ b : ℕ, 2 ≤ b → b ≤ N → b ∈ G := by
  intro b hbTwo hbN
  have hbFree : RPowerFree r b :=
    rPowerFree_of_le_of_lt_two_pow hr hN (by omega) hbN
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := 1) (G := G) hr hG).1 hSep
      b (by omega) hbN hbFree
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  cases w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
      omega
  | cons a w =>
      have hwNil : w = [] := by
        cases w with
        | nil => rfl
        | cons c w' =>
            simp at hwLen
      subst w
      have haG : a ∈ G := hwG a (by simp)
      simp [rootQuotientWordProduct] at hProd
      rw [hProd]
      exact haG

end EnterpriseMath.Quotient
