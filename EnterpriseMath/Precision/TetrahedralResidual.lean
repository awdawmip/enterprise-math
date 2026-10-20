import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralResidual

/-- Integer weights on the four Enterprise-coordinate slice charts. -/
abbrev VertexWeights := Fin 4 → ℤ

/-- Integer weights on the six shared FCC carrier line families. -/
abbrev EdgeWeights := Fin 6 → ℤ

/-- Integer weights on the three opposite-edge pairs of the tetrahedral atlas. -/
abbrev MatchingWeights := Fin 3 → ℤ

/-- Total slice-chart weight. -/
def vertexSum (v : VertexWeights) : ℤ :=
  v 0 + v 1 + v 2 + v 3

/-- Total shared-line-family weight. -/
def edgeSum (x : EdgeWeights) : ℤ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

/--
The vertex-to-edge incidence map for `K₄`.

The edge order is `01, 02, 03, 23, 13, 12`, so opposite pairs are
`(0,3)`, `(1,4)`, and `(2,5)`.
-/
def delta (v : VertexWeights) : EdgeWeights :=
  ![v 0 + v 1,
    v 0 + v 2,
    v 0 + v 3,
    v 2 + v 3,
    v 1 + v 3,
    v 1 + v 2]

/-- The three opposite-edge-pair sums. -/
def matchingSums (x : EdgeWeights) : MatchingWeights :=
  ![x 0 + x 3, x 1 + x 4, x 2 + x 5]

/-- A normal form for an edge vector whose three opposite-pair sums vanish. -/
def kernelEdge (a b c : ℤ) : EdgeWeights :=
  ![a, b, c, -a, -b, -c]

/-- Every vertex weight is counted in exactly three incident edges. -/
theorem edgeSum_delta (v : VertexWeights) :
    edgeSum (delta v) = 3 * vertexSum v := by
  simp [edgeSum, delta, vertexSum]
  ring

/-- Each opposite-edge-pair sum of a vertex-induced edge vector is the total vertex weight. -/
theorem matchingSums_delta (v : VertexWeights) :
    matchingSums (delta v) = ![vertexSum v, vertexSum v, vertexSum v] := by
  funext i
  fin_cases i <;> simp [matchingSums, delta, vertexSum] <;> ring

/-- The sum of the three matching coordinates is the total edge weight. -/
theorem matching_total (x : EdgeWeights) :
    matchingSums x 0 + matchingSums x 1 + matchingSums x 2 = edgeSum x := by
  simp [matchingSums, edgeSum]
  ring

/-- Kernel normal-form vectors have zero total edge weight. -/
theorem edgeSum_kernelEdge (a b c : ℤ) :
    edgeSum (kernelEdge a b c) = 0 := by
  simp [edgeSum, kernelEdge]

/-- Kernel normal-form vectors have all three opposite-pair sums equal to zero. -/
theorem matchingSums_kernelEdge (a b c : ℤ) :
    matchingSums (kernelEdge a b c) = 0 := by
  funext i
  fin_cases i <;> simp [matchingSums, kernelEdge]

/--
The opposite-pair map is onto the integral `A₂` plane: every triple summing to
zero is realized by a zero-sum six-edge vector.
-/
theorem matchingSums_surjective_on_zero_sum
    (m : MatchingWeights) (hm : m 0 + m 1 + m 2 = 0) :
    ∃ x : EdgeWeights, edgeSum x = 0 ∧ matchingSums x = m := by
  refine ⟨![m 0, m 1, m 2, 0, 0, 0], ?_, ?_⟩
  · simpa [edgeSum] using hm
  · funext i
    fin_cases i <;> simp [matchingSums]

/--
An edge vector has vanishing opposite-pair sums exactly when it has the
three-parameter kernel normal form.
-/
theorem matchingSums_eq_zero_iff (x : EdgeWeights) :
    matchingSums x = 0 ↔ x = kernelEdge (x 0) (x 1) (x 2) := by
  constructor
  · intro h
    have h0 := congrFun h (0 : Fin 3)
    have h1 := congrFun h (1 : Fin 3)
    have h2 := congrFun h (2 : Fin 3)
    simp [matchingSums] at h0 h1 h2
    funext i
    fin_cases i <;> simp [kernelEdge] <;> omega
  · rintro rfl
    exact matchingSums_kernelEdge _ _ _

/--
The integral parity obstruction: a zero-sum slice potential lifts
`kernelEdge a b c` exactly when `a+b+c` is even.
-/
theorem exists_zeroSum_delta_eq_kernelEdge_iff_even (a b c : ℤ) :
    (∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge a b c) ↔
      Even (a + b + c) := by
  constructor
  · rintro ⟨v, hv, hdelta⟩
    have h0 : v 0 + v 1 = a := by
      simpa [delta, kernelEdge] using congrFun hdelta (0 : Fin 6)
    have h1 : v 0 + v 2 = b := by
      simpa [delta, kernelEdge] using congrFun hdelta (1 : Fin 6)
    have h2 : v 0 + v 3 = c := by
      simpa [delta, kernelEdge] using congrFun hdelta (2 : Fin 6)
    refine ⟨v 0, ?_⟩
    dsimp [vertexSum] at hv
    omega
  · rintro ⟨s, hs⟩
    let v : VertexWeights := ![s, a - s, b - s, c - s]
    refine ⟨v, ?_, ?_⟩
    · dsimp [v, vertexSum]
      omega
    · funext i
      fin_cases i <;> simp [delta, kernelEdge, v] <;> omega

/-- The basic parity class has no integral zero-sum slice lift. -/
theorem basicParityClass_not_liftable :
    ¬ ∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge 1 0 0 := by
  intro h
  have he : Even (1 : ℤ) := by
    simpa using
      (exists_zeroSum_delta_eq_kernelEdge_iff_even 1 0 0).mp h
  rcases he with ⟨z, hz⟩
  omega

/-- Twice the basic parity class does have an integral zero-sum slice lift. -/
theorem twice_basicParityClass_liftable :
    ∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge 2 0 0 := by
  apply (exists_zeroSum_delta_eq_kernelEdge_iff_even 2 0 0).mpr
  exact ⟨1, by norm_num⟩

end EnterpriseMath.PrecisionPi.TetrahedralResidual
