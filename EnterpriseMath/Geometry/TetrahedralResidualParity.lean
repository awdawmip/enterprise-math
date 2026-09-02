import Mathlib

namespace EnterpriseMath.TetrahedralResidual

/-- Integer weights on the four slice labels of the tetrahedral carrier atlas. -/
abbrev Vertex4 := Fin 4 → ℤ

/-- Integer weights on the six shared line-family labels, ordered as
`01, 02, 03, 12, 13, 23`. -/
abbrev Edge6 := Fin 6 → ℤ

/-- Total slice weight. -/
def vertexSum (v : Vertex4) : ℤ :=
  v 0 + v 1 + v 2 + v 3

/-- Total shared-line-family weight. -/
def edgeSum (x : Edge6) : ℤ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

/-- The vertex-induced edge map on the tetrahedral `K₄` incidence carrier. -/
def delta (v : Vertex4) : Edge6 :=
  ![v 0 + v 1, v 0 + v 2, v 0 + v 3,
    v 1 + v 2, v 1 + v 3, v 2 + v 3]

/-- Every vertex weight contributes to exactly three incident edges. -/
theorem edgeSum_delta (v : Vertex4) :
    edgeSum (delta v) = 3 * vertexSum v := by
  simp [edgeSum, delta, vertexSum]
  ring

/-- The three sums over opposite edge pairs. -/
def matchingSums (x : Edge6) : Fin 3 → ℤ :=
  ![x 0 + x 5, x 1 + x 4, x 2 + x 3]

/-- The three opposite-pair sums add to the total edge weight. -/
theorem matchingSums_total (x : Edge6) :
    matchingSums x 0 + matchingSums x 1 + matchingSums x 2 = edgeSum x := by
  simp [matchingSums, edgeSum]
  ring

/-- On vertex-induced edge data, every opposite-pair sum equals the total
vertex weight. -/
theorem matchingSums_delta (v : Vertex4) :
    matchingSums (delta v) = fun _ => vertexSum v := by
  funext i
  fin_cases i <;> simp [matchingSums, delta, vertexSum] <;> ring

/-- A normal form for the kernel of the opposite-pair-sum map. -/
def kernelEdge (a b c : ℤ) : Edge6 :=
  ![a, b, c, -c, -b, -a]

/-- The kernel normal form has zero total weight. -/
theorem edgeSum_kernelEdge (a b c : ℤ) :
    edgeSum (kernelEdge a b c) = 0 := by
  simp [edgeSum, kernelEdge]

/-- The kernel normal form has vanishing opposite-pair sums. -/
theorem matchingSums_kernelEdge (a b c : ℤ) :
    matchingSums (kernelEdge a b c) = 0 := by
  funext i
  fin_cases i
  · change a + -a = 0
    ring
  · change b + -b = 0
    ring
  · change c + -c = 0
    ring

/-- Existence of an integer zero-sum slice potential inducing a kernel edge. -/
def HasZeroSumPreimage (a b c : ℤ) : Prop :=
  ∃ v : Vertex4, vertexSum v = 0 ∧ delta v = kernelEdge a b c

/-- The exact parity obstruction: a kernel edge has an integral zero-sum
slice potential if and only if `a+b+c` is even. -/
theorem hasZeroSumPreimage_iff_even (a b c : ℤ) :
    HasZeroSumPreimage a b c ↔ Even (a + b + c) := by
  constructor
  · rintro ⟨v, hv, hdelta⟩
    have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
      simpa [vertexSum] using hv
    have h01 := congrFun hdelta (0 : Fin 6)
    have h02 := congrFun hdelta (1 : Fin 6)
    have h03 := congrFun hdelta (2 : Fin 6)
    simp [delta, kernelEdge] at h01 h02 h03
    refine ⟨v 0, ?_⟩
    omega
  · rintro ⟨t, ht⟩
    let v : Vertex4 := ![t, a - t, b - t, c - t]
    refine ⟨v, ?_, ?_⟩
    · simp [v, vertexSum]
      linarith
    · funext i
      fin_cases i <;> simp [v, delta, kernelEdge] <;> linarith

/-- A primitive parity class is not induced by any integer zero-sum slice
potential. -/
theorem primitiveParity_noPreimage :
    ¬ HasZeroSumPreimage 1 0 0 := by
  intro h
  rcases (hasZeroSumPreimage_iff_even 1 0 0).1 h with ⟨t, ht⟩
  omega

/-- Twice the primitive parity class is induced by an integer zero-sum slice
potential. -/
theorem doublePrimitiveParity_hasPreimage :
    HasZeroSumPreimage 2 0 0 := by
  rw [hasZeroSumPreimage_iff_even]
  exact ⟨1, by norm_num⟩

/-- An explicit witness for the doubled primitive parity class. -/
theorem doublePrimitiveParity_explicit :
    vertexSum (![1, 1, -1, -1] : Vertex4) = 0 ∧
      delta (![1, 1, -1, -1] : Vertex4) = kernelEdge 2 0 0 := by
  native_decide

end EnterpriseMath.TetrahedralResidual
