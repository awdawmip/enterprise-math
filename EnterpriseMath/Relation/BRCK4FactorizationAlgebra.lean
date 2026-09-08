import EnterpriseMath.Relation.BRCK4OptimalExtraction
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Data.Finsupp.Fintype
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Algebraic six-edge label type in the executable K4 source order
`AB, AC, AD, BC, BD, CD`.  This is the polynomial-factorization presentation of
the derived six-axis count observer; it is not a native Cell-address claim. -/
inductive K4EdgeLabel where
  | ab | ac | ad | bc | bd | cd
  deriving DecidableEq, Fintype

/-- Read a six-edge capacity at an algebraic edge label. -/
def k4CapacityAt (n : K4Capacity) : K4EdgeLabel → ℕ
  | .ab => n.ab
  | .ac => n.ac
  | .ad => n.ad
  | .bc => n.bc
  | .bd => n.bd
  | .cd => n.cd

/-- Finitely-supported exponent vector of a K4 capacity. -/
noncomputable def k4CapacityExponent (n : K4Capacity) : K4EdgeLabel →₀ ℕ :=
  Finsupp.equivFunOnFinite.symm (k4CapacityAt n)

@[simp] theorem k4CapacityExponent_apply (n : K4Capacity) (e : K4EdgeLabel) :
    k4CapacityExponent n e = k4CapacityAt n e := by
  simp [k4CapacityExponent]

/-- Residual capacity after extracting vertex-star multiplicities `a,b,c,d`. -/
def k4ResidualCapacity (n : K4Capacity) (a b c d : ℕ) : K4Capacity where
  ab := n.ab - (a + b)
  ac := n.ac - (a + c)
  ad := n.ad - (a + d)
  bc := n.bc - (b + c)
  bd := n.bd - (b + d)
  cd := n.cd - (c + d)

/-- Unit star at vertex A. -/
def k4StarA : K4Capacity :=
  ⟨1, 1, 1, 0, 0, 0⟩

/-- Unit star at vertex B. -/
def k4StarB : K4Capacity :=
  ⟨1, 0, 0, 1, 1, 0⟩

/-- Unit star at vertex C. -/
def k4StarC : K4Capacity :=
  ⟨0, 1, 0, 1, 0, 1⟩

/-- Unit star at vertex D. -/
def k4StarD : K4Capacity :=
  ⟨0, 0, 1, 0, 1, 1⟩

/-- Exact exponent decomposition behind every feasible K4 extraction. -/
theorem k4CapacityExponent_decompose
    (n : K4Capacity) (a b c d : ℕ)
    (h : k4Feasible n a b c d) :
    k4CapacityExponent n =
      (((k4CapacityExponent (k4ResidualCapacity n a b c d) +
          a • k4CapacityExponent k4StarA) +
        b • k4CapacityExponent k4StarB) +
        c • k4CapacityExponent k4StarC) +
        d • k4CapacityExponent k4StarD := by
  rcases h with ⟨hab, hac, had, hbc, hbd, hcd⟩
  ext e
  cases e <;>
    simp [k4CapacityExponent_apply, k4CapacityAt, k4ResidualCapacity,
      k4StarA, k4StarB, k4StarC, k4StarD] <;>
    omega

/-- Six-variable commutative polynomial carrier for K4 capacity factorization. -/
abbrev K4CapacityPolynomial (R : Type*) [CommSemiring R] :=
  MvPolynomial K4EdgeLabel R

/-- Monomial attached to a six-edge capacity. -/
noncomputable def k4CapacityMonomial {R : Type*} [CommSemiring R]
    (n : K4Capacity) : K4CapacityPolynomial R :=
  MvPolynomial.monomial (k4CapacityExponent n) 1

/-- Four algebraic K4 star factors. -/
noncomputable def k4StarMonomialA {R : Type*} [CommSemiring R] :
    K4CapacityPolynomial R := k4CapacityMonomial k4StarA
noncomputable def k4StarMonomialB {R : Type*} [CommSemiring R] :
    K4CapacityPolynomial R := k4CapacityMonomial k4StarB
noncomputable def k4StarMonomialC {R : Type*} [CommSemiring R] :
    K4CapacityPolynomial R := k4CapacityMonomial k4StarC
noncomputable def k4StarMonomialD {R : Type*} [CommSemiring R] :
    K4CapacityPolynomial R := k4CapacityMonomial k4StarD

/-- Every feasible K4 extraction is literally a polynomial factorization

`X^n = X^r Q_A^a Q_B^b Q_C^c Q_D^d`.

Thus the integer extraction variables are algebraic factor exponents rather than
external geometric annotations. -/
theorem k4CapacityMonomial_factorization {R : Type*} [CommSemiring R]
    (n : K4Capacity) (a b c d : ℕ)
    (h : k4Feasible n a b c d) :
    k4CapacityMonomial (R := R) n =
      k4CapacityMonomial (R := R) (k4ResidualCapacity n a b c d) *
        k4StarMonomialA ^ a * k4StarMonomialB ^ b *
        k4StarMonomialC ^ c * k4StarMonomialD ^ d := by
  have hexp := k4CapacityExponent_decompose n a b c d h
  unfold k4CapacityMonomial k4StarMonomialA k4StarMonomialB
    k4StarMonomialC k4StarMonomialD
  rw [hexp]
  simp [MvPolynomial.monomial_pow, add_assoc]

/-- Closed-form K4 optimum is exactly the maximum total exponent of star factors
among feasible algebraic factorizations.  The witness is not canonically
single-valued: symmetric inputs may have an entire optimal factorization fibre. -/
theorem k4ClosedValue_is_maximal_starFactorCount {R : Type*} [CommSemiring R]
    (n : K4Capacity) :
    (∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = k4ClosedValue n ∧
      k4CapacityMonomial (R := R) n =
        k4CapacityMonomial (R := R) (k4ResidualCapacity n a b c d) *
          k4StarMonomialA ^ a * k4StarMonomialB ^ b *
          k4StarMonomialC ^ c * k4StarMonomialD ^ d) ∧
    ∀ a b c d : ℕ,
      k4Feasible n a b c d →
        k4ExtractionValue a b c d ≤ k4ClosedValue n := by
  rcases k4ClosedValue_optimal n with ⟨hattain, hmax⟩
  rcases hattain with ⟨a, b, c, d, hfeas, hval⟩
  constructor
  · exact ⟨a, b, c, d, hfeas, hval,
      k4CapacityMonomial_factorization (R := R) n a b c d hfeas⟩
  · exact hmax

end EnterpriseMath.BranchRecoalescence
