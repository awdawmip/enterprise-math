import EnterpriseMath.PrecisionPi.TetrahedralMatching
import EnterpriseMath.PrecisionPi.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi

/-- Four integral vertex potentials of the tetrahedral slice atlas. -/
structure TetraVertices where
  v1 : ℤ
  v2 : ℤ
  v3 : ℤ
  v4 : ℤ
  deriving DecidableEq

/-- Total vertex potential. -/
def TetraVertices.total (v : TetraVertices) : ℤ :=
  v.v1 + v.v2 + v.v3 + v.v4

/-- Pairwise vertex sums on the six tetrahedral edges. -/
def TetraVertices.toEdges (v : TetraVertices) : TetraEdges :=
  ⟨v.v1 + v.v2, v.v1 + v.v3, v.v1 + v.v4,
    v.v2 + v.v3, v.v2 + v.v4, v.v3 + v.v4⟩

/-- An edge state is induced by an integral zero-sum vertex potential. -/
def TetraEdges.vertexInduced (x : TetraEdges) : Prop :=
  ∃ v : TetraVertices, v.total = 0 ∧ v.toEdges = x

/-- Every zero-sum vertex potential has vanishing opposite-edge matching sums. -/
theorem vertexEdges_matchingSums_zero
    (v : TetraVertices) (hv : v.total = 0) :
    v.toEdges.matchingSums = (0, 0, 0) := by
  rcases v with ⟨v1, v2, v3, v4⟩
  simp only [TetraVertices.total, TetraVertices.toEdges,
    TetraEdges.matchingSums] at hv ⊢
  simp only [Prod.mk.injEq]
  constructor
  · omega
  · constructor <;> omega

/-- Exact kernel theorem for the tetrahedral residual invariant.

An integral edge state is induced by a zero-sum vertex potential iff its three
opposite-edge matching sums vanish and the sum of its three incident coordinates
at vertex `1` is even.  This is the explicit `A₂ + C₂` classification at the
kernel level. -/
theorem vertexInduced_iff_matchingSums_zero_and_even (x : TetraEdges) :
    x.vertexInduced ↔
      x.matchingSums = (0, 0, 0) ∧ intEven (x.x12 + x.x13 + x.x14) := by
  unfold TetraEdges.vertexInduced
  constructor
  · rintro ⟨v, hv, rfl⟩
    constructor
    · exact vertexEdges_matchingSums_zero v hv
    · rcases v with ⟨v1, v2, v3, v4⟩
      simp only [TetraVertices.total] at hv
      unfold intEven
      refine ⟨v1, ?_⟩
      simp only [TetraVertices.toEdges]
      omega
  · rintro ⟨hm, heven⟩
    have hm1 : x.x12 + x.x34 = 0 := by
      simpa [TetraEdges.matchingSums] using congrArg Prod.fst hm
    have hm2 : x.x13 + x.x24 = 0 := by
      simpa [TetraEdges.matchingSums] using
        congrArg (fun p : ℤ × ℤ × ℤ => p.2.1) hm
    have hm3 : x.x14 + x.x23 = 0 := by
      simpa [TetraEdges.matchingSums] using
        congrArg (fun p : ℤ × ℤ × ℤ => p.2.2) hm
    have hlift :=
      (tetrahedralVertexLift_iff_intEven x.x12 x.x13 x.x14).2 heven
    rcases hlift with
      ⟨v1, v2, v3, v4, hsum, h12, h13, h14, h23, h24, h34⟩
    refine ⟨⟨v1, v2, v3, v4⟩, ?_, ?_⟩
    · simpa [TetraVertices.total] using hsum
    · apply TetraEdges.ext <;> simp [TetraVertices.toEdges] <;> omega

/-- The primitive opposite-edge difference represents the nonzero torsion class. -/
def tetrahedralTorsionEdge : TetraEdges :=
  ⟨1, 0, 0, 0, 0, -1⟩

/-- The primitive torsion edge has zero free `A₂` residual. -/
theorem tetrahedralTorsionEdge_matchingSums_zero :
    tetrahedralTorsionEdge.matchingSums = (0, 0, 0) := by
  norm_num [tetrahedralTorsionEdge, TetraEdges.matchingSums]

/-- The primitive torsion edge is not vertex-induced over the integers. -/
theorem tetrahedralTorsionEdge_not_vertexInduced :
    ¬ tetrahedralTorsionEdge.vertexInduced := by
  intro h
  have heven :=
    (vertexInduced_iff_matchingSums_zero_and_even tetrahedralTorsionEdge).1 h |>.2
  rcases heven with ⟨t, ht⟩
  norm_num [tetrahedralTorsionEdge] at ht
  omega

/-- Doubling the primitive torsion edge makes it vertex-induced. -/
theorem tetrahedralTorsionEdge_double_vertexInduced :
    (⟨2, 0, 0, 0, 0, -2⟩ : TetraEdges).vertexInduced := by
  apply (vertexInduced_iff_matchingSums_zero_and_even
    (⟨2, 0, 0, 0, 0, -2⟩ : TetraEdges)).2
  constructor
  · norm_num [TetraEdges.matchingSums]
  · refine ⟨1, ?_⟩
    norm_num [intEven]

end EnterpriseMath.PrecisionPi
