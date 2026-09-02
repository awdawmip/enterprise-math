import EnterpriseMath.Geometry.FCCResidualBridge
import EnterpriseMath.Geometry.FCCSliceRotation
import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.FCCResidualRotation

open FCCResidualBridge FCCSliceIncidence FCCSliceRotation TetrahedralResidual

/-- Induced permutations in the residual edge order. -/
def rotate3Edge : Edge → Edge :=
  fun e => lineToEdge (rotate3Line (edgeToLine e))

def rotate3EdgeInv : Edge → Edge := ![1, 5, 3, 4, 2, 0]

def rotate4Edge : Edge → Edge :=
  fun e => lineToEdge (rotate4Line (edgeToLine e))

def rotate4EdgeInv : Edge → Edge := ![2, 4, 3, 5, 1, 0]

theorem rotate3Edge_table : ∀ e : Edge,
    rotate3Edge e = (![5, 0, 4, 2, 3, 1] : Edge → Edge) e := by
  native_decide

theorem rotate4Edge_table : ∀ e : Edge,
    rotate4Edge e = (![5, 4, 0, 2, 1, 3] : Edge → Edge) e := by
  native_decide

theorem rotate3Edge_inverse_left : ∀ e : Edge,
    rotate3EdgeInv (rotate3Edge e) = e := by
  native_decide

theorem rotate3Edge_inverse_right : ∀ e : Edge,
    rotate3Edge (rotate3EdgeInv e) = e := by
  native_decide

theorem rotate4Edge_inverse_left : ∀ e : Edge,
    rotate4EdgeInv (rotate4Edge e) = e := by
  native_decide

theorem rotate4Edge_inverse_right : ∀ e : Edge,
    rotate4Edge (rotate4EdgeInv e) = e := by
  native_decide

/-- Push-forward of edge and vertex weights under the two rotations. -/
def rotate3EdgeWeights (x : EdgeWeights) : EdgeWeights :=
  fun e => x (rotate3EdgeInv e)

def rotate4EdgeWeights (x : EdgeWeights) : EdgeWeights :=
  fun e => x (rotate4EdgeInv e)

def rotate3VertexWeights (v : VertexWeights) : VertexWeights :=
  fun s => v (rotate3SliceInv s)

def rotate4VertexWeights (v : VertexWeights) : VertexWeights :=
  fun s => v (rotate4SliceInv s)

/-- Total weights are rotation invariant. -/
theorem rotate3_vertexSum (v : VertexWeights) :
    vertexSum (rotate3VertexWeights v) = vertexSum v := by
  simp [vertexSum, rotate3VertexWeights, rotate3SliceInv]
  ring

theorem rotate4_vertexSum (v : VertexWeights) :
    vertexSum (rotate4VertexWeights v) = vertexSum v := by
  simp [vertexSum, rotate4VertexWeights, rotate4SliceInv]
  ring

theorem rotate3_edgeSum (x : EdgeWeights) :
    edgeSum (rotate3EdgeWeights x) = edgeSum x := by
  simp [edgeSum, rotate3EdgeWeights, rotate3EdgeInv]
  ring

theorem rotate4_edgeSum (x : EdgeWeights) :
    edgeSum (rotate4EdgeWeights x) = edgeSum x := by
  simp [edgeSum, rotate4EdgeWeights, rotate4EdgeInv]
  ring

/-- The vertex-to-edge incidence map commutes with both carrier rotations. -/
theorem rotate3_delta_equivariant (v : VertexWeights) :
    rotate3EdgeWeights (delta v) = delta (rotate3VertexWeights v) := by
  funext e
  fin_cases e <;>
    simp [rotate3EdgeWeights, rotate3EdgeInv, delta,
      rotate3VertexWeights, rotate3SliceInv] <;> ring

theorem rotate4_delta_equivariant (v : VertexWeights) :
    rotate4EdgeWeights (delta v) = delta (rotate4VertexWeights v) := by
  funext e
  fin_cases e <;>
    simp [rotate4EdgeWeights, rotate4EdgeInv, delta,
      rotate4VertexWeights, rotate4SliceInv] <;> ring

/-- On the free residual, `R₃` cyclically permutes the three matching coordinates. -/
theorem rotate3_matchingSums (x : EdgeWeights) :
    matchingSums (rotate3EdgeWeights x) =
      ![matchingSums x 1, matchingSums x 2, matchingSums x 0] := by
  funext i
  fin_cases i <;>
    simp [matchingSums, rotate3EdgeWeights, rotate3EdgeInv] <;> ring

/-- On the free residual, `R₄` acts by the indicated matching reflection. -/
theorem rotate4_matchingSums (x : EdgeWeights) :
    matchingSums (rotate4EdgeWeights x) =
      ![matchingSums x 2, matchingSums x 1, matchingSums x 0] := by
  funext i
  fin_cases i <;>
    simp [matchingSums, rotate4EdgeWeights, rotate4EdgeInv] <;> ring

/-- Kernel normal forms are transported to kernel normal forms. -/
theorem rotate3_kernelEdge (a b c : ℤ) :
    rotate3EdgeWeights (kernelEdge a b c) = kernelEdge b (-c) (-a) := by
  funext e
  fin_cases e <;> simp [rotate3EdgeWeights, rotate3EdgeInv, kernelEdge]

theorem rotate4_kernelEdge (a b c : ℤ) :
    rotate4EdgeWeights (kernelEdge a b c) = kernelEdge c (-b) (-a) := by
  funext e
  fin_cases e <;> simp [rotate4EdgeWeights, rotate4EdgeInv, kernelEdge]

/-- The intrinsic `C₂` parity class is invariant under both rotations. -/
theorem rotate3_even_parity_iff (a b c : ℤ) :
    Even (b - c - a) ↔ Even (a + b + c) := by
  constructor
  · rintro ⟨k, hk⟩
    refine ⟨k + a + c, ?_⟩
    omega
  · rintro ⟨k, hk⟩
    refine ⟨k - a - c, ?_⟩
    omega

theorem rotate4_even_parity_iff (a b c : ℤ) :
    Even (c - b - a) ↔ Even (a + b + c) := by
  constructor
  · rintro ⟨k, hk⟩
    refine ⟨k + a + b, ?_⟩
    omega
  · rintro ⟨k, hk⟩
    refine ⟨k - a - b, ?_⟩
    omega

/-- Liftability of a kernel residual is rotation invariant. -/
theorem rotate3_kernel_liftable_iff (a b c : ℤ) :
    (∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = kernelEdge b (-c) (-a)) ↔
      ∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = kernelEdge a b c := by
  rw [exists_zeroSum_delta_eq_kernelEdge_iff_even,
    exists_zeroSum_delta_eq_kernelEdge_iff_even]
  exact rotate3_even_parity_iff a b c

theorem rotate4_kernel_liftable_iff (a b c : ℤ) :
    (∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = kernelEdge c (-b) (-a)) ↔
      ∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = kernelEdge a b c := by
  rw [exists_zeroSum_delta_eq_kernelEdge_iff_even,
    exists_zeroSum_delta_eq_kernelEdge_iff_even]
  exact rotate4_even_parity_iff a b c

end EnterpriseMath.PrecisionPi.FCCResidualRotation
