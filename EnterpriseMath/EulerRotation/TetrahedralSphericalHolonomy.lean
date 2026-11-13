import Mathlib

namespace EnterpriseMath.EulerRotation.TetrahedralSphericalHolonomy

inductive Slice
  | A | B | C | D
  deriving DecidableEq, Fintype

@[ext]
structure Vec3 where
  x : ℤ
  y : ℤ
  z : ℤ
  deriving DecidableEq

@[ext]
structure Mat3 where
  m00 : ℤ
  m01 : ℤ
  m02 : ℤ
  m10 : ℤ
  m11 : ℤ
  m12 : ℤ
  m20 : ℤ
  m21 : ℤ
  m22 : ℤ
  deriving DecidableEq

@[ext]
structure Quat where
  r : ℤ
  i : ℤ
  j : ℤ
  k : ℤ
  deriving DecidableEq

/-- The four regular-tetrahedral FCC slice normals. -/
def normal : Slice → Vec3
  | .A => ⟨1, -1, -1⟩
  | .B => ⟨-1, 1, -1⟩
  | .C => ⟨-1, -1, 1⟩
  | .D => ⟨1, 1, 1⟩

def vscale (a : ℤ) (v : Vec3) : Vec3 :=
  ⟨a * v.x, a * v.y, a * v.z⟩

def vneg (v : Vec3) : Vec3 := vscale (-1) v

def dot (u v : Vec3) : ℤ :=
  u.x * v.x + u.y * v.y + u.z * v.z

def cross (u v : Vec3) : Vec3 :=
  ⟨u.y * v.z - u.z * v.y,
   u.z * v.x - u.x * v.z,
   u.x * v.y - u.y * v.x⟩

def determinant (u v w : Vec3) : ℤ :=
  dot u (cross v w)

def matZero : Mat3 :=
  ⟨0, 0, 0, 0, 0, 0, 0, 0, 0⟩

def matId : Mat3 :=
  ⟨1, 0, 0, 0, 1, 0, 0, 0, 1⟩

def matAdd (a b : Mat3) : Mat3 :=
  ⟨a.m00 + b.m00, a.m01 + b.m01, a.m02 + b.m02,
   a.m10 + b.m10, a.m11 + b.m11, a.m12 + b.m12,
   a.m20 + b.m20, a.m21 + b.m21, a.m22 + b.m22⟩

def matScale (c : ℤ) (a : Mat3) : Mat3 :=
  ⟨c * a.m00, c * a.m01, c * a.m02,
   c * a.m10, c * a.m11, c * a.m12,
   c * a.m20, c * a.m21, c * a.m22⟩

def matHalf (a : Mat3) : Mat3 :=
  ⟨a.m00 / 2, a.m01 / 2, a.m02 / 2,
   a.m10 / 2, a.m11 / 2, a.m12 / 2,
   a.m20 / 2, a.m21 / 2, a.m22 / 2⟩

def matMul (a b : Mat3) : Mat3 :=
  ⟨a.m00*b.m00 + a.m01*b.m10 + a.m02*b.m20,
   a.m00*b.m01 + a.m01*b.m11 + a.m02*b.m21,
   a.m00*b.m02 + a.m01*b.m12 + a.m02*b.m22,
   a.m10*b.m00 + a.m11*b.m10 + a.m12*b.m20,
   a.m10*b.m01 + a.m11*b.m11 + a.m12*b.m21,
   a.m10*b.m02 + a.m11*b.m12 + a.m12*b.m22,
   a.m20*b.m00 + a.m21*b.m10 + a.m22*b.m20,
   a.m20*b.m01 + a.m21*b.m11 + a.m22*b.m21,
   a.m20*b.m02 + a.m21*b.m12 + a.m22*b.m22⟩

def matVec (a : Mat3) (v : Vec3) : Vec3 :=
  ⟨a.m00*v.x + a.m01*v.y + a.m02*v.z,
   a.m10*v.x + a.m11*v.y + a.m12*v.z,
   a.m20*v.x + a.m21*v.y + a.m22*v.z⟩

def matTranspose (a : Mat3) : Mat3 :=
  ⟨a.m00, a.m10, a.m20,
   a.m01, a.m11, a.m21,
   a.m02, a.m12, a.m22⟩

def matDet (a : Mat3) : ℤ :=
  a.m00 * (a.m11*a.m22 - a.m12*a.m21)
  - a.m01 * (a.m10*a.m22 - a.m12*a.m20)
  + a.m02 * (a.m10*a.m21 - a.m11*a.m20)

def outer (u v : Vec3) : Mat3 :=
  ⟨u.x*v.x, u.x*v.y, u.x*v.z,
   u.y*v.x, u.y*v.y, u.y*v.z,
   u.z*v.x, u.z*v.y, u.z*v.z⟩

/-- Matrix of `x ↦ k × x`. -/
def crossMatrix (k : Vec3) : Mat3 :=
  ⟨0, -k.z, k.y,
   k.z, 0, -k.x,
   -k.y, k.x, 0⟩

/-- Three times the shortest Rodrigues rotation between distinct tetrahedral normals. -/
def scaledRotation (source target : Slice) : Mat3 :=
  let K := crossMatrix (cross (normal source) (normal target))
  matAdd (matScale 3 matId) (matAdd K (matHalf (matMul K K)))

/-- Three times the half-turn about one tetrahedral normal. -/
def scaledHalfTurn (source : Slice) : Mat3 :=
  matAdd (matScale 2 (outer (normal source) (normal source))) (matScale (-3) matId)

/-- Product of the three scaled edge transports around an oriented face. -/
def scaledFaceHolonomy (source middle target : Slice) : Mat3 :=
  matMul (scaledRotation target source)
    (matMul (scaledRotation middle target) (scaledRotation source middle))

def qmul (a b : Quat) : Quat :=
  ⟨a.r*b.r - a.i*b.i - a.j*b.j - a.k*b.k,
   a.r*b.i + b.r*a.i + a.j*b.k - a.k*b.j,
   a.r*b.j + b.r*a.j + a.k*b.i - a.i*b.k,
   a.r*b.k + b.r*a.k + a.i*b.j - a.j*b.i⟩

def qscale (c : ℤ) (q : Quat) : Quat :=
  ⟨c*q.r, c*q.i, c*q.j, c*q.k⟩

def qneg (q : Quat) : Quat := qscale (-1) q

def qconj (q : Quat) : Quat :=
  ⟨q.r, -q.i, -q.j, -q.k⟩

def qnorm (q : Quat) : ℤ :=
  q.r*q.r + q.i*q.i + q.j*q.j + q.k*q.k

def pure (v : Vec3) : Quat :=
  ⟨0, v.x, v.y, v.z⟩

def vectorPart (q : Quat) : Vec3 :=
  ⟨q.i, q.j, q.k⟩

/-- Integral spin lift `p_uv`; the unit spinor is `p_uv / sqrt 3`. -/
def edgeSpinor (source target : Slice) : Quat :=
  let k := cross (normal source) (normal target)
  ⟨1, k.x / 2, k.y / 2, k.z / 2⟩

def faceSpinor (source middle target : Slice) : Quat :=
  qmul (edgeSpinor target source)
    (qmul (edgeSpinor middle target) (edgeSpinor source middle))

def orientationSign (source middle target : Slice) : ℤ :=
  determinant (normal source) (normal middle) (normal target) / 4

def expectedFaceSpinor (source middle target : Slice) : Quat :=
  qscale (3 * orientationSign source middle target) (pure (normal source))

/-- Unnormalized quaternion conjugation action on a vector. -/
def scaledSpinAction (q : Quat) (v : Vec3) : Vec3 :=
  vectorPart (qmul (qmul q (pure v)) (qconj q))

/-- The four slice normals have the regular tetrahedral Gram matrix. -/
theorem normal_squared_norm :
    ∀ source : Slice, dot (normal source) (normal source) = 3 := by
  native_decide

theorem distinct_normal_dot :
    ∀ source target : Slice, source ≠ target →
      dot (normal source) (normal target) = -1 := by
  native_decide

theorem three_normal_determinant :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      determinant (normal source) (normal middle) (normal target) = 4 ∨
      determinant (normal source) (normal middle) (normal target) = -4 := by
  native_decide

/-- The scaled shortest rotation maps one normal to three times the next. -/
theorem scaledRotation_maps_normal :
    ∀ source target : Slice, source ≠ target →
      matVec (scaledRotation source target) (normal source) =
        vscale 3 (normal target) := by
  native_decide

/-- Each scaled transition is orthogonal up to its factor three. -/
theorem scaledRotation_orthogonal :
    ∀ source target : Slice, source ≠ target →
      matMul (matTranspose (scaledRotation source target))
        (scaledRotation source target) = matScale 9 matId := by
  native_decide

/-- Each scaled transition has determinant 27, hence the normalized map is proper. -/
theorem scaledRotation_determinant :
    ∀ source target : Slice, source ≠ target →
      matDet (scaledRotation source target) = 27 := by
  native_decide

/-- Reversing a transition gives its scaled inverse. -/
theorem scaledRotation_reverse_product :
    ∀ source target : Slice, source ≠ target →
      matMul (scaledRotation target source) (scaledRotation source target) =
        matScale 9 matId := by
  native_decide

/-- Exact three-transition face holonomy.  Dividing both sides by 27 gives
`T_wu T_vw T_uv = (2/3) n_u n_uᵀ - I`. -/
theorem scaled_face_holonomy_formula :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      scaledFaceHolonomy source middle target =
        matScale 9 (scaledHalfTurn source) := by
  native_decide

/-- The face holonomy fixes the starting normal. -/
theorem scaledHalfTurn_fixes_normal :
    ∀ source : Slice,
      matVec (scaledHalfTurn source) (normal source) =
        vscale 3 (normal source) := by
  native_decide

/-- The face holonomy reverses every shared-line tangent in the starting slice. -/
theorem scaledHalfTurn_reverses_slice_lines :
    ∀ source target : Slice, source ≠ target →
      matVec (scaledHalfTurn source) (cross (normal source) (normal target)) =
        vscale (-3) (cross (normal source) (normal target)) := by
  native_decide

/-- Every integral edge spinor has norm three. -/
theorem edgeSpinor_norm :
    ∀ source target : Slice, source ≠ target →
      qnorm (edgeSpinor source target) = 3 := by
  native_decide

/-- Exact orientation-sensitive Spin face product. -/
theorem faceSpinor_formula :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      faceSpinor source middle target =
        expectedFaceSpinor source middle target := by
  native_decide

/-- Before division by `(sqrt 3)^3`, the face spinor squares to `-27`. -/
theorem faceSpinor_square :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      qmul (faceSpinor source middle target) (faceSpinor source middle target) =
        ⟨-27, 0, 0, 0⟩ := by
  native_decide

/-- Reversing the face orientation changes only the Spin-cover sign. -/
theorem reverse_face_flips_spin_lift :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      faceSpinor source target middle = qneg (faceSpinor source middle target) := by
  native_decide

/-- The two opposite Spin lifts induce the same scaled vector rotation. -/
theorem spin_sign_is_projection_invisible :
    ∀ (q : Quat) (v : Vec3),
      scaledSpinAction (qneg q) v = scaledSpinAction q v := by
  intro q v
  ext <;> simp [scaledSpinAction, qneg, qscale, qmul, qconj, pure, vectorPart] <;> ring

/-- The face spinor conjugation reverses all three line directions in its slice.
Its norm is 27, so `-27 v` becomes `-v` after normalization. -/
theorem faceSpinor_reverses_slice_lines :
    ∀ source middle target other : Slice,
      source ≠ middle → middle ≠ target → target ≠ source → source ≠ other →
      scaledSpinAction (faceSpinor source middle target)
        (cross (normal source) (normal other)) =
      vscale (-27) (cross (normal source) (normal other)) := by
  native_decide

end EnterpriseMath.EulerRotation.TetrahedralSphericalHolonomy
