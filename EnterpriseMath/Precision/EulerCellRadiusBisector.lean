import Mathlib

namespace EnterpriseMath.Precision.EulerCellRadiusBisector

section

variable {A : Type*} [CommRing A]
variable (R r : A)

/-- The internally generated six-state rotor `G = 1 + R`. -/
def sixRotor : A := 1 + R

/-- The Cell-radius-normalized gate rotor `H = r (2 + R)`. -/
def gateRotor : A := r * (2 + R)

/-- The normalized chiral difference `J = r (R - R^2)`. -/
def chiral : A := r * (R - R ^ 2)

/-- The C3 relation makes `1 + R` a square root of `R`. -/
theorem sixRotor_sq (hR : R ^ 2 + R + 1 = 0) :
    sixRotor R ^ 2 = R := by
  unfold sixRotor
  calc
    (1 + R) ^ 2 = R + (R ^ 2 + R + 1) := by ring
    _ = R := by rw [hR, add_zero]

/-- The same square root has cube `-1`, so it has order dividing six. -/
theorem sixRotor_cube (hR : R ^ 2 + R + 1 = 0) :
    sixRotor R ^ 3 = -1 := by
  unfold sixRotor
  calc
    (1 + R) ^ 3 = -1 + (R + 2) * (R ^ 2 + R + 1) := by ring
    _ = -1 := by rw [hR]; ring

/-- The generated rotor closes after six steps. -/
theorem sixRotor_sixth (hR : R ^ 2 + R + 1 = 0) :
    sixRotor R ^ 6 = 1 := by
  calc
    sixRotor R ^ 6 = (sixRotor R ^ 3) ^ 2 := by ring
    _ = (-1) ^ 2 := by rw [sixRotor_cube (R := R) hR]
    _ = 1 := by ring

/-- The unnormalized adjacent-state sum has squared scale three. -/
theorem adjacent_sum_sq (hR : R ^ 2 + R + 1 = 0) :
    (2 + R) ^ 2 = 3 * (1 + R) := by
  calc
    (2 + R) ^ 2 = 3 * (1 + R) + (R ^ 2 + R + 1) := by ring
    _ = 3 * (1 + R) := by rw [hR, add_zero]

/-- Its cube is three times the chiral difference. -/
theorem adjacent_sum_cube (hR : R ^ 2 + R + 1 = 0) :
    (2 + R) ^ 3 = 3 * (R - R ^ 2) := by
  calc
    (2 + R) ^ 3 =
        3 * (R - R ^ 2) + (R + 8) * (R ^ 2 + R + 1) := by ring
    _ = 3 * (R - R ^ 2) := by rw [hR]; ring

/-- The Cell-radius condition `3 r^2 = 1` makes the gate rotor square to `G`. -/
theorem gateRotor_sq
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    gateRotor R r ^ 2 = sixRotor R := by
  unfold gateRotor sixRotor
  calc
    (r * (2 + R)) ^ 2 = r ^ 2 * (2 + R) ^ 2 := by ring
    _ = r ^ 2 * (3 * (1 + R)) := by
      rw [adjacent_sum_sq (R := R) hR]
    _ = (3 * r ^ 2) * (1 + R) := by ring
    _ = 1 + R := by rw [hr]; ring

/-- The cube of the gate rotor is the normalized chiral operator. -/
theorem gateRotor_cube
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    gateRotor R r ^ 3 = chiral R r := by
  unfold gateRotor chiral
  calc
    (r * (2 + R)) ^ 3 = r ^ 3 * (2 + R) ^ 3 := by ring
    _ = r ^ 3 * (3 * (R - R ^ 2)) := by
      rw [adjacent_sum_cube (R := R) hR]
    _ = (3 * r ^ 2) * r * (R - R ^ 2) := by ring
    _ = r * (R - R ^ 2) := by rw [hr]; ring

/-- The unnormalized chiral difference squares to `-3`. -/
theorem chiral_difference_sq (hR : R ^ 2 + R + 1 = 0) :
    (R - R ^ 2) ^ 2 = -3 := by
  calc
    (R - R ^ 2) ^ 2 =
        -3 + (R ^ 2 - 3 * R + 3) * (R ^ 2 + R + 1) := by ring
    _ = -3 := by rw [hR]; ring

/-- Cell-radius normalization turns the chiral difference into a complex structure. -/
theorem chiral_sq
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    chiral R r ^ 2 = -1 := by
  unfold chiral
  calc
    (r * (R - R ^ 2)) ^ 2 = r ^ 2 * (R - R ^ 2) ^ 2 := by ring
    _ = r ^ 2 * (-3) := by rw [chiral_difference_sq (R := R) hR]
    _ = -(3 * r ^ 2) := by ring
    _ = -1 := by rw [hr]

/-- Six gate steps give endpoint reversal. -/
theorem gateRotor_sixth
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    gateRotor R r ^ 6 = -1 := by
  calc
    gateRotor R r ^ 6 = (gateRotor R r ^ 3) ^ 2 := by ring
    _ = chiral R r ^ 2 := by rw [gateRotor_cube (R := R) (r := r) hR hr]
    _ = -1 := chiral_sq (R := R) (r := r) hR hr

/-- Twelve gate steps close the full rotation character. -/
theorem gateRotor_twelfth
    (hR : R ^ 2 + R + 1 = 0)
    (hr : 3 * r ^ 2 = 1) :
    gateRotor R r ^ 12 = 1 := by
  calc
    gateRotor R r ^ 12 = (gateRotor R r ^ 6) ^ 2 := by ring
    _ = (-1) ^ 2 := by rw [gateRotor_sixth (R := R) (r := r) hR hr]
    _ = 1 := by ring

end

section SegmentSpinor

variable {A : Type*} [CommRing A]
variable (a b J : A)

/-- The two-component segment numerator `a + bJ`. -/
def segmentNumerator : A := a + b * J

/-- Its Pythagorean norm square. -/
def segmentNormSq : A := a ^ 2 + b ^ 2

/-- The numerator of the doubled projective rotation character. -/
def characterNumerator : A := (a ^ 2 - b ^ 2) + 2 * a * b * J

/-- The numerator of the reflected/conjugate character. -/
def characterConjugateNumerator : A :=
  (a ^ 2 - b ^ 2) - 2 * a * b * J

/-- A Pythagorean segment is a spinor: its square is the rotation-character numerator. -/
theorem segment_spinor_sq (hJ : J ^ 2 = -1) :
    segmentNumerator a b J ^ 2 = characterNumerator a b J := by
  unfold segmentNumerator characterNumerator
  calc
    (a + b * J) ^ 2 =
        (a ^ 2 - b ^ 2) + 2 * a * b * J + b ^ 2 * (J ^ 2 + 1) := by
      ring
    _ = (a ^ 2 - b ^ 2) + 2 * a * b * J := by
      rw [hJ]
      ring

/-- Character times reflected character is the square of the segment norm. -/
theorem character_norm_sq (hJ : J ^ 2 = -1) :
    characterNumerator a b J * characterConjugateNumerator a b J =
      segmentNormSq a b ^ 2 := by
  unfold characterNumerator characterConjugateNumerator segmentNormSq
  calc
    ((a ^ 2 - b ^ 2) + 2 * a * b * J) *
        ((a ^ 2 - b ^ 2) - 2 * a * b * J) =
      (a ^ 2 + b ^ 2) ^ 2 - 4 * a ^ 2 * b ^ 2 * (J ^ 2 + 1) := by
        ring
    _ = (a ^ 2 + b ^ 2) ^ 2 := by
      rw [hJ]
      ring

/-- Adding identity to the character exposes the underlying segment direction. -/
theorem norm_plus_character :
    segmentNormSq a b + characterNumerator a b J =
      2 * a * segmentNumerator a b J := by
  unfold segmentNormSq characterNumerator segmentNumerator
  ring

/-- The scalar bisector normalization is exactly `4 a^2`. -/
theorem character_bisector_scale :
    2 * segmentNormSq a b + characterNumerator a b J +
        characterConjugateNumerator a b J = 4 * a ^ 2 := by
  unfold segmentNormSq characterNumerator characterConjugateNumerator
  ring

/-- The balanced component segment has quarter-turn character numerator `2J`. -/
theorem balanced_character_numerator :
    characterNumerator (1 : A) 1 J = 2 * J := by
  unfold characterNumerator
  ring

/-- The second boundary component has reversal character numerator `-1`. -/
theorem second_axis_character_numerator :
    characterNumerator (0 : A) 1 J = -1 := by
  unfold characterNumerator
  ring

end SegmentSpinor

end EnterpriseMath.Precision.EulerCellRadiusBisector
