import EnterpriseMath.Geometry.TetrahedralResidualKernel

namespace EnterpriseMath.TetrahedralResidual

/-- Coordinatewise subtraction of edge data. -/
def subEdge (x y : Edge6) : Edge6 := fun i => x i - y i

/-- Opposite-pair sums are additive under subtraction. -/
theorem matchingSums_sub (x y : Edge6) :
    matchingSums (subEdge x y) =
      fun i => matchingSums x i - matchingSums y i := by
  funext i
  fin_cases i <;> simp [matchingSums, subEdge] <;> ring

/-- Total edge weight is additive under subtraction. -/
theorem edgeSum_sub (x y : Edge6) :
    edgeSum (subEdge x y) = edgeSum x - edgeSum y := by
  simp [edgeSum, subEdge]
  ring

/-- Two edge configurations are equivalent when their difference is induced
by an integer zero-sum slice potential. -/
def DeltaEquivalent (x y : Edge6) : Prop :=
  ∃ v : Vertex4, vertexSum v = 0 ∧ delta v = subEdge x y

/-- Equality of opposite-pair sums forces the edge difference into the kernel. -/
theorem matchingSums_sub_eq_zero_of_eq {x y : Edge6}
    (h : matchingSums x = matchingSums y) :
    matchingSums (subEdge x y) = 0 := by
  rw [matchingSums_sub, h]
  funext i
  simp

/-- A zero-sum slice-induced difference preserves all three opposite-pair
sums. -/
theorem matchingSums_eq_of_deltaEquivalent {x y : Edge6}
    (h : DeltaEquivalent x y) : matchingSums x = matchingSums y := by
  rcases h with ⟨v, hv, hdelta⟩
  have hzero : matchingSums (subEdge x y) = 0 := by
    rw [← hdelta, matchingSums_delta, hv]
    rfl
  rw [matchingSums_sub] at hzero
  funext i
  have hi := congrFun hzero i
  simp at hi
  linarith

/-- Exact classification criterion for the tetrahedral residual relation:
two edge configurations differ by an integral zero-sum slice potential iff
(1) their free `A₂` opposite-pair data agree and (2) the remaining kernel
coordinate has even parity. -/
theorem deltaEquivalent_iff_matchingSums_eq_and_even (x y : Edge6) :
    DeltaEquivalent x y ↔
      matchingSums x = matchingSums y ∧
        Even (subEdge x y 0 + subEdge x y 1 + subEdge x y 2) := by
  constructor
  · intro h
    refine ⟨matchingSums_eq_of_deltaEquivalent h, ?_⟩
    exact even_firstThree_of_zeroSum_preimage (subEdge x y) h
  · rintro ⟨hmatching, heven⟩
    exact (kernel_preimage_iff_even_firstThree (subEdge x y)
      (matchingSums_sub_eq_zero_of_eq hmatching)).2 heven

/-- The residual equivalence is reflexive. -/
theorem deltaEquivalent_refl (x : Edge6) : DeltaEquivalent x x := by
  refine ⟨0, ?_, ?_⟩
  · simp [vertexSum]
  · funext i
    fin_cases i <;> simp [delta, subEdge]

/-- The residual equivalence is symmetric. -/
theorem deltaEquivalent_symm {x y : Edge6}
    (h : DeltaEquivalent x y) : DeltaEquivalent y x := by
  rcases h with ⟨v, hv, hdelta⟩
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  refine ⟨fun i => -v i, ?_, ?_⟩
  · change -v 0 + -v 1 + -v 2 + -v 3 = 0
    linarith
  · funext i
    have hi := congrFun hdelta i
    fin_cases i <;> simp [delta, subEdge] at hi ⊢ <;> linarith

/-- The residual equivalence is transitive. -/
theorem deltaEquivalent_trans {x y z : Edge6}
    (hxy : DeltaEquivalent x y) (hyz : DeltaEquivalent y z) :
    DeltaEquivalent x z := by
  rcases hxy with ⟨v, hv, hdeltaV⟩
  rcases hyz with ⟨w, hw, hdeltaW⟩
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  have hw' : w 0 + w 1 + w 2 + w 3 = 0 := by
    simpa [vertexSum] using hw
  refine ⟨fun i => v i + w i, ?_, ?_⟩
  · change
      (v 0 + w 0) + (v 1 + w 1) + (v 2 + w 2) + (v 3 + w 3) = 0
    linarith
  · funext i
    have hvi := congrFun hdeltaV i
    have hwi := congrFun hdeltaW i
    fin_cases i <;> simp [delta, subEdge] at hvi hwi ⊢ <;> linarith

/-- The exact relation packaged as a setoid, suitable for a future quotient
isomorphism with the free `A₂` data plus one parity class. -/
def deltaSetoid : Setoid Edge6 where
  r := DeltaEquivalent
  iseqv := ⟨deltaEquivalent_refl, deltaEquivalent_symm, deltaEquivalent_trans⟩

end EnterpriseMath.TetrahedralResidual
