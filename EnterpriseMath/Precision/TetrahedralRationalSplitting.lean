import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralRationalSplitting

abbrev QVertex := Fin 4 → ℚ
abbrev QEdge := Fin 6 → ℚ

/-- Rational extensions of the vertex and edge total-weight maps. -/
def vertexSum (v : QVertex) : ℚ := v 0 + v 1 + v 2 + v 3

def edgeSum (x : QEdge) : ℚ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

/-- Rational extension of the tetrahedral vertex-to-edge incidence map. -/
def delta (v : QVertex) : QEdge :=
  ![v 0 + v 1,
    v 0 + v 2,
    v 0 + v 3,
    v 2 + v 3,
    v 1 + v 3,
    v 1 + v 2]

/-- Orthogonal-style projection onto the plane constant on opposite edge pairs. -/
def pairAverage (x : QEdge) : QEdge :=
  ![(x 0 + x 3) / 2,
    (x 1 + x 4) / 2,
    (x 2 + x 5) / 2,
    (x 0 + x 3) / 2,
    (x 1 + x 4) / 2,
    (x 2 + x 5) / 2]

/-- The complementary opposite-pair antisymmetric residual. -/
def antiResidual (x : QEdge) : QEdge := fun e => x e - pairAverage x e

/-- Potential recovering an opposite-pair antisymmetric residual. -/
def kernelPotential (r : QEdge) : QVertex :=
  let s := (r 0 + r 1 + r 2) / 2
  ![s, r 0 - s, r 1 - s, r 2 - s]

/-- Pair averaging is constant on each opposite edge pair. -/
theorem pairAverage_opposite_constant (x : QEdge) :
    pairAverage x 0 = pairAverage x 3 ∧
    pairAverage x 1 = pairAverage x 4 ∧
    pairAverage x 2 = pairAverage x 5 := by
  simp [pairAverage]

/-- Pair averaging preserves total edge weight. -/
theorem edgeSum_pairAverage (x : QEdge) :
    edgeSum (pairAverage x) = edgeSum x := by
  simp [edgeSum, pairAverage]
  ring

/-- Hence a zero-sum edge vector has a zero-sum projected component. -/
theorem pairAverage_zero_sum
    (x : QEdge) (hx : edgeSum x = 0) : edgeSum (pairAverage x) = 0 := by
  rw [edgeSum_pairAverage, hx]

/-- The anti-residual has zero total edge weight. -/
theorem antiResidual_zero_sum (x : QEdge) :
    edgeSum (antiResidual x) = 0 := by
  simp [edgeSum, antiResidual, pairAverage]
  ring

/-- The anti-residual has vanishing opposite-pair sums. -/
theorem antiResidual_opposite_antisymmetric (x : QEdge) :
    antiResidual x 0 + antiResidual x 3 = 0 ∧
    antiResidual x 1 + antiResidual x 4 = 0 ∧
    antiResidual x 2 + antiResidual x 5 = 0 := by
  simp [antiResidual, pairAverage]
  constructor <;> ring

/-- The recovering potential is always a zero-sum four-slice potential. -/
theorem kernelPotential_zero_sum (r : QEdge) :
    vertexSum (kernelPotential r) = 0 := by
  simp [vertexSum, kernelPotential]
  ring

/-- Every pair-antisymmetric edge vector is recovered by its rational potential. -/
theorem delta_kernelPotential_of_antisymmetric
    (r : QEdge)
    (hr0 : r 0 + r 3 = 0)
    (hr1 : r 1 + r 4 = 0)
    (hr2 : r 2 + r 5 = 0) :
    delta (kernelPotential r) = r := by
  funext e
  fin_cases e <;>
    simp [delta, kernelPotential] <;> linarith

/--
Canonical rational splitting of every six-edge state into a zero-sum
slice-induced component and an opposite-pair-average component.
-/
theorem rational_splitting (x : QEdge) :
    x = delta (kernelPotential (antiResidual x)) + pairAverage x := by
  have hanti := antiResidual_opposite_antisymmetric x
  have hdelta :
      delta (kernelPotential (antiResidual x)) = antiResidual x :=
    delta_kernelPotential_of_antisymmetric (antiResidual x)
      hanti.1 hanti.2.1 hanti.2.2
  rw [hdelta]
  funext e
  simp [antiResidual]

/-- The pair-average projection is idempotent. -/
theorem pairAverage_idempotent (x : QEdge) :
    pairAverage (pairAverage x) = pairAverage x := by
  funext e
  fin_cases e <;> simp [pairAverage] <;> ring

/-- The anti-residual projection kills the pair-average plane. -/
theorem antiResidual_pairAverage (x : QEdge) :
    antiResidual (pairAverage x) = 0 := by
  funext e
  rw [antiResidual, pairAverage_idempotent]
  simp

/-- The pair-average projection kills the anti-residual component. -/
theorem pairAverage_antiResidual (x : QEdge) :
    pairAverage (antiResidual x) = 0 := by
  funext e
  fin_cases e <;> simp [pairAverage, antiResidual] <;> ring

/-- Rational image of the basic integral parity class. -/
def basicParityEdge : QEdge := ![1, 0, 0, -1, 0, 0]

/-- The basic parity class has zero pair-average component. -/
theorem basicParity_pairAverage : pairAverage basicParityEdge = 0 := by
  funext e
  fin_cases e <;> norm_num [pairAverage, basicParityEdge]

/--
Its unique rational slice potential necessarily uses half-integers.  This is
the explicit mechanism by which tensoring with `ℚ` removes the integral `C₂`
obstruction.
-/
theorem basicParity_kernelPotential :
    kernelPotential basicParityEdge = ![1 / 2, 1 / 2, -1 / 2, -1 / 2] := by
  funext s
  fin_cases s <;> norm_num [kernelPotential, basicParityEdge]

/-- The displayed half-integral potential recovers the basic parity edge. -/
theorem basicParity_delta_recovered :
    delta (![1 / 2, 1 / 2, -1 / 2, -1 / 2] : QVertex) = basicParityEdge := by
  funext e
  fin_cases e <;> norm_num [delta, basicParityEdge]

end EnterpriseMath.PrecisionPi.TetrahedralRationalSplitting
