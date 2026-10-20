import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- An explicit integral evenness predicate, used to keep the tetrahedral residual
certificate independent of any representation-specific parity API. -/
def intEven (z : ℤ) : Prop := ∃ t : ℤ, z = t + t

/-- A kernel edge state `(a,b,c,-c,-b,-a)` lifts to an integral zero-sum
vertex potential when all six edge values are induced as pairwise vertex sums. -/
def tetrahedralVertexLift (a b c : ℤ) : Prop :=
  ∃ v1 v2 v3 v4 : ℤ,
    v1 + v2 + v3 + v4 = 0 ∧
    v1 + v2 = a ∧
    v1 + v3 = b ∧
    v1 + v4 = c ∧
    v2 + v3 = -c ∧
    v2 + v4 = -b ∧
    v3 + v4 = -a

/-- Exact parity characterization of the `C₂` obstruction in the kernel of the
three opposite-edge matching sums.

The edge state `(a,b,c,-c,-b,-a)` is vertex-induced over `ℤ` iff `a+b+c`
is even. -/
theorem tetrahedralVertexLift_iff_intEven (a b c : ℤ) :
    tetrahedralVertexLift a b c ↔ intEven (a + b + c) := by
  constructor
  · rintro ⟨v1, v2, v3, v4, hsum, h12, h13, h14, h23, h24, h34⟩
    refine ⟨v1, ?_⟩
    omega
  · rintro ⟨t, ht⟩
    refine ⟨t, a - t, b - t, c - t, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> omega

/-- The primitive opposite-edge difference is not induced by an integral
zero-sum vertex potential. -/
theorem tetrahedralTorsionWitness_not_lift :
    ¬ tetrahedralVertexLift 1 0 0 := by
  intro h
  have heven : intEven (1 : ℤ) := by
    simpa using (tetrahedralVertexLift_iff_intEven 1 0 0).1 h
  rcases heven with ⟨t, ht⟩
  omega

/-- Doubling the primitive obstruction makes it vertex-induced.  Together with
`tetrahedralTorsionWitness_not_lift`, this is the explicit order-two witness. -/
theorem tetrahedralTorsionWitness_double_lift :
    tetrahedralVertexLift 2 0 0 := by
  apply (tetrahedralVertexLift_iff_intEven 2 0 0).2
  refine ⟨1, ?_⟩
  norm_num [intEven]

end EnterpriseMath.PrecisionPi
