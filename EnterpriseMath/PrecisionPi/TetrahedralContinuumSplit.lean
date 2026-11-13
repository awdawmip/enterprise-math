import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralContinuumSplit

/-- Real-valued four-slice data. -/
structure VertexDataR where
  v1 : ℝ
  v2 : ℝ
  v3 : ℝ
  v4 : ℝ
  deriving DecidableEq, Repr

/-- Real-valued six-line-family data. -/
structure EdgeDataR where
  e12 : ℝ
  e13 : ℝ
  e14 : ℝ
  e23 : ℝ
  e24 : ℝ
  e34 : ℝ
  deriving DecidableEq, Repr

/-- Coordinatewise addition of real edge data. -/
def edgeAddR (x y : EdgeDataR) : EdgeDataR :=
  ⟨x.e12 + y.e12, x.e13 + y.e13, x.e14 + y.e14,
   x.e23 + y.e23, x.e24 + y.e24, x.e34 + y.e34⟩

/-- Coordinatewise subtraction of real edge data. -/
def edgeSubR (x y : EdgeDataR) : EdgeDataR :=
  ⟨x.e12 - y.e12, x.e13 - y.e13, x.e14 - y.e14,
   x.e23 - y.e23, x.e24 - y.e24, x.e34 - y.e34⟩

/-- Real slice-to-line incidence map. -/
def deltaR (v : VertexDataR) : EdgeDataR :=
  ⟨v.v1 + v.v2, v.v1 + v.v3, v.v1 + v.v4,
   v.v2 + v.v3, v.v2 + v.v4, v.v3 + v.v4⟩

/-- Total real slice weight. -/
def vertexSumR (v : VertexDataR) : ℝ :=
  v.v1 + v.v2 + v.v3 + v.v4

/-- Total real edge weight. -/
def edgeSumR (x : EdgeDataR) : ℝ :=
  x.e12 + x.e13 + x.e14 + x.e23 + x.e24 + x.e34

/-- Orthogonal-looking continuous residual obtained by averaging each opposite edge pair. -/
def matchingResidual (x : EdgeDataR) : EdgeDataR :=
  ⟨(x.e12 + x.e34) / 2,
   (x.e13 + x.e24) / 2,
   (x.e14 + x.e23) / 2,
   (x.e14 + x.e23) / 2,
   (x.e13 + x.e24) / 2,
   (x.e12 + x.e34) / 2⟩

/-- The continuous residual is constant on every opposite edge pair. -/
theorem matchingResidual_opposite_pairs (x : EdgeDataR) :
    (matchingResidual x).e12 = (matchingResidual x).e34 ∧
    (matchingResidual x).e13 = (matchingResidual x).e24 ∧
    (matchingResidual x).e14 = (matchingResidual x).e23 := by
  exact ⟨rfl, rfl, rfl⟩

/-- Removing the averaged residual leaves an antisymmetric opposite-pair pattern. -/
theorem kernelPart_opposite_sums_zero (x : EdgeDataR) :
    let y := edgeSubR x (matchingResidual x)
    y.e12 + y.e34 = 0 ∧ y.e13 + y.e24 = 0 ∧ y.e14 + y.e23 = 0 := by
  dsimp
  constructor <;> constructor <;>
    simp [edgeSubR, matchingResidual] <;> ring

/-- Continuous witness for an antisymmetric opposite-pair pattern. -/
def continuousWitness (x : EdgeDataR) : VertexDataR :=
  let y := edgeSubR x (matchingResidual x)
  let k := (y.e12 + y.e13 + y.e14) / 2
  ⟨k, y.e12 - k, y.e13 - k, y.e14 - k⟩

/-- The continuous witness is automatically zero-sum. -/
theorem vertexSumR_continuousWitness (x : EdgeDataR) :
    vertexSumR (continuousWitness x) = 0 := by
  simp [vertexSumR, continuousWitness]
  ring

/-- Every real edge state decomposes into a zero-sum slice-induced part and the averaged
opposite-pair residual. -/
theorem deltaR_continuousWitness (x : EdgeDataR) :
    deltaR (continuousWitness x) = edgeSubR x (matchingResidual x) := by
  have h := kernelPart_opposite_sums_zero x
  dsimp at h
  rcases h with ⟨h1, h2, h3⟩
  ext <;>
    simp [deltaR, continuousWitness, edgeSubR, matchingResidual] <;>
    linarith

/-- Explicit continuum splitting. -/
theorem continuum_decomposition (x : EdgeDataR) :
    x = edgeAddR (deltaR (continuousWitness x)) (matchingResidual x) := by
  rw [deltaR_continuousWitness]
  ext <;> simp [edgeAddR, edgeSubR]

/-- Averaging opposite pairs preserves total edge weight. -/
theorem edgeSumR_matchingResidual (x : EdgeDataR) :
    edgeSumR (matchingResidual x) = edgeSumR x := by
  simp [edgeSumR, matchingResidual]
  ring

/-- Hence a balanced real state has a balanced two-dimensional residual. -/
theorem matchingResidual_preserves_zero_sum
    {x : EdgeDataR} (hx : edgeSumR x = 0) :
    edgeSumR (matchingResidual x) = 0 := by
  rw [edgeSumR_matchingResidual, hx]

/-- Over the reals there is no parity obstruction: every antisymmetric pattern has a
zero-sum slice potential, because division by two is available. -/
theorem real_kernel_has_zeroSum_potential
    (a b c : ℝ) :
    ∃ v : VertexDataR,
      vertexSumR v = 0 ∧
      deltaR v = ⟨a, b, c, -c, -b, -a⟩ := by
  let k : ℝ := (a + b + c) / 2
  refine ⟨⟨k, a - k, b - k, c - k⟩, ?_, ?_⟩
  · simp [vertexSumR, k]
    ring
  · ext <;> simp [deltaR, k] <;> ring

end EnterpriseMath.PrecisionPi.TetrahedralContinuumSplit
