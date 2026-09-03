import EnterpriseMath.Geometry.TetrahedralResidualClassification
import Mathlib.Data.ZMod.Basic

namespace EnterpriseMath.TetrahedralResidual

/-- The sum of the three edge coordinates incident with the distinguished
slice vertex.  Modulo two this is independent of the chosen lift inside a
fixed matching fiber. -/
def firstThreeSum (x : Edge6) : ℤ :=
  x 0 + x 1 + x 2

/-- Coordinatewise subtraction is compatible with the distinguished residual
sum. -/
theorem firstThreeSum_sub (x y : Edge6) :
    firstThreeSum (subEdge x y) = firstThreeSum x - firstThreeSum y := by
  simp [firstThreeSum, subEdge]
  ring

/-- The surviving order-two residual coordinate. -/
def parityBit (x : Edge6) : ZMod 2 :=
  (firstThreeSum x : ZMod 2)

/-- Equality of parity bits is exactly evenness of the residual difference. -/
theorem parityBit_eq_iff_even_sub (x y : Edge6) :
    parityBit x = parityBit y ↔ Even (firstThreeSum (subEdge x y)) := by
  change
    ((firstThreeSum x : ZMod 2) = (firstThreeSum y : ZMod 2)) ↔
      Even (firstThreeSum (subEdge x y))
  rw [ZMod.intCast_eq_intCast_iff_dvd_sub, firstThreeSum_sub,
    even_iff_two_dvd]
  constructor
  · intro h
    rw [← neg_sub, Int.dvd_neg]
    exact h
  · intro h
    rw [← neg_sub, Int.dvd_neg]
    exact h

/-- Free opposite-pair coordinates together with the residual `C₂` bit. -/
abbrev ResidualCoordinate := (Fin 3 → ℤ) × ZMod 2

/-- Complete coordinate readout before imposing the zero-total condition. -/
def residualCoordinates (x : Edge6) : ResidualCoordinate :=
  (matchingSums x, parityBit x)

/-- The matching coordinates and the parity bit form a complete invariant for
the tetrahedral slice-potential relation. -/
theorem residualCoordinates_eq_iff_deltaEquivalent (x y : Edge6) :
    residualCoordinates x = residualCoordinates y ↔ DeltaEquivalent x y := by
  constructor
  · intro h
    have hm : matchingSums x = matchingSums y := congrArg Prod.fst h
    have hp : parityBit x = parityBit y := congrArg Prod.snd h
    refine (deltaEquivalent_iff_matchingSums_eq_and_even x y).2 ⟨hm, ?_⟩
    have he := (parityBit_eq_iff_even_sub x y).1 hp
    simpa [firstThreeSum] using he
  · intro h
    apply Prod.ext
    · exact matchingSums_eq_of_deltaEquivalent h
    · apply (parityBit_eq_iff_even_sub x y).2
      have he := (deltaEquivalent_iff_matchingSums_eq_and_even x y).1 h
      simpa [firstThreeSum] using he.2

/-- The tetrahedral endpoint-sum incidence map is injective over the integers. -/
theorem delta_injective : Function.Injective delta := by
  intro v w h
  have h0 := congrFun h (0 : Fin 6)
  have h1 := congrFun h (1 : Fin 6)
  have h2 := congrFun h (2 : Fin 6)
  have h3 := congrFun h (3 : Fin 6)
  have h4 := congrFun h (4 : Fin 6)
  have h5 := congrFun h (5 : Fin 6)
  change v 0 + v 1 = w 0 + w 1 at h0
  change v 0 + v 2 = w 0 + w 2 at h1
  change v 0 + v 3 = w 0 + w 3 at h2
  change v 1 + v 2 = w 1 + w 2 at h3
  change v 1 + v 3 = w 1 + w 3 at h4
  change v 2 + v 3 = w 2 + w 3 at h5
  have hv0 : v 0 = w 0 := by omega
  have hv1 : v 1 = w 1 := by omega
  have hv2 : v 2 = w 2 := by omega
  have hv3 : v 3 = w 3 := by omega
  funext i
  fin_cases i
  · exact hv0
  · exact hv1
  · exact hv2
  · exact hv3

/-- Quotient by zero-sum slice potentials. -/
abbrev ResidualQuotient := Quotient deltaSetoid

/-- The complete residual coordinates descend to the quotient. -/
def quotientCoordinates : ResidualQuotient → ResidualCoordinate :=
  Quotient.lift residualCoordinates (by
    intro x y hxy
    exact (residualCoordinates_eq_iff_deltaEquivalent x y).2 hxy)

@[simp] theorem quotientCoordinates_mk (x : Edge6) :
    quotientCoordinates (Quotient.mk deltaSetoid x) = residualCoordinates x := rfl

/-- Complete residual coordinates separate quotient classes. -/
theorem quotientCoordinates_injective : Function.Injective quotientCoordinates := by
  intro q r
  refine Quotient.inductionOn₂ q r ?_
  intro x y h
  apply Quotient.sound
  exact (residualCoordinates_eq_iff_deltaEquivalent x y).1 h

/-- A canonical edge representative of arbitrary free-plus-parity data. -/
def coordinateRepresentative (c : ResidualCoordinate) : Edge6 :=
  ![(c.2.val : ℤ), 0, 0, c.1 2, c.1 1,
    c.1 0 - (c.2.val : ℤ)]

/-- The representative realizes the prescribed opposite-pair coordinates. -/
theorem matchingSums_coordinateRepresentative (c : ResidualCoordinate) :
    matchingSums (coordinateRepresentative c) = c.1 := by
  funext i
  fin_cases i
  · change (c.2.val : ℤ) + (c.1 0 - (c.2.val : ℤ)) = c.1 0
    ring
  · change (0 : ℤ) + c.1 1 = c.1 1
    ring
  · change (0 : ℤ) + c.1 2 = c.1 2
    ring

/-- The representative realizes the prescribed parity bit. -/
theorem parityBit_coordinateRepresentative (c : ResidualCoordinate) :
    parityBit (coordinateRepresentative c) = c.2 := by
  change (((c.2.val : ℤ) : ZMod 2)) = c.2
  rw [Int.cast_natCast, ZMod.natCast_zmod_val]

/-- The canonical representative is a right inverse to the coordinate map. -/
theorem residualCoordinates_coordinateRepresentative (c : ResidualCoordinate) :
    residualCoordinates (coordinateRepresentative c) = c := by
  apply Prod.ext
  · exact matchingSums_coordinateRepresentative c
  · exact parityBit_coordinateRepresentative c

/-- Every free-plus-parity coordinate is realized by an integral edge state. -/
theorem residualCoordinates_surjective :
    Function.Surjective residualCoordinates := by
  intro c
  exact ⟨coordinateRepresentative c,
    residualCoordinates_coordinateRepresentative c⟩

/-- Every coordinate is realized by a quotient class. -/
theorem quotientCoordinates_surjective :
    Function.Surjective quotientCoordinates := by
  intro c
  refine ⟨Quotient.mk deltaSetoid (coordinateRepresentative c), ?_⟩
  exact residualCoordinates_coordinateRepresentative c

/-- Explicit classification of the full integral tetrahedral residual quotient
as three free matching coordinates together with one `C₂` coordinate. -/
noncomputable def quotientCoordinatesEquiv :
    ResidualQuotient ≃ ResidualCoordinate :=
  Equiv.ofBijective quotientCoordinates
    ⟨quotientCoordinates_injective, quotientCoordinates_surjective⟩

/-- On the zero-total edge slice, the three free matching coordinates lie in
the integral `A₂` plane. -/
theorem matchingCoordinates_sum_eq_edgeSum (x : Edge6) :
    (residualCoordinates x).1 0 +
        (residualCoordinates x).1 1 +
        (residualCoordinates x).1 2 = edgeSum x := by
  simpa [residualCoordinates] using matchingSums_total x

/-- Zero total weight forces the free residual coordinates to sum to zero. -/
theorem matchingCoordinates_mem_A2 {x : Edge6} (hx : edgeSum x = 0) :
    (residualCoordinates x).1 0 +
        (residualCoordinates x).1 1 +
        (residualCoordinates x).1 2 = 0 := by
  rw [matchingCoordinates_sum_eq_edgeSum, hx]

end EnterpriseMath.TetrahedralResidual
