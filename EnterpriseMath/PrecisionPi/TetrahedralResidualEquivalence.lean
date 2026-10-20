import EnterpriseMath.PrecisionPi.TetrahedralInvariant

namespace EnterpriseMath.PrecisionPi

/-- Coordinatewise difference of two tetrahedral edge states. -/
def TetraEdges.edgeSub (x y : TetraEdges) : TetraEdges :=
  ⟨x.x12 - y.x12, x.x13 - y.x13, x.x14 - y.x14,
    x.x23 - y.x23, x.x24 - y.x24, x.x34 - y.x34⟩

/-- Sum of the three edge coordinates incident at slice vertex `1`. -/
def TetraEdges.vertexOneSum (x : TetraEdges) : ℤ :=
  x.x12 + x.x13 + x.x14

/-- Two six-line states carry the same tetrahedral residual when their free
opposite-edge matching coordinates agree and their remaining parity difference
is even. -/
def sameTetrahedralResidual (x y : TetraEdges) : Prop :=
  x.matchingSums = y.matchingSums ∧
    intEven (x.vertexOneSum - y.vertexOneSum)

/-- Matching sums of a difference vanish exactly when the original matching
coordinates agree. -/
theorem edgeSub_matchingSums_zero_iff (x y : TetraEdges) :
    (x.edgeSub y).matchingSums = (0, 0, 0) ↔
      x.matchingSums = y.matchingSums := by
  rcases x with ⟨x12, x13, x14, x23, x24, x34⟩
  rcases y with ⟨y12, y13, y14, y23, y24, y34⟩
  simp only [TetraEdges.edgeSub, TetraEdges.matchingSums, Prod.mk.injEq]
  omega

/-- The parity coordinate of an edge difference is the difference of the two
parity coordinates. -/
theorem edgeSub_vertexOneSum (x y : TetraEdges) :
    (x.edgeSub y).vertexOneSum = x.vertexOneSum - y.vertexOneSum := by
  simp [TetraEdges.edgeSub, TetraEdges.vertexOneSum]
  ring

/-- Complete residual classification: two six-line states differ by an
integral zero-sum slice potential iff they have identical `A₂` matching
coordinates and identical `C₂` parity. -/
theorem edgeSub_vertexInduced_iff_sameResidual (x y : TetraEdges) :
    (x.edgeSub y).vertexInduced ↔ sameTetrahedralResidual x y := by
  rw [vertexInduced_iff_matchingSums_zero_and_even]
  change
    ((x.edgeSub y).matchingSums = (0, 0, 0) ∧
      intEven ((x.edgeSub y).vertexOneSum)) ↔
      sameTetrahedralResidual x y
  rw [edgeSub_matchingSums_zero_iff, edgeSub_vertexOneSum]
  rfl

/-- Equality of residual coordinates is reflexive. -/
theorem sameTetrahedralResidual_refl (x : TetraEdges) :
    sameTetrahedralResidual x x := by
  constructor
  · rfl
  · refine ⟨0, ?_⟩
    simp [TetraEdges.vertexOneSum]

/-- Equality of residual coordinates is symmetric. -/
theorem sameTetrahedralResidual_symm {x y : TetraEdges}
    (h : sameTetrahedralResidual x y) :
    sameTetrahedralResidual y x := by
  rcases h with ⟨hmatch, t, ht⟩
  constructor
  · exact hmatch.symm
  · refine ⟨-t, ?_⟩
    omega

/-- Equality of residual coordinates is transitive. -/
theorem sameTetrahedralResidual_trans {x y z : TetraEdges}
    (hxy : sameTetrahedralResidual x y)
    (hyz : sameTetrahedralResidual y z) :
    sameTetrahedralResidual x z := by
  rcases hxy with ⟨hxyMatch, t, ht⟩
  rcases hyz with ⟨hyzMatch, u, hu⟩
  constructor
  · exact hxyMatch.trans hyzMatch
  · refine ⟨t + u, ?_⟩
    omega

/-- The primitive torsion state has the same free `A₂` coordinate as zero but
not the same complete residual class. -/
theorem tetrahedralTorsionEdge_free_zero_but_residual_nonzero :
    tetrahedralTorsionEdge.matchingSums = (0, 0, 0) ∧
      ¬ sameTetrahedralResidual tetrahedralTorsionEdge
        (⟨0, 0, 0, 0, 0, 0⟩ : TetraEdges) := by
  constructor
  · exact tetrahedralTorsionEdge_matchingSums_zero
  · intro h
    have heven := h.2
    rcases heven with ⟨t, ht⟩
    norm_num [tetrahedralTorsionEdge, TetraEdges.vertexOneSum] at ht
    omega

end EnterpriseMath.PrecisionPi
