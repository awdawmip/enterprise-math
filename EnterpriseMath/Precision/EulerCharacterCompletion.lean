import EnterpriseMath.Precision.EulerCellPolygonPi

namespace EnterpriseMath.Precision.EulerCharacterCompletion

section QuadraticCharacterNorm

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- General symmetric quadratic form in the `(1,J)` character coordinates. -/
def quadraticForm (a b c x y : F) : F :=
  a * x ^ 2 + 2 * b * x * y + c * y ^ 2

/-- Multiplication by the quarter-turn structure sends `(x,y)` to `(-y,x)`. -/
def quarterTurn (x y : F) : F × F :=
  (-y, x)

/-- A quadratic form invariant under the quarter turn and normalized at the
    identity is uniquely the Euclidean character form `x²+y²`. -/
theorem normalized_quarterTurn_invariant_unique
    (a b c : F)
    (hinv : ∀ x y : F,
      quadraticForm a b c (-y) x = quadraticForm a b c x y)
    (hnorm : quadraticForm a b c 1 0 = 1) :
    a = 1 ∧ b = 0 ∧ c = 1 := by
  have h10 := hinv (1 : F) 0
  have h11 := hinv (1 : F) 1
  have hn := hnorm
  simp [quadraticForm] at h10 h11 hn
  constructor
  · exact hn
  constructor
  · nlinarith [h11]
  · nlinarith [h10, hn]

end QuadraticCharacterNorm

section CharacterMultiplication

variable {A : Type*} [CommRing A]

/-- Squared norm in the normalized character coordinates. -/
def characterNormSq (x y : A) : A :=
  x ^ 2 + y ^ 2

/-- Coordinate multiplication for `(x+yJ)(u+vJ)`, with `J²=-1`. -/
def characterMul (x y u v : A) : A × A :=
  (x * u - y * v, x * v + y * u)

/-- The normalized character norm is multiplicative. -/
theorem characterNormSq_mul
    (x y u v : A) :
    characterNormSq (x * u - y * v) (x * v + y * u) =
      characterNormSq x y * characterNormSq u v := by
  unfold characterNormSq
  ring

end CharacterMultiplication

section MeanRenormalization

variable {F : Type*} [Field F]

/-- Current inner polygon area in root coordinates. -/
def lowerBefore (scale x y : F) : F :=
  scale * x * y

/-- Current outer polygon area in root coordinates. -/
def upperBefore (scale x y : F) : F :=
  scale * y / x

/-- Next inner polygon area after doubling the number of sides. -/
def lowerAfter (scale y : F) : F :=
  scale * y

/-- Next outer polygon area after doubling the number of sides. -/
def upperAfter (scale x y : F) : F :=
  2 * scale * y / (1 + x)

/-- The old inner area equals the new inner area times the new longitudinal
    coordinate.  Iterating this identity gives the Cell-rooted Viète product. -/
theorem lowerAfter_mul_longitudinal
    (scale x y : F) :
    lowerAfter scale y * x = lowerBefore scale x y := by
  unfold lowerAfter lowerBefore
  ring

/-- Polygon doubling updates the lower area by a geometric mean. -/
theorem lowerAfter_sq_eq_lowerBefore_mul_upperBefore
    (scale x y : F)
    (hx : x ≠ 0) :
    lowerAfter scale y ^ 2 =
      lowerBefore scale x y * upperBefore scale x y := by
  unfold lowerAfter lowerBefore upperBefore
  field_simp [hx]

/-- Polygon doubling updates the upper area by the harmonic mean of the new
    lower area and the old upper area, written without an outer division. -/
theorem upperAfter_harmonic_identity
    (scale x y : F)
    (hx : x ≠ 0)
    (hxp : 1 + x ≠ 0) :
    upperAfter scale x y *
        (lowerAfter scale y + upperBefore scale x y) =
      2 * lowerAfter scale y * upperBefore scale x y := by
  unfold upperAfter lowerAfter upperBefore
  field_simp [hx, hxp]

end MeanRenormalization

section PhaseRefinement

variable {F : Type*} [Field F] [CharZero F]

/-- Refining `(index,N)` to `(2*index,2*N)` preserves its rational phase. -/
theorem phase_fraction_refinement
    (index period : F)
    (hperiod : period ≠ 0) :
    (2 * index) / (2 * period) = index / period := by
  have htwo : (2 : F) ≠ 0 := by norm_num
  field_simp [hperiod, htwo]

end PhaseRefinement

end EnterpriseMath.Precision.EulerCharacterCompletion
