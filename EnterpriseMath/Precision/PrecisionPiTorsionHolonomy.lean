import Mathlib
import EnterpriseMath.Precision.EulerFccSpinHolonomy

namespace EnterpriseMath.Precision.PrecisionPiTorsionHolonomy

open EulerFccSpinHolonomy

/-- Integer fluctuations on the four tetrahedral slice labels. -/
@[ext]
structure VertexState where
  A : ℤ
  B : ℤ
  C : ℤ
  D : ℤ
  deriving DecidableEq, Repr

/-- Integer fluctuations on the six shared line-family labels. -/
@[ext]
structure EdgeState where
  AB : ℤ
  AC : ℤ
  AD : ℤ
  BC : ℤ
  BD : ℤ
  CD : ℤ
  deriving DecidableEq, Repr

def vadd (v w : VertexState) : VertexState :=
  ⟨v.A + w.A, v.B + w.B, v.C + w.C, v.D + w.D⟩

def eadd (x y : EdgeState) : EdgeState :=
  ⟨x.AB + y.AB, x.AC + y.AC, x.AD + y.AD,
   x.BC + y.BC, x.BD + y.BD, x.CD + y.CD⟩

def eneg (x : EdgeState) : EdgeState :=
  ⟨-x.AB, -x.AC, -x.AD, -x.BC, -x.BD, -x.CD⟩

def esub (x y : EdgeState) : EdgeState :=
  eadd x (eneg y)

def escale (c : ℤ) (x : EdgeState) : EdgeState :=
  ⟨c * x.AB, c * x.AC, c * x.AD,
   c * x.BC, c * x.BD, c * x.CD⟩

def vertexTotal (v : VertexState) : ℤ :=
  v.A + v.B + v.C + v.D

def edgeTotal (x : EdgeState) : ℤ :=
  x.AB + x.AC + x.AD + x.BC + x.BD + x.CD

/-- Endpoint-sum map from four slice fluctuations to six line fluctuations. -/
def delta (v : VertexState) : EdgeState :=
  ⟨v.A + v.B, v.A + v.C, v.A + v.D,
   v.B + v.C, v.B + v.D, v.C + v.D⟩

def matchingSums (x : EdgeState) : ℤ × ℤ × ℤ :=
  (x.AB + x.CD, x.AC + x.BD, x.AD + x.BC)

def starA (x : EdgeState) : ℤ :=
  x.AB + x.AC + x.AD

/-- `+1` on the triangular face opposite a vertex and `-1` on its star. -/
def faceContrast : Slice → EdgeState
  | .A => ⟨-1, -1, -1, 1, 1, 1⟩
  | .B => ⟨-1, 1, 1, -1, -1, 1⟩
  | .C => ⟨1, -1, 1, -1, 1, -1⟩
  | .D => ⟨1, 1, -1, 1, -1, -1⟩

/-- Explicit balanced potential lifting twice the face contrast. -/
def faceDoubleLift : Slice → VertexState
  | .A => ⟨-3, 1, 1, 1⟩
  | .B => ⟨1, -3, 1, 1⟩
  | .C => ⟨1, 1, -3, 1⟩
  | .D => ⟨1, 1, 1, -3⟩

/-- Explicit balanced potential relating every face contrast to the A-face contrast. -/
def faceToAComparisonLift : Slice → VertexState
  | .A => ⟨0, 0, 0, 0⟩
  | .B => ⟨2, -2, 0, 0⟩
  | .C => ⟨2, 0, -2, 0⟩
  | .D => ⟨2, 0, 0, -2⟩

/-- Quotient equivalence under a balanced endpoint-sum lift. -/
def ResidualEquivalent (x y : EdgeState) : Prop :=
  ∃ v : VertexState, vertexTotal v = 0 ∧ x = eadd y (delta v)

theorem edgeTotal_faceContrast (s : Slice) :
    edgeTotal (faceContrast s) = 0 := by
  cases s <;> norm_num [edgeTotal, faceContrast]

theorem matchingSums_faceContrast (s : Slice) :
    matchingSums (faceContrast s) = (0, 0, 0) := by
  cases s <;> norm_num [matchingSums, faceContrast]

theorem starA_faceContrast_odd (s : Slice) :
    starA (faceContrast s) % 2 = 1 := by
  cases s <;> norm_num [starA, faceContrast]

theorem starA_delta_of_balanced
    (v : VertexState)
    (h : vertexTotal v = 0) :
    starA (delta v) = 2 * v.A := by
  simp [starA, delta, vertexTotal] at h ⊢
  linarith

theorem faceContrast_not_balanced_endpoint_sum (s : Slice) :
    ¬ ∃ v : VertexState, vertexTotal v = 0 ∧ delta v = faceContrast s := by
  rintro ⟨v, hv, hdelta⟩
  have hstar := starA_delta_of_balanced v hv
  have hmod : starA (delta v) % 2 = 0 := by
    rw [hstar]
    omega
  rw [hdelta] at hmod
  rw [starA_faceContrast_odd s] at hmod
  omega

theorem faceDoubleLift_balanced (s : Slice) :
    vertexTotal (faceDoubleLift s) = 0 := by
  cases s <;> norm_num [vertexTotal, faceDoubleLift]

theorem delta_faceDoubleLift (s : Slice) :
    delta (faceDoubleLift s) = escale 2 (faceContrast s) := by
  cases s <;>
    ext <;> norm_num [delta, faceDoubleLift, escale, faceContrast]

theorem faceContrast_has_order_two_certificate (s : Slice) :
    (¬ ∃ v : VertexState, vertexTotal v = 0 ∧ delta v = faceContrast s) ∧
      ∃ v : VertexState,
        vertexTotal v = 0 ∧ delta v = escale 2 (faceContrast s) := by
  constructor
  · exact faceContrast_not_balanced_endpoint_sum s
  · exact ⟨faceDoubleLift s, faceDoubleLift_balanced s, delta_faceDoubleLift s⟩

theorem faceToAComparisonLift_balanced (s : Slice) :
    vertexTotal (faceToAComparisonLift s) = 0 := by
  cases s <;> norm_num [vertexTotal, faceToAComparisonLift]

theorem faceContrast_difference_from_A (s : Slice) :
    faceContrast s =
      eadd (faceContrast .A) (delta (faceToAComparisonLift s)) := by
  cases s <;>
    ext <;> norm_num [faceContrast, eadd, delta, faceToAComparisonLift]

theorem all_faceContrasts_same_residual_class (s : Slice) :
    ResidualEquivalent (faceContrast s) (faceContrast .A) := by
  exact ⟨faceToAComparisonLift s,
    faceToAComparisonLift_balanced s,
    faceContrast_difference_from_A s⟩

/-- The squared normalization coefficient is the A5/A3 covolume-square ratio
    divided by the square of the order-two torsion. -/
theorem precision_normalization_square_identity :
    (3 / 8 : ℚ) = 6 / (2 ^ 2 * 4) := by
  norm_num

/-- After multiplying by the A3/A5 covolume-square ratio, the coefficient is
    exactly the square of one half. -/
theorem torsion_reduced_covolume_ratio_square :
    (3 / 8 : ℚ) * (4 / 6) = (1 / 2 : ℚ) ^ 2 := by
  norm_num

/-- The finite face contrast selects the nontrivial tangent half-turn. -/
theorem faceContrast_matches_face_halfTurn
    (omitted source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source)
    (v : Vec3)
    (hv : dot (normal source) v = 0) :
    (starA (faceContrast omitted) % 2 = 1) ∧
      faceTransport source middle target v = vneg v := by
  constructor
  · exact starA_faceContrast_odd omitted
  · exact face_transport_negates_slice source middle target h₁ h₂ h₃ v hv

end EnterpriseMath.Precision.PrecisionPiTorsionHolonomy
