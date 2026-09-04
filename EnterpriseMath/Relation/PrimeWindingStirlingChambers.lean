import Mathlib.Combinatorics.Enumerative.Stirling
import Mathlib.Tactic

namespace EnterpriseMath.PrimeWindingStirlingChambers

open scoped BigOperators

/-- Compatibility lemma added after the repository's pinned mathlib revision. -/
theorem descFactorial_mul_self_local (n j : ℕ) :
    n.descFactorial j * n =
      n.descFactorial (j + 1) + j * n.descFactorial j := by
  rcases le_or_gt j n with h | h
  · rw [Nat.descFactorial_succ, ← Nat.add_mul, Nat.sub_add_cancel h,
      Nat.mul_comm]
  · simp [Nat.descFactorial_of_lt h]

/--
Every power is the Stirling expansion in descending factorials. This proof is
kept locally because the theorem postdates the pinned mathlib revision.
-/
theorem pow_eq_sum_stirlingSecond_mul_descFactorial_local (n k : ℕ) :
    n ^ k =
      ∑ j ∈ Finset.range (k + 1),
        Nat.stirlingSecond k j * n.descFactorial j := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hshift :
        ∑ j ∈ Finset.range (k + 1),
            Nat.stirlingSecond k j * (j * n.descFactorial j) =
          ∑ j ∈ Finset.range (k + 1),
            (j + 1) *
              (Nat.stirlingSecond k (j + 1) * n.descFactorial (j + 1)) := by
      rw [Finset.sum_range_succ'
          (fun j ↦ Nat.stirlingSecond k j * (j * n.descFactorial j)) k,
        Finset.sum_range_succ
          (fun j ↦ (j + 1) *
            (Nat.stirlingSecond k (j + 1) * n.descFactorial (j + 1))) k,
        Nat.stirlingSecond_eq_zero_of_lt k.lt_add_one]
      simp [mul_left_comm]
    rw [pow_succ, ih, Finset.sum_mul,
      Finset.sum_range_succ'
        (fun j ↦ Nat.stirlingSecond (k + 1) j * n.descFactorial j) (k + 1)]
    simp only [mul_assoc, descFactorial_mul_self_local, mul_add,
      Finset.sum_add_distrib, hshift, Nat.stirlingSecond_succ_succ,
      add_mul, Nat.stirlingSecond_succ_zero, zero_mul, add_zero]
    exact add_comm _ _

/--
Integer chamber multiplicity with `j` occupied scale bins among `r` history
coordinates: choose the occupied labels and map onto all of them.
-/
def imageChamberCount (r j : ℕ) : ℕ :=
  Nat.stirlingSecond r j * r.descFactorial j

/-- All functions from `r` history slots to `r` scale bins partition by image size. -/
theorem sum_imageChamberCount (r : ℕ) :
    ∑ j ∈ Finset.range (r + 1), imageChamberCount r j = r ^ r := by
  symm
  simpa [imageChamberCount] using
    pow_eq_sum_stirlingSecond_mul_descFactorial_local r r

/-- Chamber multiplicity indexed by image deficiency `k=r-j`. -/
def deficiencyChamberCount (r k : ℕ) : ℕ :=
  imageChamberCount r (r - k)

/-- At degree two the core and one-overcut chambers have equal total volume. -/
theorem degreeTwo_chambers :
    deficiencyChamberCount 2 0 = 2 ∧
      deficiencyChamberCount 2 1 = 2 ∧
      2 ^ 2 = 2 + 2 := by
  native_decide

/--
At degree three the `3!` permutation core, one-overcut chamber, and deepest
constant-map chamber have exact integer multiplicities `6`, `18`, and `3`.
-/
theorem degreeThree_chambers :
    deficiencyChamberCount 3 0 = 6 ∧
      deficiencyChamberCount 3 1 = 18 ∧
      deficiencyChamberCount 3 2 = 3 ∧
      3 ^ 3 = 6 + 18 + 3 := by
  native_decide

/-- The degree-three core chamber is literally the factorial provenance count. -/
theorem degreeThree_core_eq_factorial :
    deficiencyChamberCount 3 0 = Nat.factorial 3 := by
  native_decide

/-- The deepest degree-three chamber has normalized mass `1/9`. -/
theorem degreeThree_deep_fraction :
    (deficiencyChamberCount 3 2 : ℚ) / (3 ^ 3 : ℚ) = 1 / 9 := by
  norm_num [deficiencyChamberCount, imageChamberCount, Nat.stirlingSecond]

end EnterpriseMath.PrimeWindingStirlingChambers
