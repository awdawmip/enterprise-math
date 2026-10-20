import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- Six integer edge coordinates of a tetrahedron, ordered as
`12,13,14,23,24,34`. -/
structure TetraEdges where
  x12 : ℤ
  x13 : ℤ
  x14 : ℤ
  x23 : ℤ
  x24 : ℤ
  x34 : ℤ
  deriving DecidableEq

/-- Total edge variation. -/
def TetraEdges.total (x : TetraEdges) : ℤ :=
  x.x12 + x.x13 + x.x14 + x.x23 + x.x24 + x.x34

/-- The three opposite-edge matching sums. -/
def TetraEdges.matchingSums (x : TetraEdges) : ℤ × ℤ × ℤ :=
  (x.x12 + x.x34, x.x13 + x.x24, x.x14 + x.x23)

/-- Zero total edge variation forces the three matching sums into the integral
`A₂` plane. -/
theorem matchingSums_sum_zero (x : TetraEdges) (hx : x.total = 0) :
    let m := x.matchingSums
    m.1 + m.2.1 + m.2.2 = 0 := by
  rcases x with ⟨x12, x13, x14, x23, x24, x34⟩
  simp only [TetraEdges.total, TetraEdges.matchingSums] at hx ⊢
  omega

/-- Every integral `A₂` residual is realized by a zero-total tetrahedral edge
state.  This is the explicit free two-dimensional quotient map used in the
Enterprise-coordinate correspondence. -/
theorem matchingSums_surjective_on_A2
    (m1 m2 m3 : ℤ) (hm : m1 + m2 + m3 = 0) :
    ∃ x : TetraEdges,
      x.total = 0 ∧ x.matchingSums = (m1, m2, m3) := by
  refine ⟨⟨m1, m2, m3, 0, 0, 0⟩, ?_, ?_⟩
  · simp [TetraEdges.total, hm]
  · simp [TetraEdges.matchingSums]

/-- The matching residual is unchanged by adding an edge state whose three
opposite-edge sums all vanish. -/
theorem matchingSums_add_kernel
    (x : TetraEdges) (a b c : ℤ) :
    let y : TetraEdges := ⟨a, b, c, -c, -b, -a⟩
    (TetraEdges.matchingSums
      ⟨x.x12 + y.x12, x.x13 + y.x13, x.x14 + y.x14,
        x.x23 + y.x23, x.x24 + y.x24, x.x34 + y.x34⟩) =
      x.matchingSums := by
  dsimp
  simp only [TetraEdges.matchingSums, Prod.mk.injEq]
  constructor
  · ring
  · constructor <;> ring

end EnterpriseMath.PrecisionPi
