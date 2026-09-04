import Mathlib.Combinatorics.Enumerative.Stirling
import Mathlib.Tactic

namespace EnterpriseMath.PrimeWindingStirlingChambers

open scoped BigOperators

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
    Nat.pow_eq_sum_stirlingSecond_mul_descFactorial r r

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
    deficiencyChamberCount 3 0 = 3 ! := by
  native_decide

/-- The deepest degree-three chamber has normalized mass `1/9`. -/
theorem degreeThree_deep_fraction :
    (deficiencyChamberCount 3 2 : ℚ) / (3 ^ 3 : ℚ) = 1 / 9 := by
  norm_num [deficiencyChamberCount, imageChamberCount, Nat.stirlingSecond]

end EnterpriseMath.PrimeWindingStirlingChambers
