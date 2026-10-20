import EnterpriseMath.Geometry.TetrahedralResidualParity

namespace EnterpriseMath.TetrahedralResidual

/-- Rational slice weights used after scalar extension. -/
abbrev Vertex4Q := Fin 4 → ℚ

/-- Rational edge weights used after scalar extension. -/
abbrev Edge6Q := Fin 6 → ℚ

/-- Total rational slice weight. -/
def vertexSumQ (v : Vertex4Q) : ℚ :=
  v 0 + v 1 + v 2 + v 3

/-- Rational extension of the tetrahedral vertex-to-edge map. -/
def deltaQ (v : Vertex4Q) : Edge6Q :=
  ![v 0 + v 1, v 0 + v 2, v 0 + v 3,
    v 1 + v 2, v 1 + v 3, v 2 + v 3]

/-- Rational kernel normal form. -/
def kernelEdgeQ (a b c : ℚ) : Edge6Q :=
  ![a, b, c, -c, -b, -a]

/-- The canonical half-coordinate lift of a kernel edge. -/
def rationalKernelLift (a b c : ℚ) : Vertex4Q :=
  ![(a + b + c) / 2,
    (a - b - c) / 2,
    (-a + b - c) / 2,
    (-a - b + c) / 2]

/-- The canonical rational lift has zero total slice weight. -/
theorem vertexSumQ_rationalKernelLift (a b c : ℚ) :
    vertexSumQ (rationalKernelLift a b c) = 0 := by
  norm_num [vertexSumQ, rationalKernelLift]
  ring

/-- Every rational kernel edge is induced by its canonical half-coordinate
slice potential. -/
theorem deltaQ_rationalKernelLift (a b c : ℚ) :
    deltaQ (rationalKernelLift a b c) = kernelEdgeQ a b c := by
  funext i
  fin_cases i <;>
    norm_num [deltaQ, rationalKernelLift, kernelEdgeQ] <;> ring

/-- Scalar extension therefore removes the integer parity obstruction. -/
theorem rationalKernel_hasZeroSumPreimage (a b c : ℚ) :
    ∃ v : Vertex4Q, vertexSumQ v = 0 ∧ deltaQ v = kernelEdgeQ a b c := by
  exact ⟨rationalKernelLift a b c,
    vertexSumQ_rationalKernelLift a b c,
    deltaQ_rationalKernelLift a b c⟩

/-- Explicit half-integral lift of the primitive integer parity class. -/
def primitiveParityLiftQ : Vertex4Q :=
  ![(1 : ℚ) / 2, (1 : ℚ) / 2, -(1 : ℚ) / 2, -(1 : ℚ) / 2]

/-- The explicit primitive rational lift is zero-sum. -/
theorem primitiveParityLiftQ_sum : vertexSumQ primitiveParityLiftQ = 0 := by
  norm_num [vertexSumQ, primitiveParityLiftQ]

/-- The explicit primitive rational lift maps to the primitive kernel edge. -/
theorem primitiveParityLiftQ_delta :
    deltaQ primitiveParityLiftQ = kernelEdgeQ 1 0 0 := by
  funext i
  fin_cases i <;> norm_num [deltaQ, primitiveParityLiftQ, kernelEdgeQ]

/-- The same primitive class has a rational lift but no integer lift. -/
theorem primitiveParity_integral_vs_rational :
    (∃ v : Vertex4Q,
        vertexSumQ v = 0 ∧ deltaQ v = kernelEdgeQ 1 0 0) ∧
      ¬ HasZeroSumPreimage 1 0 0 := by
  exact ⟨rationalKernel_hasZeroSumPreimage 1 0 0,
    primitiveParity_noPreimage⟩

end EnterpriseMath.TetrahedralResidual
