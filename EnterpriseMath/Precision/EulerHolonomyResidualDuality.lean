import EnterpriseMath.Precision.EulerC12RootTorsorFlatness

namespace EnterpriseMath.Precision.EulerHolonomyResidualDuality

open EnterpriseMath.Precision.EulerC12RootTorsorFlatness

@[ext]
structure VertexValues where
  a : Bool
  b : Bool
  c : Bool
  d : Bool
  deriving DecidableEq, Fintype

@[ext]
structure AffineResidual where
  p : Bool
  q : Bool
  e : Bool
  deriving DecidableEq, Fintype

/-- Evaluate the affine residual `f(x,y)=e+p*x+q*y` on
    `A=(0,0), B=(1,0), C=(0,1), D=(1,1)`. -/
def residualValues (r : AffineResidual) : VertexValues :=
  ⟨r.e,
   Bool.xor r.e r.p,
   Bool.xor r.e r.q,
   Bool.xor (Bool.xor r.e r.p) r.q⟩

/-- Recover affine coordinates from an even four-value vector. -/
def residualFromValues (v : VertexValues) : AffineResidual :=
  ⟨Bool.xor v.a v.b, Bool.xor v.a v.c, v.a⟩

/-- The face opposite each vertex supplies its value.  The stored holonomy
    code is `(ABC, ABD, ACD)` and `BCD` is their xor. -/
def holonomyValues (h : HolonomyCode) : VertexValues :=
  let hBCD := Bool.xor (Bool.xor h.abc h.abd) h.acd
  ⟨hBCD, h.acd, h.abd, h.abc⟩

/-- Explicit bridge from the three graph-holonomy bits to endpoint-residual
    affine coordinates. -/
def holonomyToResidual (h : HolonomyCode) : AffineResidual :=
  residualFromValues (holonomyValues h)

/-- Inverse bridge: faces `ABC, ABD, ACD` are opposite `D, C, B`. -/
def residualToHolonomy (r : AffineResidual) : HolonomyCode :=
  let v := residualValues r
  ⟨v.d, v.c, v.b⟩

def edgeToResidual (e : EdgeBits) : AffineResidual :=
  holonomyToResidual (holonomyCode e)

def zeroResidual : AffineResidual := ⟨false, false, false⟩
def torsionResidual : AffineResidual := ⟨false, false, true⟩
def allFaceFlipCode : HolonomyCode := ⟨true, true, true⟩

def residualXor (x y : AffineResidual) : AffineResidual :=
  ⟨Bool.xor x.p y.p, Bool.xor x.q y.q, Bool.xor x.e y.e⟩

def addTorsion (r : AffineResidual) : AffineResidual :=
  residualXor r torsionResidual

def complementValues (v : VertexValues) : VertexValues :=
  ⟨!v.a, !v.b, !v.c, !v.d⟩

def bitNat (b : Bool) : ℕ := if b then 1 else 0

def supportCard (r : AffineResidual) : ℕ :=
  let v := residualValues r
  bitNat v.a + bitNat v.b + bitNat v.c + bitNat v.d

/-- The holonomy and endpoint-residual coordinate systems are exact mutual
    inverses. -/
theorem holonomy_residual_left_inverse : ∀ h : HolonomyCode,
    residualToHolonomy (holonomyToResidual h) = h := by
  native_decide

theorem holonomy_residual_right_inverse : ∀ r : AffineResidual,
    holonomyToResidual (residualToHolonomy r) = r := by
  native_decide

/-- Evaluation identifies affine residuals with all even-parity functions on
    the four tetrahedral vertices. -/
theorem affine_values_have_even_parity : ∀ r : AffineResidual,
    Bool.xor
      (Bool.xor (residualValues r).a (residualValues r).b)
      (Bool.xor (residualValues r).c (residualValues r).d) = false := by
  native_decide

theorem residual_values_roundtrip : ∀ r : AffineResidual,
    residualFromValues (residualValues r) = r := by
  native_decide

theorem holonomy_values_agree : ∀ h : HolonomyCode,
    residualValues (holonomyToResidual h) = holonomyValues h := by
  native_decide

/-- The endpoint residual obtained from face holonomy is a complete gauge
    invariant on the K4 one-skeleton. -/
theorem endpoint_residual_classifies_gauge_orbits : ∀ x y : EdgeBits,
    GaugeEquivalent x y ↔ edgeToResidual x = edgeToResidual y := by
  native_decide

/-- The unique all-face-flip class maps to the constant-one affine residual,
    i.e. the mod-two torsion line. -/
theorem all_face_flip_maps_to_torsion :
    holonomyToResidual allFaceFlipCode = torsionResidual := by
  native_decide

/-- Every nonzero residual other than the constant-one torsion state has a
    two-vertex support; these are the six K4 edge states. -/
theorem nonconstant_residual_has_two_point_support : ∀ r : AffineResidual,
    r ≠ zeroResidual → r ≠ torsionResidual → supportCard r = 2 := by
  native_decide

/-- Adding the invariant torsion state complements the vertex support. -/
theorem torsion_complements_support_values : ∀ r : AffineResidual,
    residualValues (addTorsion r) = complementValues (residualValues r) := by
  native_decide

/-! ## S4 invariant line via adjacent transpositions -/

/-- Swap the values at vertices `A` and `B`. -/
def swapABValues (v : VertexValues) : VertexValues :=
  ⟨v.b, v.a, v.c, v.d⟩

/-- Swap the values at vertices `B` and `C`. -/
def swapBCValues (v : VertexValues) : VertexValues :=
  ⟨v.a, v.c, v.b, v.d⟩

/-- Swap the values at vertices `C` and `D`. -/
def swapCDValues (v : VertexValues) : VertexValues :=
  ⟨v.a, v.b, v.d, v.c⟩

def swapABResidual (r : AffineResidual) : AffineResidual :=
  residualFromValues (swapABValues (residualValues r))

def swapBCResidual (r : AffineResidual) : AffineResidual :=
  residualFromValues (swapBCValues (residualValues r))

def swapCDResidual (r : AffineResidual) : AffineResidual :=
  residualFromValues (swapCDValues (residualValues r))

/-- The only states fixed by the three adjacent transpositions generating
    `S4` are zero and the constant-one torsion state. -/
theorem s4_fixed_states_are_torsion_line : ∀ r : AffineResidual,
    (swapABResidual r = r ∧ swapBCResidual r = r ∧ swapCDResidual r = r) ↔
      r = zeroResidual ∨ r = torsionResidual := by
  native_decide

/-- The two invariant states are indeed fixed by every displayed generator. -/
theorem zero_and_torsion_are_s4_fixed :
    (swapABResidual zeroResidual = zeroResidual ∧
     swapBCResidual zeroResidual = zeroResidual ∧
     swapCDResidual zeroResidual = zeroResidual) ∧
    (swapABResidual torsionResidual = torsionResidual ∧
     swapBCResidual torsionResidual = torsionResidual ∧
     swapCDResidual torsionResidual = torsionResidual) := by
  native_decide

end EnterpriseMath.Precision.EulerHolonomyResidualDuality
