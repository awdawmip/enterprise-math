import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralRationalSplittingChecked

abbrev QVertex := Fin 4 → ℚ
abbrev QEdge := Fin 6 → ℚ

def vertexSum (v : QVertex) : ℚ := v 0 + v 1 + v 2 + v 3

def edgeSum (x : QEdge) : ℚ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

def delta (v : QVertex) : QEdge :=
  ![v 0 + v 1,
    v 0 + v 2,
    v 0 + v 3,
    v 2 + v 3,
    v 1 + v 3,
    v 1 + v 2]

def pairAverage (x : QEdge) : QEdge :=
  ![(x 0 + x 3) / 2,
    (x 1 + x 4) / 2,
    (x 2 + x 5) / 2,
    (x 0 + x 3) / 2,
    (x 1 + x 4) / 2,
    (x 2 + x 5) / 2]

def antiResidual (x : QEdge) : QEdge := fun e => x e - pairAverage x e

def kernelPotential (r : QEdge) : QVertex :=
  let s := (r 0 + r 1 + r 2) / 2
  ![s, r 0 - s, r 1 - s, r 2 - s]

theorem pairAverage_opposite_constant (x : QEdge) :
    pairAverage x 0 = pairAverage x 3 ∧
    pairAverage x 1 = pairAverage x 4 ∧
    pairAverage x 2 = pairAverage x 5 := by
  simp [pairAverage]

theorem edgeSum_pairAverage (x : QEdge) :
    edgeSum (pairAverage x) = edgeSum x := by
  simp [edgeSum, pairAverage]
  ring

theorem pairAverage_zero_sum
    (x : QEdge) (hx : edgeSum x = 0) : edgeSum (pairAverage x) = 0 := by
  rw [edgeSum_pairAverage, hx]

theorem antiResidual_zero_sum (x : QEdge) :
    edgeSum (antiResidual x) = 0 := by
  simp [edgeSum, antiResidual, pairAverage]
  ring

theorem antiResidual_opposite_antisymmetric (x : QEdge) :
    antiResidual x 0 + antiResidual x 3 = 0 ∧
    antiResidual x 1 + antiResidual x 4 = 0 ∧
    antiResidual x 2 + antiResidual x 5 = 0 := by
  constructor
  · simp [antiResidual, pairAverage]
    ring
  · constructor
    · simp [antiResidual, pairAverage]
      ring
    · simp [antiResidual, pairAverage]
      ring

theorem kernelPotential_zero_sum (r : QEdge) :
    vertexSum (kernelPotential r) = 0 := by
  simp [vertexSum, kernelPotential]
  ring

theorem delta_kernelPotential_of_antisymmetric
    (r : QEdge)
    (hr0 : r 0 + r 3 = 0)
    (hr1 : r 1 + r 4 = 0)
    (hr2 : r 2 + r 5 = 0) :
    delta (kernelPotential r) = r := by
  funext e
  fin_cases e <;>
    simp [delta, kernelPotential] <;> linarith

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

theorem pairAverage_idempotent (x : QEdge) :
    pairAverage (pairAverage x) = pairAverage x := by
  funext e
  fin_cases e <;> simp [pairAverage]

theorem antiResidual_pairAverage (x : QEdge) :
    antiResidual (pairAverage x) = 0 := by
  funext e
  simp [antiResidual, pairAverage_idempotent]

theorem pairAverage_antiResidual (x : QEdge) :
    pairAverage (antiResidual x) = 0 := by
  funext e
  fin_cases e <;> simp [pairAverage, antiResidual] <;> ring

def basicParityEdge : QEdge := ![1, 0, 0, -1, 0, 0]

theorem basicParity_pairAverage : pairAverage basicParityEdge = 0 := by
  native_decide

theorem basicParity_kernelPotential :
    kernelPotential basicParityEdge = ![1 / 2, 1 / 2, -1 / 2, -1 / 2] := by
  native_decide

theorem basicParity_delta_recovered :
    delta (![1 / 2, 1 / 2, -1 / 2, -1 / 2] : QVertex) = basicParityEdge := by
  native_decide

end EnterpriseMath.PrecisionPi.TetrahedralRationalSplittingChecked
