import EnterpriseMath.Precision.EulerCellRadiusBisector
import EnterpriseMath.Precision.EulerCayleyBridge

namespace EnterpriseMath.Precision.EulerCellPolygonPi

open EulerCellRadiusBisector

section RotorCoordinates

variable {A : Type*} [CommRing A]

/-- Relative to the complex-structure element `J = r(R-R^2)`, the internally
    generated six-state rotor has coordinates `(1/2, 3r/2)`, written without
    division. -/
theorem sixRotor_chiral_coordinates
    (R r : A)
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    2 * sixRotor R = 1 + 3 * r * chiral R r := by
  unfold sixRotor chiral
  calc
    2 * (1 + R) =
        1 + 3 * r * (r * (R - R ^ 2)) +
          (R ^ 2 + R + 1) + (1 - 3 * r ^ 2) * (R - R ^ 2) := by
            ring
    _ = 1 + 3 * r * (r * (R - R ^ 2)) := by
      rw [hR, hr]
      ring

/-- The actual twelve-phase gate rotor has coordinates `(3r/2, 1/2)` in the
    same `(1,J)` basis, again written without division. -/
theorem gateRotor_chiral_coordinates
    (R r : A)
    (hR : R ^ 2 + R + 1 = 0) :
    2 * gateRotor R r = 3 * r + chiral R r := by
  unfold gateRotor chiral
  calc
    2 * (r * (2 + R)) =
        3 * r + r * (R - R ^ 2) + r * (R ^ 2 + R + 1) := by
          ring
    _ = 3 * r + r * (R - R ^ 2) := by
      rw [hR]
      ring

end RotorCoordinates

section PolygonArea

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Cayley half-step / tangent half-side coordinate. -/
def tangentParameter (c s : F) : F :=
  s / (1 + c)

/-- Area of the regular `N`-gon inscribed in the unit character circle when
    consecutive unit states have oriented determinant `s`. -/
def inscribedArea (N : ℕ) (s : F) : F :=
  (N : F) * s / 2

/-- Area of the regular `N`-gon circumscribed about the unit character circle
    when the tangent half-side is `t`. -/
def circumscribedArea (N : ℕ) (t : F) : F :=
  (N : F) * t

/-- The Cayley parameter times `1+c` is the skew coordinate. -/
omit [LinearOrder F] [IsStrictOrderedRing F] in
theorem tangentParameter_mul_one_add
    {c s : F}
    (hc : 1 + c ≠ 0) :
    tangentParameter c s * (1 + c) = s := by
  unfold tangentParameter
  field_simp [hc]

/-- On the unit conic, the same parameter is the tangent intersection height
    `(1-c)/s`.  This is kept in cross-multiplied form. -/
theorem tangentParameter_mul_skew
    {c s : F}
    (hunit : c ^ 2 + s ^ 2 = 1)
    (hc : 1 + c ≠ 0) :
    tangentParameter c s * s = 1 - c := by
  unfold tangentParameter
  field_simp [hc]
  nlinarith [hunit]

/-- Exact finite polygon gap: outer area minus inner area equals the inner area
    times the square of the Cayley half-step. -/
theorem polygon_area_gap
    (N : ℕ)
    {c s : F}
    (hunit : c ^ 2 + s ^ 2 = 1)
    (hc : 1 + c ≠ 0) :
    circumscribedArea N (tangentParameter c s) - inscribedArea N s =
      inscribedArea N s * tangentParameter c s ^ 2 := by
  let t : F := tangentParameter c s
  have ht1 : t * (1 + c) = s := by
    simpa [t] using tangentParameter_mul_one_add (c := c) (s := s) hc
  have ht2 : t * s = 1 - c := by
    simpa [t] using tangentParameter_mul_skew (c := c) (s := s) hunit hc
  have htwo : 2 * t = s * (1 + t ^ 2) := by
    calc
      2 * t = t * (1 + c) + t * (1 - c) := by ring
      _ = s + t * (t * s) := by rw [ht1, ← ht2]
      _ = s * (1 + t ^ 2) := by ring
  change circumscribedArea N t - inscribedArea N s =
    inscribedArea N s * t ^ 2
  unfold circumscribedArea inscribedArea
  calc
    (N : F) * t - (N : F) * s / 2 =
        ((N : F) / 2) * (2 * t - s) := by ring
    _ = ((N : F) / 2) * (s * t ^ 2) := by rw [htwo]; ring
    _ = ((N : F) * s / 2) * t ^ 2 := by ring

/-- Algebraic form of the sharp width-refinement ratio.  If `u` is the new
    Cayley half-step, then the next width is `(1-u^4)/4` times the old width. -/
theorem polygon_width_refinement_identity
    (A u : F)
    (hden : 1 - u ^ 2 ≠ 0) :
    (A * (1 + u ^ 2) / (1 - u ^ 2)) * u ^ 2 =
      (A * (2 * u / (1 - u ^ 2)) ^ 2) * ((1 - u ^ 4) / 4) := by
  field_simp [hden]
  ring

/-- A nonzero positive new half-step makes the refinement factor strictly less
    than one quarter. -/
theorem polygon_width_factor_lt_quarter
    {u : F}
    (hu : 0 < u) :
    (1 - u ^ 4) / 4 < 1 / 4 := by
  have hu4 : 0 < u ^ 4 := pow_pos hu 4
  nlinarith

/-- The normalized inscribed area of the twelve-phase Cell/gate polygon is
    exactly three. -/
theorem c12_inscribed_area_exact :
    inscribedArea (F := F) 12 (1 / 2) = 3 := by
  unfold inscribedArea
  norm_num

/-- With the current Cell radius relation `3r^2=1`, the physical C12
    dodecagon has exact area one. -/
theorem physical_c12_dodecagon_area_one
    (r : F)
    (hr : 3 * r ^ 2 = 1) :
    r ^ 2 * inscribedArea (F := F) 12 (1 / 2) = 1 := by
  rw [c12_inscribed_area_exact]
  nlinarith

/-- The first C12 Cayley half-step is `2-3r`. -/
theorem c12_tangent_parameter
    (r : F)
    (hr : 3 * r ^ 2 = 1)
    (hrpos : 0 < r) :
    tangentParameter (3 * r / 2) (1 / 2) = 2 - 3 * r := by
  have hden : 2 + 3 * r ≠ 0 := by positivity
  unfold tangentParameter
  field_simp [hden]
  nlinarith [hr]

/-- The physical outer tangent dodecagon has area `8-12r`, i.e.
    `8-4*sqrt(3)` when `r=1/sqrt(3)`. -/
omit [LinearOrder F] [IsStrictOrderedRing F] in
theorem physical_c12_outer_area
    (r : F)
    (hr : 3 * r ^ 2 = 1) :
    r ^ 2 * (12 * (2 - 3 * r)) = 8 - 12 * r := by
  calc
    r ^ 2 * (12 * (2 - 3 * r)) =
        8 * (3 * r ^ 2) - 12 * r * (3 * r ^ 2) := by ring
    _ = 8 - 12 * r := by rw [hr]; ring

end PolygonArea

end EnterpriseMath.Precision.EulerCellPolygonPi
