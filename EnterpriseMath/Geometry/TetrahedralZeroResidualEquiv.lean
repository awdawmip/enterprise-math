import EnterpriseMath.Geometry.TetrahedralResidualCoordinates

namespace EnterpriseMath.TetrahedralResidual

/-- Integral edge states with zero total variation. -/
abbrev ZeroEdge := {x : Edge6 // edgeSum x = 0}

/-- The free integral `A₂` residual plane. -/
abbrev A2Coordinate :=
  {m : Fin 3 → ℤ // m 0 + m 1 + m 2 = 0}

/-- Zero-total residual data: a free `A₂` coordinate and one `C₂` bit. -/
abbrev ZeroResidualCoordinate := A2Coordinate × ZMod 2

/-- Restriction of the tetrahedral slice-potential relation to zero-total edge
states. -/
def zeroDeltaSetoid : Setoid ZeroEdge where
  r x y := DeltaEquivalent x.1 y.1
  iseqv := ⟨
    fun x => deltaEquivalent_refl x.1,
    fun _ _ h => deltaEquivalent_symm h,
    fun _ _ _ hxy hyz => deltaEquivalent_trans hxy hyz⟩

/-- The zero-total quotient appearing in the Enterprise-coordinate geometric
correspondence. -/
abbrev ZeroResidualQuotient := Quotient zeroDeltaSetoid

/-- Complete zero-total residual coordinates. -/
def zeroResidualCoordinates (x : ZeroEdge) : ZeroResidualCoordinate :=
  (⟨matchingSums x.1, by
      simpa [x.2] using matchingSums_total x.1⟩,
    parityBit x.1)

/-- The `A₂ × C₂` coordinate is a complete invariant on zero-total states. -/
theorem zeroResidualCoordinates_eq_iff_deltaEquivalent
    (x y : ZeroEdge) :
    zeroResidualCoordinates x = zeroResidualCoordinates y ↔
      DeltaEquivalent x.1 y.1 := by
  constructor
  · intro h
    have hm : matchingSums x.1 = matchingSums y.1 := by
      simpa [zeroResidualCoordinates] using
        congrArg (fun c : ZeroResidualCoordinate => c.1.1) h
    have hp : parityBit x.1 = parityBit y.1 := by
      simpa [zeroResidualCoordinates] using
        congrArg (fun c : ZeroResidualCoordinate => c.2) h
    exact (residualCoordinates_eq_iff_deltaEquivalent x.1 y.1).1
      (Prod.ext hm hp)
  · intro h
    have hfull : residualCoordinates x.1 = residualCoordinates y.1 :=
      (residualCoordinates_eq_iff_deltaEquivalent x.1 y.1).2 h
    apply Prod.ext
    · apply Subtype.ext
      exact congrArg Prod.fst hfull
    · exact congrArg Prod.snd hfull

/-- The complete zero-total coordinate descends to the quotient. -/
def zeroQuotientCoordinates :
    ZeroResidualQuotient → ZeroResidualCoordinate :=
  Quotient.lift zeroResidualCoordinates (by
    intro x y hxy
    exact (zeroResidualCoordinates_eq_iff_deltaEquivalent x y).2 hxy)

@[simp] theorem zeroQuotientCoordinates_mk (x : ZeroEdge) :
    zeroQuotientCoordinates (Quotient.mk zeroDeltaSetoid x) =
      zeroResidualCoordinates x := rfl

/-- The descended coordinates separate zero-total quotient classes. -/
theorem zeroQuotientCoordinates_injective :
    Function.Injective zeroQuotientCoordinates := by
  intro q r
  refine Quotient.inductionOn₂ q r ?_
  intro x y h
  apply Quotient.sound
  exact (zeroResidualCoordinates_eq_iff_deltaEquivalent x y).1 h

/-- Canonical zero-total representative of an `A₂ × C₂` coordinate. -/
def zeroCoordinateRepresentative
    (c : ZeroResidualCoordinate) : ZeroEdge :=
  ⟨coordinateRepresentative (c.1.1, c.2), by
    have htotal :=
      matchingSums_total (coordinateRepresentative (c.1.1, c.2))
    rw [matchingSums_coordinateRepresentative] at htotal
    linarith [c.1.2]⟩

/-- The canonical zero-total representative realizes the prescribed
coordinate. -/
theorem zeroResidualCoordinates_zeroCoordinateRepresentative
    (c : ZeroResidualCoordinate) :
    zeroResidualCoordinates (zeroCoordinateRepresentative c) = c := by
  apply Prod.ext
  · apply Subtype.ext
    exact matchingSums_coordinateRepresentative (c.1.1, c.2)
  · exact parityBit_coordinateRepresentative (c.1.1, c.2)

/-- Every `A₂ × C₂` coordinate is represented by a zero-total edge state. -/
theorem zeroResidualCoordinates_surjective :
    Function.Surjective zeroResidualCoordinates := by
  intro c
  exact ⟨zeroCoordinateRepresentative c,
    zeroResidualCoordinates_zeroCoordinateRepresentative c⟩

/-- Every `A₂ × C₂` coordinate is represented by a zero-total quotient
class. -/
theorem zeroQuotientCoordinates_surjective :
    Function.Surjective zeroQuotientCoordinates := by
  intro c
  refine ⟨Quotient.mk zeroDeltaSetoid (zeroCoordinateRepresentative c), ?_⟩
  exact zeroResidualCoordinates_zeroCoordinateRepresentative c

/-- Exact zero-total residual classification:
`E₀ / δ(V₀) ≃ A₂(ℤ) × C₂`. -/
noncomputable def zeroQuotientCoordinatesEquiv :
    ZeroResidualQuotient ≃ ZeroResidualCoordinate :=
  Equiv.ofBijective zeroQuotientCoordinates
    ⟨zeroQuotientCoordinates_injective,
      zeroQuotientCoordinates_surjective⟩

/-- Build an `A₂` coordinate from two free integers. -/
def a2OfPair (p : ℤ × ℤ) : A2Coordinate :=
  ⟨![p.1, p.2, -p.1 - p.2], by
    simp
    ring⟩

/-- Read the first two coordinates of the `A₂` plane. -/
def a2ToPair (m : A2Coordinate) : ℤ × ℤ :=
  (m.1 0, m.1 1)

/-- The integral `A₂` plane is explicitly equivalent to `ℤ²`. -/
def a2PairEquiv : A2Coordinate ≃ ℤ × ℤ where
  toFun := a2ToPair
  invFun := a2OfPair
  left_inv := by
    intro m
    apply Subtype.ext
    funext i
    fin_cases i
    · rfl
    · rfl
    · have hm := m.2
      change -m.1 0 - m.1 1 = m.1 2
      linarith
  right_inv := by
    rintro ⟨a, b⟩
    rfl

/-- Fully explicit abelian classification:
`E₀ / δ(V₀) ≃ ℤ² × C₂`. -/
noncomputable def zeroQuotientZ2C2Equiv :
    ZeroResidualQuotient ≃ (ℤ × ℤ) × ZMod 2 :=
  zeroQuotientCoordinatesEquiv.trans
    (Equiv.prodCongr a2PairEquiv (Equiv.refl (ZMod 2)))

end EnterpriseMath.TetrahedralResidual
